import logging
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import os
load_dotenv()

logging.getLogger('transformers').setLevel(logging.ERROR)  #Python logging system's setting

CHROMA_STORE="chroma_store"
COLLECTION="faq"
CSV_PATH=os.path.join("database", "faq.csv")
EMBED_MODEL="sentence-transformers/all-MiniLM-L6-v2"

def load_faq_documents(csv_path:str):
  df=pd.read_csv(csv_path)
  docs=[]
  for _, row in df.iterrows():
    content=f"Q: {row['question']}\nA: {row['answer']}"
    docs.append(Document(page_content=content, metadata={"source":"faq_Source", "category": row['category'], "faq_id": str(row['id'])}))
  return docs
    
def main():
  print(f"Loading FAQ documents....")
  docs =load_faq_documents(CSV_PATH)
  print(f"length of document={len(docs)}")
  
  print("Initializing Embedding Model")
  embeddings=HuggingFaceEmbeddings(model_name=EMBED_MODEL)
  
  print(f"Embedding and storing at chroma collection: '{COLLECTION}'....")
  vector_store=Chroma.from_documents(documents=docs,
                                     embedding=embeddings,
                                     collection_name=COLLECTION,
                                     persist_directory=CHROMA_STORE)
  print(f"Vectors stored. Total {vector_store._collection.count()} vectors stored")
  

if __name__ == "__main__":
  main()
  

    
  
  