from fastapi import FastAPI
from pydantic import BaseModel
from app.service import review_code_with_gemini

app = FastAPI()

class ReviewRequest(BaseModel):
    code: str

@app.post("/review")
def review_code(request: ReviewRequest):
    review = review_code_with_gemini(request.code)
    return {"review": review}
