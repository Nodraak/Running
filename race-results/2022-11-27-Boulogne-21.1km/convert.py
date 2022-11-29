"""
Takes ~20 sec to run.

Splits: 0.0 km, 5.3 km, 9.5 km, 15.0 km, 21.1 km
"""

import json
import re
from bs4 import BeautifulSoup


FILEPATH_IN = "data/partenaire-20190624003678-{offset:03d}-100.htm"
FILEPATH_OUT = "./data.json"


def open_and_parse(filepath):
    with open(filepath, "rb") as f:
        print("Reading the file %s..." % filepath)
        html = f.read()
    print("Parsing HTML...")
    soup = BeautifulSoup(html, "html.parser")
    print("Ok!")

    return soup


def parse_time(s):
    toks = s.split(":")
    t = 3600*int(toks[0]) + 60*int(toks[1]) + int(toks[2])
    return t


def parse_results(soup):
    tbody = soup.find(class_="afficheResultat").find("tbody")

    results = []
    for tr in tbody.find_all("tr"):
        tds = [td for td in tr.find_all("td")]

        if len(tds) == 8:
            # summary
            _, place, time, name, gender, _cat, _team, _ = tds
        elif len(tds) == 1:
            # details, corresponding to the previous row

            elem = tds[0].find_all("div")[4]
            html = str(elem)
            matches = re.findall(r"Club/Equipe : .+<br/>Place sexe : .+<br/>5.3km : (.+)<br/>9.5km : (.+)<br/>15km : (.+)</br></div>", html)

            if len(matches) == 0:
                ts = [0, 0, 0, 0, 0]
            else:
                ts = [0] + [parse_time(m) for m in matches[0]] + [results[-1]["time_raw"]]

            results[-1]["splits"] = ts

            continue
        else:
            raise Exception(len(tds))

        place = int(place.get_text())
        time_raw = parse_time(time.get_text())
        name = name.get_text()
        gender = gender.get_text()

        results.append({
            "name": name,
            "gender": gender,
            "time_raw": time_raw,
            "place_overall": place,
            # TODO others
        })

    return results


def main():

    data = []
    for off in range(0, 81+1):
        f = FILEPATH_IN.format(offset=off*100)
        soup = open_and_parse(f)
        r = parse_results(soup)
        data.extend(r)

    # Save to json

    with open(FILEPATH_OUT, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
