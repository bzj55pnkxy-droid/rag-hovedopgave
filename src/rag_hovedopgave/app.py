from typing import Dict, List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_ai_sdk import AIStreamBuilder, ai_endpoint
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage

from .models import ChatRequest

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = ChatAnthropic(model="claude-haiku-4-5-20251001", streaming=True)


@app.post("/api/chat")
@ai_endpoint()
async def root(request: ChatRequest):
    langchain_messages = []
    for msg in request.messages:
        text_content = msg.content
        if not msg.content and msg.parts:
            for part in msg.parts:
                if part.get("type") == "text":
                    text_content = part.get("text")
                    break
        if msg.role == "user":
            langchain_messages.append(HumanMessage(content=text_content))
        elif msg.role == "assistant":
            langchain_messages.append(AIMessage(content=text_content))
    result = model.invoke(langchain_messages)
    builder = AIStreamBuilder()
    builder.text(result.content)
    return builder


# =============================================================================
# EXAMPLE: How to extract content from parts when msg.content is None
# =============================================================================
# text_content = msg.content
# if not text_content and msg.parts:
#     for part in msg.parts:
#         if part.get("type") == "text":
#             text_content = part.get("text")
#             break
# =============================================================================


# =============================================================================
# EXAMPLE: Using fastapi-ai-sdk for streaming responses
# =============================================================================
# Step 1: Import from fastapi_ai_sdk
# from fastapi_ai_sdk import AIStreamBuilder, ai_endpoint
#
# Step 2: Add @ai_endpoint() decorator AFTER @app.post()
# @app.post("/api/chat")
# @ai_endpoint()
# async def root(request: ChatRequest):
#     ...your message conversion logic...
#     result = model.invoke(langchain_messages)
#
#     # Step 3: Use AIStreamBuilder instead of returning dict
#     builder = AIStreamBuilder()
#     builder.text(result.content)
#     return builder
# =============================================================================
