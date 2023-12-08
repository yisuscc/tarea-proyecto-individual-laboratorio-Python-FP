'''
Created on 10 nov. 2020

@author: jesus
'''
# IMPORTS

import csv 
import datetime
from collections import  namedtuple, Counter
from calendar import monthrange


#funciones auxiliares 
def rellena_desconocidos(celda):
    ''' relena con unknown los huecos vacios'''
    if celda =="":
        celda = "Unknown"
    else:
        celda = celda
    return celda 

def  creador_false(celda):
    '''
    La intencion es que rellene los huecos vacios o distinto de yes del fichero modificado con un false pensado para las columnas con huecos vacios
    '''
    if celda == 'Yes':
        celda = True
    else:
        celda = False
    return celda


def separador(lista):
    sep_1 = [] #guarda la separación por comas
    sep_2= [] #guarda la separacion por /
    #separacion por comas
    for element in lista:
        for item in element.split(','):
            sep_1.append(item.strip())
    # separacion por barras
    for elemento in sep_1:       
        for item in elemento.split('/'):
            item_1 = item.strip() #elimina espacios
            item_2 = item_1.capitalize()#capitaliza
            sep_2.append(item_2)
    return sep_2

def localizador_maximo_random_number(año,mes_numero,lista):
    lista_aux = []
    for periodista in lista:
        if periodista.date.year == año and mes_numero == periodista.date.month:
            lista_aux.append(periodista.random_number)
        else:
            lista_aux.append(0)
    maximo = max(lista_aux)
    return maximo
            
     

# funciones principales
Periodista = namedtuple('Periodista', 'type,date,name,sex,country_killed,organization,nationality,medium,job,coverage,freelance,local_Foreign,source_fire,type_death,impunity_for_murder,taken_captive,threatened,tortured,random_number') 
periodista = Periodista # para que me salga en el autocompletar   

def lee_fichero(fichero): 
    with open(fichero,'r',encoding='utf-8')  as f:
        lector = csv.reader(f)
        next(lector)
        res =[Periodista(str(type),
                          datetime.datetime.strptime(date,"%B %d, %Y"),
                          name,
                          rellena_desconocidos(sex),
                          rellena_desconocidos(country_killed),
                          rellena_desconocidos(organization),
                          rellena_desconocidos(nationality),
                          rellena_desconocidos(medium),
                          rellena_desconocidos(job),
                          rellena_desconocidos(coverage),
                          bool(creador_false(freelance)),
                          rellena_desconocidos(local_Foreign),
                          rellena_desconocidos(source_fire),
                          rellena_desconocidos(type_death),
                          bool(creador_false(impunity_for_murder)),
                          bool(creador_false(taken_captive)),
                          bool(creador_false(threatened)),
                          bool(creador_false(tortured)),
                          int(random_number))
                          for type,date,name,sex,country_killed,organization,nationality,medium,job,coverage,freelance,local_Foreign,source_fire,type_death,impunity_for_murder,taken_captive,threatened,tortured, random_number in lector]
    return res
# Funciones ordenadoras
def ordena_por_fecha(lista):
    '''
    Devuelve la lista de namedtuple periodista enera pero ordenada por fecha
    ordenarFecha: Devuelve la lista de registros ordenados según el valor de la fecha
    '''
    res = sorted(lista, key = lambda periodista:periodista.date)
    return res 

def ordena_por_organizacion(lista):
    '''
    Devuelve la lista de namedtuple periodista enera pero ordenada por fecha
    ordenarFecha: Devuelve la lista de registros ordenados según el valor de la fecha
    '''
    res = sorted(lista, key = lambda periodista:periodista.organization)
    return res

#funcion paresxy
def pares_periodista_motivo(lista):
    '''
    paresXY: Devuelve un listado de tuplas con los valores de los atributos X,Y
    '''
    res =[(periodista.name,periodista.type) for periodista in lista]
    return res


# funciones conjunto 
'''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.)
'''
  
def conjunto_paises(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.)
 Devuelve el cunjunto de todos los paises del dataset
    '''
    #funciona
    res ={periodista.country_killed for periodista in lista}
    return res 

def conjunto_organizaciones(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.)
 Devuelve el conjunto de todas las organizaciones presentes
    '''
    
    res = {periodista.organization for periodista in lista}
    return res

