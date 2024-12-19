import psycopg2
import re
from psycopg2.extensions import AsIs

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
    user="lbergli",
    password="9Prr8H9S")
print(conn)

# Create a cursor. The cursor allows you to execute database queries.
cur = conn.cursor()

def program_loop():
    while True:
        search_for = input("""What would you like to do? \n 1. Search for an airport.
 2. See speakers of a language. \n 3. Input a desert.\n 4. Commit\n""")

        if search_for == "1": 
            search_airport()    
        elif  search_for == "2":
            countries_speak()
        elif search_for == "3":
            yummy_desert()
        elif search_for == "4":
            conn.commit()
        else:
            print("Bruh u stupid")
        print("\n")
def search_airport():
    search_by_type = input(" 1. IATA\n 2. Name \n 3. Both\n")
    query = ""
    if search_by_type == "1":
        search_by = input("search for IATA\n")
        query = """
        SELECT IATACode, Name, Country
        FROM airport
        WHERE IATACode = %s;
        """
        cur.execute(query, (search_by,))
    elif search_by_type == "2":        
        search_by = input("search for name\n")
        query = """
            SELECT IATACode, Name, Country
            FROM airport
            WHERE NAME LIKE %s;
            """
        cur.execute(query, (f"%{search_by}%",))
        #cur.execute(query, ("%" + search_by + "%",))
    else:
        search_by = input("search for Name AITA\n")
        both = search_by.split()
        query = """
            SELECT IATACode, Name, Country
            FROM airport
            WHERE NAME LIKE %s OR IATACode = %s;
            """
        cur.execute(query, (both[0], both[1],))
    result = cur.fetchall()
    print(result)

def countries_speak():
    lang = input("what lenguade\n")
    query = """
        SELECT Country.Name, CAST((Country.Population * Spoken.Percentage)/100 AS INT) FROM
        Country
        JOIN
        Spoken ON Country.Code = Spoken.Country
        WHERE Spoken.Language = %s
        ORDER BY Country;"""
    cur.execute(query, (lang,))
    result = cur.fetchall()
    print(result)

def yummy_desert():
    name = input("Desert name:\n")
    area = input("Desert area:\n")
    province = input("Desert province:\n")
    country = input("Desert country:\n")
    coord = input("Desert coord:\n")

    check = """
        SELECT * FROM Province 
        WHERE Name = %s AND Country = %s;"""
    cur.execute(check, (province, country,))
    check_res = cur.fetchall()
    if check_res == []:
        print("U stupid")
        return

    ################################################################
    # P+

    check_9_provinces = """
        SELECT Province 
        FROM geo_Desert 
        WHERE Desert = %s;"""
    cur.execute(check_9_provinces, (name,))
    check_9_res = cur.fetchall()
    if len(check_9_res) >= 9:
        print("A desert cant 9 province")
        return

    check_area = """
        SELECT Province 
        FROM Province 
        WHERE Name = %s AND %s > 30 * Area;"""
    cur.execute(check_area, (province, area,))
    check_area_res = cur.fetchall()
    if len(check_area_res) > 0:
        print("Deser too phat")
        return

    check_deserts_country = """
        SELECT Desert 
        FROM geo_Desert 
        WHERE Country = %s;"""
    cur.execute(check_deserts_country, (country,))
    check_deserts_country_res = cur.fetchall()
    if len(check_deserts_country_res) >= 20:
        print("Too mamy desert there brother")
        return
    
    #######################################################
    # Back to P

    check_des = "SELECT * FROM Desert WHERE Name = %s;"
    cur.execute(check_des, (name,))
    check_des_res = cur.fetchall()

    insert_geo = """
        INSERT INTO geo_Desert 
        VALUES(%s, %s, %s);"""
    cur.execute(insert_geo, (province, country, name,))
    if check_des_res == []:
        print("Inserting into desert")
        insert_des = """
            INSERT INTO Desert 
            VALUES(%s, %s, (%s));"""
        cur.execute(insert_des, (name, area, AsIs(coord)))

    # Just for debugging output

    cur.execute("SELECT * FROM geo_Desert WHERE Country = '" + country + "';")
    geo_res = cur.fetchall()
    print(geo_res)
    cur.execute("SELECT * FROM Desert WHERE Name = '" + name + "';")
    des_res = cur.fetchall()
    print(des_res)
    #conn.commit()
    #print("DELETE * FROM geo_Desert WHERE Name = '" + name + "';")
    #print("DELETE * FROM Desert WHERE Name = '" + name + "';")



if __name__ == "__main__":
    # Example:
    # Execute a query which returns all genres including the genre id.
    # cur.execute("SELECT * from genre ")
    #cur.execute("SELECT * FROM Country")
    program_loop()
    #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #countries_speak()
    
    #cur.execute("SELECT * FROM Country")

    # Print the first row returned.
    #print(cur.fetchone())

    # Print the next row returned.
    #print(cur.fetchone())

    # Print all the remaining rows returned.
    #print(cur.fetchall())

    # Close the connection to the database.
    #conn.close()

    # SQL Injection P+
    # usersearch = "'; DROP TABLE fines; --"
