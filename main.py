from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend ishlayapti"}

@app.get("/health")
def health():
 
 return {"ok": True}