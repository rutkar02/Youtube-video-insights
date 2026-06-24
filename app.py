import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from dotenv import load_dotenv
import os
import math
import numpy as np

# here pypdf, openai, dotenv are toolboxes and PdfReader, OpenAi, load_dotenv are the actual tools we are gonna use

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

st.title("Youtube Video Q&A")

video_url = st.text_input(
    "Enter a Youtube URL"
)

all_text = ""

def create_chunks(text,chunk_size):
    i = 0
    chunks = []
    while(i<len(text)):
        chunks.append(text[i:i+chunk_size])
        i+=chunk_size
    return chunks  
  
def get_embedding(text):
    response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
    )
    return response.data[0].embedding  

def cosine_similarity(vec1,vec2):
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    return np.dot(v1,v2)/(
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )

if video_url:
    video_id = video_url.split("v=")[1]
    ytt_api = YouTubeTranscriptApi()
    transcript_data = ytt_api.fetch(video_id)
    for transcript in transcript_data:
        all_text += transcript.text + " "

    chunks = create_chunks(all_text,500)    
    if "data" not in st.session_state or st.session_state.video_id!=video_id:
        data = []
        for chunk in chunks:
            embedding = get_embedding(chunk)
            data.append({"text":chunk, "embedding":embedding})
        st.session_state.data = data 
        st.session_state.video_id = video_id
    question = st.text_input(
        "Ask a question about the video",
        key=f"question_{video_id}"
    )
    
    best_chunk = ""
    storage = []
    data = st.session_state.data

    if question.strip()!="" and all_text.strip()!="":
        question_embedding = get_embedding(question)

        for chunk in data:
            score = cosine_similarity(chunk["embedding"],question_embedding)
            storage.append((score,chunk["text"]))

        storage.sort(reverse=True)
        top_3 = storage[:3]

        for x in top_3:
            best_chunk += x[1]   

        prompt =f"""
        you are an assistant whose purpose is to help user understand the given document 


        Relevant context:
        {best_chunk}

        Question:
        {question}

        Answer the given question using only the relevant context available here
        Be as concise and precise as u can be
        Also if u cant answer based on it just tell him so
        """
        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )   
        st.write(response.output_text)