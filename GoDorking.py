import argparse
import requests
from halo import Halo
import time
from googlesearch import search

# Configuración de argparse
parser = argparse.ArgumentParser(description="Busqueda de resultados con Google Dorking")
parser.add_argument("query", help="Query de búsqueda")
parser.add_argument("-i","--inurl", required=False, help="Parámetro de búsqueda en URL")
parser.add_argument("-f","--filetype", required=True,help="Parámetro de busqueda según la extensión de archivo proporcionada")
parser.add_argument("-s","--site", required=False,help="Parámetro de busqueda en una lista de todas las URL indexadas de un sitio web o dominio")
parser.add_argument("-t","--intext", required=False,help="Parámetro de busqueda que contienen ciertos caracteres o cadenas dentro de su texto")
parser.add_argument("-T","--intitle", required=False,help="Parámetro de busqueda que contienen ciertos caracteres o cadenas dentro de su texto")
parser.add_argument("--banner", required=False,action='store_true',help="Parámetro para no mostrar el banner")


args = parser.parse_args()

search_params = {
    'inurl': 'inurl:',
    'filetype': 'filetype:',
    'site': 'site:',
    'intext': 'intext:',
    'intitle': 'intitle:',
}



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


def build_query(args):
    query = args.query
    for arg_name, arg_value in vars(args).items():
        if arg_value is not None and arg_name in search_params:
            query += f' {search_params[arg_name]}{arg_value}'
    return query


# Función que realiza la búsqueda con Google Dorking y devuelve los resultados
def search(query, param):
    # Concatenamos la query y el parámetro de búsqueda
    query = f"{query} {param}"

    # Realizamos la búsqueda con googlesearch
    results = list(search(query, num=10, stop=10))  #no funciona, mirar.

    return results



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
    # Delete the banner
    if not args.banner: 
        banner()

    query = build_query(args)
    filetype = args.filetype

    perform_search(query, filetype)
