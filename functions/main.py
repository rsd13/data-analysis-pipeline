import argparse
from clear import data_clear 
from analytic import compare_city,compare_state
from pdf import PDF

def parse():
    parser = argparse.ArgumentParser()                 # analizador de argumentos
    #grupo que limpia 
    grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
    grupo.add_argument('-c', '--clear', help='Limpia el dataset y lo deja prepardo para el analisis',action='store_true')           # action guarda el argumento
    grupo.add_argument('-ac',action='append', dest='cities',default=[],help="Añade las ciudades que se quiere comparar. Ej: -ac 'New York' -ac Phoenix ...")
    grupo.add_argument('-as',action='append', dest='states',default=[],help="Añade los estados que se quiere comparar. Ej: -as California -as 'New York' ...")
    grupo.add_argument('-at',action='store', dest='type',default=[],help="Indica que tipo de restaurante se pide mas en una ciudad (pizza o hamburguesa)")

    #parser.add_argument('string1', help='Primer numero de la operacion.',type=str)
    return parser.parse_args()


def main(): 

    args=parse()

    # opciones
    pdf = PDF()
    pdf.add_page()
    pdf.input_title("Analisis de comida pedida en EUUU")
    if args.clear:
        data_clear(pdf)
    elif args.cities:
        print("-----------------Analizando----------------------")
        pdf.input_subtitle("Comparación de restaurantes consumidos por ciudades.")
        result = ", "
        a = (lambda lst: lst)
        cities = result.join(a(args.cities))
        pdf.input_line("Ciudades comparadas: {}.".format(cities))
        pdf.ln()
        compare_city(args.cities,pdf)

    elif args.states:
        print("-----------------Analizando----------------------")
        pdf.input_subtitle("Comparación de restaurantes consumidos por estados.")
        #transfomo las ciudades de la lista en un string
        result = ", "
        a = (lambda lst: lst)
        cities = result.join(a(args.states))
        pdf.input_line("Ciudades comparadas: {}.".format(cities))
        pdf.ln()
        compare_state(args.states,pdf)
       
    else:
        print ('Error: se requiere uno o mas argumentos para realizar la accion. Pulsa -h para más información')
    

    pdf.output('analyti1c.pdf', 'F')



if __name__=='__main__':
	main()
