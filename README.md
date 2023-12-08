# Proyecto individual laboratorio de Jesús Carrascosa Carro IC-3: Periodistas asesinados desde 1922.
## Descripción del datataset:
Este dataset consta de unas 19 columnas:
> *Type,Date,Name,Sex,Country_killed,Organization,Nationality,Medium,Job,Coverage,Freelance,Local_Foreign,Source_fire,Type_death,Impunity_for_murder,Taken_captive,Threatened,Tortured,Random_number*.

De las cuales 12 son de tipo **str** (*Type,Date, Name, Sex, Country_killed,Organization,Nationality, Medium,Job,Coverage,Local_Foreign,Source_fire,Type_death*).Otra  es de tipo str pero que se corresponde a una fecha,por lo tanto hay  que convertirla a datetime con la ayuda de datetime.strptime(*Date*), Enteros (Random_number), PseudoBooleanos (Freelance, contiene Yes, No y Partial,este ultimo va a ser interpretado como un No mediante la funcion **conversor_booleano**) y booleanas (son las columnas *Impunity for murder,Taken captive,Threathened,Tortured*). Aparte este dataset, contiene unas columnas (*nationality,medium, job, coverage) en las que hay varios elementos dentro de una misma columna, lo que implica  la necesidad de separar dichos elementos para no tomarlos como uno solo.
## Problemas del dataset:
Este dataset tiene una serie de problemas:
- Hetereogenedidad de las fechas en la columna Date: Ha sido resuelto modificando las fechas que no cumplian con la estructura (Mes dia, año) por lo cual las fechas no se deben de considerar como correctas.
- Celdas vacias: para solucionar este problema, se  utiliza la función **rellena_desconocidos** que me rellena las celdas vacías con Unknown, y para las celdas vacias de booleanos se utiliza la función **creador_false** que interpreta todo lo que sea distinto de Yes como un False incluyendo celdas vacías, esta función además sirve para corregir el problema que se  sdescribe a continuación.
- Permutación de los elementos de una columna con otra: en algunas líneas, se da el caso de que un dato que debería pertenecer a una columna aparece en otra, esto sobretodo perjudica  a las columnas booleanas y pseudobooleanas. Por lo tanto para solucionarlo se ha utilizado la función **creador_false** que convierte todo lo que sea distinto de Yes en un False.Pese a que este problema también está presente en las columnas de tipo str, al no dar un conflito de tipos, no se han modificado, por lo tanto es posible que una organización aparezaca en la columna de nacionalidad entre otros casos.

## Modificaciones hechas al dataset:
- Homogeneización de las fechas en la columna *Date*.
- Eliminación de una columna sin nombre que solo tenía un dato.
- Añadida una columna de enteros llamada *Random_number*.

## Estructura y descripción del código:
### Funciones Auxiliares:
#### 1º rellena_desconocidos:
Es una función auxiliar, que cuando es invocada sobre una celda, si está vacía la rellena con un Unknown (desconocido en inglés) y si no , la deja tal cual. Esta función auxiliar se utiliza en la función principal **lee_fichero**, para rellenar las celdas vacías en las columnas de tipo **str**.
#### 2º creador_false:
Es una función auxiliar que se utiliza para convertir valores binarios(Yes, No) en valores **bool**. Los convierte a booleanos asignando el valor True a Yes y al resto les asigna el valor False, esto es así ya que hay celdas vacías o cuyo valor no corresponde con la columna en la que se encuentra.

#### 3º separador:
Esta es una función auxiliar que se utiliza en un subtipo de funciones conjunto, que contienen varios elementos por celda. Dada una lista de elementos que contenga elemento anidados(es decir que dentro de la lista  haya elementos formados por dos o más elementos).los separa en elementos individuales

