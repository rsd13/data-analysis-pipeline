import argparse
from clear import data_clear 
from analytic import compare_city

def parse():
    parser = argparse.ArgumentParser()                 # analizador de argumentos
    #grupo que limpia 
    grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
    grupo.add_argument('-c', '--clear', help='Limpia el dataset y lo deja prepardo para el analisis',action='store_true')           # action guarda el argumento
    grupo.add_argument('-ac',action='append', dest='collection',default=[],help='Add repeated values to a list')


    
    
    print(parser)
    #parser.add_argument('string1', help='Primer numero de la operacion.',type=str)
    return parser.parse_args()


def main(): 

    args=parse()

    # opciones
    print(args)
    if args.clear:
        print("-----------------LIMPIANDO----------------------")
        print("Limpiando el dataset para su futuro analisis.\n")

        #data_clear()
    elif args.collection:
        compare_city(args.collection)
    else:
        print ('Error: se requiere uno o mas argumentos para realizar la accion. Pulsa -h para más información')
    

   



if __name__=='__main__':
	main()
