# AI Course Teaching Assistant

An interactive chatbot that answers students' questions about an Artificial Intelligence course. Built with **Streamlit** and **Google Gemini API**, it provides 24/7 support for course content, assignments, and logistics.

---

## Problem Definition & User Persona

**Problem**  
Students often have repetitive questions about AI courses—concepts, deadlines, tools—and human TAs are not always available. This chatbot offers instant, consistent answers, reducing wait times and helping students learn more efficiently.

**User Persona**  
- **Name**: Alex  
- **Role**: Undergraduate student taking an Introduction to AI course  
- **Background**: Knows basic Python; comfortable with programming but needs quick clarifications on AI topics and course logistics  
- **Goals**: Get accurate answers anytime, without waiting for email replies or office hours  

---

## Features

- ✅ Answers questions about course modules, assignments, prerequisites, and policies  
- ✅ Friendly conversational interface built with Streamlit  
- ✅ Powered by Google Gemini 2.5 Flash – fast and free tier available  
- ✅ Easy to update course knowledge – just edit a text block  
- ✅ Remembers last 10 messages for context  

---

## Tech Stack

- **Frontend**: Streamlit (Python)  
- **LLM**: Google Gemini 2.5 Flash (`google-generativeai`)  
- **Environment**: Python 3.14.3, virtual environment, `python-dotenv` for API keys  

---

## Installation & Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/ai-course-chatbot.git
   cd ai-course-chatbot