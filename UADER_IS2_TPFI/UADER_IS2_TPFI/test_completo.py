
import boto3
from pprint import pprint

# Inicializar conexión a DynamoDB
dynamodb = boto3.resource("dynamodb")

# Acceder a la tabla
log_table = dynamodb.Table("CorporateLog")


def mostrar_corporate_log():
    """Muestra todos los registros de la tabla CorporateLog sin límite."""
    items = []
    response = log_table.scan()
    items.extend(response.get("Items", []))

    # Paginado: seguir trayendo mientras haya más resultados
    while "LastEvaluatedKey" in response:
        response = log_table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        items.extend(response.get("Items", []))

    # Ordenar por timestamp descendente
    items.sort(key=lambda x: str(x.get("timestamp", "")), reverse=True)

    print(f"\nTotal de registros en CorporateLog: {len(items)}\n")
    for item in items:
        pprint(item)


if __name__ == "__main__":
    print("Mostrando todos los registros de CorporateLog...\n")
    mostrar_corporate_log()
    print("\nFin de la ejecución, se mostraron todos los registros disponibles.")

