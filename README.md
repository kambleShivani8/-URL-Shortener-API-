🔗 URL Shortener API (FastAPI + SQLAlchemy + SQLite)
This is a beginner-friendly URL Shortener backend project built using FastAPI, SQLAlchemy ORM, and SQLite. It converts a long URL into a short link (code) and redirects users when they open the short link.

✅ What is FastAPI?
FastAPI is a Python framework used to create REST APIs very quickly. It automatically gives:

✅ Swagger UI for testing APIs (/docs)
✅ Fast performance
✅ Input validation using Pydantic
✨ Features
✅ Create short URL from any long URL (POST /shorten)
✅ Redirect to original URL using code (GET /{code})
✅ Show click count and created time (GET /stats/{code})
✅ SQLite database file stores your short links
🧱 Technologies Used
FastAPI (API framework)
Uvicorn (server to run FastAPI)
SQLAlchemy (ORM to connect Python with DB)
SQLite (database stored as .db file)
Pydantic (validates request/response data)
python-dotenv (reads .env file)
📁 Project Structure
url_shortener/ app/ init.py main.py database.py models.py schemas.py routers/ init.py shortener.py .env requirements.txt

📌 Libraries / Packages (Why we use them)
Install these packages:

fastapi → to create API endpoints
uvicorn → to run the FastAPI app
sqlalchemy → database operations (insert/select/update)
python-dotenv → load .env file values
pydantic → validation (ex: URL must be valid)
⚙️ How to Run This Project (Beginner Steps)
✅ Step 1: Open CMD / Terminal
Open Command Prompt or VS Code Terminal.

✅ Step 2: Go to Desktop (Example)
cd Desktop

✅ Step 3: Go inside your project folder
cd url_shortener

✅ Step 4: Create virtual environment (recommended)
python -m venv venv

✅ Step 5: Install packages
pip install fastapi uvicorn sqlalchemy python-dotenv pydantic

Create .env File (Important)
In the project root (same level as app/), create .env and paste:

DATABASE_URL=sqlite:///shortener.db BASE_URL=http://127.0.0.1:8000

✅ DATABASE_URL → tells which database to use ✅ BASE_URL → used to generate short link output

Run Server
From the project root folder:

uvicorn app.main:app --reload in command prompt

Now open: copy this url in browser

Swagger UI: http://127.0.0.1:8000/docs Home: http://127.0.0.1:8000/

Steps to test your URL Shortener on Swagger (FastAPI)
Run the server
In VS Code terminal (project root):

uvicorn app.main:app --reload

Open Swagger UI
Open this in browser: http://127.0.0.1:8000/docs

Test 1: Shorten a URL (POST /shorten)
In Swagger, find POST /shorten

Click it → click Try it out

In the Request body box, paste:

{ "url": "https://www.google.com/" }

Click Execute

You will get a response like:

{ "code": "Ab12Xy", "short_url": "http://127.0.0.1:8000/Ab12Xy", "original_url": "https://www.google.com/" }

Test 2: Redirect (GET /{code})
Copy the code from the response (example: Ab12Xy)

In Swagger, open GET /{code}

Click Try it out

Enter code: Ab12Xy

Click Execute

✅ It will return a redirect response (307). (For real redirect, open the short_url in browser.)

Test 3: Stats (GET /stats/{code})
In Swagger, open GET /stats/{code}

Click Try it out

Enter code: Ab12Xy

Click Execute ✅ You will see clicks + created time.

🌐 Live Demo Link (After Deployment)

After deploying to Render/Railway, paste your links here:

https://yourapp.onrender.com

https://yourapp.onrender.com/docs
