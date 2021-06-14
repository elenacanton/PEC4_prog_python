#!/usr/bin/env python
import pandas as pd
from matplotlib import pyplot as plt


from exercises.ex1 import count_times_word
from exercises.ex2 import filter_polls_data
from exercises.ex3 import totals_results_by_party, create_plot

###BORRAR: RECOMENDACION USAR PRINTS AQUI EN EL MAIN EN CADA FUNCION PARA ENSEÑAR RESULTADOS
## LOGGING EN LOS MODULOS
from src.exercises.ex4 import (
    count_total_participation,
    count_concerned_economy,
    create_plot_concerns_economy,
    count_concerned_infected,
    create_plot_concerns_infected,
    get_min_grade
)


def main():
    # ejercicio 1
    print("Ejercicio 1")
    covid_approvals_path = "../data/covid_approval_polls.csv"
    huffington_search_word = "Huffington Post"
    times_huffington_post = count_times_word(
        covid_approvals_path, huffington_search_word
    )
    print(times_huffington_post)

    urls_pdf_files = ".pdf"
    times_url_pdf_file = count_times_word(covid_approvals_path, urls_pdf_files)
    print(times_url_pdf_file)

    # ejercicio 2
    """Leer los archivos facilitados de la forma más eficiente teniendo en cuenta las tareas pedidas a continuación
    y en el ejercicio 3, 4 y 5. Justificar vuestra decisión.
    Preparad los datos para cada .csv, obteniendo dos tablas que llamaremos approval_polls
    (proveniente de covid_approval_polls.csv) y concern_polls (proveniente de covid_concern_polls.csv) de
    forma que se cumplan todos los siguientes requisitos:

    Sólo estaremos interesados en las entrevistas en las cuales su agente entrevistador (pollster) esté
    en la tabla pollster_ratings.xlsx
    Sólo estaremos interesados en las entrevistas sin tracking.
    Sólo estaremos interesados en las entrevistas en las cuales su agente entrevistador no ha estado vetado (banned)."""
    approvals_df = pd.read_csv(covid_approvals_path)
    concerns_path = "../data/covid_concern_polls.csv"
    concerns_df = pd.read_csv(concerns_path)
    pollster_path = "../data/pollster_ratings.xlsx"
    pollster_df = pd.read_excel(pollster_path, engine="openpyxl")

    approvals_modified, concerns_modified = filter_polls_data(
        approvals_df, concerns_df, pollster_df
    )

    # ejercicio 3
    """Sobre los datos extraídos en el ejercicio 2 de la tabla approval_polls, calculad y representad gráficamente:

    3.1 El número de personas que aprueban (approve) y el número de personas que desaprueban (disapprove), para las 
    preguntas que contienen las palabras Trump y coronavirus en el texto. Representaremos estos datos por cada partido 
    (party) (D (demócratas), R (republicanos), I (independientes), all (personas sin clasificar por partido)).
    """
    total_results = totals_results_by_party(approvals_modified)
    create_plot(total_results)
    print(total_results)
    plt.show()

    # ejercicio 4
    """Sobre los datos extraídos en el ejercicio 2 de la tabla concern_polls, teniendo en cuenta las siguientes 
    transformaciones sobre el grado en la clasificación (grade) *, calculad y represen- tad gráficamente (excepto el 4.1):
    4.1 Cuánta gente ha participado en las entrevistas. Representar el resultado por pantalla debidamente formatado.
    4.2 Cuánta gente en la materia (subject) de la entrevista relacionada con la economia (econ- omy) está very 
    (concern, preocupación) y cuánta está not_at_all (concern, preocupación).
    4.3 Cuál es el porcentaje de gente en la matèria (subject) de la entrevista relacionada con la infección 
    (infected) está very (concern, preocupación) y cuánta está not_at_all (concern, preocu- pación).
    4.4 Cuántas entrevistas hay por cada nota clasificatoria (grade)."""
    # 4.1

    print(count_total_participation(concerns_modified))

    # 4.2
    print(count_concerned_economy(concerns_modified))
    total_results_economy = count_concerned_economy(concerns_modified)
    create_plot_concerns_economy(total_results_economy)
    plt.show()

    # 4.3
    print(count_concerned_infected(concerns_modified))
    total_results_infected = count_concerned_infected(concerns_modified)
    create_plot_concerns_infected(total_results_infected)
    plt.show()

    # 4.4
    pollster_path = "../data/pollster_ratings.xlsx"
    pollster_data = pd.read_excel(pollster_path, engine="openpyxl")

    lowest_grade = []
    for elem in pollster_data["538 Grade"]:
        result = get_min_grade(elem)
        lowest_grade.append(result)

    pollster_data["lowest_grade"] = lowest_grade
    # print(pollster_data['lowest_grade'])



if __name__ == "__main__":
    main()
