from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document





CHROMA_DIR='chroma_store'
EMBED_MODEL="sentence-transformers/all-MiniLM-L6-v2"

def build_retriever(k_faq: int=3, k_tickets: int=3, k_pdf:int=3)->RunnableLambda:
  embeddings=HuggingFaceEmbeddings(model_name=EMBED_MODEL)
  faq_store=Chroma(
    collection_name="faq",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR
  )
  tickets_store=Chroma(
    collection_name='tickets',
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR
  )
  pdf_store=Chroma(
    collection_name="telecom_pdf",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR
  )
  
  retriever_faq=faq_store.as_retriever(search_kwargs={"k":k_faq})
  retriever_tickets=tickets_store.as_retriever(search_kwargs={"k":k_tickets})
  retriever_pdf=pdf_store.as_retriever(search_kwargs={"k":k_pdf})
  
  def retrieve(query:str)->list[Document]:
    return(retriever_faq.invoke(query) + retriever_tickets.invoke(query) + retriever_pdf.invoke(query))
  
  return RunnableLambda(retrieve)
  


