import ollama

# initialize the ollama client
client = ollama.Client()

# Define the model and input prompt
model = "mario"
prompt = "How to use ollama and free minimax model in vscode in mac?"

# send the query to the model
response = client.generate(model=model, prompt=prompt)

# print the response from the model
print("response from ollama..")
print(response.response)