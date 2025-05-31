# Backend Assignment - Django REST Framework with Google OAuth 2.0

A robust Django REST Framework application implementing Google OAuth 2.0 authentication and comprehensive data management APIs for an Order Management System.

## 🚀 Project Overview

This project demonstrates the integration of key backend technologies:
- **Google OAuth 2.0 Authentication** with access and refresh token management
- **RESTful API endpoints** for data entry and retrieval using Django REST Framework
- **Secure data management** with protected routes and user-specific filtering
- **Order Management System** foundational architecture

Built as part of the **Ywork.ai Backend Developer Assessment**.

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: Google OAuth 2.0
- **Database**: SQLite (Development) / PostgreSQL (Production Ready)
- **Python**: 3.8+
- **Additional Libraries**: 
  - `google-auth`
  - `google-auth-oauthlib`
  - `djangorestframework`
  - `python-dotenv`
  - `corsheaders`

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git
- Google Developer Console account
- Postman (for API testing)

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Venky-43/Backend-Assignment.git
cd Backend-Assignment
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root directory:

```env
# Django Configuration
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth 2.0 Credentials
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback/

# Database Configuration (Optional - for PostgreSQL)
DATABASE_URL=postgresql://username:password@localhost:5432/backend_assignment
```

### 5. Google OAuth 2.0 Setup

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Google+ API
   - Google OAuth2 API
4. Create OAuth 2.0 Credentials:
   - **Application Type**: Web Application
   - **Authorized Redirect URIs**: `http://localhost:8000/auth/google/callback/`
5. Copy the **Client ID** and **Client Secret** to your `.env` file

### 6. Database Setup

```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

🎉 **Server will be available at**: `http://localhost:8000`

## 📚 API Documentation

### 🔐 Authentication Endpoints

#### 1. Initiate Google OAuth Login
```http
GET /auth/google/login/
```
**Description**: Redirects to Google OAuth consent screen

**Response**: Redirects to Google authorization URL

---

#### 2. OAuth Callback Handler
```http
GET /auth/google/callback/?code={authorization_code}
```
**Description**: Handles OAuth callback and exchanges authorization code for tokens

**Response**:
```json
{
    "access_token": "ya29.a0AfH6SMC...",
    "refresh_token": "1//04...",
    "user_info": {
        "id": "123456789",
        "email": "user@gmail.com",
        "name": "User Name"
    }
}
```

---

#### 3. Refresh Access Token
```http
POST /auth/refresh/
Content-Type: application/json

{
    "refresh_token": "your_refresh_token"
}
```

### 📊 Data Management Endpoints

#### 1. Create New Data Entry
```http
POST /api/data/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "title": "Sample Order",
    "description": "This is a sample order description"
}
```

**Response**:
```json
{
    "id": 1,
    "title": "Sample Order",
    "description": "This is a sample order description",
    "created_at": "2025-05-31T10:30:00Z",
    "user": "user@gmail.com"
}
```

---

#### 2. Retrieve All Data
```http
GET /api/data/
Authorization: Bearer {access_token}
```

**Query Parameters**:
- `title`: Filter by title (partial match)
- `user`: Filter by user email

**Examples**:
```http
GET /api/data/?title=order
GET /api/data/?user=user@gmail.com
```

---

#### 3. Retrieve Specific Data Entry
```http
GET /api/data/{id}/
Authorization: Bearer {access_token}
```

---

#### 4. Update Data Entry
```http
PUT /api/data/{id}/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "title": "Updated Order",
    "description": "Updated description"
}
```

---

#### 5. Delete Data Entry
```http
DELETE /api/data/{id}/
Authorization: Bearer {access_token}
```

## 🧪 Testing with Postman

### Step 1: OAuth Authentication Flow

1. **Start OAuth Flow**:
   ```
   GET http://localhost:8000/auth/google/login/
   ```
   - Copy the redirect URL and open in your browser
   - Complete Google authentication
   - Copy the authorization code from the callback URL

2. **Get Tokens**:
   ```
   GET http://localhost:8000/auth/google/callback/?code=AUTHORIZATION_CODE
   ```

### Step 2: API Testing

1. **Set Authorization Header** for all API requests:
   ```
   Authorization: Bearer YOUR_ACCESS_TOKEN
   ```

