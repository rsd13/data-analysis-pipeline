import argparse
from clear import data_clear 


def parse():
	parser = argparse.ArgumentParser()                 # analizador de argumentos
	grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)

	grupo.add_argument('-c', '--clear', help='Limpia el dataset y lo deja prepardo para el analisis', action='store_true')           # action guarda el argumento
	
	#parser.add_argument('string1', help='Primer numero de la operacion.', type=str)
	return parser.parse_args()


def main(): 

    args=parse()

    # opciones
    print(args)
    if args.clear:
        print("-----------------LIMPIANDO----------------------")
        print("Limpiando el dataset para su futuro analisis.\n")

        data_clear()

    else:
        print ('Error: se requiere un argumento para realizar la accion.')



if __name__=='__main__':
	main()
