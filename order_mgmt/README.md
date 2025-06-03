# Backend Assignment: Order Management System

## Features
- Google OAuth 2.0 Authentication
- Data Entry (POST) and Retrieval (GET) via Django REST Framework

## Setup

```bash
git clone <repo>
cd order_mgmt
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## OAuth

POST `/api/oauth/`
```json
{
  "code": "auth_code",
  "redirect_uri": "http://localhost"
}
```

## Entries

POST `/api/entries/`
GET `/api/entries/list/?title=value`
