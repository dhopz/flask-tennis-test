# Tennis API

As the president of the local Tennis Club, this backend API will manage its players and their rankings.


## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.8](https://www.python.org/downloads/release/python-389/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. Clone the repo:

    ```
    $ git clone https://github.com/dhopz/flask-tennis-test.git
    $ cd flask-tennis-test
    ```

2. With Python 3.8 and Pip installed:

    ```
    $ virtualenv --python=python3 env --no-site-packages
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```

3. Create a PostgreSQL user with the username and password `postgres` and create a database called `tennis`:

    ```
    $ createuser --interactive --pwprompt
    $ createdb tennis
    ```

4. Export the required environment variables:

    ```
    $ export FLASK_APP=app.py
    ```

5. Execute the migrations to create the `tennis` table:

    ```
    $ flask db migrate
    $ flask db upgrade
    ```

6. Run the Flask API:

    ```
    $ flask run
    ```

7. Navigate to `http://localhost:5000/players` to view the player data.
