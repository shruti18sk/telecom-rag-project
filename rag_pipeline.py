from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from retriever import build_retriever
from langchain_groq import ChatGroq

def format_docs(docs: list[Document]) -> str:
    sections = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown").upper()
        sections.append(f"[{source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(sections)

SYSTEM_PROMPT= """You are a helpful and professional telecom customer care assistant.
Your job is to help customers resolve technical issues with their mobile service.

Use ONLY the context below to answer the customer's question.
The context comes from two sources:
- FAQ entries (general policy and how-to information)
- Past support tickets (real resolved cases with step-by-step resolutions)

If the context does not contain enough information to answer confidently, say so clearly
and suggest the customer call 611 or use the MyTelecom app.

Context:
{context}
"""

def build_chain():
  retriever=build_retriever()
  
  prompt=ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", "{question}")])

  llm=ChatGroq(model='qwen/qwen3.8-27b', temperature=0, reasoning_format='parsed')

  chain= ({"context": retriever | format_docs, "question": RunnablePassthrough()}
        |prompt
        |llm
        |StrOutputParser())
  
  return chain