def conjunto_sexo(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.).
 Devuelve el conjunto de todos los sexos presentes en el dataset.
    '''
    
    res ={periodista.sex for periodista in lista}
    return res
def conjunto_tipo_muerte(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.).
 Devuelve el conjunto de todos los tipos de muerte presentes en el dataset.
    '''
    res ={periodista.type_death for periodista in lista}
    return res
def conjunto_medios(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.).
 Devuelve el conjunto de todos los tipos de medios presentes en el dataset previamente separandolos puesto que las celdas de medios contienen varios atributos en una misma celda
    '''
    list_aux = [periodista.medium for periodista in lista]
    res = set(separador(list_aux))
    return res
    
    
def conjunto_trabajo(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.).
 Devuelve el conjunto de todos los tipos de trabajos presentes en el dataset previamente separandolos por la misma razon qu en conjunto medios.
    '''
    res = [periodista.job.strip(',') for periodista in lista]
    res = set(separador(res))
    return res 

def conjunto_coverage(lista):
    '''
Función que cuente el número de valores distintos de un atributo o que devuelva un conjunto 
con los valores distintos (ver como ejemplo la función numero_nacionalidades_distintas del proyecto Extranjeria,
 o la función calcula_paises del proyecto Poblaciones.).
 Devuelve el conjunto de todos los tipos de reportajes presentes en el dataset preiamente separandolos, ver la función conjunto medios para el razonamiento.
    '''
    list_aux = [periodista.coverage for periodista in lista]
    res = set(separador(list_aux))
    return res

def conjunto_nacionalidades(lista): 
    list_aux = [periodista.nationality for periodista in lista]
    res = set(separador(list_aux))
    return res
        
# Funcion filtro con varios parametros
def selecciona_torturados_amenazados_y_secuestrados(lista,torturado=False, amenazado= False, secuestrado= False): 
    '''
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    seleccionaXY:  Igual que la anterior pero el filtro debe cumplir dos restricciones, por tanto debe estar formado por una condición and/or
    '''
    res = []
    for periodista in lista:
        if periodista.taken_captive == secuestrado and periodista.threatened == amenazado and periodista.tortured == torturado :
            res.append((periodista))
    return res



def selecciona_pais_fallecimiento_y_año(lista,pais_fallecimiento='Libya',año=1970):
    '''
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    seleccionaXY:  Igual que la anterior pero el filtro debe cumplir dos restricciones, por tanto debe estar formado por una condición and/or
    '''
    res = []
    for periodista in lista:
        if periodista.date.year == año and pais_fallecimiento == periodista.country_killed:
            res.append((periodista))
    return res 

# filtros con un solo parametro:
    '''
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si coinciden con los parametros dados
    '''

def selecciona_por_nacionalidad(lista, nacionalidad):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
     
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si coinciden con los parametros dados(nacionalidad)
    '''
    res = []
    for periodista in lista:
        if periodista.nationality == nacionalidad:
            res.append(periodista)
    return res

def selecciona_organizacion(lista, organización):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y 
    devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera) y la mete en una lista si coinciden con los parametros dados (organizacion)
    '''
    res = []
    for periodista in lista:
        if periodista.organization == organización:
            res.append(periodista)
    return res 

def selecciona_medio(lista,medio):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
     
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si si el parametro dado está presente en la columna(medio) ver README para ver el razonamiento
    '''
    res =[]
    for periodista in lista:
        if medio in periodista.medium:
            res.append(periodista)
    return res
    
def selecciona_trabajo(lista,trabajo):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
     
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si si el parametro dado está presente en la columna(trabajo)
    '''
    res = [periodista for periodista in lista if trabajo in periodista.job]
    return res 

def selecciona_coverage(lista,coverage):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) 
    y devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si si el parametro dado está presente en la columna(coverage)
    '''
    res = [periodista for periodista in lista if coverage in periodista.coverage]
    return res 

def selecciona_pais_fallecimiento(lista, pais_fallecimiento='Libya'):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) 
    y devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si si el parametro dado está presente en la columna(country_killed)
    '''
    res = []
    for periodista in lista:
        if periodista.country_killed == pais_fallecimiento:
            res.append(periodista)
    return res 

