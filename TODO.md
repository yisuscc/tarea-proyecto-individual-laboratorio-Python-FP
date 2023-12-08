1. **HECHO**Función que devuelva los N (que se pasa por parámetro a la función) claves con más/menos número de elementos para una clave en concreto, tras agruparlos por una propiedad y contar cuántos elementos hay de esa propiedad (clave). Ejemplo: genero_mas_presente proyecto videojuegos, pero en vez de máximo, se cogen los N elementos.

2. **Hecho** Función que agrupe los registros a partir de la fecha en un diccionario, donde la clave sea el año y el valor sea una lista de 12 elementos, con los mayores valores de una propiedad en cada mes.

3. **HECHO**Función que devuelva un diccionario cuya clave sea PAR/IMPAR dependiendo de si el día de una propiedad de tipo fecha es par/impar y el valor sea los N mayores elementos de esa categoría según una propiedad diferente y numérica.

4. **HECHO**Función que devuelva un diccionario en el que los valores son un tanto por ciento. Ejemplo: dicc_porcentaje_ventasJP_por_año del proyecto videojuegos.

5. **No FUnciona**Función que devuelva una lista de tuplas (fecha, incremento/decremento) (datetime.datetime, float) utilizando un diccionario en el que, dado una lista de tuplas de vuestro dataset, un mes y un año, las claves son los días del mes y los valores son los incrementos/decrementos repecto al día anterior (del que se dispongan datos). Si para una fecha no hay datos, devolverá (fecha, 0).