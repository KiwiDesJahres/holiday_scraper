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
