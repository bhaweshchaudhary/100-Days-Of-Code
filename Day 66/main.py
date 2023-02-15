from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World!"}


@app.get('/contact')
async def root():
    return {"Name": "Bhawesh Chaudhary", "Phone Number": 8374734258}


@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    return {"new posts": f"Title: {payloads['title']} Content: {payloads['content']}"}