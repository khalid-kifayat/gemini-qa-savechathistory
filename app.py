from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Built Automations")

st.header('Hello, I am your AI Automation Assistant 🤖', divider='rainbow')
st.caption("Ask me anything, I will assist you")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("Answer: ")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
 
# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000000; /* Black background color */
    color: #ffffff; /* White text color */
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p class="footer">Generative AI : Python-Langchain Application <br>  Created by Khalid Kifayat <br> (www.beingkhalid.com / www.builtautomations.com)</p>', unsafe_allow_html=True)


hide_streamlit_style = """
            <style>

            [data-testid="stToolbar"] {visibility: hidden;}
            .reportview-container {
            margin-top: -2em;
        }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            #stDecoration {display:none;}
            footer {visibility: hidden;}
            div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    
