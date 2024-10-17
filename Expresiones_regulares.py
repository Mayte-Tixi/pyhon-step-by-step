#Expresiones_regulares
import re
mensaje="Esto es un mensaje de prueba para el curso de Python."
match=re.search("curso",mensaje)
print("Inicio=",match.start(),"Final=",match.end())

#split# Devolverá una lista donde cada elemento es una palabra del mensaje.
dividir=re.split(' ',mensaje)
print(dividir)

'''sub(): permite sustituir los patrones encontrados por otra subcadena que
pasamos por parámetro.'''
mensaje = "Esto es un mensaje de prueba para el curso de Python."
re.sub('Python', 'Java', mensaje) # Devolverá 'Esto es un mensaje de prueba para el curso de Java.'
print(mensaje)

"""findall(): busca todas las apariciones de un patrón dentro de una cadena de
caracteres. Como resultado nos devolverá una lista con todas las subcadenas que
cumplen con el patrón."""
mensaje1 = "Esto es un mensaje de prueba para el curso de Python."
re.findall('de', mensaje1) # Devolverá ['de', 'de']
print(mensaje1)

'''• \n: salto de línea.
• \t: tabulador.
• \\: barra diagonal inversa.
• \d: un dígito.
• \w: un carácter alfanumérico.
• \s: un espacio en blanco.
• \D: carácter que no sea un dígito.
• \W: carácter que no sea alfanumérico.'''




texto = "Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido.\
También es una composición de caracteres imprimibles (con grafema) generados\
por un algoritmo de cifrado que, aunque no tiene sentido para cualquier persona, \
sí puede ser descifrado por su destinatario original.\
En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto."

remplazo_dondehayespacios=re.sub("\s","5",texto)#dentro de la cadena de texto donde hay espacios en blanco remplaza por con 5 
print(remplazo_dondehayespacios)
patron="se\w+"#buscar dentro del texto las palbras que inicien con se 
a=re.findall(patron,texto)
print(a)

patron1="de\w+\s\w+"
e=re.findall(patron1,texto)
print(e)


''' Metacaracteres: los metacaracteres son caracteres que tienen un significado
especial dentro de las expresiones regulares. Estos metacaracteres permiten
buscar repeticiones de patrones, tipos de caracteres, etc. A continuación,
describiremos algunos de los metacaracteres más comunes:
'''
patron2="es|ser"
i=re.sub(patron2,'es',texto)
print(i)

'''?: el elemento que le precede aparece una vez o ninguna. Imaginemos, en el
siguiente ejemplo, que buscamos cualquier número que tenga un dígito o
ninguno seguido de un espacio:'''
ejemplo = '1 22 333 4444'
pattern = '\d?\s'
n=re.findall(pattern, ejemplo) # Devolverá ['1 ', '2 ', '3 ']
print(n)

'''+: el elemento que le precede aparece una o más veces. Por ejemplo, en el
siguiente ejemplo, vamos a buscar el número donde aparezca el dígito 3 una o
más veces:'''
ejemplo = '1 22 333 4444'
pattern = '3+'
re.findall(pattern, ejemplo) # Devolverá ['333']

''''*: el elemento que le precede aparece ninguna o más veces. Por ejemplo, en el
siguiente ejemplo buscaremos qué parte contiene el dígito 1 ninguna o más
veces seguido del número 2:'''
ejemplo = '122333114444'
pattern = '(2*2)'
d=re.findall(pattern, ejemplo) # Devolverá ['12', '2']
print(d)

'''• {n}: el elemento que le precede aparece n veces. En el siguiente ejemplo
buscaremos qué parte de la cadena de caracteres tiene exactamente 3 dígitos:'''
ejemplo = '1 22 333 4444'
pattern = '\d{3}'
n=re.findall(pattern, ejemplo) # Devolverá ['333', '444']
print(n)

'''{n,m}: el elemento anterior aparece entre n y m. Si n está vacío significará que
el elemento aparece de 0 a m veces. Si, por el contrario, m es vacío significará
que el elemento aparece n o más veces. A continuación, buscaremos qué parte
de la cadena de texto tiene 2 o 3 dígitos seguidos:'''
ejemplo = '1 22 333 4444'
pattern = '\d{2,3}'
m=re.findall(pattern, ejemplo) # Devolverá ['22', '333', '444']
print(m)
'''• []: nos permite representar clases de caracteres, es decir, buscará cadenas que
tengan algunos de los caracteres definidos dentro de los corchetes. Por
ejemplo, a continuación, buscaremos qué parte de la cadena tiene los dígitos 2
o 3 repetidos entre 2 y 3 veces:'''
ejemplo = '1 22 333 4444'
pattern = '[2,3]{2,3}'
r=re.findall(pattern, ejemplo) # Devolverá ['22', '333']
print(r)

'''• -: nos permite definir un rango de caracteres. En el ejemplo siguiente,
buscaremos qué parte de la cadena tiene los valores entre 1 y 3 repetidos 2 o
más veces.'''
ejemplo = '1 22 333 4444'
pattern = '[1-4]{2,}'
g=re.findall(pattern, ejemplo) # Devolverá ['22', '333']
print(g)

