# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Crear carpeta docs si no existe
    os.makedirs("docs", exist_ok=True)

    # Cargar los datos
    df = pd.read_csv("files/input/shipping-data.csv")  # Usa tu ruta relativa si es necesario

    # 1. Gráfico de envíos por almacén
    plt.figure(figsize=(8, 6))
    df["Warehouse_block"].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # 2. Gráfico de modos de envío
    plt.figure(figsize=(8, 6))
    df["Mode_of_Shipment"].value_counts().plot(kind='bar', color='lightgreen')
    plt.title("Mode of Shipment")
    plt.xlabel("Shipment Mode")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # 3. Gráfico de calificación del cliente
    plt.figure(figsize=(8, 6))
    df["Customer_rating"].value_counts().sort_index().plot(kind='bar', color='orange')
    plt.title("Average Customer Rating")
    plt.xlabel("Customer Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # 4. Histograma del peso
    plt.figure(figsize=(8, 6))
    plt.hist(df["Weight_in_gms"], bins=30, color='salmon', edgecolor='black')
    plt.title("Weight Distribution")
    plt.xlabel("Weight (gms)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # 5. HTML del dashboard
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Shipping Dashboard</title>
    </head>
    <body>
        <h1>Shipping Dashboard</h1>
        <h2>Shipping per Warehouse</h2>
        <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">

        <h2>Mode of Shipment</h2>
        <img src="mode_of_shipment.png" alt="Mode of Shipment">

        <h2>Average Customer Rating</h2>
        <img src="average_customer_rating.png" alt="Average Customer Rating">

        <h2>Weight Distribution</h2>
        <img src="weight_distribution.png" alt="Weight Distribution">
    </body>
    </html>
    """

    with open("docs/index.html", "w") as f:
        f.write(html_content)

