# company_manager

## Current state:

It is possible to register. You have to use password that is *8-digit long, has numbers, upper- and lowercase letters.*
You can add admin user by givin admin code: "admin123"
After registering you can login. It is possible to add new work. (This needs some work to make sure information is given correctly, but as long you give work-info in correct form it works.)
It is possible to search all types of work. You will be shown a list of all the work you have done.

Modify was not something I was prepared to do at the start of the project, but I try to implement it as soon as possible. You might have a need to change the status of the work at some point. This feature is not ready.

Code needs some cleaning up.

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
