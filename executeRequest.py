from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar El cliente con la ApiKey
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

# Función para generar una receta basada en una lista de ingredientes
def generar_receta(ingredientes):
    # Preparamos el prompt para enviar a GPT
    prompt = (
        "Teniendo en cuenta los siguientes ingredientes: "
        f"{', '.join(ingredientes)}, sugiéreme una receta. "
        "No es necesario usar todos los ingredientes, pero puedes incluir especias básicas, azúcar, sal, aceite, harina u otros ingredientes comunes. "
        "Proporciona la receta con las cantidades necesarias por persona, y asegúrate de que los ingredientes y los pasos no se repitan. "
        "Por favor, limita la respuesta a una receta clara y concisa, sin repeticiones innecesarias."
        "Al final, agrega un consejo extra para mejorar la preparación, presentación o el sabor del platillo."
    )


    # Llamada a la API de OpenAI
    try:
        print("Llamando a API...")
        response = client.chat.completions.create(
            model="chatgpt-4o-latest",  # Ver modelos -> https://openai.com/api/pricing/
            messages=[
                {
                "role": "user",
                "content": prompt,
            },
            ],
            max_tokens=500,  # Ajusta según la cantidad de respuesta que esperes
            temperature=0.7
        )
        #si no ha saltado ningun error:
        print("Respuesta exitosa de la API")
        return response

    except Exception as e:
        print(f"Error en la llamada a la API: {str(e)}")
        return None
    
    return response

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ingredientes que tienes disponibles
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
    
    # Generar la receta
    response = generar_receta(ingredientes)
    
    ########################### Salida por Terminal: ###############################
    print('///////////////////////////////////////////////////////////////////\n')
    
    print("USAGE DATA:")
    print(dict(response).get('usage'))
    
    print('\n///////////////////////////////////////////////////////////////////\n')
    
    print("OBJETO RESPONSE EN FORMATO JSON")
    print(response.model_dump_json(indent=2))
    
    print('\n///////////////////////////////////////////////////////////////////\n')
    
    print("TEXTO GENERADO:")
    print(response.choices[0].message.content)

    print('\n///////////////////////////////////////////////////////////////////')