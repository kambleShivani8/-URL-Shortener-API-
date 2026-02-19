# 🔗 URL Shortener API (FastAPI + SQLAlchemy + SQLite)

This is a beginner-friendly **URL Shortener** backend project built using **FastAPI**, **SQLAlchemy ORM**, and **SQLite**.  
It converts a long URL into a short link (code) and redirects users when they open the short link.

---

## ✅ What is FastAPI?
**FastAPI** is a Python framework used to create **REST APIs** very quickly. It automatically gives:
- ✅ Swagger UI for testing APIs (`/docs`)
- ✅ Fast performance
- ✅ Input validation using **Pydantic**

---

## ✨ Features
- ✅ Create short URL from any long URL (**POST** `/shorten`)
- ✅ Redirect to original URL using code (**GET** `/{code}`)
- ✅ Show click count and created time (**GET** `/stats/{code}`)
- ✅ **Custom Alias**: user can give a custom name instead of random code (example: `/shivani`)
- ✅ **QR Code**: generate QR for the short link (**GET** `/qr/{code}`)
- ✅ SQLite database file stores your short links

---

## 🧱 Technologies Used
- **FastAPI** (API framework)
- **Uvicorn** (server to run FastAPI)
- **SQLAlchemy** (ORM to connect Python with DB)
- **SQLite** (database stored as `.db` file)
- **Pydantic** (validates request/response data)
- **python-dotenv** (reads `.env` file)
- **qrcode[pil]** (creates QR images)

---
## 🧱 Technologies Used
- **FastAPI** (API framework)
- **Uvicorn** (server to run FastAPI)
- **SQLAlchemy** (ORM to connect Python with DB)
- **SQLite** (database stored as `.db` file)
- **Pydantic** (validates request/response data)
- **python-dotenv** (reads `.env` file)
- **qrcode[pil]** (creates QR images)

---

## 📁 Project Structure
url_shortener/
app/
main.py
database.py
models.py
schemas.py
routers/
shortener.py
.env

---

## 📌 Libraries / Packages (Why we use them)
Install these packages:
- **fastapi** → create API endpoints
- **uvicorn** → run the FastAPI app
- **sqlalchemy** → database operations (insert/select/update)
- **python-dotenv** → load `.env` file values
- **pydantic** → validation (example: URL must be valid)
- **qrcode[pil]** → generate QR code images

---

## ⚙️ How to Run This Project (Beginner Steps)

### ✅ Step 1: Open CMD / Terminal
Open **Command Prompt** or **VS Code Terminal**.

### ✅ Step 2: Go to Desktop (Example)

cd Desktop
cd Desktop
### ✅ Step 3: Go inside your project folder

cd url_shortener

### ✅ Step 4: Create virtual environment (recommended)

python -m venv venv

### ✅ Step 5: Install packages

pip install fastapi uvicorn sqlalchemy python-dotenv pydantic qrcode[pil]

### 🧾 Create .env File (Important)

DATABASE_URL=sqlite:///shortener.db
BASE_URL=http://127.0.0.1:8000

✅ DATABASE_URL → tells which database to use
✅ BASE_URL → used to generate short link output

### ▶️ Run Server

From the project root folder:

uvicorn app.main:app --reload


### Now open:

Home: http://127.0.0.1:8000/

Swagger UI: http://127.0.0.1:8000/docs

### Steps to Test on Swagger (FastAPI)
✅ Test 1: Shorten a URL (POST /shorten)

Open Swagger UI: http://127.0.0.1:8000/docs

Find POST /shorten

Click Try it out

Paste request body:

{
  "url": "https://www.google.com/"
}


Click Execute

✅ Example output:

{
  "code": "Ab12Xy",
  "short_url": "http://127.0.0.1:8000/Ab12Xy",
  "original_url": "https://www.google.com/"
}

✅ Test 2: Custom Alias (POST /shorten)

Use alias instead of random code:

{
  "url": "https://github.com/kambleshivani8",
  "alias": "shivani"
}


✅ Output short link will look like:

http://127.0.0.1:8000/shivani

✅ Test 3: Redirect (GET /{code})

Copy the code from response (example: Ab12Xy or shivani)

Open in browser:

http://127.0.0.1:8000/Ab12Xy

http://127.0.0.1:8000/shivani

✅ It redirects to the original URL.

✅ Test 4: Stats (GET /stats/{code})

Open:

http://127.0.0.1:8000/stats/Ab12Xy

✅ You will see clicks + created time.

✅ Test 5: QR Code (GET /qr/{code})

Open:

http://127.0.0.1:8000/qr/Ab12Xy
(or)

http://127.0.0.1:8000/qr/shivani

✅ It will return a QR image for the short link.

### 🌐 Live Demo Link (After Deployment)

After deploying to Render/Railway, paste your links here:

Live API: https://yourapp.onrender.com

Swagger Docs: https://yourapp.onrender.com/docs


## 📁 Project Structure

