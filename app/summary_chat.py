from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

parser = StrOutputParser()

# ==========================================
# Chat Prompt
# ==========================================

chat_template = """
You are a helpful AI assistant.

Here is a summary of the older conversation:
{summary}

Here are the recent messages:
{recent_messages}

Current user question:
{question}

Use the conversation summary and recent messages to understand the context.

Rules:
- Keep the answer under 5 words.
- Do not add extra explanations unless the user explicitly asks.
- Be concise and direct.
"""

chat_prompt = PromptTemplate.from_template(chat_template)
chat_chain = chat_prompt | llm | parser

# ==========================================
# Summary Prompt
# ==========================================

summary_template = """
Summarize the following conversation.

Keep only important information that may be useful
for answering future questions.

Conversation:
{old_messages}

Previous Summary:
{previous_summary}

Create a short summary.
Do not include unnecessary details.
"""

summary_prompt = PromptTemplate.from_template(summary_template)
summary_chain = summary_prompt | llm | parser

# ==========================================
# Global Variables
# ==========================================

history = []
summary = ""
MAX_MESSAGES = 6

# ==========================================
# Main Function
# ==========================================

def ask_ai(question: str):
    global history, summary

    if question.lower() == "exit":
        return "Chat Ended!"

    # Get Recent Messages
    recent_messages = history[-MAX_MESSAGES:]
    recent_messages_text = "\n".join(recent_messages)

    # Generate AI Response
    response = chat_chain.invoke({
        "summary": summary,
        "recent_messages": recent_messages_text,
        "question": question
    })

    # Save Conversation
    history.append(f"Human: {question}")
    history.append(f"AI: {response}")

    # Update Summary
    if len(history) > MAX_MESSAGES:

        old_messages = history[:-MAX_MESSAGES]
        old_messages_text = "\n".join(old_messages)

        summary = summary_chain.invoke({
            "old_messages": old_messages_text,
            "previous_summary": summary
        })

        # Keep Only Recent Messages
        history = history[-MAX_MESSAGES:]

    return response