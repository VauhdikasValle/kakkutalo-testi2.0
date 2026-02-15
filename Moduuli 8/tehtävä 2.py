import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Valtteri',
    password='Pallero1234',
    autocommit=True
)


def get_airports_by_country(country_code):
    kursori = yhteys.cursor()
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori.execute(sql, (country_code,))
    tulos = kursori.fetchall()
    kursori.close()
    return tulos


def run_country_program():
    koodi = input("Enter the country code (e.g., FI for Finland): ").upper()
    lentokentat = get_airports_by_country(koodi)


    if len(lentokentat) == 0:
        print(f"No airports found for country code '{koodi}''.")
    else:
        print(f"\nAirports in {koodi}:")
        for rivi in lentokentat:
            print(f"{rivi[1]} {rivi[0]} airports")


run_country_program()