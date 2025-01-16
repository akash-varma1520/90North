# Full Stack Web Project

This project is a full-stack web application combining a **frontend** and a **backend** to demonstrate a responsive web interface and backend services.


---

## 🌟 Features

- **Frontend**:
  - Responsive layout with a fixed navbar, main content, left menu, and right panel.
  - Dynamic scaling of the interface based on screen width.
  - Toggleable menu for better navigation.

- **Backend**:
  - A Django-based backend with a simple chat app.
  - API routes defined for backend functionalities.
  - Uses SQLite for database management.

- **AWS Integration**:
  - Includes scripts for uploading files to an S3 bucket.
  - Simple utility script for arithmetic operations.

---

## 🚀 How to Run the Project

### 1. Backend Setup
1. Install Python (version 3.10 or later recommended).
2. Navigate to the `backend/` directory:
   ```bash
   cd backend
3.Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate      # On Linux/MacOS
  venv\Scripts\activate         # On Windows
4.Run the Django development server:
  python manage.py runserver
5.Access the backend at: http://127.0.0.1:8000.

### 2. Frontend Setup
1.Navigate to the frontend/ directory.
2.Open the index.html file directly in your browser OR start a lightweight HTTP server:
  python -m http.server
3.If using the HTTP server, access the frontend at: http://127.0.0.1:8000.

🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python, Django
Database: SQLite
AWS Integration: boto3 for S3 interactions


