import psycopg2
import re

"""
Note: It's essential never to include database credentials in code pushed to GitHub.
Instead, sensitive information should be stored securely and accessed through environment variables or similar.
However, in this particular exercise, we are allowing it for simplicity, as the focus is on a different aspect.
Remember to follow best practices for secure coding in production environments.
"""

# Acquire a connection to the database by specifying the credentials.
conn = psycopg2.connect(
    host="psql-dd1368-ht23.sys.kth.se",
    database="lbergli",
    user="simonsev",
    password="egbvJJab")
print(conn)

# Create a cursor. The cursor allows you to execute database queries.
cur = conn.cursor()

def program_loop():
    while True:
        search_for = input("""What would you like to do? \n 1. Search for an airport.
 2. See speakers of a language. \n 3. Input a desert.\n""")

        if search_for == "1": 
            search_airport()    
        elif  search_for == "2":
            countries_speak()
        elif search_for == "3":
            yummy_desert()
        else:
            print("Bruh u stupid")
        print("\n")
def search_airport():
    search_by = input("ärpord\n")
    query = "SELECT IATACode, Name, Country FROM Airport WHERE Name LIKE '%" + search_by + "%';"
    cur.execute(query)
    result = cur.fetchall()
    print(result)

def countries_speak():
    lang = input("what lenguade\n")
    query = """SELECT Country.Name, CAST((Country.Population * Spoken.Percentage)/100 AS INT) FROM
        Country
        JOIN
        Spoken ON Country.Code = Spoken.Country
        WHERE Spoken.Language = '""" + lang + """'
        ORDER BY Country;"""
    cur.execute(query)
    result = cur.fetchall()
    print(result)
    #titles = [row[0] for row in result]

    #print(titles)

def yummy_desert():
    name = input("Desert name:\n")
    area = input("Desert area:\n")
    province = input("Desert province:\n")
    country = input("Desert country:\n")
    coord = input("Desert coord:\n")

    check = "SELECT * FROM Province WHERE Name = '" + province + "' AND Country = '" + country + "';"
    cur.execute(check)
    check_res = cur.fetchall()
    if check_res == []:
        print("U stupid")
        return
    
    insert_geo = "INSERT INTO geo_Desert VALUES('" + province + "','" + country + "','" + name + "');"
    cur.execute(insert_geo)
    insert_des = "INSERT INTO Desert VALUES('" + name + "', '" + area + "', '(" + coord + ")');"
    cur.execute(insert_des)
    cur.execute("SELECT * FROM geo_Desert WHERE Country = '" + country + "';")
    geo_res = cur.fetchall()
    print(geo_res)
    cur.execute("SELECT * FROM Desert WHERE Name = '" + name + "';")
    des_res = cur.fetchall()
    print(des_res)
    print("DELETE * FROM geo_Desert WHERE Name = '" + name + "';")
    print("DELETE * FROM Desert WHERE Name = '" + name + "';")
    


# Simple function to get all books with a specific genre.
#def get_book_title_by_genre():
#    genre = input("Please enter a genre: ")
#    query = f"SELECT books.title FROM books LEFT JOIN genre ON books.bookid = genre.bookid WHERE genre.genre = '{genre}'"
#    cur.execute(query)
#    result = cur.fetchall()
#    titles = [row[0] for row in result]

#    print(titles)

if __name__ == "__main__":
    # Example:
    # Execute a query which returns all genres including the genre id.
    # cur.execute("SELECT * from genre ")
    #cur.execute("SELECT * FROM Country")
    program_loop()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    countries_speak()
    
    #cur.execute("SELECT * FROM Country")

    # Print the first row returned.
    #print(cur.fetchone())

    # Print the next row returned.
    #print(cur.fetchone())

    # Print all the remaining rows returned.
    #print(cur.fetchall())

    # Close the connection to the database.
    conn.close()
