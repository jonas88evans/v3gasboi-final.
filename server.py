from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "V3gasboi is LIVE"}

@app.on_event("shutdown")
async def shutdown():
    pass
  
