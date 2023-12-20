from fastapi import FastAPI

app = FastAPI(
  title='langchain server',
  version='0.1.0',
  description='langchain server'
)

@app.get('/')
async def root():
  return { 'message': 'Hello Workd!' }

if __name__ == '__main__':
  import uvicorn

  uvicorn.run(app, host='0.0.0.0', port=8080)