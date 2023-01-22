# company_manager

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
