from fastapi import FastAPI

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