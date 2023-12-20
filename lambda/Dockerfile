FROM public.ecr.aws/lambda/python:3.10

WORKDIR /app

RUN pip install --upgrade pip --no-cache-dir

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY lambda_function.py .

CMD [ "lambda_function.handler" ]