from fastapi import FastAPI, Body

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World!"}


@app.get('/contact')
async def root():
    return {"Name": "Bhawesh Chaudhary", "Phone Number": 8374734258}


@app.post("/createposts")
async def create_post(payloads: dict = Body(...)):
    print(payloads)
    return {"new posts": f"Title: {payloads['title']} Content: {payloads['content']}"}