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
        "Qué puedo hacer con: "
        f"{', '.join(ingredientes)}"
    )


    # Llamada a la API de OpenAI
    try:
        print("Llamando a API...")
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal:recetas:AKk7Noeo",  # Ver modelos -> https://openai.com/api/pricing/
            messages=[
                {
                "role": "user",
                "content": prompt,
            },
            ],
            #max_tokens=600,  # Ajusta según la cantidad de respuesta que esperes
            temperature=0.5
        )
        #si no ha saltado ningun error:
        print("Respuesta exitosa de la API")
        return response

    except Exception as e:
        print(f"Error en la llamada a la API: {str(e)}")
        return None


def generar_imagen(infoReceta):

    # Llamada a la API de OpenAI para generar la imagen
    try:
        # Llamada a la API de OpenAI para generar imagen con DALL·E
        prompt_imagen = f"Generate a detailed image of the following dish: {infoReceta}"
        print("Llamando a API para generar imagen...")
        imagen_response = client.images.generate(
            prompt=prompt_imagen,
            n=1,
            size="1024x1024"
        )
        
        return imagen_response

    except Exception as e:
        print(f"Error en la llamada a la API: {str(e)}")
        return None

# Ejemplo de uso
if __name__ == "__main__":

    ############################# TEXTO RECETA ###################################

    
    # Lista de ingredientes que tienes disponibles
    ingredientes = [
    "Aceite de Girasol Koipesol 1L",
    "Sal Gorda Hacendado 1kg",
    "Azúcar Blanco Hacendado 1kg",
    "Pimienta Blanca Molida Hacendado 50g",
    "Ajo Seco Hacendado 300g",
    "Cebolla Roja 1kg",
    "Calabaza Troceada Hacendado 500g",
    "Brócoli Fresco 500g",
    "Pimiento Amarillo 500g",
    "Pepino Nacional 1kg",
    "Tomate Cherry Hacendado 250g",
    "Tomate Frito Hacendado 400g",
    "Lechuga Romana 1 unidad",
    "Rúcula Fresca Hacendado 100g",
    "Cilantro Fresco Hacendado 25g",
    "Champiñones Enteros Hacendado 400g",
    "Garbanzos Secos Hacendado 500g",
    "Judías Blancas Cocidas Hacendado 400g",
    "Cuscús Hacendado 500g",
    "Pasta Farfalle Gallo 500g",
    "Fideos Finos Nº1 Hacendado 500g",
    "Harina Integral Hacendado 1kg",
    "Leche Semidesnatada Hacendado 1L",
    "Nata para Montar Hacendado 200ml",
    "Queso Manchego Curado Hacendado 150g",
    "Queso Cheddar Lonchas Hacendado 200g",
    "Queso Azul Hacendado 100g",
    "Muslos de Pollo Hacendado 1kg",
    "Solomillo de Cerdo Hacendado 500g",
    "Sardinas en Aceite de Oliva Hacendado Pack 3x85g"
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
    

    ############################# IMAGEN RECETA ###################################
    '''
    imagen_response = generar_imagen('Pasta con salsa de cebolla caramelizada y setas')
    print("imagen_url: ", imagen_response.data[0].url)
    print("respuesta completa: ", imagen_response.__dict__)
    '''