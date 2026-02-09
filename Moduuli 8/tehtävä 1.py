import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Valtteri',
    password='Pallero1234',
    autocommit=True
)

icao_code = input("Enter the ICAO code of an airport: ")
sql = f"SELECT name, municipality FROM airport WHERE airport.ident = '{icao_code}'"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if not tulos:
    print(f"No airport found with ICAO code: {icao_code.upper()}")

else:
    for now in tulos:
        print(f"Airport name: {now[0]}" )
        print(f"Location: {now[1]}" )
