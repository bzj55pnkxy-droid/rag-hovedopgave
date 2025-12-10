from typing import Dict, List

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage
from fastapi.middleware.cors import CORSMiddleware

from rag_hovedopgave.models import ChatRequest

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
async def root(request: ChatRequest):
    result = model.invoke(request.messages)
    return result