2. **Test Data Creation**:
   ```json
   POST http://localhost:8000/api/data/
   {
       "title": "Test Order #1",
       "description": "First test order for the system"
   }
   ```

3. **Test Data Retrieval**:
   ```
   GET http://localhost:8000/api/data/
   GET http://localhost:8000/api/data/?title=Test
   GET http://localhost:8000/api/data/1/
   ```

## 🏗️ Project Structure

```
Backend-Assignment/
├── manage.py
├── requirements.txt
├── .env
├── README.md
├── .gitignore
├── backend_assignment/          # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── authentication/              # OAuth authentication app
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── utils.py
├── api/                        # Data management API app
│   ├── __init__.py
│   ├── models.py               # Data model (title, description)
│   ├── views.py                # API viewsets
│   ├── urls.py
│   ├── serializers.py
│   └── permissions.py
└── static/
    └── admin/
```

## 🔒 Security Features

- **Environment Variables**: All sensitive data stored securely in `.env`
- **Token-Based Authentication**: OAuth 2.0 access tokens for API security
- **Protected Endpoints**: All data APIs require valid authentication
- **User-Specific Data**: Users can only access their own data
- **Input Validation**: Comprehensive validation using DRF serializers
- **CORS Configuration**: Proper cross-origin resource sharing setup

## 🚀 Deployment Ready

### Production Environment Setup

1. **Environment Variables**:
   ```env
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

2. **Security Checklist**:
   - [ ] `DEBUG=False` in production
   - [ ] Proper `ALLOWED_HOSTS` configuration
   - [ ] HTTPS enabled
   - [ ] Environment variables secured
   - [ ] OAuth redirect URIs updated for production domain
   - [ ] Database credentials secured

### Deployment Commands

```bash
# Install production dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Run with gunicorn (production server)
gunicorn backend_assignment.wsgi:application
```

## 🔧 Key Features Implemented

✅ **Google OAuth 2.0 Integration**
- Complete OAuth flow implementation
- Access token and refresh token handling
- User profile information retrieval

✅ **RESTful API Design**
- Full CRUD operations
- Query parameter filtering
- Proper HTTP status codes
- JSON response formatting

✅ **Data Model**
- Title and description fields as required
- User association for data isolation
- Timestamp tracking

✅ **Security Implementation**
- Protected API endpoints
- Token-based authentication
- Input validation and sanitization

✅ **Documentation**
- Comprehensive API documentation
- Clear setup instructions
- Testing guidelines

## 🐛 Troubleshooting

### Common Issues & Solutions

1. **OAuth Redirect URI Mismatch**:
   - Ensure redirect URI in Google Console exactly matches your application
   - Check for trailing slashes: `/callback/` vs `/callback`

2. **Token Expired Error**:
   - Use the refresh token endpoint to get a new access token
   - Implement automatic token refresh in your client application

3. **Database Connection Issues**:
   - Verify database credentials in `.env`
   - Ensure PostgreSQL service is running (if using PostgreSQL)
   - Check firewall settings

4. **CORS Issues**:
   - Verify `ALLOWED_HOSTS` in settings
   - Check CORS configuration for frontend integration

## 📈 Future Enhancements

- [ ] Rate limiting implementation
- [ ] Caching for improved performance
- [ ] Email notifications
- [ ] Advanced filtering and search
- [ ] Pagination for large datasets
- [ ] API versioning
- [ ] Comprehensive logging
- [ ] Unit and integration tests

## 👤 Author

**Venkannababu Kothapalli**
- GitHub: [@Venky-43](https://github.com/Venky-43)
- Repository: [Backend-Assignment](https://github.com/Venky-43/Backend-Assignment)

## 📄 License

This project is developed as part of the Ywork.ai Backend Developer Assessment.

---

## 🎯 Assessment Completion Checklist

✅ Google OAuth 2.0 API Authentication implemented  
✅ Access Token and Refresh Token handling  
✅ POST API endpoint for data entry  
✅ GET API endpoint with query filtering  
✅ Protected endpoints with authentication  
✅ Model with title and description fields  
✅ Well-documented code with best practices  
✅ Security measures for sensitive data  
✅ Clear setup and usage instructions  

