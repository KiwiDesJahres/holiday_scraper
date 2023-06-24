# Holiday Scraper

Dieses kleine Scraping Tool liefert die gesetzlichen Feiertage in Deutschland als JSON-Ausgabe.

## Installation

```bash
sudo apt update -y
sudo apt install -y python3 python3-pip
pip3 install pipenv
```

```bash
git clone git@github.com:KiwiDesJahres/holiday_scraper.git
cd holiday_scraper
pipenv install
pipenv shell
python3 main.py
less results.json
```

## Einstellungen

In `main.py` können die gewünschten Bundesländer und Jahre eingetragen werden. Es muss sich exakt an folgende Schreibweise der Bundesländer gehalten werden:

```python
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
```
## Beispiel-Ausgabe

```JSON
[
	{
		"state": "baden-wuerttemberg",
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
				"2023-10-03",
				"2023-11-01",
				"2023-12-25",
				"2023-12-26"
			],
			"2024": [
				"2024-01-01",
				"2024-01-06",
				"2024-03-29",
				"2024-04-01",
				"2024-05-01",
				"2024-05-09",
				"2024-05-20",
				"2024-05-30",
				"2024-10-03",
				"2024-11-01",
				"2024-12-25",
				"2024-12-26"
			]
		}
	},
	{
		"state": "saarland",
		"holidays": {
			"2023": [
				"2023-01-01",
				"2023-04-07",
				"2023-04-10",
				"2023-05-01",
				"2023-05-18",
				"2023-05-29",
				"2023-06-08",
				"2023-08-15",
				"2023-10-03",
				"2023-11-01",
				"2023-12-25",
				"2023-12-26"
			],
			"2024": [
				"2024-01-01",
				"2024-03-29",
				"2024-04-01",
				"2024-05-01",
				"2024-05-09",
				"2024-05-20",
				"2024-05-30",
				"2024-08-15",
				"2024-10-03",
				"2024-11-01",
				"2024-12-25",
				"2024-12-26"
			]
		}
	}
]
```