#### 4º localizador_maximo_random_number:
Es una función auxiliar que recibe como parametros, un año, un mes en formato numérico, y una lista . Devolviendo el maximo numero aleatorio que se encuentre en los periodistas que murieron en la misma fecha(año, mes), en caso de que no hubiese periodista en esa fecha devuelve un cero.
### Funciones Principales:
#### 1.lee_fichero:
Es una función que abre el fichero, se salta la cabecera, y que mediante un bucle for, asigna los tipos a cada columna (con ayuda de la las funciones auxiliares **rellena_desconocidos** para las str y **creador_false** para las booleanas) y los mete en la tupla con nombre Periodista.

Recibe un fichero *csv* y devuelve una lista de *namedtuple* Periodista.

#### 2. Funciones ordenadoras:
Son las funciones **ordena_por_fecha** y **ordena_por_organizacion**.Se corresponden con las funciones requeridas: ordenarFecha(*Devuelve la lista de registros ordenados según el valor de la fecha*) y ordenarX (*Devuelve la lista de registros ordenados según el valor del atributo X*).
#### 3. Función pares_periodista_motivo:
Se corresponde con la función requerida ParesXY (*Devuelve un listado de tuplas con los valores de los atributos X,Y*). En este caso, Reive una lista de tuplas Periodista y devuelve otra  formada por el nombre y la confirmación del motivo.
Recibe *lista de tuplas* -> Devuelve *lista de tuplas* de 2 elementos (*str*,*str*)


#### 4.Funciones conjunto(conjunto_paises, conjunto organizaciones, conjunto_sexo, conjunto_tipo_muerte, conjunto_medios,conjunto_trabajo,conjunto_coverage, conjunto_nacionalidades):
Este tipo de funciones se pueden dividir en 2 funciones, las que están asociadas a columnas con un solo valor como son las funciones conjunto_paises, conjunto organizaciones, conjunto_sexo, conjunto_tipo_muerte y las que están asociadas las columnas con varios elementos como son las funciones conjunto_medios,conjunto_trabajo,conjunto_coverage y conjunto_nacionalidades, para estas últimas, se utiliza la función **separador**, que nos separa los elementos.
La finalidad  de este tipo de funciones es agrupar todos los elementos de cada columnas sin que se repitan(por eso se utiliza los conjuntos).

