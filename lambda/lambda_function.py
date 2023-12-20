import boto3
import urllib.parse

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

AWS_BUCKET = 'chatbot-data-storage'


def s3PdfDoader(s3_path):
    bucket = boto3.resource('s3').Bucket(AWS_BUCKET)
    pdf_obj = bucket.Object(s3_path).get()['Body'].read()
    tmp_path = f'/tmp/{s3_path.split("/")[-1]}'

    print('pdf_obj: ', pdf_obj)
    print('tmp_path: ', tmp_path)

    with open(tmp_path, 'wb') as f:
        f.write(pdf_obj)
        print('f: ', f)

    return PyPDFLoader(tmp_path)


def handler(event, context):
    s3_path = urllib.parse.unquote(
        event['Records'][0]['s3']['object']['key']
    )

    print('s3_path: ', s3_path)

    
    loader = s3PdfDoader(s3_path)
    documents = loader.load_and_split(
        text_splitter=CharacterTextSplitter(
            separator='\n',
            chunk_size=200,
            chunk_overlap=20
        )
    )
    
    print('documents: ', documents)