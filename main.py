import arrow
import requests
import json
import traceback

def descarga_archivos():
    try:
        # URL de autenticación y reportes
        url_token = "https://back.cafam.org.ar/api/auth/login"
        url_reportes = "https://back.cafam.org.ar/api/reportes"

        # Credenciales de usuario
        payload = json.dumps({
            "usuario": "corven motors",
            "password": "corven2023"
        })
        headers_token = {
            'content-type': 'application/json'
        }

        # Obtener token de autenticación
        response = requests.request("POST", url_token, headers=headers_token, data=payload)
        res_json = json.loads(response.text)
        token = res_json['token']

        # Cabeceras con token
        headers = {
            'content-type': 'application/json',
            'x-token': token
        }

        # Variables para iterar sobre reportes
        hoy = arrow.now().format('YYYY-MM-DD')
        lista_reportes = [
            ('Diario', '2024-11-01', 'diario', '2024-11-01', hoy, 'marca', '', 'Editar Fecha Header'),
            ('Mensual', '2024-11-01', 'periodo', '2024-01-01', hoy, 'RegistroNombre', 'modelo', ''),
            ('Anio_Anterior', '2023-11-01', 'periodo', '2023-01-01', '2023-12-31', 'RegistroNombre', 'modelo', '')
        ]

        # Función para imprimir claves de JSON
        def print_keys(data, prefix=""):
            if isinstance(data, dict):
                for key in data.keys():
                    print(f"{prefix}{key}")
                    print_keys(data[key], prefix=prefix + "  ")
            elif isinstance(data, list):
                if data and isinstance(data[0], dict):  # Si es una lista de objetos, procesamos el primero
                    print_keys(data[0], prefix=prefix + "  ")

        # Iterar sobre cada reporte
        for reporte in lista_reportes:
            payload_reporte = json.dumps({
                "format": "cantidad",
                "formatBy": reporte[2],
                "selectedFilters": {
                    "dateFrom": reporte[3],
                    "dateTo": reporte[4],
                    "zones": [],
                    "provinces": [],
                    "cities": [],
                    "brands": [],
                    "types": [],
                    "categories": [],
                    "origins": [],
                    "ccFrom": 0,
                    "ccTo": 10000,
                    "models": []
                },
                "groupBy1": reporte[5],
                "groupBy2": reporte[6]
            })

            # Solicitar datos del reporte
            response = requests.request("POST", url_reportes, headers=headers, data=payload_reporte)
            res_json = json.loads(response.text)

            print(f"\nClaves del JSON devuelto para el reporte {reporte[0]}:")
            print_keys(res_json)

        return "Claves obtenidas correctamente para todos los reportes."

    except Exception as e:
        # Manejo de errores
        with open("Log Errores.txt", "a+") as file:
            file.write(f"{arrow.now()} {str(traceback.format_exc())}\n")
        return str(traceback.format_exc())

descarga_archivos()