Recibe una lista de *namedtuple* Periodista y devuelve un *set*
#### 5.Funciones Seleccionadoras:
Filtran por uno o mas atributos y devuelven la tupla entera. Se corresponde con la función requerida para el 8 de diciembre(*Función que filtre y/o seleccione una serie de filas y/o columnas del dataset (ver como ejemplo, las funciones filtra_por_pais o filtra_por_paises_y_años del proyecto Poblaciones.*). Que tambíen se corresponde con los tpos de función requerida Selecciona_X(* Recibe como parámetro un valor (puede ser del tipo que queráis) y devuelve el conjunto de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro*) y la función Selecciona_XY(*Igual que la anterior pero el filtro debe cumplir dos restricciones, por tanto debe estar formado por una condición and/or*).
 Reciben una lista de *namedtuple* ->Devuelven una lista de *namedtuple*
 

#### 6. Función total_periodistas_freelance_torturados:
Es una función que calcula el número total de periodistas freelance(independientes) que han sido torturados. Se corresponde con la 3ª función solicitada para el día 8 de diciembre:
*Función que calcule la suma, el total, o la media de una propiedad*. Que también se corresponde con la función requerida de tipo conteoX(* Recibe como parámetro un valor (puede ser del tipo que queráis) y devuelve el número de registros que cumplen que el atributo X tiene un valor igual/mayor/menor a ese valor del parámetro*).

Devuelve un *int*
#### 7. Funciones diccionario:
Esta categoría de funciones agrupa a disversas subcategorias que en su funcionamiento, utilizan los diccionarios.:
	##### 5.1 Diccionarios agrupadores:
Esta subcategoría está compuesta por  funciones que utilizan los diccionarios para agruparac. Las funciones son las siguientes:
###### 7.1.1 agrupa_por_paises_fallecidos:
Esta función agrupa a los periodistas por su pais de fallecimiento, siendo esa la clave , y los valores se componen por una tupla formada por el nombre y el año de fallecimiento. 
###### 7.1.2 agrupa_por_sexo:
Esta función utiliza como clave el género/sexo del periodista y como valor solamente el nombre.
###### 7.1.3 agrupa_por_organizacion_ordenado_por_año:
Crea un diccionario cuyas claves son las organizaciones y cuyos valores son una lista de tuplas formadaas por el nombre del periodista y el año. Posteriormente al diccionario se le aplica un bucle for al diccionario que le reasigna a las claves sus lista de tuplas que ha sido ordenada por año anteriormente mediante la función sorted.
 Se corresponde con la 2º función solicitada para el 22 de diciembre: *Función que devuelva un diccionario en el que los valores son el máximo de una propiedad, ordenados de mayor a menor.
 
Recibe una lista de *namedtuple* Periodista  y devuelve un diccionario cuyos valores son [(*str*,*datetime.datetime*)].
##### 7.2 Diccionarios contadores:
###### 7.2.1 diccionarios contadores básicos:
Se corresponden con las funciones **dicc_cont_mes** y **dic_cont_random_number**.  Son diccionarios contadores que cuentan las veces que aparecen las claves mediante un bucle for.

Recibe una lista de *namedtuple* Periodista -> Devuelve un Diccionario de valores *int*.
###### 7.2.2 funciones mas presentes:
Se corresponden con las funciones **organización_mas_presente**, **pais_mas_presente** y  **coverage_mas_presente**. Mediante el objeto counter  se mide la frecuencia con la que aparecen las organizaciones, los paises o los temas de reportaje en la lista de namedtuple Periodista. A continuación ese diccionario es transformado a una lista de tuplas clave-valor que posteriormente es ordenada en de mayosr a menor según su orden descendente. Finalmente de la lista de tuplas se coge las n primeras tuplas que coincide con las organizaciones, países o temas de reportaje mas presentes y su correspodiente frecuencia  que más se repiten.
Se corresponde con la 3º función solicitada para el día 22: *Función que devuelva los N (que se pasa por parámetro a la función) claves con más/menos número de elementos para una clave en concreto, tras agruparlos por una propiedad y contar cuántos elementos hay de esa propiedad (clave)* ycon  la función requerida: *- registroMasX:  Devuelve el registro con mayor valor de X*.

Recibe una lista de *namedtuple* Periodista -> Devuelve una tupla (*str*, *int*).

##### 7.3 Otros Diccionarios:
###### 7.3.1 dicc_primer_periodista_asesinado_por_org:
Es una función que crea un diccionario cuyas claves son las organizaciones  y cuyos valores son una tupla formada por el nombre del primer periodista asesinado de dicha organización y su año. Es una variacíon de la función 5.1.3 y 52.1.

Recibe una lista de *namedtuple* Periodista y defuelve un diccionario cuya clave es *str* y sus valores son *str,int.*

###### 7.3.2 dicc_media_random_number_por_org:
Es una función que crea un diccionario cuyas claves son las organizaciones y cuyos valores son las medias de los numeros aleatorios de los periodistas de cada organización.
Recibe uan lista de *namedtuple* Periodista ->Devuelve un diccionario cuyas claves son organizacion(*str*) y cuyos valores son la media(*float*)

###### 7.3.3 dicc_anual_maximos_mensuales:
Se corresponde con la 1º función solicitada para el 8 de enero:*Función que agrupe los registros a partir de la fecha en un diccionario, donde la clave sea el año y el valor sea una lista de 12 elementos, con los mayores valores de una propiedad en cada mes*. La propiedad en este caso es el random number, en caso de que no haya para ese mes un random number se le asigna un cero.

Recibe una lista de *namedtuple* Periodista -> Devuelve un diccionario cuyas claves son de tipo *int* y cuyos valores son una lista de 12 elementos de tipo *int*.

###### 7.3.4 separador_dia_par_impar_n_maximos:
 Se corresponde con la 2º función para el día 8 de enero: *Función que devuelva un diccionario cuya clave sea PAR/IMPAR dependiendo de si el día de una propiedad de tipo fecha es par/impar y el valor sea los N mayores elementos de esa categoría según una propiedad diferente y numérica.*. La propiedad en este caso es el random_number de cada periodista.
 Recibe una lista de *namedtuple* y n de tipo *int*. -> Devuelve un diccionario cuyas claves son de tipo *str* y cuyos valores son una lista de n elementos de tipo *int*.

###### 7.3.5 dicc_porcentaje_random_number:
Es una función que devuelve un diccionario cuyas claves son los nombres de los periodistas y cuyos valores son el porcentaje que ocupa el número aleatorio de cada periodista  respecto al total de su organización.

 Se corresponde con la 3º Función solicitada para el 8 de enero: *Función que devuelva un diccionario en el que los valores son un tanto por ciento*.
 
 Recibe una lista de *namedtuple* Periodista -> Devuelve un diccionario de clave *str* y de valor *float*.
 
###### 7.3.6 comparador_random_number:
Se corresponde con la 4 función solicitada para el día 8 de enero: *Función que devuelva una lista de tuplas (fecha, incremento/decremento) (datetime.datetime, float) utilizando un diccionario en el que, dado una lista de tuplas de vuestro dataset, un mes y un año, las claves son los días del mes y los valores son los incrementos/decrementos repecto al día anterior (del que se dispongan datos). Si para una fecha no hay datos, devolverá (fecha, 0)*.
En este caso los elementos a comparar son los random number disponibles.Hay tres variaciones de este tipo de función según como se interprete el enunciado:
####### 7.3.6.2 comparador_random_number_v1:
En esta primera versión del comparador. Primero, se crea un diccionario cuyas claves son los dias que cumplen la condición de mes y de año y sus valores son los numeros aleatorios correspondientes, a continuación, se rellena el diccionario con los dias que falten y se les asignan como valor un cero y finalmente hace la comparación de los dias, esto hace que el valor de el primer dia que cumpla la condición su incremento/ decremento sea igual a su número aleatorio.
**NOTA: las claves en los diccionarios en este caso son los dias en tipo int **

Recibe una lista de *namedtuple* Periodista y devuelve una lista de tupla fecha (*datetime.datetime*), incremento(*float*).
####### 7.3.6.1 comparador_random_number_v2:
En esta versión del comparador, hace la comparación solo y exclusivamente con los números aleatorios de los días que cumplen la condicíon de mes y de año( si solo cumple la función los dias 2,5,6,9 se hace la comparación con esos números, además el primer día disponible , se compara con el último 9)  después rellena los dias que faltan y le pone como valor un cero.

**NOTA: las claves en los diccionarios en este caso son los días en tipo *datetime.datetime * **

Recibe una lista de *namedtuple* Periodista y devuelve una lista de tupla fecha(*datetime.datetime*), incremento (*float*)
####### 7.3.6.2 comparador_random_number_v3:
Esta versíon del compardor, sigue una estructura muy parecida a la  versión 1 del comparador, es decir:
1º Coge las fechas  y su valor aleatorio correspondiente, que cumplan la condición de mes y año.
2º rellena las fechas que faltan y les asigan un valor de 0.0.
3º Hacer la comparación con das las fechas a partir del dia 2.
4º Lo pasa a lista de tuplas ordenadas según la fecha y la devuelve.
Todo esto con la diferencia que en todo momento se utilizan las fechas de tipo *datetime.datetime* y se hace uso de la expresíon timedelta para averiguar la fecha anterior. 
Respecto a la versión 1 del comparador, esta versión la  supera en legibilidad y funcionamiento.








