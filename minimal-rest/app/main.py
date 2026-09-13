import os

import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "todos")
DB_USER = os.getenv("DB_USER", "todo")
DB_PASSWORD = os.getenv("DB_PASSWORD", "todo")


class Todo(BaseModel):
    title: str


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


@app.get("/todos")
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title FROM todos ORDER BY id")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [{"id": row[0], "title": row[1]} for row in rows]


@app.post("/todos")
def create_todo(todo: Todo):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO todos (title) VALUES (%s) RETURNING id, title",
        (todo.title,),
    )

    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": row[0],
        "title": row[1],
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT 1")

        cur.close()
        conn.close()

        return {"status": "ready"}

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="database unavailable",
        )
