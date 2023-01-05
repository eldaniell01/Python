def message_creator(text):
   respuestas = {"computadora": "Con mi computadora puedo programar usando Python",
   "celular": "En mi celular puedo aprender usando la app de Platzi",
   "cable": "¡Hay un cable en mi bota!"}
   if text in respuestas.keys():
      return respuestas[text]
   else:
      return 'articulo no encontrado'

text = 'casd'
response = message_creator(text)
print(response)