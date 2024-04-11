import streamlit as st
import spacy
from spacy import displacy
from newspaper import Article
from collections import Counter

nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities")


text = st.text_area("Enter a paragraph")
url = st.text_input("Enter an URL:")
st.info("(or)")


if(st.button("Analyze")):
  if url:
    article = Article(url)
    article.download()
    article.parse()
    doc = nlp(article.text)
    ent_html = displacy.render(doc, jupyter=False, style='ent')
    st.markdown(ent_html, unsafe_allow_html=True)    
  
  elif text:  
    doc = nlp(text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
    st.markdown(ent_html, unsafe_allow_html=True)
