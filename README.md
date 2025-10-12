# 🧰 Property Maintenance Lite

**A lightweight Django REST Framework (DRF) application** that models property maintenance workflows — including properties, work orders, notes, and assignments.  
Built as a production-quality demo to showcase software engineering discipline, testing, CI/CD, and deployment best practices.

---

## 🚀 Live Demo
**Swagger API Docs:** [https://property-maintenance-lite.onrender.com/api/docs/](https://property-maintenance-lite.onrender.com/api/docs/)

---

## 🧩 Features

- Django + Django REST Framework backend
- API schema via **drf-spectacular** (`/api/schema/`)
- Interactive API docs via **Swagger UI**
- CRUD endpoints for:
  - `Property`
  - `WorkOrder`
  - Work order notes, status transitions, and assignments
- Automated testing with **pytest**
- Linting and formatting enforced by:
  - `black`
  - `isort`
  - `flake8`
- Pre-commit hooks for consistent code quality
- Dockerized for consistent local development
- Continuous Deployment on **Render.com**

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Backend Framework** | Django 5 + Django REST Framework |
| **API Schema / Docs** | drf-spectacular + Swagger UI |
| **Testing** | Pytest + pytest-django |
| **Code Quality** | Black, Isort, Flake8, Pre-commit hooks |
| **Database** | SQLite (default) |
| **Containerization** | Docker |
| **Deployment** | Render.com |

---

## ⚙️ Local Development

```bash
# Clone repository
git clone https://github.com/joshzd/property-maintenance-lite.git
cd property-maintenance-lite

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # (Windows)
# or
source .venv/bin/activate   # (macOS/Linux)

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Run tests
pytest -q

# Run development server
python manage.py runserver
```

Then open:  
➡️ [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

---

## 🧪 Testing

All test cases are located in `core/tests/test_api.py`.

```bash
pytest -q
```

✅ Output (all tests passing):
```
core/tests/test_api.py .....                                            [100%]
5 passed in 0.25s
```

---

## 🧱 Project Structure

```
property-maintenance-lite/
│
├── app/                 # Main Django project settings & URLs
├── core/                # Domain logic: models, serializers, views, tests
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests/
│
├── requirements.txt
├── Dockerfile
├── pytest.ini
├── .flake8
├── .pre-commit-config.yaml
└── README.md
```

---

## 👨‍💻 Author

**Joshua Davis**   
📍 Black Hawk, SD  
🔗 [GitHub: @joshzd](https://github.com/joshzd)

---

## 🧠 Notes

- The goal of this project is to demonstrate:
  - backend design and modular architecture
  - testing and CI/CD proficiency
  - deployment and API documentation
- It’s intentionally minimal — easy to expand with authentication, PostgreSQL, or front-end integration.

---

### 🏁 Summary

A clean, modern Django REST API project demonstrating **end-to-end software engineering best practices** — from local dev setup through automated testing and cloud deployment.
