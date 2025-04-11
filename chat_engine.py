import os

from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core.chat_engine import SimpleChatEngine


load_dotenv()


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0,  # 0.1 def
    # max_tokens=256,
    # max_retries, timeout, etc
    #  etc
)

chat_engine = SimpleChatEngine.from_defaults(
    llm=llm,
    # chat_history,
    # memory,
    # system_prompt | prefix_messages
)

def try_simple() -> None:
    resp = chat_engine.chat("Hello, my name is A")
    print(resp)
    print(chat_engine.chat_history)
    resp2 = chat_engine.chat("What's my name?")  # Your name is A. How can I help you today, A?
    print(resp2)

if __name__ == "__main__":
    try_simple()