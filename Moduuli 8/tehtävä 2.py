import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Valtteri',
    password='Pallero1234',
    autocommit=True
)

country_code = input("Enter the country code (e.g., FI for Finland): ")
sql = f"SELECT type, COUNT(*) FROM airport WHERE airport.iso_country = '{country_code}' GROUP BY type"

def get_airports_by_country(country_code):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def run_country_program():
    airport_types = []
    airport_types.append(get_airports_by_country())
    for n in airport_types:
        print(f"{n}")
run_country_program()



# if not tulos:
#     print(f"No airports found for country code: {country_code.upper()}")
# else:
#     for now in tulos:
#         print(f"Airport name: {now[0]}")
#         print(f"Location: {now[1]}")
