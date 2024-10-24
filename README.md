# E-commerce API

A RESTful API for managing an e-commerce platform, built with Django and Django REST Framework. This API allows users to manage products, orders, and user accounts effectively, with features like pagination and search.

## Features

- **Product Management**:
  - Create, update, and delete products.
  - Retrieve a list of all products or details of a specific product.
  - Search and filter products by category, name, and brand.
  - Support for pagination to handle large datasets efficiently.

- **User Account Management**:
  - User registration and authentication.
  - Update user account information.

- **Order Management**:
  - Create new orders.
  - View order history and details.
  - Update order status.
  - Cancel orders.

- **Category Management**:
  - Create, update, and delete product categories.
    
- **Review and Comment Management**:
  - Users can create reviews for products, including a rating and comments.
  - Retrieve all reviews for a product.
  - Update or delete reviews.

- **Authentication**:
  - Secure endpoints using JWT (JSON Web Token) authentication.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite 
- **Authentication**: JSON Web Token 
