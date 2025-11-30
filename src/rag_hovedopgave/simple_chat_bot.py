from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

messages = []

while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))

    response = model.invoke(messages)
    messages.append(response)

    print(f"Assistant: {response.content}\n")
    print(response.response_metadata)