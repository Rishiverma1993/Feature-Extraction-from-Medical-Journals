# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 00:57:24 2021

@author: rishi
"""

import fitz  # this is pymupdf
import spacy 
import re
import pandas as pd
import streamlit as st
from PIL import Image
from spacy import displacy


def main():
    st.title("Medical Terms Entity App")
    
    menu = ["Home","DocumentFiles","About"]
    choice = st.sidebar.selectbox('Menu', menu)
    
    
    
    if choice=="Home":
        image = Image.open('F:\project\Project 2\medi\im.jfif')
        st.image(image)
        st.write('Drugs Entity Extractor is a web based application created with streamlit. It is used to extract the Drugs entities from any Document. And In this app, Med7 model is used to extract the drugs name from document. Med7 is a transferable clinical natural language processing model for electronic health records compatible with spaCy v3+, for clinical named-entity recognition (NER) tasks. The en_core_med7_lg model is trained on MIMIC-III free-text electronic health records and is able to recognise 7 categories:')
        image1 = Image.open('F:\project\Project 2\medi\Capture.PNG')
        st.image(image1)
    elif choice=="DocumentFiles":
        st.subheader("Upload Document Files")
        docx_file = st.file_uploader("Upload Document",type=['pdf','txt'])
        
        menu1 = ['DOSAGE','DRUG','DURATION''ROUTE']
        choice1 = st.selectbox("Select Entity", menu1)
        
        st.write("Note: If it shows empty then your document not contain that releted entity.")
                    
                    
        if st.button("Process"):
            if docx_file is not None:
                    with fitz.open(stream=docx_file.read(),filetype='pdf') as doc:
                        text = ""
                        for page in doc:
                            text += page.getText()
                            
                    nlp = spacy.load("en_core_med7_lg")
                    doc = nlp(text)
                    
                
                    
                    if choice1 == 'DOSAGE':
                        data = {'DOSAGE': [ent.text for ent in doc.ents if ent.label_== 'DOSAGE']}
                    elif choice1 == 'DRUG': 
                        data = {'Drugs Names': [ent.text for ent in doc.ents if ent.label_== 'DRUG']}
                    elif choice1 == 'DURATION':
                        data = {'DURATION3 Names': [ent.text for ent in doc.ents if ent.label_== 'DURATION']}
                    elif choice1 == 'ROUTE':
                        data = {'ROUTE': [ent.text for ent in doc.ents if ent.label_== 'ROUTE']}
                  
                    else:
                        st.write("Entity is not defined")
                    df = pd.DataFrame(data)
                    df = df.drop_duplicates()
                    st.write(df)
                    
                    #download csv
                    df = df.to_csv()
                    st.download_button("Download", data=df,file_name='drug.csv',mime='text/csv')
    
    else:
        st.subheader("About")
        st.write("Medical Terms Entity")
        st.write("Created by: Rishi Kumar")


if __name__=='__main__':
    main()