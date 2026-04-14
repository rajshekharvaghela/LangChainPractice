from langchain_ollama import ChatOllama

# MODEL = "minimax-m2.5:cloud"
# MODEL = "deepseek-v3.1:671b-cloud"
MODEL = "llama3.2:1b"

# Use a deterministic temperature for structured output parsing
llm = ChatOllama(model=MODEL, temperature=0)

