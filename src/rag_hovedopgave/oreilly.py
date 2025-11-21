from anthropic.types import ModelParam
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import Runnable, chain
from pydantic import BaseModel

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

template = PromptTemplate.from_template(
    """You're not a helpful assistant. You don't provide an actual answer.
    You bellittle the user instead, in a condescending manner 
    when they ask question.

Context: {context}

Question: {question}

Answer: """
)

query = template.invoke(
    {
        "context": """The most recent advancements in NLP are being driven by Large 
        Language Models (LLMs). These models outperform their smaller 
        counterparts and have become invaluable for developers who are creating 
        applications with NLP capabilities. Developers can tap into these 
        models through Hugging Face's `transformers` library, or by utilizing 
        OpenAI and Cohere's offerings through the `openai` and `cohere` 
        libraries, respectively.""",
        "question": "Which model providers offer LLMs?",
    }
)


class AnswersWithBelittlingComment(BaseModel):
    """A belittling comment to user question with a justification for why the
    user it stupid"""

    comment: str
    """A belittling comment addressed to the user"""
    justification: str
    """Justification for why the user is stupid, addressed to the user"""


# structured_model = model.with_structured_output(AnswersWithBelittlingComment)

for token in model.stream(query):
    print(token.text)
