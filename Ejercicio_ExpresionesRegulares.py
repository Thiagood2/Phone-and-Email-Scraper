import re
import pyperclip 

#Extrar Expresion Regular PARA TELEFONO
telefonos = re.compile(r'''
(            
((\d\d\d) | (\ (\d\d\d)))?       #Codigo de Area   
(\s|-)                           #Separacion
\d\d\d                           #3 numeros
-                                #Separacion
\d\d\d\d                         #4 numeros
)
''', re.VERBOSE)


#Extraer Expresion Regular Para MAILS
emails = re.compile(r'''
[a-zA-z0-9_.]+ #Comienzo del Correo
@              #Arroba
[a-zA-z0-9_.]+ #Codominio y dominio

''', re.VERBOSE)

#Texto de donde provinene los correos e emails
texto = pyperclip.paste()
TelefonosRegex = telefonos.findall(texto)
Lista_Emails = emails.findall(texto)
Lista_Telefonos = []    #Crear una lista para telefonos

for i in TelefonosRegex:
    Lista_Telefonos.append(i[0])


resultados = '\n'.join(Lista_Telefonos)+'\n'+'\n'.join(Lista_Emails)
pyperclip.copy(resultados)
