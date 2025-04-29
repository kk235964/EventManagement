# EventManagement

A full-featured **Event Management System** built with **Django**, allowing users to register for events, view announcements, and for admins to manage event data, participants, and notifications.

---

## 📌 Features

### 👥 User Features
- Register and log in
- View upcoming events
- Register for events
- Download event participation list (if permitted)
- Receive broadcasted notices
- Read published articles or updates

### 🛠️ Admin Features
- Create, edit, and delete events
- View and manage user registrations
- Broadcast notices to users
- Upload or publish articles and updates
- Download user registration lists

---

##  Tech Stack

- **Backend:** Django, SQLite / PostgreSQL
- **Frontend:** HTML, CSS, JavaScript (with Django templates)
- **Authentication:** Django built-in auth
- **Deployment:** (Microsoft azure)

---

## Getting Started

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/EventManagement.git
   cd EventManagement
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

📧 Contact
Created by [Kamal Ahmad] – [kk235964@gmail.com]
