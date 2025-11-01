from flask import Flask, render_template, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

@app.route('/')
def index():
    return "Hello! Your Flask app is running!"

@app.route('/test-db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Database connected! Version: {db_version}"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
```

## Step 2: Create a `.env` File for Local Development

Create a file called `.env` in your project folder:
```
DATABASE_URL=postgresql://username:password@localhost:5432/mydatabase
```

(We'll update this with the real Railway database URL later)

## Step 3: Create `.gitignore`

Create a file called `.gitignore` to keep secrets out of Git:
```
venv/
.env
__pycache__/
*.pyc
