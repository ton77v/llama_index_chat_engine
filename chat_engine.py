import os

from dotenv import load_dotenv
from llama_index.core.chat_engine.types import StreamingAgentChatResponse
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


msg1 = "Hello, my name is A"
msg2 = "What's my name?"


def try_simple() -> None:
    resp = chat_engine.chat(msg1)
    print(resp)
    print(chat_engine.chat_history)
    resp2 = chat_engine.chat(msg2)  # Your name is A. How can I help you today, A?
    print(resp2)


def print_stream(resp: StreamingAgentChatResponse) -> None:
    for token in resp.response_gen:
        print(token, end="", flush=True)
    print("\n")


def try_stream() -> None:
    resp = chat_engine.stream_chat(msg1)
    print_stream(resp)
    print(chat_engine.chat_history)
    resp2 = chat_engine.stream_chat(msg2)
    print_stream(resp2)


if __name__ == "__main__":
    print("Simple chat")
    try_simple()
    print("\n\nStreaming chat")
    try_stream()