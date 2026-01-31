import streamlit as st
from analyzer import analyzer

st.title("File Analyzer")
st.subheader("Upload a .txt file to get basic info about it")

file = st.file_uploader("Upload a file")

try:
    if file:
            fileText = analyzer.FileAnalyzer(file.read().decode("utf-8"))
            if(file.name.endswith(".txt")):
                st.badge("Text file detected!", color="blue")
                st.header(f"File Name: {file.name}")
                col1, col2, col3 = st.columns(3)

                col1.metric("Characters", fileText.char_count())
                col2.metric("Lines", fileText.line_count())
                col3.metric("Words", fileText.word_count())
            else:
                st.error("Unsupported file detected! Please upload a .txt file")
except UnicodeDecodeError:
            st.error("An error occured!")