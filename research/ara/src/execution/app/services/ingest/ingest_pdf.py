# Grounding: transcribed from oshima/api/app/services/ingest/ingest_pdf.py
#!/usr/bin/env python3
"""
PDF Text Extraction Pipeline - Step 1: Extract and Save Raw JSON

This module handles the first step of the PDF extraction pipeline:
1. Takes a PDF file path as input
2. Calls Adobe PDF Services API to extract structured data
3. Saves the raw JSON output as {pdfname}.json

Usage:
    python ingest_pdf.py /path/to/document.pdf

Output:
    - document.json (raw structured data from Adobe API)
"""

import json
import logging
import os
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Optional

from adobe.pdfservices.operation.auth.service_principal_credentials import (
    ServicePrincipalCredentials,
)
from adobe.pdfservices.operation.exception.exceptions import (
    SdkException,
    ServiceApiException,
    ServiceUsageException,
)
from adobe.pdfservices.operation.io.cloud_asset import CloudAsset
from adobe.pdfservices.operation.io.stream_asset import StreamAsset
from adobe.pdfservices.operation.pdf_services import PDFServices
from adobe.pdfservices.operation.pdf_services_media_type import PDFServicesMediaType
from adobe.pdfservices.operation.pdfjobs.jobs.extract_pdf_job import ExtractPDFJob
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_element_type import (
    ExtractElementType,
)
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_pdf_params import (
    ExtractPDFParams,
)
from adobe.pdfservices.operation.pdfjobs.result.extract_pdf_result import (
    ExtractPDFResult,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class PDFExtractor:
    """Handles PDF text extraction using Adobe PDF Services API"""

    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize the PDF extractor

        Args:
            credentials_path: Path to Adobe API credentials JSON file
                            If None, uses default location
        """
        self.credentials_path = credentials_path or self._get_default_credentials_path()
        self.credentials = self._load_credentials()
        self.pdf_services = PDFServices(credentials=self.credentials)

    def _get_default_credentials_path(self) -> str:
        """Get the default path to Adobe API credentials"""
        # We're in /api/app/services/ingest/ and credentials are in /api/config/adobe/
        script_dir = Path(__file__).parent
        credentials_path = (
            script_dir
            / ".."
            / ".."
            / ".."
            / "config"
            / "adobe"
            / "pdfservices-api-credentials.json"
        )
        return str(credentials_path.resolve())

    def _load_credentials(self) -> ServicePrincipalCredentials:
        """Load Adobe API credentials from environment variables or JSON file"""
        # First try environment variables
        client_id = os.getenv("PDF_SERVICES_CLIENT_ID")
        client_secret = os.getenv("PDF_SERVICES_CLIENT_SECRET")

        if client_id and client_secret:
            logger.info(
                "Using Adobe PDF Services credentials from environment variables"
            )
            return ServicePrincipalCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )

        # Fall back to JSON file if env vars not available
        try:
            with open(self.credentials_path, "r") as cred_file:
                cred_data = json.load(cred_file)

            return ServicePrincipalCredentials(
                client_id=cred_data["client_credentials"]["client_id"],
                client_secret=cred_data["client_credentials"]["client_secret"],
            )
        except FileNotFoundError:
            logger.error(
                f"Adobe credentials not found in environment variables and credentials file not found at: {self.credentials_path}"
            )
            logger.error(
                "Please set PDF_SERVICES_CLIENT_ID and PDF_SERVICES_CLIENT_SECRET environment variables"
            )
            raise
        except (KeyError, json.JSONDecodeError) as e:
            logger.error(f"Invalid credentials file format: {e}")
            raise

    def extract_pdf(self, pdf_path: str, output_dir: str = None) -> str:
        """
        Extract structured data from a PDF file

        Args:
            pdf_path: Path to the input PDF file
            output_dir: Directory to save output (defaults to current directory)

        Returns:
            Path to the saved JSON file

        Raises:
            FileNotFoundError: If PDF file doesn't exist
            ServiceApiException: If Adobe API call fails
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        if output_dir is None:
            output_dir = Path.cwd()
        else:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"Extracting text from PDF: {pdf_path}")

        try:
            # Read the PDF file
            with open(pdf_path, "rb") as file:
                input_stream = file.read()

            # Upload the PDF to Adobe services
            logger.info("Uploading PDF to Adobe services...")
            input_asset = self.pdf_services.upload(
                input_stream=input_stream, mime_type=PDFServicesMediaType.PDF
            )

            # Configure extraction parameters
            extract_pdf_params = ExtractPDFParams(
                elements_to_extract=[ExtractElementType.TEXT],
            )

            # Create and submit the extraction job
            logger.info("Submitting extraction job...")
            extract_pdf_job = ExtractPDFJob(
                input_asset=input_asset, extract_pdf_params=extract_pdf_params
            )

            location = self.pdf_services.submit(extract_pdf_job)
            pdf_services_response = self.pdf_services.get_job_result(
                location, ExtractPDFResult
            )

            # Download the result
            logger.info("Downloading extraction results...")
            result_asset: CloudAsset = pdf_services_response.get_result().get_resource()
            stream_asset: StreamAsset = self.pdf_services.get_content(result_asset)

            # Save the ZIP file temporarily
            temp_zip_path = (
                output_dir
                / f"temp_extract_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            )
            with open(temp_zip_path, "wb") as file:
                file.write(stream_asset.get_input_stream())

            # Extract JSON from ZIP and save with proper naming
            json_output_path = self._extract_and_save_json(
                temp_zip_path, pdf_path, output_dir
            )

            # Clean up temporary ZIP file
            temp_zip_path.unlink()

            logger.info(f"✓ Extraction complete. JSON saved to: {json_output_path}")
            return str(json_output_path)

        except (ServiceApiException, ServiceUsageException, SdkException) as e:
            logger.error(f"Adobe API error during extraction: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during extraction: {e}")
            raise

    def _extract_and_save_json(
        self, zip_path: Path, pdf_path: Path, output_dir: Path
    ) -> Path:
        """
        Extract JSON from the Adobe result ZIP and save with proper naming

        Args:
            zip_path: Path to the ZIP file from Adobe API
            pdf_path: Original PDF path (for naming)
            output_dir: Directory to save the JSON

        Returns:
            Path to the saved JSON file
        """
        # Generate output filename based on PDF name
        pdf_name = pdf_path.stem  # Get filename without extension
        json_output_path = output_dir / f"{pdf_name}.json"

        # Extract JSON from ZIP
        with zipfile.ZipFile(zip_path, "r") as archive:
            # Read the structured data JSON
            with archive.open("structuredData.json") as json_entry:
                json_data = json_entry.read()
                structured_data = json.loads(json_data)

        # Save the structured data as the raw JSON file
        with open(json_output_path, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=2, ensure_ascii=False)

        return json_output_path


def main():
    """Command line interface for PDF extraction"""
    if len(sys.argv) != 2:
        print("Usage: python ingest_pdf.py <pdf_path>")
        print("Example: python ingest_pdf.py /path/to/document.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    try:
        extractor = PDFExtractor()
        output_path = extractor.extract_pdf(pdf_path)
        print(f"✓ Successfully extracted PDF data to: {output_path}")

    except FileNotFoundError as e:
        logger.error(f"File error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
