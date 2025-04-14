# 📝 Django RESTful BlogPost API

A simple RESTful API built with **Django** and **Django REST Framework** for performing CRUD operations on blog posts.

---

## 📌 Project Overview

This API allows you to:
- ✅ Create blog posts
- 🔍 Read (list/retrieve) blog posts
- ✏️ Update existing blog posts
- ❌ Delete blog posts

It follows RESTful design principles, making it easy to integrate into any frontend (React, Vue, mobile apps, etc.).

---

## ⚙️ Technologies Used

| Tool                      | Purpose                          |
|---------------------------|----------------------------------|
| Python                    | Backend programming language     |
| Django                    | Web framework                    |
| Django REST Framework     | API toolkit for Django           |
| Environs                  | Manage environment variables     |

---

## 
- Each endpoint calls a **View**, which uses a **Serializer** to interact with the **Model** (BlogPost).

---

## 🔗 API Endpoints

| Method | URL                        | Description                     |
|--------|----------------------------|---------------------------------|
| GET    | `/blogposts/`              | List all blog posts             |
| POST   | `/blogposts/`              | Create a new blog post          |
| GET    | `/blogposts/<int:pk>/`     | Retrieve a specific blog post   |
| PUT    | `/blogposts/<int:pk>/`     | Update an existing blog post    |
| DELETE | `/blogposts/<int:pk>/`     | Delete a specific blog post     |

Test endpoints via:
- Django's Browsable API: [http://127.0.0.1:8000/blogposts/](http://127.0.0.1:8000/blogposts/)
- Postman or any HTTP client

---

## 🛠️ Getting Started

### 1. Clone the Repository


git clone https://github.com/MondeNel/Django_RESTFUL_API.git
cd Django_RESTFUL_API

### 2. Create and Activate Virtual Environment
```
python -m venv venv

- source venv/Scripts/activate    # Git Bash (Windows)

- venv\Scripts\activate           # CMD (Windows)

- source venv/bin/activate        # macOS/Linux
```

### 3. Install Requirements
```
pip install -r requirements.txt
```
### 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```
python manage.py runserver
```

📍 Open in browser: http://127.0.0.1:8000/blogposts/








