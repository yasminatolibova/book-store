Instagram Clone

This is a backend Book Store project built with Django and Django REST Framework.

🚀 Features

· User Registration, Login, Logout & Reset password

· Finding out which author books and which books are available in this book store

· Comment System

· Rating System

· Wishlist

· Cart

· Order

· Promo Code

🛠 Tech Stack

Python

Django

Django REST Framework


⚙️ Installation
Clone the repository:

git clone https://github.com/yasminatolibova/book-store.git cd store

Create virtual environment:

python -m venv env

Activate environment Windows: env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

The first thing after that filling models.py is crucial if not you cant makemigrations. 

Then register all the models Run migrations:

python manage.py makemigrations

python manage.py migrate

Run server:

python manage.py runserver


## 🔐 Authentication

This project uses **Token Authentication**.

After login, include token in header:

Authorization: Token your_token_here

---

## 📌 API Endpoints

### 🔐 Authentication

- POST /api/register/

- POST /api/login/

- POST /api/logout/

- POST /api/reset_password/


📚 Book Store API
🔐 Authentication
POST /api/register/

POST /api/login/

POST /api/logout/

POST /api/reset_password/


📂 Categories
GET    /api/categories/

POST   /api/categories/

GET    /api/categories/{id}/

PUT    /api/categories/{id}/

PATCH  /api/categories/{id}/

DELETE /api/categories/{id}/


📚 Books
GET    /api/books/

POST   /api/books/

GET    /api/books/{slug}/

PUT    /api/books/{slug}/

PATCH  /api/books/{slug}/

DELETE /api/books/{slug}/

Filters
GET /api/books/?search=title

GET /api/books/?ordering=language


✍️ Authors
GET    /api/authors/

POST   /api/authors/

GET    /api/authors/{id}/

PUT    /api/authors/{id}/

PATCH  /api/authors/{id}/

DELETE /api/authors/{id}/


🎟 Promo Codes
GET    /api/coupons/

POST   /api/coupons/


❤️ Wishlist
POST   /api/wishlist/

GET    /api/wishlist_detail/

DELETE /api/wishlist_detail/{id}/

📌 Comments API
GET     /api/comments/
          
POST    /api/comments/ 
         
GET     /api/comments/{id}/
     
PUT     /api/comments/{id}/
     
PATCH   /api/comments/{id}/  
  
DELETE  /api/comments/{id}/     

GET /api/comments/?book=1

⭐ Rating API
GET     /api/rating/

POST    /api/rating/

GET     /api/rating/{id}/

PUT     /api/rating/{id}/

PATCH   /api/rating/{id}/

DELETE  /api/rating/{id}/

💬 Comments

Users can leave comments on books
Supports full CRUD operations

⭐ Ratings

Users can rate books (1–5 stars)

Each rating linked to a book and user


🔐 Authentication

📚 Books

📂 Categories

✍️ Authors

🎟 Coupons

❤️ Wishlist

💬 Comments

⭐ Ratings

🛒 Cart 

📦 Orders
Swagger UI:  /swagger/

API Documentation

<img width="1264" height="637" alt="image" src="https://github.com/user-attachments/assets/a603eebf-10c9-4497-bb0c-d1ca3421ade0" />


📂 Project Structure
apps/

├── accounts/

├── book/

├── comment/

├── cart/


🏗 Architecture
Modular apps structure
Pagination enabled
Filtering, Search, Ordering
Separate comment app
Separate cart app

👩🏼‍💻 Author
Yasmina Tolibova
