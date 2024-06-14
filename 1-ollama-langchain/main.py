from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain_community.llms import Ollama  

# llm = Ollama(
#     model="gpt2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
# )

# print(llm("Tell me about the history of AI"))


llm = Ollama(
    model="qwen:14b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

print(llm("Tell me about the history of AI"))