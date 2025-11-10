import pandas as pd
import numpy as np


# cargar datos

def cargar_datos(ruta):
    """Carga el dataset de ventas en línea."""
    try:
        df = pd.read_csv("Online_Retail.csv", encoding='ISO-8859-1')
        print(" Dataset cargado correctamente.")
        print("Filas y columnas:", df.shape)
        return df
    except FileNotFoundError:
        print(" Error: no se encontró el archivo.")
        return None



#    limpiar valores nulos

def limpiar_datos(df):
    """Limpia valores nulos y duplicados del dataset."""
    df = df.copy()

    # eliminar filas con codigos nulos
    if "InvoiceNo" in df.columns:
        df = df.dropna(subset=["InvoiceNo"])

    # eliminar duplicados
    df = df.drop_duplicates()

    # rellenar valores nulos  de texto
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("Desconocido")

    # rellenar valores nulos numéricos con la mediana
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        df[col] = df[col].fillna(df[col].median())

    print(" Limpieza de valores nulos y duplicados completada.")
    return df



# corregir tipos de datos

def transformar_tipos(df):
    """Convierte columnas a tipos de datos adecuados."""
    df = df.copy()

    if "InvoiceDate" in df.columns:
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    if "CustomerID" in df.columns:
        df["CustomerID"] = df["CustomerID"].astype("Int64")

    print(" Conversión de tipos completada.")
    return df



# eliminar valores atípicos

def eliminar_outliers(df):
    """Elimina valores extremos en cantidad y precio."""
    df = df.copy()

    if "Quantity" in df.columns:
        df = df[df["Quantity"] > 0]

    if "UnitPrice" in df.columns:
        df = df[df["UnitPrice"] > 0]

    print("⚖️ Valores atípicos eliminados.")
    return df



# normalizar datos numéricos

def normalizar_datos(df):
    """Escala las variables numéricas entre 0 y 1."""
    df = df.copy()

    columnas_numericas = df.select_dtypes(include=["float64", "int64"]).columns
    df[columnas_numericas] = (df[columnas_numericas] - df[columnas_numericas].min()) / (
        df[columnas_numericas].max() - df[columnas_numericas].min()
    )

    print(" Normalización completada.")
    return df



#  función principal

def preprocesar_online_retail(ruta):
    """Ejecuta todo el flujo de preprocesamiento para el dataset Online Retail."""
    df = cargar_datos(ruta)
    if df is not None:
        df = limpiar_datos(df)
        df = transformar_tipos(df)
        df = eliminar_outliers(df)
        df = normalizar_datos(df)
        print(" Preprocesamiento finalizado correctamente.")
        print("\nVista previa de los datos procesados:\n", df.head())
        return df
    else:
        print(" No se pudo procesar el dataset.")
        return None



#   si se corre directamente

if __name__ == "__main__":
    ruta = "Online_Retail.csv"
    datos_procesados = preprocesar_online_retail(ruta)
    if datos_procesados is not None:
        datos_procesados.to_csv("Online_Retail_procesado.csv", index=False)
        print(" Archivo limpio guardado como 'Online_Retail_procesado.csv'")