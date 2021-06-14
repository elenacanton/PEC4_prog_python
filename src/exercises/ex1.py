import csv

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""EJERCICIOS
Será necesario que generéis funciones que os permitan hacer los siguientes cálculos:

Del archivo covid_approval_polls.csv:
1.1 Implementad una función que cuente de forma eficiente y muestre por pantalla el número de veces que aparecen los patrones descritos (es decir, en cuántas líneas aparece) a continuación en el archivo, incluyendo un mensaje explicativo de los valores que mostráis por pantalla.
Los patrones a considerar son:

El término Huffington Post

Una url (sea http o https) con formato pdf. Por ejemplo: https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/73jqd6u5mv/econTabReport.pdf

Un ejemplo de output sería:

The pattern Huffington_Post appears X times.

The pattern url_pdf appears Y times."""

# Ejercicio 1
"""Del archivo covid_approval_polls.csv:
1.1 Implementad una función que cuente de forma eficiente y muestre por pantalla el número de veces que aparecen los patrones descritos (es decir, en cuántas líneas aparece) a continuación en el archivo, incluyendo un mensaje explicativo de los valores que mostráis por pantalla. Los patrones a considerar son:
• El término Huffington Post
•Una url (sea http o https) con formato pdf. Por ejemplo:
https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/pip document/73jqd6u5mv/econTabReport.pdf Un ejemplo de output sería:
The pattern Huffington_Post appears X times.
The pattern url_pdf appears Y times."""

# df_1_approvals = pd.read_csv('../../data/covid_approval_polls.csv')
# df_2_concerns = pd.read_csv('../../data/covid_concern_polls.csv')
# df_3_pollster = pd.read_excel('../data/pollster_ratings.xlsx', engine='openpyxl')


def count_times_word(csv_filepath: str, search_word: str) -> str:
    """Returns the number of times search words appears in path_csv

    The function loads the path_csv file as a CSV file and reads it line by line.

    :param csv_filepath: Filepath for CSV
    :param search_word: String to search in file
    :return: Number of times search_word appears in path_csv
    """
    with open(csv_filepath, "r", encoding="utf-8") as csvfile:
        # print(f"Reading '{path_csv}' csv")
        reader = csv.reader(csvfile, delimiter=";")
        ctr = 0
        rows = 0
        for record in reader:
            if search_word in record[0]:
                rows += 1
                ctr += record[0].count(search_word)
        return f"The pattern {search_word} appears {ctr} times"


#
# path_csv = '../../data/covid_approval_polls.csv'
# print(count_times_word(path_csv, 'Huffington Post'))
# print(count_times_word(path_csv, '.pdf'))


"""1.2 ¿Si tuviéramos un archivo de 1Gb lo harías igual? Si no es así, implementar la solución para este caso."""
"""Sí, lo haría igual, ya que he intentado parametrizar lo máximo posible la función, indicando el file a leer fuera del 
cuerpo de la función, y la palabra o palabras a buscar en el dataset. La función que he implementado por tanto,
debería funcionar sin importar el tamaño del archivo."""

"""1.3 ¿Si tuviéramos 100 archivos de 1Gb cómo lo harías? No hace falta implementar la solu- ción, 
sólo una pequeña descripción de cómo resolverías el problema."""
"""Para este caso sí tendría que implementar una nueva solución. Creo que en este caso encapsularía
esta función dentro de otra. La función de fuera haría un for loop para iterar sobre cada uno de los files.
La solución más sencilla, para no tener que indicar cada nombre de archivo en el que buscar, sería tener todos
esos archivos en la misma ruta, y por tanto, el parámetro de la función de fuera sería la carpeta en la que buscar
los archivos sobre los que leer."""
