'''
Created on 10 nov. 2020

@author: jesus
'''
from journalists import *
fichero = '../data/cpj.csv'
lista = lee_fichero(fichero)
def test_lee_fichero(lista):
    print("Estas son las 3 primeros periodistas del fichero",lista[:3])

def test_funciones_ordenadoras(lista):
    f = ordena_por_fecha(lista)[:3]
    o = ordena_por_organizacion(lista)[:3]
    print(''' Estas son las 3 primeras lineas del la lista de periodistas ordenada por la fecha {}
    . Y estas son las 3 primeras lineas de la lista de periodistas ordenadas por su organización{}'''.format(f,o))
    
def test_pares_periodista_motivo(lista):
    print(''' Estas son las primeras pparejas nombre y confirmación del motivo''',pares_periodista_motivo(lista)[:3])
    
def test_funciones_conjunto(lista):
    # IMPORTANTE: leer la lista de problemas del dataset en el readme:
    # renombro las funciones para que ocupen menos
    n = conjunto_nacionalidades(lista)
    o = conjunto_organizaciones(lista)
    c = conjunto_coverage(lista)
    m = conjunto_medios(lista)
    print(''' En el dataset aparecen {} nacionalidades distintas  como por ejemplo {} . Además  hay {}
    organizaciones distintas por ejemplo {} que cubren temas como{} en medios tan variados como{} '''.format(len(n),list(n)[:3],len(o),list(o)[:3],c,m))

def test_funciones_seleccionadoras_monoparametrales(lista):
    t = len(selecciona_trabajo(lista,'Camera Operator'))
    p = len(selecciona_pais_fallecimiento(lista,'Iraq'))
    print("Desde 1992 hasta 2017, han muerto {} operadores de cámara y han fallecido {} periodistas en Iraq".format(t,p))
    
def test_funciones_selecionadoras_poliparametrales(lista):
    t_a_s = len(selecciona_torturados_amenazados_y_secuestrados(lista, False, False, False))
    p_y_a = len(selecciona_pais_fallecimiento_y_año(lista,'Iraq', 2016))
    print(''' Solo {} periodistas, no han sido secuestrados, ni amenazados, ni torturados.
    {} Periodistas han muerto en Iraq en 2016'''.format(t_a_s, p_y_a))
 
def test_funciones_total(lista):
    print("Este es el total de periodistas independientes que han sido torturados",total_periodistas_freelance_torturados(lista))
 
def test_diccionario_agrupador(lista):
    n =int( input('¿Qué función quiere ejecutar: 1) agrupa_por sexo,2) agrupa por paises fallecidos,3) agrupa_por_organización  ordenado por año'))
    if n == 1:
        print("Este es el diccionario resultante tras agrupar los sexos",agrupa_por_sexo(lista))
    elif n == 2:
        print("Este es el diccionario resultante tras arupar a los periodistas por pais de fallecimiento",agrupa_por_paises_fallecidos(lista))
    elif n == 3:
        print("Este es el diccionario resultante tras agrupar a los periodistas por su organización y luego ordenarlos por años", agrupa_por_organizacion_ordenado_por_año(lista))
    else:
        print(" La  opción {} no existe por favor, seleccione la opción 1, 2 o 3".format(n))
def test_dicc_contador(lista):
    print("Estos son el total de muertos agrupados por cada mes :",dicc_cont_mes(lista),"Estos son los puertos agrupados por paises",  dicc_cont_pais_fallecidos(lista))

def test_dicc_mas_presentes(lista):
    print(''' La organización con mas periodistas asesinados es {}.
    Este es el tipo de reportaje que mas riesgo tiene cubrir{}
    Y estos son los2 paises mas peligrosos {}'''.format(*organización_mas_presente(lista,1),coverage_mas_presente(lista,1), pais_mas_presente(lista,2))
    )

def test_dicc_primer_periodista_asesinado_por_org(lista):
    print ("Estos son los 3 primeras parejas clave-valor del diccionario que contiene al primer periodista asesinado por organización", list(dicc_primer_periodista_asesinado_por_org(lista).items())[:3])

def test_dicc_media_random_number(lista):
    print("Estas son las  3 primeras medias de los numeros aleatorios asignados a cada org y agrupadas según la organización",list(dicc_media_random_number_por_org(lista).items())[:3])
    
def test_dicc_anual_maximos_mensuales(lista):
    print('''Estos son los 3 "primeras" (es un diccionario, no hay orden) agrupaciones por año de los máximos mensuales''',list(dicc_anual_maximos_mensuales(lista).items())[:3])

def test_separador_dia_par_impar_random_number(lista):
    print(''' Estos son los 5  números aleatorios mas grandes agrupados según su paridad''', separador_dia_par_impar_n_maximos(lista,5))
    
def test_dicc_porcentaje_random_number(lista):
    print("Este es porcentaje que ocupa el numero aleatorio de cada periodista, respecto de su total anual",list(dicc_porcentaje_random_number_respecto_al_total_anual(lista).items())[:3])

def test_comparador_random_number(lista):
    n = int(input("1) comparador version 1. 2) comparador version 2, 3) comparador version 3 (el mejor)"))
    if n == 1:
        print("Estas son las comparaciones de los 7 primeros dias de octubre de 2016 con la versión 1 del comparador",comparador_random_number_v1(lista, 10, 2016)[:7])
    elif n == 2:
        print("Estas son las comparaciones de los 7 primeros dias de octubre de 2016 con la versión 2 del comparador",comparador_random_number_v2(lista, 10, 2016)[:7]) #poner [:7]
    elif n == 3:
        print("Estas son las comparciones de los 7 primeros dias de octubre de 2016 con la versión 3 del comparador",comparador_random_number_v3(lista, 2016, 10)[:7])
    else:
        print("La opción {} no existe,por favor seleccione la opción 1,la 2  o la 3".format(n))


if __name__=='__main__':
    #test_lee_fichero(lista)
    #test_funciones_ordenadoras(lista)
    #test_pares_periodista_motivo(lista)
    #test_funciones_conjunto(lista)
    #test_funciones_seleccionadoras_monoparametrales(lista)
    #test_funciones_selecionadoras_poliparametrales(lista)
    #test_funciones_total(lista)
    #test_diccionario_agrupador(lista)
    #test_dicc_contador(lista)
    #test_dicc_mas_presentes(lista)
    #test_dicc_primer_periodista_asesinado_por_org(lista)
    #test_dicc_media_random_number(lista)
    #test_dicc_anual_maximos_mensuales(lista)
    #test_separador_dia_par_impar_random_number(lista)
    #test_dicc_porcentaje_random_number(lista)
    test_comparador_random_number(lista)
   