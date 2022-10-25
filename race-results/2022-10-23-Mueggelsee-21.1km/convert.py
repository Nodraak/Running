import json
from bs4 import BeautifulSoup


FILEPATH_IN = "Ergebnisse - 16. Müggelsee-Halbmarathon 2022 - davengo.html"
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
    # tbody = soup.find(id="search").find("tbody")
    # trs = tbody.find_all("tr")[1:]  # skip header

    trs = soup.find_all("tr")

    print("Parsing %d results..." % len(trs))

    results = []
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) != 10:
            continue

        place_overall, place_m, place_w, _dossard, first_name, last_name, place, cat, _team, time = tds

        if place_overall.get_text() == "Platz":
            continue

        name = first_name.get_text() + " " + last_name.get_text()
        gender = "U"
        if place_m.get_text():
            gender = "M"
        if place_w.get_text():
            gender = "W"

        place_overall = int(place_overall.get_text().strip("."))

        t_h, t_m, t_s = time.get_text().split(":")
        time_raw = int(t_h)*3600 + int(t_m)*60 + int(t_s)

        results.append({
            "name": name,
            "gender": gender,
            "time_raw": time_raw,
            "place_overall": place_overall,
            # TODO others
        })

    print("Parsed %d results!" % len(results))

    return results


def main():

    soup = open_and_parse(FILEPATH_IN)
    data = parse_results(soup)

    # Save to json

    with open(FILEPATH_OUT, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
