import logging
from typing import Tuple

import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# add ch to logger
logger.addHandler(ch)


def filter_polls_data(
    approvals: pd.DataFrame, concerns: pd.DataFrame, polls: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Filters the 2 files according to the polls we are interested in.

    Based on polls data interviewers and not banned, filters approvals and concerns.
    Interviewer means that the interviewer in approvals and concerns exists in polls dataframe.
    Not banned means that the interviewer has not been marked as "Banned by 538".

    :param approvals: Approvals from interviews about Donald Trump's behaviour during the pandemic
    :param concerns: Concerns from interviews about how the pandemic's impact
    :param polls: Information about credibility of interviewers
    :return: approvals and concerns dataframe filtered
    """
    logger.info(f"Number of row interviewers polls: {polls.shape[0]}")
    # Create Dataframe filtering out banned interviewers from polls
    polls_not_banned = polls.loc[polls["Banned by 538"] == "no"]

    logger.info(f"Number of row interviewers polls not banned: {polls_not_banned.shape[0]}")
    # Print results approvals and disapprovals before
    logger.info(f"Number of approvals before: {approvals.shape[0]}")
    logger.info(f"Number of concerns before approvals: {concerns.shape[0]}")

    # Applies filters on approvals and disapprobals based on polls: Not banned and with no tracking
    approvals_filtered = approvals.loc[
        (approvals["pollster"].isin(polls_not_banned["Pollster"]))
        & (approvals["tracking"] == False)
    ]
    concerns_filtered = concerns.loc[
        (concerns["pollster"].isin(polls_not_banned["Pollster"]))
        & (concerns["tracking"] == False)
    ]
    logger.info(f"Number of rows with common pollsters approvals: {approvals_filtered.shape[0]}")
    logger.info(f"Number of rows with common pollsters concerns: {concerns_filtered.shape[0]}")

    return approvals_filtered, concerns_filtered

