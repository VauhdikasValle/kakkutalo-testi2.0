import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Valtteri',
    password='Pallero1234',
    autocommit=True
)


def get_airport_coordinates(icao_code):
    kursori = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao_code,))
    tulos = kursori.fetchone()
    kursori.close()
    return tulos


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    koord1 = get_airport_coordinates(icao1)
    koord2 = get_airport_coordinates(icao2)

    if koord1 and koord2:
        etäisyys = geodesic(koord1, koord2).kilometers
        print(f"\nDistance between {icao1} and {icao2}: {etäisyys:.2f} kilometers")
    else:
        if not koord1:
            print(f"Airport with ICAO code {icao1} not found in the database.")
        if not koord2:
            print(f"Airport with ICAO code {icao2} not found in the database.")


run_airport_distance()