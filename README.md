## Twitter API <a><img src="https://img.icons8.com/color/48/000000/twitter--v1.png" width="3%"></a>

This is a project for  [**Platzi's FastAPI course.**](https://platzi.com/cursos/fastapi-modularizacion-datos/)

<a><img src="https://user-images.githubusercontent.com/95726794/194726089-94b2c627-3561-419b-959c-0158bb105799.jpeg" width="50%" heigth="50%"></a>

## Table of Contents:
- [Twitter API <a><img src="https://img.icons8.com/color/48/000000/twitter--v1.png" width="3%"></a>](#twitter-api-)
- [Table of Contents:](#table-of-contents)
- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Description

Twitter REST API made with FastAPI for learning purposes.

## Features

- User signup and login.
- JSON Web Tokens Authentication.
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

1. Go to the app directory: ` cd app`

2. Change the ` env.example` file name to ` .env`, pay atenttion to the dot before env.

3. Run the server: ` uvicorn main:app --reload`

4. Open a browser and go to: ` http://127.0.0.1:8000/`

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

[Back to top ??????](#twitter-api-)