def selecciona_nacionalidad(lista, nacionalidad):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) 
    y devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    
    Seleccionan la tupla periodista (entera y la mete en una lista si si el parametro dado está presente en la columna(nacionalidad)
    '''
    res = []
    for periodista in lista:
        if nacionalidad in periodista.nationality:
            res.append(periodista)
    return res

def selecciona_sexo(lista, sexo):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) 
    y devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset
     (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
     '''
    res = [periodista for periodista in lista if sexo == periodista.sex]
    return res

def selecciona_freelance(lista,freelance):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset
     (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
     '''
    res = [periodista for periodista in lista if freelance == periodista.freelance]
    return res

def selecciona_tipo_muerte(lista,muerte):
    '''
    seleccionaX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro
    Función que filtre y/o seleccione una serie de filas y/o columnas del dataset 
    (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.
    '''
    res = [periodista for periodista in lista if muerte == periodista.type_death]
    return res

# Funciones 'total':
def total_periodistas_freelance_torturados(lista):
    '''
    conteoX: Recibe como parámetro un valor (puede ser del tipo que queráis) y
     devuelve el número de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro pero con 2 parametros
     
    Función que calcule la suma, el total, o la media de una propiedad. 
    Ejemplos de funciones de este tipo son: calcular_total_camas_centros_accesibles y 
    calcular_media_coordenadas del proyecto Centros Sanitarios.
    
    En este caso las condiciones son si han sidocapturados y si son independientes 
    '''
    contador = 0
    for periodista in lista:
        if  periodista.taken_captive == True and periodista.freelance == True:
            contador +=1
    return contador
    
#Funciones diccionario:
def agrupa_por_paises_fallecidos(lista):
    
    '''
    Función que agrupe en un diccionario una lista de las filas del dataset, teniendo como clave algunos de las columnas del dataset.
    
    Dada una lista de periodistas, crea un diccionario cuyas claves son los paises donde han fallecido y los valores los nombres de los periodistas
    fallecidos en ese país junto con el año de la muerte
    '''
    dic = dict()
    for periodista in lista:
        
        if periodista.country_killed in dic:
            dic[periodista.country_killed].append((periodista.name,periodista.date.year))
        else:
            dic[periodista.country_killed] = [(periodista.name, periodista.date.year)]
    return dic

def agrupa_por_sexo(lista):
    '''
    Función que agrupe en un diccionario una lista de las filas del dataset, teniendo como clave algunos de las columnas del dataset.
    Igual que el anterior pero con el sexo y solo almacena el nombre
    '''
    dicc = dict()
    for periodista in lista:
        clave = periodista.sex
        valor = periodista.name
        if clave in dicc:
            dicc[clave].append(valor)
        else:
            dicc[clave] =  [valor]
    return dicc

def agrupa_por_organizacion_ordenado_por_año(lista):
    '''
    Una combinación de los 2  siguientes enunciados:
    Función que devuelva un diccionario en el que los valores son el máximo de una propiedad, ordenados de mayor a menor. 
    Ejemplo: ventas_por_año del ejercicio videojuegos (ordenando el año de mayor a menor total de ventas) y ejemplos de clase de teoría.
    y 
    Función que agrupe en un diccionario una lista de las filas del dataset, teniendo como clave algunos de las columnas del dataset.
    
    Dada una lista de periodistas crea un diccionario cuyas claves son las organzaciones para las que trabajaban y los valores son los nombres y el año de la muerte, 
    ordenados por su año
    '''
   
    dic = dict()
    res_dic = dict()
    lista_aux = []
    for periodista in lista:#crea un diccionario
        clave = periodista.organization
        valor = (periodista.name,periodista.date.year)
        if clave in dic:
            dic[clave].append(valor)
        else:
            dic[clave] = [valor]
    for clave  in dic.keys(): #ordena el diccionario anterior
        valores = dic.get(clave)
        valores_ordenados = sorted(valores,reverse = True ,key = lambda x : x[1])
        res_dic[clave] = valores_ordenados
    return res_dic

def dicc_cont_mes(lista):
    '''
    agrupaXFecha: Devuelve un diccionario que relaciona el número de  
    registros de un mes o un año en concreto (por ej: cuenta total de aplicaciones que se generan en cada mes)
    
    Función que devuelva un diccionario en el que el valor sea suma de una cierta propiedad
     de las tuplas agrupadas por una clave en concreto. 
     Ejemplo: total_extranjeros_por_pais del proyecto 02_Extranjeria y ejemplos puestos en teoría.
    
    cuenta los periodistas fallecidos por cada mes independientemente del año
     '''
    
    dicc_cont = dict()
    for periodista in lista:
        clave = periodista.date.strftime('%B')# nos da el mes en "letra"
        if clave not in dicc_cont:
            dicc_cont[clave]  =1
        else:
            dicc_cont[clave] += 1
    return dicc_cont

def dicc_cont_pais_fallecidos(lista):
    '''
    Función que devuelva un diccionario en el que el valor sea suma de una cierta propiedad de las tuplas agrupadas 
    por una clave en concreto. 
    Ejemplo: total_extranjeros_por_pais del proyecto 02_Extranjeria y ejemplos puestos en teoría.
    '''
    dicc_cont = dict()
    for periodista in lista:
        clave = periodista.country_killed
        if clave not in dicc_cont:
            dicc_cont[clave]  =1
        else:
            dicc_cont[clave] += 1
    return dicc_cont

def organización_mas_presente(lista,n):
    '''
    - registroMasX:  Devuelve el registro con mayor valor de X
    
    Función que devuelva los N (que se pasa por parámetro a la función) claves con más/menos número de elementos 
    para una clave en concreto, tras agruparlos por una propiedad y contar cuántos elementos hay de esa propiedad (clave). 
    Ejemplo: genero_mas_presente proyecto videojuegos, pero en vez de máximo, se cogen los N elementos.
    
    '''
    #se puede ampliar 
    lista_org = [periodista.organization for periodista in lista]
    dic_cont = Counter(lista_org)
    lista_tupla = [(clave,valor)for clave, valor in dic_cont.items()]# se puede  hacer con un list(dicc.items())
    lista_tupla_ordenadas = sorted(lista_tupla, key=lambda x:x[1], reverse=True)
    return lista_tupla_ordenadas[:n]

def pais_mas_presente(lista ,n):
    '''
    - registroMasX:  Devuelve el registro con mayor valor de X
    
    Función que devuelva los N (que se pasa por parámetro a la función) claves con más/menos número de elementos para una clave en concreto, tras agruparlos por una propiedad y contar cuántos elementos hay de esa propiedad (clave)
    . Ejemplo: genero_mas_presente proyecto videojuegos, 
    pero en vez de máximo, se cogen los N elementos.
    '''
    lista_pais = [periodista.country_killed for periodista in lista]
    dic_cont = Counter(lista_pais)
    lista_tupla = [(clave,valor)for clave, valor in dic_cont.items()]
    lista_tupla_ordenadas = sorted(lista_tupla, key=lambda x:x[1], reverse=True)
    return lista_tupla_ordenadas[:n]

def coverage_mas_presente(lista,n):
    '''
    - registroMasX:  Devuelve el registro con mayor valor de X
    Función que devuelva los N (que se pasa por parámetro a la función) claves con más/menos número de elementos para una clave en concreto, 
    tras agruparlos por una propiedad y contar cuántos elementos hay de esa propiedad (clave).
     Ejemplo: genero_mas_presente proyecto videojuegos, pero en vez de máximo, se cogen los N elementos.
    Caso en el que la columna posea varios elementos dentro por celda
    '''

    #como es una columna que contienen varios elementos por celda, voy a asegurarme de que estén bien capitalizados
#    lista_aux = [periodista.coverage for periodista in lista]
    lista_coverage_separados = separador([periodista.coverage for periodista in lista])
    dic_cont = Counter(lista_coverage_separados)
    lista_tupla = [(clave,valor)for clave, valor in dic_cont.items()]
    lista_tupla_ordenadas = sorted(lista_tupla, key= lambda x:x[1], reverse=True)
    return lista_tupla_ordenadas[:n]
    
def dicc_primer_periodista_asesinado_por_org(lista):
    '''
    ES una sintesis del tipo de función agrupa por categoría y ordena por fecha
    Devuelve un diccionario cuyas claves son las organizaciones y cuyos valores son  una tupla
    con el primer  periodista de cada organización junto con el año
    Se puede hacer con  una llamada a la función agrupa_por_organizacion_ordenado por año 
    y asignando a acada clave el elemento que esté en la posición valor[-1]
    '''
    dic_aux = dict()
    for  periodista in lista:
        clave = periodista.organization
        valor = (periodista.name,periodista.date)
        if clave not in dic_aux:
            dic_aux[clave] = [valor]
        else:
           dic_aux[clave].append(valor)
    res = {clave:min(dic_aux[clave], key = lambda x:x[1]) for clave in dic_aux.keys()}#asigna a la clave el periodista con el año mas pequeño
    return res 

def dicc_media_random_number_por_org(lista):
    '''
    Es una función que crea un diccionario cuyas claves son las organizaciones y cuyos valores son las medias de los numeros aleatorios de los periodistas de cada organización.
    
    variación del enunciado de: Función que devuelva un diccionario en el que los valores son un tanto por ciento. En vez de un porcentaje, devuelve unla media
    '''

    dic = dict()
    res = {}
    for periodista in lista:
        clave = periodista.organization
        valor = periodista.random_number
        if clave not in dic :
            dic[clave] = [valor]
        else:
            dic[clave].append(valor)
    for clave in dic.keys():
        media = sum(dic[clave])/len(dic[clave])
        res[clave] = media
    return res  
    

def dicc_anual_maximos_mensuales(lista):
    '''
    
    Función que agrupe los registros a partir de la fecha en un diccionario,
    donde la clave sea el año y el valor sea una lista de 12 elementos, con los mayores valores de una propiedad en cada mes.
    
    Hace un diccionario cuyas claves son los  años y cuyos valores son una lista  de 12 elementos de los random_number maximos de cada mes
    '''
    dic = {}
    for periodista in lista:
        clave  = periodista.date.year
        if clave not in dic:
            dic[clave] = [localizador_maximo_random_number(clave,i, lista) for i in range(1,13)]#los meses numericos nos lo da el range 
    return dic

def separador_dia_par_impar_n_maximos(lista,n):
    '''
    Función que devuelva un diccionario cuya clave sea PAR/IMPAR dependiendo de si el día de una propiedad de tipo fecha es par/impar y
     el valor sea los N mayores elementos de esa categoría según una propiedad diferente y numérica.
     La propiedad en este caso es el número aleatorio
     '''
    # 1º Creamos el diccionario que discrimina segun si el dia es par o impar y seleciona los números aleatorios como valor
    dic_paridad = {"DIA_PAR":[],"DIA_IMPAR":[]}
    for periodista in lista:
        #caso par
        if periodista.date.day %2 == 0:
            dic_paridad["DIA_PAR"].append(periodista.random_number)
        #caso impar (el resto)
        else:
            dic_paridad["DIA_IMPAR"].append(periodista.random_number)
    
    #2º ordenamos y seleccionamos los n numeros mas grandes de cada clave
    for clave in dic_paridad.keys():     
        dic_paridad[clave]= sorted(set(dic_paridad[clave]), reverse=True)[:n] #para que no haya repeticiones meto los valores en un set
    return dic_paridad
    
def dicc_porcentaje_random_number_respecto_al_total_anual(lista):
    '''
    Función que devuelva un diccionario en el que los valores son un tanto por ciento. 
    Ejemplo: dicc_porcentaje_ventasJP_por_año del proyecto videojuegos.
    
     Es una función que devuelve un diccionario cuyas claves son los nombres de los periodistas y 
     cuyos valores son el porcentaje que ocupa el número aleatorio de cada periodista respecto al total de su organización.
     '''
    
    res = {}
    for periodista in lista:
        clave = periodista.name
        año = periodista.date.year
        
        if clave not in res:
            lista_rand_num = [periodista.random_number for periodista  in lista if periodista.date.year == año]
            porcentaje = periodista.random_number/sum(lista_rand_num) *100
            res[clave]= porcentaje
    return res 



def comparador_random_number_v1(lista, mes,año):
    
    '''
    Función que devuelva una lista de tuplas (fecha, incremento/decremento) 
    (datetime.datetime, float) utilizando un diccionario en el que, dado una lista de tuplas de vuestro dataset, 
    un mes y un año, las claves son los días del mes (lo entiendo como un int) y los valores son los incrementos/decrementos repecto al día anterior
     (del que se dispongan datos).
     Si para una fecha no hay datos, devolverá (fecha, 0).
    
    '''
    '''
    En esta versión del comparador. Primero, se crea un diccionario cuyas 
    claves son los dias que cumplen la condición de mes y de año y sus valores son los numeros aleatorios 
    correspondientes, a continuación, se rellena el diccionario con los dias que falten y se les asignan como valor un cero y 
    finalmente hace la comparación de los dias, esto hace que el valor de el primer dia que cumpla la condición su incremento/ decremento 
    sea igual a su número aleatorio.
    Devuelve una lista de tuplas con (datetime.datetime (año,mes,dia) y un float)
    '''
    #NOTA: En este caso las claves de los diccionarios son los dias comoun int que se pasan a datetime mediante un zip
    dic_fechas = {periodista.date.day:periodista.random_number for periodista in lista if periodista.date.year == año and periodista.date.month ==mes}
    dic_fechas[0] = 0.0 # añadimos el dia cero
    dic_incrementos = {}
    n_dias = monthrange(año, mes)[1]
    # completamos los dias
    lista_dias_mes = []
    for dia in range(1,n_dias+1): #+1 para que aparezca el último dia 
        lista_dias_mes.append(datetime.datetime(año,mes,dia)) #creamos las fechas a prateir de los dias de tipo datetime 
        if dia not in dic_fechas.keys(): # completa los dias
            dic_fechas[dia] = 0.0
        dic_incrementos[dia] = float(dic_fechas[dia] - dic_fechas[dia-1]) #hace la comparación
        
    lista_valores = list(dic_incrementos.values())
    res = zip(lista_dias_mes,lista_valores)
    return list(res)

def comparador_random_number_v2(lista, mes,año):
    
    '''
    Función que devuelva una lista de tuplas (fecha, incremento/decremento) 
    (datetime.datetime, float) utilizando un diccionario en el que, dado una lista de tuplas de vuestro dataset, 
    un mes y un año, las claves son los días del mes(lo entiendo como un datetime.datetime) y los valores son los incrementos/decrementos repecto al día anterior
     (del que se dispongan datos).
     Si para una fecha no hay datos, devolverá (fecha, 0).
    
    Este comparador , primero compara los numeros aleatorios de los día que cumplen la condición de año y mes (primero con el último, 
    si el primer dia disponible es el 2 y el ultimo es el 8 compara el numero aleatorio del 2 con el 8) ,  despué rellena con los días que faltan
    '''
    #NOTA en este caso las claves de los diccionarios son los dias en tipo datetime.datetime
    dic_fechas = {datetime.datetime(año,mes,periodista.date.day):periodista.random_number for periodista in lista if periodista.date.year == año and periodista.date.month ==mes}
    dic_incrementos = dict()
    n_dias = monthrange(año, mes)[1]
    lista_dias_disponibles = sorted(list(dic_fechas.keys()))
    
    # hacemos la comparacion (es circular el prime dia disponibe , se compara con el último dia disponible)
    for posicion in range(len(lista_dias_disponibles) ):#creo que se puede reducir a un solo bucle con un enumerate y un lambda 
        dia = lista_dias_disponibles[posicion]
        dic_incrementos[dia] = float( dic_fechas[lista_dias_disponibles[posicion]]- dic_fechas[lista_dias_disponibles[posicion-1]])# compara y convierte a float
    #rellenamos         
    for dia in range(1, n_dias+1):
        fecha = datetime.datetime(año,mes,dia)
        if fecha not in dic_incrementos.keys():
            dic_incrementos[fecha] = 0.0

    res = sorted(dic_incrementos.items())
    return res

def comparador_random_number_v3(lista, año,mes):
    '''
    Igual que el compardor v1 pero con timedelta y por ende solo datetimes
    '''
    dicc_fechas = {periodista.date:float(periodista.random_number) for periodista in lista if periodista.date.year == año and periodista.date.month == mes}
    n_dias = monthrange(año, mes)[1]
    dicc_incrementos = {}
    
    #bucle que rellena los dias que faltan:
    for dia in range(1,n_dias+1): #para que aparzca el último día
        fecha = datetime.datetime(año,mes,dia)
        if fecha not in dicc_fechas:
            dicc_fechas[fecha] = 0.0
    #añadimos el dia 1 al diccionario de incrementos 

    dia_uno = datetime.datetime(año,mes,1)
    dicc_incrementos[dia_uno] = float(dicc_fechas[dia_uno])
    # bucle comparador compara a partir del dia 2
    for dia in range(2,n_dias+1): #se empieza con un 2 porque el uno no se puede comparar con el cero, porque no existe
        fecha = datetime.datetime(año,mes,dia)
        fecha_anterior = fecha - datetime.timedelta(days =1)
        dicc_incrementos[fecha] = float(dicc_fechas[fecha] - dicc_fechas[fecha_anterior])
    
    res = sorted(dicc_fechas.items())
    return res 

    
            