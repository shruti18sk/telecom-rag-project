from langchain_huggingface import HuggingFaceEmbeddings
import logging
import pandas as pd
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import os

logging.getLogger('transformers').setLevel(logging.ERROR)

CHROMA_DIR="chroma_store"
COLLECTION="telecom_pdf"
PDF_PATH=os.path.join("database", "telecom_guide.pdf")
EMBED_MODEL="sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE=600
CHUNK_OVERLAP=100

def main():
  print("Loading PDF...")
  loader=PyPDFLoader(PDF_PATH)
  pages=loader.load()
  print(f"  {len(pages)} pages loaded.")
  
  print(f"Chunking (size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})...")
  splitter = RecursiveCharacterTextSplitter(
          chunk_size=CHUNK_SIZE,
          chunk_overlap=CHUNK_OVERLAP,
          separators=["\n\n", "\n", ".", " "],
      )
  chunks = splitter.split_documents(pages)
  
  for i, chunk in enumerate(chunks):
    
    chunk.metadata["source"] = "guide"
    chunk.metadata["chunk_index"] = i
  
  print(f"  {len(chunks)} chunks produced.")
  
  print("Initialising embedding model...")
  embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
  
  print(f"Embedding and storing in Chroma collection '{COLLECTION}'...")
  vectorstore = Chroma.from_documents(
          documents=chunks,
          embedding=embeddings,
          collection_name=COLLECTION,
          persist_directory=CHROMA_DIR,
      )
  print(f"  Done. {vectorstore._collection.count()} vectors stored.")
  
      


if __name__ == "__main__":
    main()