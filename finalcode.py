# -*- coding: utf-8 -*-
"""finalcode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uGQJ5v4tMr0ubMbvMYJmY6q7tXWWtlta
"""

pip install pdfminer.six

import os
from pdfminer.high_level import extract_text

pdf_names=os.listdir(r'F:\project\Project 2\New folder (2)\dataset')
pdf_names

#empty corpus to store text from all pdf
corpus=str()

for i in pdf_names:
    directory="F:\\project\\Project 2\\New folder (2)\\dataset\\"+str(i)
    text=extract_text(directory)
    corpus+=text
    print(len(corpus))

#removing line break/New line character from corpus
corpus=corpus.replace("\n"," ")

import nltk
from nltk.tokenize import sent_tokenize
sent=sent_tokenize(corpus)

print(corpus)

import spacy
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

!pip install https://huggingface.co/kormilitzin/en_core_med7_lg/resolve/main/en_core_med7_lg-any-py3-none-any.whl

med7 = spacy.load("en_core_med7_lg")

# create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}


doc = med7(corpus)

spacy.displacy.render(doc, style='ent', jupyter=True, options=options)

[(ent.text, ent.label_) for ent in doc.ents]



doc = med7(corpus)

entities = []
labels = []
position_start = []
position_end = []

for ent in doc.ents:
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)
    
df = pd.DataFrame({'Entities':entities,'Labels':labels,'Position_Start':position_start, 'Position_End':position_end})

df
