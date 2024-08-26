import ollama
import streamlit as st


# Load environment variables


# Define a function to interact with the LLaMA model using the ollama package
def get_llama_response(prompt_text):
    try:
        # Assuming you are using a LLaMA model called "llama-2" on the Ollama platform
          # Adjust the model name as needed
        response = ollama.chat(model='llama3.1', messages=[
            {
                'role': 'user',
                'content': prompt_text,
             },
        ])
        return response['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit interface
st.title("LLaMA Chatbot Demo with Ollama")
input_text = st.text_input("Search the topic you want")

if input_text:
    prompt = f"You are a helpful assistant. Please provide a response to the user's query: {input_text}"
    response = get_llama_response(prompt)
    print(response)
    st.write(response)
