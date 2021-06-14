import logging
from typing import Tuple

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)

# Ejercicio 3
"""Sobre los datos extraídos en el ejercicio 2 de la tabla approval_polls,
calculad y representad gráficamente:
3.1 El número de personas que aprueban (approve) y el número de personas que desaprueban
(disapprove), para las preguntas que contienen las palabras Trump y coronavirus en el texto.
Representaremos estos datos por cada partido (party) (D (demócratas), R (republicanos), I (independientes),
all (personas sin clasificar por partido)).
"""


def totals_results_by_party(
    approvals: pd.DataFrame,
) -> Tuple[pd.DataFrame]:

    # Column people approves & dissaproves in approval_polls dataframe:
    approvals.loc[:, "people_approve"] = (
        approvals["sample_size"] * approvals["approve"]
    ) / 100
    approvals["sample_size"] = approvals["sample_size"].fillna(0)  # Relleno los na
    approvals["people_approve"] = (approvals["people_approve"].fillna(0)).astype(
        np.int64
    )  # Relleno los na
    # df_1_approvals['people_approve'] = df_1_approvals['people_approve'].astype(np.int64)  # Convierto a integer

    approvals.loc[:, "people_disapprove"] = (approvals["sample_size"] * approvals["disapprove"]) / 100
    approvals.loc[:, "people_disapprove"] = (
        approvals["people_disapprove"].fillna(0).astype(np.int64)
    )  # Relleno los na

    # Create column searchfor, to confirm if the values we search are present
    searchfor = ["Trump", "Coronavirus"]
    approvals["TrueFalse"] = approvals["text"].apply(
        lambda x: 1 if any(i in x for i in searchfor) else 0
    )
    total_results = approvals.groupby("party").agg(
        {"people_approve": "sum", "people_disapprove": "sum"}
    )

    return total_results

def create_plot(results):
    results.plot.bar(title="Approvals and dispprovals by party") #, stacked=True
    plt.ticklabel_format(style='plain', axis='y')
