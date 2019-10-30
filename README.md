# Let's Go Out v.0

*It is my first program: a v0 without screens (it only works in terminal).*

A program to help you decide where to go to eat outside. You can register places, add price level and food's category. You also can list the places already registered.

So when you can't decide where you want to go, the program will help you showing a random registered place.

## Getting started

### Prerequisites
* `python3`
* `postgreSQL`

### Python requirements
* `psycopg2`

### Create and config database
* Use `db.sql` to create the data table
* Make a copy of the file `example_config.py` and name it `config.py`
* Change the infos of the copied file

If you don't know portuguese, please use the file `letsgooutv0_en.py`

## Built With
* Python 3
* PostgreSQL using pgAdmin4
* psycopg2 *(library to connect Python to PostgreSQL)*

## Next Steps
* Improve database struct
* Add aleatory draw with filter by price and/or category
* Create screens

## Acknowledgments
* [vmunhoz](https://github.com/vmunhoz) to teach me a basic of database and to help me with the psycopg2 commands
