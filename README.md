# Django DRF Recipes API Documentation

This is a Python Docker backend project for a food recipe app. Users can register and manage recipes and categories. Below is a detailed explanation of the API functionality, along with instructions on how to set up and use the application.

---

## Table of Contents

1. [Introduction](#introduction)
2. [How to Use the App](#how-to-use-the-app)
3. [API Overview](#api-overview)
   - [Recipes Endpoints](#recipes-endpoints)
   - [User Endpoints](#user-endpoints)
4. [Authentication](#authentication)
5. [Project Features](#project-features)
6. [Technologies Used](#technologies-used)
7. [Development Setup](#development-setup)
8. [API Documentation](#api-documentation)

---

## Introduction

This project is a **Python Docker backend** for a food recipe app. Users can register, add, modify, and delete recipes and categories. **GET** requests do not require authentication, allowing anyone to access them without registering. However, actions such as adding, modifying, or deleting posts or categories require user authentication. Only the users who created recipes or categories can modify or delete them.

To make the API endpoints easy to understand, I used Swagger and Redoc to provide comprehensive API documentation.

Throughout this project, I learned to use the Django Rest Framework and GitHub Actions to handle the entire development process through continuous integration (CI). I also employed Docker to containerize the project, using Docker volumes to store persistent data, ensuring data retention even if the containers are removed.

---

## How to Use the App

### Starting the Application

To build and run the application, use the following Docker commands:

- **Build and run with terminal output:**
  ```bash
  docker-compose up --build

- **Run in detached mode (without terminal output):**
  ```bash
  docker-compose up --build -d

### Database Migration

After building the containers, migrate the database using the following commands:

- **Migrate using Docker Compose:**
  ```bash
  docker-compose run web python manage.py makemigrations
  docker-compose run web python manage.py migrate

- **Using the integrated terminal:**
  ```bash
  docker-compose exec -it web bash -l
  python manage.py makemigrations
  python manage.py migrate
  
- **Create a Superuser**
- To create a superuser for accessing the Django admin panel:
  ```bash
  python manage.py createsuperuser
  
- **Importing Dummy Data**
- You can populate the database with dummy data using custom commands. Ensure to follow the order due to relational models. For educational purposes, categories and meals can be imported from The Meal DB API.

- Custom commands available in `recipes/management/commands` directory
  ```bash
  python manage.py import_users
  python manage.py import_categories
  python manage.py import_meals

## API Overview

The API is structured into two main sections: **Recipes** and **User**. Below are the available endpoints and their descriptions.

### Recipes Endpoints

| Method  | Endpoint                                | Description                                        |
|---------|-----------------------------------------|----------------------------------------------------|
| `GET`   | `/recipes/`                             | Retrieve a list of all recipes.                    |
| `GET`   | `/recipes/categories/`                  | Retrieve a list of all categories.                 |
| `POST`  | `/recipes/category/`                    | Create a new category (requires authentication).   |
| `GET`   | `/recipes/category/{category_id}/`      | Retrieve a specific category by ID.                |
| `PATCH` | `/recipes/category/{category_id}/`      | Update a category by ID (requires authentication). |
| `DELETE`| `/recipes/category/{category_id}/`      | Delete a category by ID (requires authentication). |
| `POST`  | `/recipes/meal/`                        | Create a new meal (requires authentication).       |
| `GET`   | `/recipes/meal/{meal_id}/`              | Retrieve a specific meal by ID.                    |
| `PATCH` | `/recipes/meal/{meal_id}/`              | Update a meal by ID (requires authentication).     |
| `DELETE`| `/recipes/meal/{meal_id}/`              | Delete a meal by ID (requires authentication).     |
| `GET`   | `/recipes/random/`                      | Retrieve a random recipe.                          |
| `GET`   | `/recipes/search/`                      | Search for recipes using query parameters.         |

### User Endpoints

| Method  | Endpoint                     | Description                                        |
|---------|------------------------------|----------------------------------------------------|
| `POST`  | `/user/api/token/`           | Obtain a new token for authentication.             |
| `POST`  | `/user/api/token/refresh/`   | Refresh the authentication token.                  |
| `GET`   | `/user/me/`                  | Retrieve the authenticated user's details.         |
| `PUT`   | `/user/me/`                  | Update the authenticated user's details.           |
| `POST`  | `/user/register/`            | Register a new user.                               |
| `GET`   | `/user/{user_id}/`           | Retrieve a specific user's details by ID.          |

## Authentication

- **Public Access:** **GET** requests to list or retrieve resources do not require authentication, allowing public access.
- **Authenticated Access:** Actions like creating, updating, or deleting recipes and categories require user authentication. Only the creator of a recipe or category can modify or delete it.

## Project Features

- **User Registration:** Allows users to register and access additional features.
- **Recipe Management:** Users can add, modify, and delete recipes and categories.
- **API Documentation:** API documentation is provided using Swagger and Redoc for easy understanding of endpoints.
- **Data Persistence:** Utilizes Docker volumes to ensure data persistence even if containers are removed.

## Technologies Used

- **Python**
- **Django Rest Framework**
- **Docker**
- **Swagger UI / Redoc**
- **GitHub Actions for Continuous Integration (CI)**

## Development Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

![image](https://github.com/user-attachments/assets/c9662e76-037b-4d85-ae1e-027518c9a1ab)
![image](https://github.com/user-attachments/assets/b07192a4-3b5f-4eba-b9cf-1b39a8a2397c)



## Front-end - under development

Repo: https://github.com/IsuruFerna/FE_React-FoodRecipes/tree/development
