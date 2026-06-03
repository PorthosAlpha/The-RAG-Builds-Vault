from llama_index.llms.ollama import Ollama

# Initialize the model you pulled
# On 8GB RAM, we use a generous timeout to allow for 'Thinking' time
llm = Ollama(model="deepseek-r1:8b", request_timeout=360.0)

print("--- AI Logic Test: Nuclear Biomolecular + Financial Futures ---")

prompt = (
    "Briefly explain how molecular stability in a nuclear environment "
    "could theoretically act as a leading indicator for financial commodity futures."
)

response = llm.complete(prompt)
print(f"\nAI RESPONSE:\n{response}")
