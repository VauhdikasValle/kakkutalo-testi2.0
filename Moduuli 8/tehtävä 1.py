import mysql.connector
from mysql.connector import Error

def get_airport_by_icao(icao_code):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='flight_game',
            user='Valtteri',
            password='Pallero1234'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = """
            SELECT name, municipality FROM airport WHERE ident = %s
            """

            cursor.execute(query, (icao_code,))
            result = cursor.fetchone()

            return result

    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    icao_code = input("Enter the ICAO code of an airport: ").strip().upper()

    airport_info = get_airport_by_icao(icao_code)

    if airport_info:
        print(f"Airport name: {airport_info['name']}")
        print(f"Location: {airport_info['municipality']}")
    else:
        print(f"No airport found with ICAO code {icao_code}")

main()