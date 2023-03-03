# company_manager

## What it is for?

Company manager helps to manage companies, that sell their work to multiple costumers.

## What you can do?
- Register + login
- Add new work
- Search by name + year
- Sort work
- Modify work
- Add notes
- Comment notes

Protip: If you want to be admin user, while registering add admin code as: "admin123"

## Instructions:

Clone the ropository.

Create .env file and insert:

    DATABASE_URL=<your url>
    
    SECRET_KEY=<random numbers/letters>

Enter the following command to your terminal:

    python3 -m venv venv

    source venv/bin/activate

    (venv) $ pip install flask

    (venv) $ pip install flask-sqlalchemy

    (venv) $ pip install psycopg2

    (venv) $ pip install python-dotenv

    (venv) $ pip install -r requirements.txt

    (venv) $ psql < schema.sql

    (venv) $ flask run

## Original idea

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

## Created product:

I have database with 5 tables: users, work, modify, notes, comments

Users:
- Stores user data. Username, password and admin

Work:
- Stores work data. Costumer, work_type, price, status, date
- References users

Modify:
- Stores copy of modified work and time, explination
- References users and work

Notes:
- Sores notes for all to see. Time, memo
- References users

Comments:
- Stores comments for notes. Time, comment
- References users and notes

## Toughts:

It was really satisfying to work on this project. I am really happy on the final product.

### Other
This is for tsoha 2023
