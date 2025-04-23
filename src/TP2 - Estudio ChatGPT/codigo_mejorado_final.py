
import readline
import openai


openai.api_key = "TU_API_KEY_AQUI"

if not openai.api_key:
    raise ValueError("API Key no configurada. Por favor, proporciona tu API key.")

def invocar_chatgpt(prompt):
    """
    Llama a la API real de OpenAI para obtener una respuesta a la consulta.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except openai.error.OpenAIError as e:
        return f"Error de OpenAI: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

def procesar_entrada():
    """
    Obtiene la entrada del usuario, la valida y la limpia.
    """
    entrada = input(">>> ").strip()
    if not entrada:
        print("La consulta no puede estar vacía.")
        return None
    return entrada

def imprimir_respuesta(entrada):
    """
    Imprime la respuesta de ChatGPT, llamando a la API.
    """
    print(f"You: {entrada}")
    respuesta = invocar_chatgpt(entrada)
    print(f"chatGPT: {respuesta}")

def main():
    """
    Función principal que coordina la interacción con el usuario.
    """
    print("Consulta a ChatGPT (usa ↑ para recuperar la última consulta, 'salir' para terminar)")
    ultima_consulta = ""

    while True:
        entrada = procesar_entrada()
        if entrada is None:
            continue
        if entrada.lower() == "salir":
            break

        if entrada != ultima_consulta:
            readline.add_history(entrada)
        
        ultima_consulta = entrada
        imprimir_respuesta(entrada)

if __name__ == "__main__":
    main()
