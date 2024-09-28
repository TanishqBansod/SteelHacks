from fastapi import FastAPI
from uuid import uuid4
import sqlite3
from pydantic import BaseModel

app = FastAPI()
conn = sqlite3.connect('hackathon.db')

cursor = conn.cursor()

class User(BaseModel):
    name: str
    position: str

## create user table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL
    )
''')

## create review table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ureview (
        id TEXT PRIMARY KEY,
        from_id TEXT NOT NULL,
        to_id TEXT NOT NULL,
        review TEXT NOT NULL
    )
''')

## create final review
cursor.execute('''
    CREATE TABLE IF NOT EXISTS freview (
        id TEXT PRIMARY KEY,
        userid TEXT NOT NULL,
        review TEXT NOT NULL
    )
''')
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/user")
async def create_user(user: User):
    print("test")
    user_id = str(uuid4())
    # make a db call to store new user information
    cursor.execute('''
            INSERT INTO user (id, name, position)
            VALUES (?, ?, ?)
        ''', (user_id, user.name, user.position))
    conn.commit()
    return {"user_id": user_id, "name": user.name, "position": user.position}

@app.get("/user_info")
async def read_user():
    # make a db call to fetch user information if exists
    cursor.execute('SELECT * FROM user')
    all_users = cursor.fetchall()
    user_str = ""
    print("All users in the database:")
    for user in all_users:
        user_str += user[0] + " " + user[1]
    return {"item_id": user_str}


# @app.get("/final_review")
# async def final_review(user_id: str):
#     # make a db call table3 that contains the final one liner review
#     return {"item_id": item_id, "query": q}


