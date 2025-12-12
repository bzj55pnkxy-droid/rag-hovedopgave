import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_ai_sdk import (
    AIStreamBuilder,
    ai_endpoint,
    create_ai_stream_response,
)
from fastapi_ai_sdk.models import (
    FinishEvent,
    StartEvent,
    TextDeltaEvent,
    TextEndEvent,
    TextStartEvent,
)
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

    async def stream_response():
        message_id = f"txt_{uuid.uuid4().hex[:8]}"
        text_id = f"txt_{uuid.uuid4().hex[:8]}"

        yield StartEvent(message_id=message_id).to_sse()

        yield TextStartEvent(id=text_id).to_sse()

        async for chunk in model.astream(langchain_messages):
            yield TextDeltaEvent(id=text_id, delta=chunk.content).to_sse()

        yield TextEndEvent(id=text_id).to_sse()

        yield FinishEvent().to_sse()

    return create_ai_stream_response(stream_response())
