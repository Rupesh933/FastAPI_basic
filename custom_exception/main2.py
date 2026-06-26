from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()

def verify_token(x_token: str = Header()):
    if x_token != "abcdefgh123":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return x_token

@app.get('/profile')
def get_token(token: str = Depends(verify_token)):
    return{
        "message": 'Welcome Rupesh',
        "token": token
    }