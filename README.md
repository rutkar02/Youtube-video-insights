YouTube Video Insights

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about any YouTube video using its transcript.

Features

* Analyze YouTube videos using natural language
* Automatic transcript extraction
* Intelligent document chunking
* OpenAI embeddings generation
* Cosine similarity search
* Top-K retrieval
* Context-aware question answering
* Embedding caching for faster follow-up questions

Tech Stack

* Python
* Streamlit
* OpenAI API
* youtube-transcript-api
* NumPy

How It Works

1. User enters a YouTube video URL.
2. The application extracts the video ID.
3. Transcript is fetched using YouTube Transcript API.
4. Transcript text is combined into a single document.
5. Document is split into chunks.
6. Embeddings are generated for each chunk.
7. Embeddings are cached in session state.
8. User question is converted into an embedding.
9. Cosine similarity identifies the most relevant chunks.
10. GPT generates an answer using the retrieved context.

Architecture

YouTube URL
→ Video ID
→ Transcript
→ Chunking
→ Embeddings
→ Vector Store (Session State)
→ Similarity Search
→ Top-K Retrieval
→ GPT Response

Run Locally

pip install -r requirements.txt
streamlit run app.py

Example Questions

* What is the main idea of this video?
* Summarize the video in 5 bullet points.
* What are the key takeaways?
* What does the speaker say about AI?
* Explain the concepts discussed in simple terms.

Future Improvements

* Support multiple videos
* Timestamp citations
* Chat history
* Persistent vector database
* Playlist analysis
* Video comparison
* Speaker identification
* Hybrid search

Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Embeddings
* Cosine Similarity
* Semantic Search
* Transcript Processing
* Caching
* Top-K Retrieval
* LLM Application Development
