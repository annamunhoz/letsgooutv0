from config import DBNAME, DBUSER, DBPASSWORD, DBHOST
import psycopg2
connection = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port="5432")

# Print places
def print_place(name, price, category):
    print("Nome: {}".format(name))
    print("Faixa de preço: {}".format(price))
    print("Tipo de comida: {}\n".format(category))


# List places
def list_places():
    print("Lista de lugares já cadastrados:\n")
    
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
    name_place = input("Digite o nome do lugar: ")

    # price_place
    while True:
        print("\nDigite o número para selecionar a faixa de preço:\n"
              "1: Barato\n"
              "2: Médio\n"
              "3: Caro\n")
        price_place = int(input())

        if price_place == 1:
            price_place = "Barato"
            break

        elif price_place == 2:
            price_place = "Médio"
            break

        elif price_place == 3:
            price_place = "Caro"
            break

        print("Opção não encontrada.\n")

    # category_place
    print("\nDigite a categoria (tipo de comida) do lugar:\n"
          "Se houver mais de uma, separe-as por vírgulas.")
    category_place = input()

    insert_place(name_place, price_place, category_place)

    print("\nLugar cadastrado com sucesso!\n")


def lets_go_out():
    print("Sorteio de lugares sem filtro.\n")

    cursor = connection.cursor()
    cursor.execute('SELECT name, price, category from "PLACES" order by random() limit 1')
    place = cursor.fetchone()
    
    print_place(place[0], place[1], place[2])


# Choose options
while True:
    print("\nDigite o número para selecionar as opções:\n"
          "1: Listar lugares cadastrados\n"
          "2: Cadastrar um novo lugar\n"
          "3: Let's go Out!\n"
          "4: Sair\n")

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
        print("Opção não encontrada.\n")

    input("\nAperte enter para continuar.")
