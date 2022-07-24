import json
from bs4 import BeautifulSoup


FILEPATH_IN = [
    "Résultats 20km - Trophée intermarché - 1.html",
    "Résultats 20km - Trophée intermarché - 2.html",
    "Résultats 20km - Trophée intermarché - 3.html",
    "Résultats 20km - Trophée intermarché - 4.html",
]

FILEPATH_OUT = "./data.json"


def open_and_parse(filepath):
    with open(filepath, "r") as f:
        print("Reading the file %s..." % filepath)
        html = f.read()
    print("Parsing HTML...")
    soup = BeautifulSoup(html, "html.parser")
    print("Ok!")

    return soup


def parse_results(soup):
    tbody = soup.find(class_="tableResultats").find("tbody")

    results = []
    for tr in tbody.find_all("tr"):
        tds = [td for td in tr.find_all("td")]

        place_overall, _dossard, name_gender_cat, place_cat, _team, times, _delay, nat, _details = tds
        name, gender, cat = name_gender_cat.find_all("span")

        time_raw, _time_net = times.get_text().split(" ")
        time_raw = time_raw.split(":")
        time_raw = 3600*int(time_raw[0]) + 60*int(time_raw[1]) + int(time_raw[2])

        name = name.get_text()
        gender = gender.get_text()

        place_overall = int(place_overall.get_text())

        results.append({
            "name": name,
            "gender": gender,
            "time_raw": time_raw,
            "place_overall": place_overall,
            # TODO others
        })

    return results


def main():

    data = []
    for f in FILEPATH_IN:
        soup = open_and_parse(f)
        r = parse_results(soup)
        data.extend(r)

    # Save to json

    with open(FILEPATH_OUT, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
