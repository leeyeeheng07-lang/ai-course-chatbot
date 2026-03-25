import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

COURSE_CONTEXT = """
You are a teaching assistant for an AI course. Answer questions about the course.

Course: Introduction to Artificial Intelligence

Course structure:
1. The Fundamentals of AI - covers history, search algorithms, problem solving.
2. Introduction to Generative AI - basics of generative models, prompt engineering.
3. Machine Learning & Deep Learning for Generative AI - neural networks, transformers, diffusion models.
4. Building with Generative AI - hands-on projects using LangChain, APIs, etc.
5. Real-World Applications - case studies in healthcare, creative AI, business.
6. Capstone Project: From Idea to Impact - final project where students build a generative AI application.

Additional info:
- Prerequisites: Basic Python, willingness to learn.
- Tools used: Python, Jupyter notebooks, OpenAI API, Google Colab.
- Assessment: Completion of module quizzes, final project submission.
- Support: Office hours via Discord every Thursday 5pm.

Answer in a friendly, detailed manner. If asked about topics outside this course, politely redirect.
"""

def get_response(user_input, chat_history):
    """Generate a response using Gemini API."""
    prompt = f"{COURSE_CONTEXT}\n\nConversation history:\n{chat_history}\nStudent: {user_input}\nTA:"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, I'm having trouble answering. Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Course Assistant", page_icon="🤖")
st.title("🤖 AI Course Teaching Assistant")
st.markdown("Ask me anything about the *Introduction to Artificial Intelligence* course.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I'm your AI teaching assistant. How can I help you today?"})

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if user_input := st.chat_input():
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build conversation history (last 10 messages)
    chat_history = ""
    for m in st.session_state.messages[-10:]:
        role = "Student" if m["role"] == "user" else "TA"
        chat_history += f"{role}: {m['content']}\n"

    with st.spinner("Thinking..."):
        response = get_response(user_input, chat_history)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})