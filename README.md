# 🚗 Car Routes API (Flask)

## 📌 Description

This project is a simple Flask-based API that simulates a car company database.
It allows users to view available car models, retrieve details for a specific car, add new cars, and delete existing ones.

The application demonstrates RESTful routing and basic CRUD operations using Flask.

---

## 🧱 Project Structure

```
server/
│
├── app.py              # Main Flask application
├── testing/            # Test files
├── Pipfile             # Dependencies
├── Pipfile.lock
├── pytest.ini
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pipenv install
```

### 2. Activate virtual environment

```bash
pipenv shell
```

### 3. Run the server

```bash
python app.py
```

The app will run on:

```
http://127.0.0.1:5000
```

---

## 🚀 API Routes

### 1. Home Route

**GET /**
Returns a welcome message and available car models.

---

### 2. Get Specific Car

**GET /cars/<model>**

Example:

```
/cars/toyota
```

---

### 3. Add a New Car

**POST /cars**

Request Body (JSON):

```json
{
  "brand": "mercedes",
  "model": "Mercedes C200",
  "year": 2023,
  "price": 48000
}
```

---

### 4. Delete a Car

**DELETE /cars/<model>**

Example:

```
/cars/mercedes
```

---

## 🧠 Concepts Covered

* Flask routing
* RESTful APIs
* CRUD operations
* JSON handling
* Request validation

---

## ⚠️ Note

This project uses an in-memory dictionary as a database.
Data will reset every time the server restarts.

---

## 🔮 Future Improvements

* Connect to a real database (SQLite/PostgreSQL)
* Add PUT/PATCH routes for updating cars
* Add authentication
* Build a React frontend

---

## 👨‍💻 Author

Built as part of a Flask backend lab.
