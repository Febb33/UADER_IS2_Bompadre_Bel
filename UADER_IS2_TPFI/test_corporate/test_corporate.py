
import socket
import logging
import json
import threading
import time
from singletonproxyobservertpfi import ProxyServer, configurar_logger


# ---------- CONFIGURACIÓN ----------
HOST = "localhost"
PORT = 9090   # usa un puerto diferente al 8080 por si hay otro proceso
TIMEOUT = 2   # segundos de espera entre tests
TEST_ID = "UADER-FCyT-IS2-TEST"


# ---------- FUNCIONES AUXILIARES ----------
def send_request(request):
    """Envía una solicitud JSON al servidor y devuelve la respuesta decodificada."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(request).encode("utf-8"))
        data = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
    return json.loads(data.decode("utf-8"))


# ---------- SERVIDOR EN HILO SEPARADO ----------
def start_server():
    configurar_logger(verbose=False)
    logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s") 
    server = ProxyServer(host=HOST, port=PORT)
    server.start()


# ---------- TESTS ----------
def test_set():
    # SET
    set_request = {
        "UUID": "123456",
        "ACTION": "set",
        "DATA": {
            "id": TEST_ID,
            "cp": "3260",
            "CUIT": "30-70925411-8",
            "domicilio": "25 de Mayo 385-1P",
            "idreq": "473",
            "idSeq": "1146",
            "localidad": "Concepción del Uruguay",
            "provincia": "Entre Ríos",
            "sede": "FCyT",
            "seqID": "23",
            "telefono": "03442 43-1442",
            "web": "http://www.uader.edu.ar"
        }
    }

    response_set = send_request(set_request)
    assert response_set["id"] == TEST_ID, "El registro no se guardó correctamente"
    #print("\n✅ SET response:", json.dumps(response_set, indent=4))

    get_request = {
        "ACTION": "get",
        "ID":TEST_ID
    }

    response_get = send_request(get_request)
    assert response_get["id"] == response_set["id"], "El registro no se guardó correctamente"
    #print("\n✅ GET response:", json.dumps(response_get, indent=4))

    get_log_request = {
        "ID": response_set["log_id"],
        "ACTION": "get_log"
    }

    response_get_log = send_request(get_log_request)   
    assert response_get_log["extra"] == response_set["id"], "El registro no se guardó correctamente"
    assert response_get_log["action"] == "set"
    #print("\n✅ log response:", json.dumps(response_get_log, indent=4))

    print("\n✅ SET OK")


def test_list():
    list_request = {
        "ACTION": "list"
    }

    response_list = send_request(list_request)
    assert any(item["id"] == TEST_ID for item in response_list), "El registro no aparece en LIST"

    get_log_request = {
        "ID": response_list[0]["log_id"],
        "ACTION": "get_log"
    }

    response_get_log = send_request(get_log_request)   
    assert response_get_log["extra"] == "", "El registro no se guardó correctamente"
    assert response_get_log["action"] == "list"

    print("\n✅ List OK")


def test_get():
    get_request = {
        "ACTION": "get",
        "ID": TEST_ID
    }

    response_get = send_request(get_request)
    assert response_get["id"] == TEST_ID

    get_log_request = {
        "ID": response_get["log_id"],
        "ACTION": "get_log"
    }

    response_get_log = send_request(get_log_request)   
    assert response_get_log["extra"] == TEST_ID, "El registro no se guardó correctamente"
    assert response_get_log["action"] == "get"

    print("\n✅ GET OK")
    

def test_errorget():
    get_request = {
        "ACTION": "get",
    }

    response_get = send_request(get_request)
    assert response_get["Error"] == "Falta ID para accion get"
    print("\n✅ Errorget OK")


# set, no cargar un dato
# list, darle un id que no sea correcto


def test_dobleserver():
    try:
        start_server()
    except Exception as e:
        assert e.args[0] == "Error: ya existe una instancia del servidor en el puerto."
        print("\n✅ Error dobleserver OK")


def test_errorset():
    set_request = {
        "UUID": "123456",
        "ACTION": "set",
    }

    response_set = send_request(set_request)
    assert response_set["Error"] == "Falta campo DATA"
    print("\n✅ Errorset OK")


def test_errorlist():
    # Enviamos una solicitud de LIST "normal"
    list_request = {
        "ACTION": "list"
    }

    response_list = send_request(list_request)

    # Si la respuesta es un error (dict con "Error"), verificamos que esté bien formado
    if isinstance(response_list, dict) and "Error" in response_list:
        print(f"⚠️ El servidor devolvió un error controlado: {response_list['Error']}")
        assert "Error" in response_list, "La respuesta de error no tiene campo 'Error'"
    else:
        # Si no hay error, comprobamos que haya al menos un item en la lista
        assert isinstance(response_list, list), "La respuesta LIST no es una lista"
        assert len(response_list) > 0, "La lista devuelta está vacía"
        assert "id" in response_list[0], "Los ítems no tienen campo 'id'"

    # Probamos también el get_log con un ID que no existe
    get_log_request = {
        "ID": "x-noestoy_enladb-x",
        "ACTION": "get_log"
    }
    response_get_log = send_request(get_log_request)

    # Validamos que el servidor respondió correctamente al ID inexistente
    assert "Error" in response_get_log or "id" in response_get_log, \
        "El servidor no respondió correctamente al get_log inexistente"

    print("\n✅ test_errorlist OK")


if __name__ == "__main__":
    # 1️⃣ Levantar servidor en hilo
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()
    time.sleep(TIMEOUT)
    test_set()
    test_list()
    test_get()
    test_errorget()
    test_dobleserver()
    test_errorset()
    test_errorlist()

