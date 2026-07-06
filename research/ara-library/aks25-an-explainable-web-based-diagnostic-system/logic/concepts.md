# Concepts

> Grounding: abstract-only. Definitions of the paper's genuine technical terms are drawn from the
> abstract and the verified dataset record; where a term is named but not defined in the abstract,
> boundary conditions are marked "Not available from provided input (no full text)". General
> definitions of well-known architectures/methods are standard field knowledge, flagged as such.

## XRAI (eXplanation with Ranked Area Integrals)
- **Notation**: —
- **Definition**: A region-based explainable-AI attribution method that produces saliency maps by aggregating pixel attributions into coherent image regions, ranking regions by their contribution to the model's prediction. In this paper XRAI is integrated to provide "region-based attribution maps" for the AD classifier. (Per `sources.yaml`, implemented via the Saliency library's XRAI module.)
- **Boundary conditions**: Applied here to 2D brain MRI classification; parameterization and segmentation settings not available from provided input (no full text).
- **Related concepts**: Explainable AI (XAI), region-based attribution map, MobileNet-V3 Large.

## Explainable AI (XAI)
- **Definition**: A family of frameworks that make a model's decision-making interpretable to humans; the paper frames XAI (via XRAI) as the means to "bridge th[e] gap" between high-performance AD models and clinical deployment by providing "clinically meaningful visualizations of model decision-making".
- **Notation**: —
- **Boundary conditions**: Here used specifically for clinician-facing interpretation of AD severity predictions.
- **Related concepts**: XRAI, region-based attribution map, clinical interpretability.

## Region-based attribution map
- **Definition**: A visual explanation that highlights contiguous image regions (rather than isolated pixels) responsible for a model's prediction; produced by XRAI in this system and compared against "known neuroanatomical patterns of AD progression".
- **Notation**: —
- **Boundary conditions**: Meaningful when highlighted regions correspond to AD-relevant neuroanatomy; quantitative overlap thresholds not available from provided input (no full text).
- **Related concepts**: XRAI, XAI.

## AD severity classification
- **Definition**: The supervised task of assigning a brain MRI slice to one of four Alzheimer's disease severity classes. Per `sources.yaml`, the four classes are NonDemented, VeryMildDemented, MildDemented, and ModerateDemented.
- **Notation**: —
- **Boundary conditions**: Defined over 2D axial T1/T2 MRI slices from the Kaggle dataset; four-class scheme.
- **Related concepts**: 2D brain MRI, Augmented Alzheimer MRI Dataset.

## MobileNet-V3 Large
- **Definition**: A lightweight convolutional neural network architecture designed for efficient inference (standard field knowledge). In this paper it is one of three trained architectures and is reported as the best-performing while using the fewest parameters (4.2M).
- **Notation**: —
- **Boundary conditions**: Used as an image classifier over 2D MRI slices; training hyperparameters not available from provided input (no full text).
- **Related concepts**: EfficientNet-B4, ResNet-50, parameter efficiency.

## EfficientNet-B4
- **Definition**: A convolutional neural network from the EfficientNet family using compound scaling of depth/width/resolution (standard field knowledge). One of the three architectures compared in this study.
- **Notation**: —
- **Boundary conditions**: Parameter count and per-model accuracy not available from provided input (no full text).
- **Related concepts**: MobileNet-V3 Large, ResNet-50.

## ResNet-50
- **Definition**: A 50-layer residual convolutional neural network using skip connections (standard field knowledge). One of the three architectures compared in this study.
- **Notation**: —
- **Boundary conditions**: Parameter count and per-model accuracy not available from provided input (no full text).
- **Related concepts**: MobileNet-V3 Large, EfficientNet-B4.

## Gradio clinical web interface
- **Definition**: A web-based user interface (built with the Gradio library) that delivers real-time AD-severity predictions and visual XRAI explanations; reported to provide sub-20-second inference "supporting real-world diagnostic workflows".
- **Notation**: —
- **Boundary conditions**: Deployment hardware and hosting details not available from provided input (no full text).
- **Related concepts**: XRAI, real-time inference, clinical deployment.
