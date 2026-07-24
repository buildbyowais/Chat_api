# Chat API with Conversation Summary

## Description

This project is a FastAPI-based Chat API integrated with Google Gemini using LangChain. It accepts a user's question through a POST endpoint and returns an AI-generated response. The application maintains recent conversation history and automatically summarizes older messages to preserve context while keeping memory usage efficient.

## Features

* FastAPI REST API
* Google Gemini Integration
* LangChain Prompt Templates
* Conversation History Management
* Automatic Conversation Summarization
* JSON Request and Response

## Technologies Used

* Python
* FastAPI
* LangChain
* Google Gemini API
* python-dotenv

## API Endpoint

**POST** `/chat`

### Request

```json
{
  "question": "What is Artificial Intelligence?"
}
```

### Response

```json
{
  "answer": "Artificial Intelligence is..."
}
```

## How It Works

1. The user sends a question to the API.
2. The system retrieves the recent conversation history.
3. Older messages are summarized to maintain context.
4. The AI generates a response using the summary, recent messages, and current question.
5. The conversation history is updated for future requests.
