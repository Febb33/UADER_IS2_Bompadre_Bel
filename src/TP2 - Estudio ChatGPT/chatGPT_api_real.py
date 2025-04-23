
import readline
import openai


openai.api_key = "TU_API_KEY_AQUI"

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
    except Exception as e:
        return f"Error al invocar ChatGPT: {e}"

def main():
    print("Consulta a ChatGPT (usa ↑ para recuperar la última consulta, 'salir' para terminar)")
    ultima_consulta = ""

    while True:
        try:
            
            try:
                entrada = input(">>> ").strip()
            except KeyboardInterrupt:
                print("\nInterrumpido por el usuario.")
                break

            if entrada.lower() == "salir":
                break

            if not entrada:
                print("La consulta no puede estar vacía.")
                continue

            
            ultima_consulta = entrada
            readline.add_history(ultima_consulta)

            
            consulta = f"You: {entrada}"
            print(consulta)

            
            respuesta = invocar_chatgpt(consulta)
            print(f"chatGPT: {respuesta}")

        except Exception as e:
            print(f"Error general: {e}")

if __name__ == "__main__":
    main()
