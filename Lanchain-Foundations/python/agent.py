from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent

# llm = OllamaLLM(model = "llama3.2:1b")


# # 2. Create a prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant. Answer the user's query."),
#     ("human", "{text}")
# ])

# # 3. Create a chain
# # The pipe operator `|` chains the components together: Prompt | Model | Output Parser
# chain = prompt | llm | StrOutputParser()

# # 4. Invoke the chain to get a response
# response = chain.stream({"text": "I love large language models"})
# print(response)

from langchain.agents import create_agent

llm = ChatOllama(model="llama3.2:1b")


def send_email(to: str, subject: str, body: str):
    """Send an email"""
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    # ... email sending logic

    return f"Email sent to {to}"

def web_search(user_request: str):
    """Search in web about the content the user has asked for"""


agent = create_agent(
    llm,
    tools=[send_email],
    system_prompt="You are an email assistant. Always use the send_email tool.",
)