from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import sqlite3
import os
from openai import OpenAI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# OpenAI API Key
OPENAI_API_KEY = "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"  # Replace with your actual OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Models
class User(BaseModel):
    name: str
    position: str

class Review(BaseModel):
    from_id: str
    to_id: str
    review: str

class FinalReviewRequest(BaseModel):
    user_id: str

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('hackathon.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create User Endpoint
@app.post("/user")
async def create_user(user: User):
    user_id = str(uuid4())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user (id, name, position) VALUES (?, ?, ?)', (user_id, user.name, user.position))
    conn.commit()
    conn.close()
    return {"user_id": user_id, "name": user.name, "position": user.position}

# Submit Review Endpoint
@app.post("/submit_review")
async def submit_review(review: Review):
    review_id = str(uuid4())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ureview (id, from_id, to_id, review) VALUES (?, ?, ?, ?)', 
                   (review_id, review.from_id, review.to_id, review.review))
    conn.commit()
    conn.close()
    return {"review_id": review_id, "message": "Review submitted successfully."}

# Generate Final Review (AI) Endpoint
@app.post("/generate_final_review")
async def generate_final_review(request: FinalReviewRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT review FROM ureview WHERE to_id = ?', (request.user_id,))
    reviews = cursor.fetchall()
    
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this user")
    
    review_texts = [review['review'] for review in reviews]
    final_summary = generate_summary(review_texts, batch_size=5)
    
    final_review_id = str(uuid4())
    cursor.execute('INSERT INTO freview (id, userid, review) VALUES (?, ?, ?)', 
                   (final_review_id, request.user_id, final_summary))
    conn.commit()
    conn.close()
    
    return {"final_review_id": final_review_id, "final_summary": final_summary}

# Helper functions for summarization
def summarize_reviews(reviews_chunk):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes people reviews."},
            {"role": "user", "content": f"Here are some reviews, summarize in a few lines: {reviews_chunk}"}
        ],
        max_tokens=300,
        temperature=0.5
    )
    return response.choices[0].message.content

def generate_summary(reviews, batch_size):
    summaries = []
    for i in range(0, len(reviews), batch_size):
        reviews_chunk = " ".join(reviews[i:i + batch_size])
        summary = summarize_reviews(reviews_chunk)
        summaries.append(summary)
    
    final_summary = summarize_reviews(" ".join(summaries))
    return final_summary

# Routes to render pages
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/submit-review")
async def submit_review_page(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.get("/generate-summary")
async def generate_summary_page(request: Request):
    return templates.TemplateResponse("summary.html", {"request": request})
