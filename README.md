
## 🚀 Overview

This repository contains two distinct specialized modules designed to demonstrate advanced database operations, including CRUD (Create, Read, Update, Delete) operations, relational mapping, and automated data handling.

---

## 📂 Project Modules

### 🚗 1. Automotive & Customer Management System
This module is designed for managing vehicle inventories and customer relationships. It focuses on tracking high-value assets and their owners.

- Core Functionalities:
       *Vehicle Tracking: Extracts and stores car details including Model, Year of Manufacture, and Price.
           *Customer CRM: Manually or automatically manages customer records.
       *Smart Deletion: Features an intelligent deletion system where customer records can be removed or automatically purged, while ensuring the core vehicle/transaction data remains intact in the database.
- Key Files:
     `CarData.db` / `CarData_Relation.db` (Database files)
     `app1.py` (Core Logic)

---

### 🎓 2. Student Academic Record System
A specialized module for educational data management, focusing on tracking student progress and academic achievements.

- Core Functionalities:
     *Student Profiles: Stores student identities and academic details.
     *Grade Management: Records grades for various subjects.
     *Automated Passing Logic: Automatically marks and records grades only for subjects that the student has successfully passed.
     *Relational Data: Uses structured tables to link students to their specific grades and subjects.
- Key Files:
     `SchoolData.db` / `StudentsSimple.db` (Database files)
     `app2.py` (Core Logic)

---

## 🛠️ Technologies Used

| Technology | Role |
| :--- | :--- |
| Python | Primary Programming Language |
| SQLAlchemy | ORM for Database Management |
| SQLite | Lightweight Relational Database |

---

## ⚙️ Installation & Setup

1. Clone the repository:
   git clone https://github.com/karimhanaei-lang/sqlalchemy.git
   cd sqlalchemy
   

2. Install required dependencies:
   pip install sqlalchemy
   

3. Run a module:
   Navigate to the desired app and run it:
   python app1.py  # For Car Management
   # OR
   python app2.py  # For Student Management
   

---

## 👤 Author
Karim Hanaei*
- GitHub: @karimhanaei-lang

---
⭐ If you find this project helpful, please consider giving it a star!
```

---
