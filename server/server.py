import os

from fastapi import FastAPI

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


app = FastAPI(
  title='langchain server',
  version='0.1.0',
  description='langchain server'
)




@app.get('/')
async def root():
  return { 'message': 'Hello World!' }

if __name__ == '__main__':
  import uvicorn

  uvicorn.run("server:app", host='0.0.0.0', port=8080, reload=True)