# Smart ToDo API 📝

*A secure, scalable REST API for task management*

## 📌 Overview

**Smart ToDo API** is a backend RESTful service built with **FastAPI** and **MongoDB**, providing secure user authentication and full CRUD operations for task management.
The project demonstrates clean backend architecture, JWT-based authentication, environment-based configuration, and production-ready API design.

This project is suitable for **real-world applications**, **backend interviews**, and **portfolio review**.

---

## 🚀 Features

* User registration & login (JWT authentication)
* Secure password hashing
* Auth-protected endpoints
* Create, read, update, and delete tasks
* MongoDB integration with proper connection lifecycle
* Request validation using Pydantic
* Environment-based configuration
* Interactive API documentation (Swagger UI)

---

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database:** MongoDB
* **Authentication:** JWT (OAuth2 Password Flow)
* **ORM/Driver:** Motor (Async MongoDB)
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Language:** Python 3.10+

---

## 📂 Project Structure

```
smart-todo-api/
│
├── app/
│   ├── main.py              # Application entry point
│   ├── config/              # Settings & database configuration
│   ├── models/              # Database models
│   ├── schemas/             # Request/response schemas
│   ├── routers/             # API routes
│   ├── utils/               # Auth & helper utilities
│   └── __init__.py
│
├── .env.example             # Environment variables template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/RanoshisDas/smart-todo-api.git
cd smart-todo-api
```

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create a `.env` file using the example:

```bash
cp .env.example .env
```

Update values if needed:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=smart_todo_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
```

---

### 5️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Once the server is running:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **OpenAPI JSON:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🔐 Authentication Flow

1. Register a user → `/api/auth/register`
2. Login → `/api/auth/login`
3. Receive JWT access token
4. Pass token in headers:

```
Authorization: Bearer <your_token>
```

5. Access protected endpoints (`/tasks`, `/auth/me`)

---

## 🧪 API Endpoints (Summary)

### Auth

* `POST /api/auth/register` – Register user
* `POST /api/auth/login` – Login user
* `GET /api/auth/me` – Get current user

### Tasks

* `POST /api/tasks/` – Create task
* `GET /api/tasks/` – List tasks
* `GET /api/tasks/{id}` – Get task by ID
* `PUT /api/tasks/{id}` – Update task
* `DELETE /api/tasks/{id}` – Delete task

---

## ✅ Project Status

✔️ Fully functional
✔️ Authenticated CRUD operations
✔️ Interview-ready backend architecture

---

## 👨‍💻 Author

**Ranoshis Das**
B.Tech CSE (Data Science)
Backend & Android Developer

* GitHub: [https://github.com/RanoshisDas](https://github.com/RanoshisDas)
* Portfolio: *(add if available)*

---

## 📄 License

This project is licensed under the **MIT License**.

---