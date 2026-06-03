import os
import warnings
warnings.filterwarnings("ignore")
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# 1. Connect to the Chroma Database you just built
persist_dir = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

# 2. Connect to the AI Brain (Qwen running via Ollama)
llm = OllamaLLM(model="qwen") 

print("\n" + "="*60)
print("🧠 Conversational PhD Agent Online (GPU Accelerated)")
print("Ask natural questions. The AI will handle the keyword translation.")
print("Type 'exit' to quit.")
print("="*60 + "\n")

while True:
    user_query = input("\n🎙️ Dr. Moncriffe: ")
    if user_query.lower() in ['exit', 'quit']:
        print("Shutting down the lab. Goodbye, Doctor.")
        break
        
    print("\n⚙️  [Agent Thinking] Translating your thought into database keywords...")
    
    # --- AGENT STEP 1: Keyword Extraction ---
    keyword_prompt = f"Extract 3 to 5 highly specific noun keywords from this query to search an academic database. Return ONLY the keywords separated by commas, no introductory text. Query: {user_query}"
    search_terms = llm.invoke(keyword_prompt).strip()
    print(f"🔍  [Database Search] Sweeping vault for: {search_terms}")
    
    # --- AGENT STEP 2: Database Retrieval ---
    docs = vectordb.similarity_search(search_terms, k=6) 
    vault_evidence = "\n\n".join([doc.page_content for doc in docs])
    
    if not vault_evidence:
        print("⚠️ No direct evidence found for those terms. Try rephrasing.")
        continue
        
    print("📖  [Evidence Found] Synthesizing a doctoral response using Apple Silicon...")
    
    # --- AGENT STEP 3: Final Doctoral Synthesis ---
    synthesis_prompt = f"""You are an expert academic research assistant working for a researcher in Integrative Social Work. 
    Answer the following question using ONLY the provided evidence from the user's research vault.
    Maintain a highly academic, doctoral, and clinical tone. 
    If the evidence does not contain the answer, explicitly state that the vault does not contain the answer. Do not make up information.
    
    Question: {user_query}
    
    Vault Evidence:
    {vault_evidence}
    
    Doctoral Synthesis:"""
    
    response = llm.invoke(synthesis_prompt)
    
    print("\n" + "="*60)
    print("🤖 Qwen Synthesis:\n")
    print(response)
    print("="*60)
    
    with open("Research_Synthesis_Log.md", "a") as f:
        f.write(f"## Query: {user_query}\n**Keywords Searched:** {search_terms}\n\n**Synthesis:**\n{response}\n\n---\n")
    print("💾 Automatically saved to Research_Synthesis_Log.md")
