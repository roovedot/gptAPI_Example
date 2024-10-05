import openai
import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar la clave de API desde el archivo .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Lista de ingredientes aleatoria
ingredientes = [
    "pollo", 
    "tomates", 
    "ajo", 
    "cebolla", 
    "aceite de oliva", 
    "pimienta", 
    "sal", 
    "papas"
]

# Crear el prompt que le pedimos al modelo
prompt = f"Dame una receta usando los siguientes ingredientes: {', '.join(ingredientes)}. Por favor, incluye el nombre de la receta, las cantidades de los ingredientes y los pasos detallados para la preparación."

# Hacer una solicitud a la API de OpenAI
response = openai.ChatCompletion.create(
    model="gpt-4",  # O usa "gpt-3.5-turbo" si prefieres un modelo más económico
    messages=[
        {"role": "system", "content": "Eres un experto chef que ayuda a crear recetas."},
        {"role": "user", "content": prompt}
    ]
)
'''
# Guardar el objeto completo 'response' en un archivo JSON
with open("response.json", "w") as json_file:
    json.dump(response, json_file, indent=4)
'''
# Acceder al contenido del mensaje generado
response_content = response['choices'][0]['message']['content']

# Imprimir la receta generada
print("Receta generada:\n", response_content)

# Imprimir la información sobre el uso de tokens
#print("Uso de tokens:", response['usage'])
