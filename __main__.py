from collections import defaultdict
import json
from statistics import mean

import pandas as pd

FIRST_YEAR = 1950


def elo(rating1, rating2, vs1, vs2, K=200):
    if vs1 < 0 or vs2 < 0 or vs1 + vs2 <= 0:
        return 0
    expected = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    score = round(vs1 / (vs1 + vs2), 2)
    if 0 <= score < 0.25:
        point = 0
    elif 0.25 <= score <= 0.40:
        point = 0.3
    elif 0.40 < score < 0.60:
        point = 0.5
    elif 0.60 <= score <= 0.75:
        point = 0.7
    elif 0.75 < score <= 1:
        point = 1
    else:
        return 0
    return round(K * (point - expected))


if __name__ == "__main__":
    firstYear = json.load(open("firstYear.json"))
    driverPoints = json.load(open("driverPoints.json"))

    df = pd.DataFrame(firstYear.items(), columns=['DRIVER', 'FIRST YEAR'])

    year = FIRST_YEAR
    for year, seasonTable in pd.read_csv("qualifying_battles.csv").groupby("YEAR"):
        helperDict = defaultdict(list)
        for row in seasonTable.itertuples():
            rating1 = driverPoints[row.DRIVER1]
            rating2 = driverPoints[row.DRIVER2]
            gain = elo(rating1, rating2, row.VS1, row.VS2)
            helperDict[row.DRIVER1].append(gain)
            helperDict[row.DRIVER2].append(-gain)

        for driver, gainList in helperDict.items():
            driverPoints[driver] += round(mean(gainList))

        df[year] = [
            (point if year >= firstYear[driver] else 0)
            for driver, point in driverPoints.items()
        ]

    df["POINTS"] = df[year]
    df = df.sort_values("POINTS", ascending=False)
    df["MAX"] = df.iloc[:, 4:].max(axis=1)
    df = df[["DRIVER", "POINTS", "FIRST YEAR", "MAX", *range(year, FIRST_YEAR - 1, -1)]]

    df.to_excel(f'elo{year}.xlsx', sheet_name='POINTS', columns=df.columns, index=False)
