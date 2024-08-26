#!/bin/bash
echo "Starting script..."
pip install -r requirements.txt
echo "Pip install done."
ollama pull llama3.1
echo "Ollama pull done."
ollama start
echo "Ollama start done."
streamlit run app.py
echo "Streamlit app started."
