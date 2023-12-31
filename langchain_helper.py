
import streamlit as st
from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory,
                                                  ConversationBufferWindowMemory,
                                                  ConversationSummaryMemory)

#load_dotenv()
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None

    
def getresponse(userInput, api_key):
    if st.session_state['conversation'] is None:
        llm = OpenAI(temperature=0,
                    openai_api_key=api_key,
                    model_name="text-davinci-003")

        st.session_state['conversation'] = ConversationChain(
            llm =llm,
            verbose =True,
            memory=ConversationBufferMemory()
        )
    response = st.session_state['conversation'].predict(input=userInput)
    return response