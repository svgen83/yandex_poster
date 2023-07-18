# Website about agencies organizing walks in interesting places in Moscow

The site is an interactive map of Moscow, which displays types of outdoor activities with detailed descriptions and comments.

## Run

You will need Python 3 to run the site.

Download the code from GitHub. Install dependencies:

```sh
pip install -r requirements.txt
```

Create a SQLite database

```sh
python3 manage.py migrate
```

Start the development server

```
python3 manage.py runserver
```

## Environment variables

Part of the project settings is taken from the environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`.

There are 3 variables available:
- `DEBUG` - debug mode. Set to `True` to see debug information in case of an error.
- `SECRET_KEY` — project secret key
- `ALLOWED_HOSTS` - see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Project Goals

The code is written for educational purposes - for the course on Python and web development on the [Devman] site (https://dvmn.org).