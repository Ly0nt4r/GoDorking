import argparse
import requests
from halo import Halo
import time

# Configuración de argparse
parser = argparse.ArgumentParser(description="Busca resultados con Google Dorking")
parser.add_argument("query", help="Query de búsqueda")
parser.add_argument("--inurl", required=False, help="Parámetro de búsqueda en URL")
parser.add_argument("--filetype", required=False,help="Parámetro de busqueda según la extensión de archivo proporcionada")
parser.add_argument("--site", required=False,help="Parámetro de busqueda en una lista de todas las URL indexadas de un sitio web o dominio")
parser.add_argument("--intext", required=False,help="Parámetro de busqueda que contienen ciertos caracteres o cadenas dentro de su texto")
parser.add_argument("--intitle", required=False,help="Parámetro de busqueda que contienen ciertos caracteres o cadenas dentro de su texto")



# Añadir más argumentos


def banner():
	print(
	'''
 	@@@@@@@@   @@@@@@      @@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@  @@@  @@@   @@@@@@@@
	@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@  @@@@ @@@  @@@@@@@@@
	!@@        @@!  @@@     @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  @@!  @@!@!@@@  !@@
	!@!        !@!  @!@     !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!  !@!  !@!!@!@!  !@!
	!@! @!@!@  @!@  !@!     @!@  !@!  @!@  !@!  @!@!!@!   @!@@!@!   !!@  @!@ !!@!  !@! @!@!@
	!!! !!@!!  !@!  !!!     !@!  !!!  !@!  !!!  !!@!@!    !!@!!!    !!!  !@!  !!!  !!! !!@!!
	:!!   !!:  !!:  !!!     !!:  !!!  !!:  !!!  !!: :!!   !!: :!!   !!:  !!:  !!!  :!!   !!:
	:!:   !::  :!:  !:!     :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  :!:  !:!  :!:   !::
 	::: ::::  ::::: ::      :::: ::  ::::: ::  ::   :::   ::  :::   ::   ::   ::   ::: ::::
 	:: :: :    : :  :      :: :  :    : :  :    :   : :   :   :::  :    ::    :    :: :: :

	''')

# Función que realiza la búsqueda con Google Dorking y devuelve los resultados
def search(query, param):
    # Concatenamos la query y el parámetro de búsqueda
    url = f"https://www.google.com/search?q={query} {param}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Hacemos la solicitud HTTP a Google
    response = requests.get(url, headers=headers)


# Función que muestra animación de carga mientras se realiza una búsqueda
def perform_search(query, param):
    spinner = Halo(text=f"Buscando resultados para query '{query}' con parámetro '{param}'...", spinner="dots")
    spinner.start()

    results = search(query, param)

    spinner.stop()
    print(f"Se encontraron {len(results)} resultados:")
    for result in results:
        print(result)

if __name__ == "__main__":
	banner() # delete con condicional, añadir en el siguiente push 
