#!/usr/bin/env python3
"""Ingest any PDFs dropped in pdfs_dropzone/ (named <slug>.pdf or <doi-with-slashes-as->.pdf).
Extract text -> fulltext/<slug>.txt. Reports coverage. Then re-type via typing_fulltext workflow."""
import os, re, json, subprocess, glob
corpus={p['id'].split('/')[-1]:p for p in json.load(open('corpus.json'))}
doi2slug={}
for slug,p in corpus.items():
    d=(p.get('doi') or '').replace('https://doi.org/','').lower()
    if d: doi2slug[d]=slug; doi2slug[d.replace('/','_')]=slug; doi2slug[d.replace('/','-')]=slug
os.makedirs('fulltext',exist_ok=True)
done=0
for pdf in glob.glob('pdfs_dropzone/*.pdf')+glob.glob('pdfs_dropzone/*.PDF'):
    base=os.path.splitext(os.path.basename(pdf))[0]
    slug = base if base in corpus else doi2slug.get(base.lower())
    if not slug:
        print('?? cannot map',base,'(name it <slug>.pdf)'); continue
    with open(pdf,'rb') as f:
        if f.read(5)!=b'%PDF-': print('!! not a pdf:',base); continue
    txt=f'fulltext/{slug}.txt'
    subprocess.run(['pdftotext','-q',pdf,txt],capture_output=True)
    if os.path.exists(txt) and os.path.getsize(txt)>3000:
        t=re.split(r'\n\s*[Rr]eferences\s*\n',open(txt,errors='ignore').read())[0]
        open(txt,'w').write(t[:16000]); done+=1
        print('OK',slug,len(t),'chars')
    else: print('!! extract failed/short:',slug)
have=set(os.path.splitext(f)[0] for f in os.listdir('fulltext') if f.endswith('.txt'))
print('\nfull text now available: %d/72  (need %d more)'%(len(have),72-len(have)))
