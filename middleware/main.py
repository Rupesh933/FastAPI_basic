from fastapi import FastAPI, Header, Request

app = FastAPI()

@app.middleware('http')
async def my_middleware(request: Request, call_next):
    print("Before Request")
    response = await call_next(request)
    print("After Response")
    return response


# Logging Example
@app.middleware('http')
async def log_request(request: Request, call_next):
    print(f'Path: {request.url.path}')
    print(f'Method: {request.method}')
    response = await call_next(request)
    print(f'Status Code: {response.status_code}')
    return response