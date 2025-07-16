# 🍬 Sweet Shop Management System

A simple and user-friendly **Sweet Shop Inventory System** built using **Python**, **Flask**, **SQLite**, and developed using **Test-Driven Development (TDD)** principles with `pytest`.

---

## ✨ Features Overview

| Feature         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| ➕ Add Sweet     | Add new sweets with unique ID, name, category, price, and quantity         |
| ❌ Delete Sweet  | Remove a sweet from the database                                            |
| 👁 View All      | Display all sweets in a well-structured table                               |
| 🔍 Search        | Filter sweets by **name**, **category**, or **price range**                |
| ⬆️ Sort          | Sort sweets by **name**, **category**, **price**, or **quantity**          |
| 🛒 Purchase      | Purchase sweets (quantity reduces automatically; prevents stock underflow) |
| 🔁 Restock       | Restock sweets (increases quantity)                                         |
| 🎨 Frontend      | Simple Bootstrap 5-based web interface using Flask                          |

---

## ✅ Test-Driven Development (TDD)

- Developed using **TDD principles**.
- Test cases written **before implementing functionality**.
- Full test suite included (`pytest`).
- All core functions are covered.

### 🧪 Run Tests
```
pytest test_sweetshop.py > test_report.txt
```
---


# 💻 Technologies Used

- Python 3

- Flask (web framework)

- SQLite (database)

- Bootstrap 5 (frontend styling)

- Pytest (unit testing)

---


## 📂 Project Structure
```
Sweet-Shop/
├── sweetshop.py           # Core logic (Add, Delete, Search, Sort, etc.)
├── test_sweetshop.py      # Unit tests for all features
├── test_report.txt        # Output file from pytest
├── sweetshop.db           # SQLite database file
├── flask_app/
│   ├── app.py             # Flask web server
│   └── templates/
│       └── index.html     # HTML UI with Bootstrap
└── README.md              # Project documentation

```

---

## 🛠️  How to Run the Web App

### 1. Install Flask
```
pip install pytest
```

### 2. Run the Flask App
```
cd flask_app
python app.py
```

# 📸 UI Preview
![Sweet Shop Preview](https://github.com/riteshb040/sweet-shop-management-system/blob/main/images/Sweet_shop.png)


---

# 👨‍💻 Author


**Ritesh Bavaliya**  
Python Developer | TDD Practitioner  
GitHub: [@riteshb040](https://github.com/riteshb040)

---

## 📄 License

This project is part of the Incubyte TDD Assessment and is intended for learning and evaluation purposes only.
