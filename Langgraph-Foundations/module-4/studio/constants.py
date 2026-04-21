from langchain_ollama import ChatOllama

# MODEL = "minimax-m2.5:cloud"
MODEL = "deepseek-v3.1:671b-cloud"
# MODEL = "qwen2.5:3b"
# MODEL = "glm-4.6:cloud"

# Use a deterministic temperature for structured output parsing
llm = ChatOllama(model=MODEL, temperature=0)

