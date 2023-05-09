import argparse
import requests
from halo import Halo
import time

# Configuración de argparse
parser = argparse.ArgumentParser(description="Busca resultados con Google Dorking")
parser.add_argument("query", help="Query de búsqueda")
parser.add_argument("--inurl", required=False, help="Parámetro de búsqueda en URL")
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
