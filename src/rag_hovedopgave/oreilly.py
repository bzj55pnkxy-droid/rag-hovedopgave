from anthropic.types import ModelParam
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_anthropic import ChatAnthropic
from langchain_core import messages
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# model = ChatAnthropic(model="claude-haiku-4-5-20251001", temperature=1)

model = init_chat_model("claude-haiku-4-5-20251001")

response = model.invoke("What's the capital of Denmark?")

print(response.text)

# system_message = [
#     SystemMessage("You're a helpful assistant that respondsto questions with three question marks")
# ]

# prompt = [HumanMessage("What's the capital of France?")]

# print(model.invoke([system_message, prompt]).text)
