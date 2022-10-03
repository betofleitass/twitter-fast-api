## Twitter API <a><img src="https://img.icons8.com/color/48/000000/twitter--v1.png" width="3%"></a>

This is a project for  [**Platzi's FastAPI course.**](https://platzi.com/cursos/fastapi-modularizacion-datos/)

<a><img src="https://user-images.githubusercontent.com/95726794/193625614-56272b6d-9629-49b5-9aaf-45ffa5d38fcd.jpeg" width="40%" heigth="40%"></a>

## Table of Contents:
- [Description](#description)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Run it locally](#run-it-locally)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Description

It's a Twitter REST API made with FastAPI for learning purposes.

## Features

- FastAPI Routers.
- SQLite3 conecction with SQLAlchemy.
- SQLAlchemy models.
- Data validation.
- Users CRUD operations.
- Tweets CRUD operations
- Pydantic models.

## Tech Stack

- FastAPI, Python 3.10, SQLite3, SQLAlchemy

## Installation
    
  1. Clone or download the repository:

  ` git clone https://github.com/betofleitass/twitter-fast-api`

  2. Go to the project directory

  ` cd twitter-fast-api`

  2. Create a virtual environment (PowerShell):

  ```
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```

  3. Install dependencies:

  ` pip install -r requirements.txt`
  
## Run it locally

1. Go to the api directory: ` cd api`

2. Run the server: ` uvicorn main:app --reload`

3. Open a browser and go to: ` http://127.0.0.1:8000/`

## Documentation

Once the server is running go to [http://localhost:8000/docs](http://localhost:8000/docs) to view the API documentation.

## Contributing

Contributions are always welcome!

- Fork this repository;

- Create a branch with your feature: `git checkout -b my-feature`;

- Commit your changes: `git commit -m "feat: my new feature"`;

- Push to your branch: `git push origin my-feature`.

## Authors

- [@betofleitass](https://www.github.com/betofleitass)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#twitter-api-)
