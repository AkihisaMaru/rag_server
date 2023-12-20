import boto3
import urllib.parse

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings

AWS_BUCKET = 'chatbot-data-storage'


def s3PdfDoader(s3_path):
    bucket = boto3.resource('s3').Bucket(AWS_BUCKET)
    pdf_obj = bucket.Object(s3_path).get()['Body'].read()
    tmp_path = f'/tmp/{s3_path.split("/")[-1]}'

    print('pdf_obj: ', pdf_obj)
    print('tmp_path: ', tmp_path)

    with open(tmp_path, 'wb') as f:
        f.write(pdf_obj)

    return PyPDFLoader(tmp_path)


def handler(event, context):
    embeddings = OpenAIEmbeddings()

    s3_path = urllib.parse.unquote(
        event['Records'][0]['s3']['object']['key']
    )

    print('s3_path: ', s3_path)

    
    loader = s3PdfDoader(s3_path)
  
    documents = loader.load()

    text = ''
    for x in documents:
        text = text + x.page_content
        print(x)

    print('text: ', text)

    # documents = loader.load_and_split(
    #     text_splitter=CharacterTextSplitter(
    #         separator='\n',
    #         chunk_size=200,
    #         chunk_overlap=20
    #     )
    # )
    # documents = loader.load_and_split()
    # documents = loader.load()
    
    print('documents: ', documents)

    vector_store = FAISS.from_documents(documents=documents, embedding=embeddings)
    print('vector_store: ', vector_store)

    serialized_vector_store = vector_store.serialize_to_bytes()
    print('serialized_vector_store: ', serialized_vector_store)
