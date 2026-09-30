from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import pandas as pd
import logging
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

logging.getLogger('transformers').setLevel(logging.ERROR)

CHROMA_DIR='chroma_store'
COLLECTION='tickets'
DB_PATH=os.path.join('database', 'tickets.db')
EMBED_MODEL='sentence-transformers/all-MiniLM-L6-v2'

def load_ticket_documents(db_path:str):
  conn=sqlite3.connect(db_path)
  conn.row_factory=sqlite3.Row
  rows=conn.execute("SELECT * FROM tickets_file WHERE STATUS= ?", ('resolved',)).fetchall()
  conn.close()
  docs=[]
  for row in rows:
    content= (
                f"Issue: {row['ISSUE_TYPE']}\n"
                f"Description: {row['DESCRIPTION']}\n"
                f"Resolution: {row['RESOLUTION']}"
            )
    docs.append(Document(page_content=content,
                         metadata={
                           "source": "ticket",
                           "ticket_id": row['TICKET'],
                           "category": row['CATEGORY'],
                           "status": row['STATUS'],
                         },))
  return docs

def main():
    print("Loading ticket documents from SQLite...")
    docs = load_ticket_documents(DB_PATH)
    print(f"  {len(docs)} resolved tickets loaded.")

    print("Initialising embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    print(f"Embedding and storing in Chroma collection '{COLLECTION}'...")
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION,
        persist_directory=CHROMA_DIR,
    )
    print(f"  Done. {vectorstore._collection.count()} vectors stored.")
    
if __name__ == "__main__":
  main()