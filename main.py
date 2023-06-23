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
        results.append(tds[1].text[4:])
    return results


def formatDate(date):
    day, month, year = date.split(".")
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"


def exportResults(data):
    with open("results.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


dict1 = {
    "state": "Baden-Württemberg",
    "holidays": {
        "2023": [
            "2023-01-01",
            "2023-01-06",
            "2023-04-07",
            "2023-04-10",
            "2023-05-01",
            "2023-05-18",
            "2023-05-29",
            "2023-06-08",
            "2023-06-09",
            "2023-10-03",
            "2023-10-31",
            "2023-11-01",
            "2023-12-25",
            "2023-12-26",
        ],
        "2024": [
            "2024-01-01",
            "2024-01-06",
            "2024-04-12",
            "2024-04-15",
            "2024-05-01",
            "2024-05-09",
            "2024-05-20",
            "2024-05-30",
            "2024-08-15",
            "2024-10-03",
            "2024-10-31",
            "2024-11-01",
            "2024-12-25",
            "2024-12-26",
        ],
        "2025": [
            "2025-01-01",
            "2025-01-06",
            "2025-04-04",
            "2025-04-07",
            "2025-05-01",
            "2025-05-29",
            "2025-06-08",
            "2025-06-09",
            "2025-10-03",
            "2025-10-31",
            "2025-11-01",
            "2025-12-25",
            "2025-12-26",
        ],
    },
}

dict2 = {
    "state": "Berlin",
    "holidays": {
        "2023": [
            "2023-01-01",
            "2023-04-07",
            "2023-04-10",
            "2023-05-01",
            "2023-05-18",
            "2023-05-29",
            "2023-06-08",
            "2023-10-03",
            "2023-10-31",
            "2023-12-25",
            "2023-12-26",
        ],
        "2024": [
            "2024-01-01",
            "2024-04-12",
            "2024-04-15",
            "2024-04-26",
            "2024-05-01",
            "2024-05-09",
            "2024-05-20",
            "2024-05-30",
            "2024-10-03",
            "2024-10-31",
            "2024-12-25",
            "2024-12-26",
        ],
        "2025": [
            "2025-01-01",
            "2025-04-04",
            "2025-04-07",
            "2025-04-18",
            "2025-05-01",
            "2025-05-29",
            "2025-06-08",
            "2025-10-03",
            "2025-10-31",
            "2025-12-25",
            "2025-12-26",
        ],
    },
}

exportResults([dict1, dict2])
