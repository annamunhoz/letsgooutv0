from config import DBNAME, DBUSER, DBPASSWORD, DBHOST
import psycopg2
connection = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port="5432")

# Print places
def print_place(name, price, category):
    print("Name: {}".format(name))
    print("Price's level: {}".format(price))
    print("Food's category: {}\n".format(category))


# List places
def list_places():
    print("List of places already registered:\n")
    
    cursor = connection.cursor()
    cursor.execute('SELECT name, price, category from "PLACES"')
    places = cursor.fetchall()

    for place in places:
        print_place(place[0], place[1], place[2])


# Insert places in database
def insert_place(name, price, category):
    cursor = connection.cursor()

    # Insert data into "table" (collums) / SQL text
    # Insert values [list] as a second parameter (this is a specific way in library psycopg2)
    cursor.execute('INSERT INTO "PLACES" (name, price, category) VALUES (%s, %s, %s)',
                    [name, price, category])
    
    connection.commit()


# Register places
def register_place():
    # name_place
    name_place = input("Type the name of the place: ")

    # price_place
    while True:
        print("\nType a number to select the price's level:\n"
              "1: Cheap\n"
              "2: Average\n"
              "3: Expensive\n")
        price_place = int(input())

        if price_place == 1:
            price_place = "Cheap"
            break

        elif price_place == 2:
            price_place = "Average"
            break

        elif price_place == 3:
            price_place = "Expensive"
            break

        print("Option not found.\n")

    # category_place
    print("\nType the food's category of the place:\n"
          "If it has more than one, please separate them using commas.")
    category_place = input()

    insert_place(name_place, price_place, category_place)

    print("\nSuccessfully registered place!\n")


def lets_go_out():
    print("Draw of places without filters.\n")

    cursor = connection.cursor()
    cursor.execute('SELECT name, price, category from "PLACES" order by random() limit 1')
    place = cursor.fetchone()
    
    print_place(place[0], place[1], place[2])


# Choose options
while True:
    print("\nType a number to select an option:\n"
          "1: List places already registered\n"
          "2: Register a new place\n"
          "3: Let's go Out!\n"
          "4: Exit\n")

    selected_option = int(input())

    if selected_option == 1:
        list_places()

    elif selected_option == 2:
        register_place()

    elif selected_option == 3:
        lets_go_out()

    elif selected_option == 4:
        break

    else:
        print("Option not found.\n")

    input("\nPress enter to continue.")
