import json
import requests
from bs4 import BeautifulSoup

YEARS = [2023, 2024, 2025]
STATES = [
    "baden-wuerttemberg",
    "bayern",
    "berlin",
    "brandenburg",
    "bremen",
    "hamburg",
    "hessen",
    "mecklenburg-vorpommern",
    "niedersachsen",
    "nordrhein-westfalen",
    "rheinland-pfalz",
    "saarland",
    "sachsen",
    "sachsen-anhalt",
    "schleswig-holstein",
    "thueringen",
]
URL = "https://www.arbeitstage.org/"


def requestHolidays(year, state):
    results = []
    url = URL + f"{state}/feiertage-{year}-{state}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find(attrs={"class": "tableJahrFeier"})
    holiday_lines = table.findAll("tr")
    holiday_lines.pop(0)
    for line in holiday_lines:
        tds = line.findAll("td")
        results.append(formatDate(tds[1].text[4:]))
    return results


def formatDate(date):
    day, month, year = date.split(".")
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"


def exportResults(data):
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def buildStateData(state):
    data, holidays_in_year = {}, {}
    data["state"] = f"{state}"
    for year in YEARS:
        holidays_in_year[f"{year}"] = requestHolidays(year, state)
    data["holidays"] = holidays_in_year
    return data


exportResults([buildStateData(state) for state in STATES])
