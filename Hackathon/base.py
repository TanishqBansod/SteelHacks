from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import uuid

app = FastAPI()

class User(BaseModel):
    name: str
    position: str
    review: str = None

def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.post("/add_user")
def add_user(user: User):
    try:
        # Insert data into the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, position, review) VALUES (?, ?, ?)", (user.name, user.position, user.review))
        conn.commit()
        conn.close()

        return {"message": "User added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)