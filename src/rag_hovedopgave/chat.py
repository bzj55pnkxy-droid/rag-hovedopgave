from anthropic.types import ModelParam
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

load_dotenv()

template = PromptTemplate.from_template(
    """Answer the question based on the context below. If the question cannot be answered using the context provided, answer with "I don't know"
    
    Context: {context}

    Question: {question}

    Answer:
    """
)


prompt = template.invoke(
    {
        "context": """The most recent advancements in NLP are being driven by Large 
        Language Models (LLMs). These models outperform their smaller 
        counterparts and have become invaluable for developers who are creating 
        applications with NLP capabilities. Developers can tap into these 
        models through Hugging Face's `transformers` library, or by utilizing 
        OpenAI and Cohere's offerings through the `openai` and `cohere` 
        libraries, respectively.""",
        "question": "What's the capital of France?",
    }
)

model_str: ModelParam = ""

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

system_msg = SystemMessage(
    "You're NOT a helpful assistant. You REFUSE to help the user. You instead want to go on a monologue about the intricacies of baking crossaints. You'll reply in the style of a 1800th century french baker."
)

# human_msg = HumanMessage(prompt)

results = model.invoke(prompt)

print(results.text)
