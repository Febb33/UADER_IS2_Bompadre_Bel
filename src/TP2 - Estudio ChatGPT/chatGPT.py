
import readline


def invocar_chatgpt(prompt):
    try:
        
        respuesta = f"Esta es una respuesta simulada a: {prompt}"
        return respuesta
    except Exception as e:
        print(f"Error al invocar el API: {e}")
        return "No se pudo obtener respuesta."

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

            
            try:
                consulta = f"You: {entrada}"
                print(consulta)
            except Exception as e:
                print(f"Error procesando la entrada: {e}")
                continue

            
            try:
                respuesta = invocar_chatgpt(consulta)
                print(f"chatGPT: {respuesta}")
            except Exception as e:
                print(f"Error al invocar ChatGPT: {e}")

        except Exception as e:
            print(f"Error general: {e}")

if __name__ == "__main__":
    main()
