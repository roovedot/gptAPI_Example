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
        "No es necesario usar todos los ingredientes." 
        "Puedes incluir especias básicas, azúcar, sal, aceite, harina, cebolla o ajo, u otros ingredientes comunes. "
        "Proporciona la receta con las cantidades necesarias por persona. "
        "Explica los pasos para la elaboración de manera clara y concisa."
        "Limítate a: Título, Ingredientes, preparación y consejo extra"
        "Al final, agrega un consejo extra para mejorar la preparación, presentación o el sabor del plato."
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
            max_tokens=600,  # Ajusta según la cantidad de respuesta que esperes
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
    "Tomate Frito",
    "Leche entera Hacendado",
    "Manzanas",
    "Cebolla",
    "Carne picada Vacuno 500gr",
    "Aceite de oliva",
    "Pechga de pollo 380gr",
    "Pimiento rojo",
    "Queso Philadelphia",
    "Arroz gordo 1kg",
    "Queso Rallado Mozzarela 300gr"
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
    texto = response.choices[0].message.content
    print(texto)

    print('\n///////////////////////////////////////////////////////////////////')