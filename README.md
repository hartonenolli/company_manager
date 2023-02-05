# company_manager

## Current state:

Currently, the application can only retrieves the number of customers. I assume that making other more challenging searches will be smooth, now that I have a working foundation.
Work cannot be added yet, even though the addition form exists. The addition should be done quickly. At the moment, anyone can log in to the application with any password.

To be honest, I still have a lot of work to do. This is because I had major problems getting the database to work. For some reason, a connection could not be established. It took 3-4 days to fix the issue.

But you can still test these if you like. First clone the repo, then:

python3 -m venv venv

source venv/bin/activate

(venv) $ pip install flask

(venv) $ pip install flask-sqlalchemy

(venv) $ pip install psycopg2

(venv) $ pip install python-dotenv

(venv) $ pip install -r requirements.txt

(venv) $ psql < schema.sql

(venv) $ flask run

## What is this?

    The application helps users maintain completed and unfinished work.

## Who is it for?

    This is to help companies that sells services to different locations.

## Basics

The idea is to maintain a database with (at least) following data:

| ID        | WORK          | WORKER         | PRICE        | STATUS       | DATE     | COSTUMER     |
| --------- |:-------------:| :-------------:| :-----------:| :-----------:| :-------:| :-----------:|
| 1         | MAINTNANCE    | Harjakainen    | 50           | DONE         | 01.12.22 | Suominen     |
| 2         | MAINTNANCE    | Korhonen       | 70           | DONE         | 03.12.22 | Hollola      |
| 3         | INSTALLATION  | Virtanen       | 200          | IN PROGRESS  | 10.01.23 | Attila       |
| 4         | OTHER         | Harjakainen    | 1000         | NOT STARTED  | 10.02.23 | Kummajainen  |

Application allows user to input data and search information in different ways from the database.

Example:

    How many works have Harjakainen been assigned to?
    
    What is the combined price?

And many more..

There could be two different users:
- manager that has access to everything
- worker that has  access to own work

### Other
This is for tsoha 2023
