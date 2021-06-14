import logging
import re
from typing import Tuple

import pandas as pd
from matplotlib import pyplot as plt

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)

# Ejercicio 4.1
"""4.1 Cuánta gente ha participado en las entrevistas. Representar el resultado por pantalla debidamente formatado."""


def count_total_participation(concerns: pd.DataFrame) -> int:
    """Returns number of persons that particpated in the interviews

    :type concerns: Dataframe
    :param concerns: Dataframe in which we'll do the calculation
    :return: total number of participants
    """
    concerns.loc[:, "number_participants"] = (
        (concerns["sample_size"] * concerns["very"])
        + (concerns["sample_size"] * concerns["somewhat"])
        + (concerns["sample_size"] * concerns["not_very"])
        + (concerns["sample_size"] * concerns["not_at_all"])
    ) / 100

    # logger.info(f"Number of rows: {concerns.shape[0]}")
    total_participants = concerns["number_participants"].sum()
    total_participants = print(
        f"The total number of participants is: {total_participants}"
    )
    return f" The total number of partipants is {total_participants}"


# Ejercicio 4.2


def count_concerned_economy(
    concerns: pd.DataFrame,
) -> Tuple[pd.DataFrame]:  # -> Tuple[int, int]:
    """ "Returns number of persons concerned very and not at all about economy

    :type concerns: Dataframe
    :param concerns: Dataframe in which we'll do the calculation
    :return: total number of participants concerned
    """

    df_concerns_economy = concerns.loc[concerns["subject"] == "concern-economy"]
    # df_concerns_economy["very_concerned"] = (df_concerns_economy["sample_size"] * df_concerns_economy["very"]) / 100
    df_concerns_economy.loc[:, "very_concerned"] = (
        df_concerns_economy["sample_size"] * df_concerns_economy["very"]
    ) / 100
    total_very_concerned_economy = df_concerns_economy["very_concerned"].sum()

    df_concerns_economy.loc[:, "no_at_all_concerned"] = (
        df_concerns_economy["sample_size"] * df_concerns_economy["not_at_all"]
    ) / 100
    total_notatall_concerned_economy = df_concerns_economy["no_at_all_concerned"].sum()
    total_results_economy = df_concerns_economy.groupby("subject").agg(
        {"very_concerned": "sum", "no_at_all_concerned": "sum"}
    )
    # return total_very_concerned_economy, total_notatall_concerned_economy
    return total_results_economy


def create_plot_concerns_economy(results):
    results.plot.bar(title="Very and not at all concerned economy")
    plt.ticklabel_format(style="plain", axis="y")


# Ejercicio 4.3
"""4.3 Cuál es el porcentaje de gente en la matèria (subject) de la entrevista relacionada con la 
infección (infected) está very (concern, preocupación) y cuánta está not_at_all (concern, preocu- pación)."""


def count_concerned_infected(
    concerns: pd.DataFrame,
) -> Tuple[int, int]:  #  -> Tuple[pd.DataFrame]
    """ "Returns number of persons concerned very and not at all about economy

    :rtype: object
    :type concerns: Dataframe
    :param concerns: Dataframe in which we'll do the calculation
    :return: total number of participants concerned
    """
    concerns.loc[:, "number_participants"] = (
        (concerns["sample_size"] * concerns["very"])
        + (concerns["sample_size"] * concerns["somewhat"])
        + (concerns["sample_size"] * concerns["not_very"])
        + (concerns["sample_size"] * concerns["not_at_all"])
    ) / 100
    total_participants = concerns["number_participants"].sum()
    df_concerns_infected = concerns.loc[concerns["subject"] == "concern-infected"]
    df_concerns_infected.loc[:, "very_concerned"] = (
        df_concerns_infected["sample_size"] * df_concerns_infected["very"]
    ) / 100
    perc_very_concerned_infected = round(
        (df_concerns_infected["very_concerned"].sum()) / total_participants * 100, 2
    )

    # df_concerns_infected["no_at_all_concerned"] = (df_concerns_infected["sample_size"] * df_concerns_infected[
    #    "not_at_all"]) / 100
    df_concerns_infected.loc[:, "no_at_all_concerned"] = (
        df_concerns_infected["sample_size"] * df_concerns_infected["not_at_all"]
    ) / 100
    perc_notatall_concerned_infected = round(
        (df_concerns_infected["no_at_all_concerned"].sum()) / total_participants * 100,
        2,
    )
    # total_results_infected = df_concerns_infected.groupby("subject").agg(
    #     {"very_concerned": "sum", "no_at_all_concerned": "sum"}
    # )
    # return total_very_concerned_economy, total_notatall_concerned_economy
    return f"The total percentage of participants very concerned and not at all concerned about economy is: {perc_very_concerned_infected}, {perc_notatall_concerned_infected}"


def create_plot_concerns_infected(results):
    results.plot.bar(title="Very and not at all concerned infected")
    plt.ticklabel_format(style="plain", axis="y")


# Ejercicio 4.4
def get_min_grade(grade: str):
    """Returns lowest grade from a formated grade

    Valide formats for grade are:
    - "A"
    - "A+"
    - "A-"
    - "A/B"


    :param grade:
    :return:
    """
    grade_modifiers_re = r"\+|-"
    r = re.compile(grade_modifiers_re, re.IGNORECASE)
    grade = r.sub("", grade)
    return max(grade.split("/"))


# data_polls =pd.read_excel('../../data/pollster_ratings.xlsx', engine='openpyxl')
#
# for elem in data_polls['538 Grade']:
#     print(get_min_grade(elem))


# def get_min_grade(polls_df: pd.DataFrame):
#     """Returns lowest grade from a formated grade
#
#     Valide formats for grade are:
#     - "A"
#     - "A+"
#     - "A-"
#     - "A/B"
#
#
#     :param grade:
#     :return:
#     """
#     # grade_modifiers_re = r"\+|-"
#     # r = re.compile(grade_modifiers_re, re.IGNORECASE)
#     # grade = r.sub("", grade)
#     # replace_values = {'+': '', '-': ''}
#     # Replace values
#     polls_df['grade_modified'] = polls_df['538 Grade'].str.replace(r"\+|-", '')
#     polls_df["grade_modified"] = polls_df["grade_modified"].str.split("/", expand=True)
#     print(polls_df)
#     #polls_df["grade_modified"] = max(grade.split("/"))
#     return polls_df


# def get_min_grade_2(df: pd.DataFrame):
#     """Returns lowest grade from a formated grade from a dataframe given column
#
#     Valide formats for grade are:
#     - "A"
#     - "A+"
#     - "A-"
#     - "A/B"
#
#
#     :param df: Dataframe to transform column '538 Grade'. First symbols are replaced; second
#         the data is split by "/" and we only keep the first character (the lowest grade)
#     :return: df
#     """
#     #data_polls =pd.read_excel('data/pollster_ratings.xlsx', engine='openpyxl')
#     df['538 Grade'] = df['538 Grade'].str.replace(r"\+|-", '')
#     #df["538 Grade"] = pd.DataFrame(df["538 Grade"].str.split("/", expand=True).tolist(), columns = ['higuest_grade', 'lowest_grade'])
#     df["lowest_grade"] = df["538 Grade"].str.split("/")
#     return df
#
# data_polls =pd.read_excel('../../data/pollster_ratings.xlsx', engine='openpyxl')
# get_min_grade_2(data_polls)
# print(data_polls['lowest_grade'])
# #print(data_polls['538 Grade'])
