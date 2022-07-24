"""
* Parse the participants file, and builds a dict.
* Parse the result files and update the dict.
* Save the dict as json.

Takes ~15 sec.
"""

import json
from bs4 import BeautifulSoup


FILEPATH_PARTICIPANTS = "./data/Meldeliste 20. \"Unser Jubiläum\" Spreewaldmarathon 2022.html"
P_TITLE_21 = "21,1 km Halbmarathon-Lauf Teilnehmerlimit: 500 Sportler am 24.04.2022 um 10:30 Uhr in Burg"
P_TITLE_42 = "42,195 km Marathon-Lauf Teilnehmerlimit: 300 Sportler\nPokale für Platz 1 bis 3 in allen Altersklassen.Diese werden per Post versendet. am 24.04.2022 um 10:30 Uhr in Burg"

FILEPATH_RESULTS_21 = "./data/Auswertung Gesamt (Brutto) 20. Spreewaldmarathon - 21,1 km Halbmarathon-Lauf - portal.lausitz-timing.de.html"
FILEPATH_RESULTS_42 = "./data/Auswertung Gesamt (Brutto) 20. Spreewaldmarathon - 42,195 km Marathon-Lauf - portal.lausitz-timing.de.html"

FILEPATH_OUT_OLD = "./data-old.json"
FILEPATH_OUT_21 = "./data.json"


def open_and_parse(filepath):
    with open(filepath, "r") as f:
        print("Reading the file...")
        html = f.read()
    print("Parsing HTML...")
    soup = BeautifulSoup(html, "html.parser")
    print("Ok!")

    return soup


def birth2age(birthyear):
    assert isinstance(birthyear, int)
    return 2022-birthyear+1


def parse_participants(filepath, data):
    soup = open_and_parse(filepath)

    title = None
    for tr in soup.find("table").find_all("tr"):
        klass = tr.get("class")
        if klass is None:  # sep
            pass
        elif klass == ["zeile3"]:  # title
            title = tr.get_text()

            if title == P_TITLE_21:
                title = "21"
            elif title == P_TITLE_42:
                title = "42"
            else:
                title = None
        elif klass == ["zeile5"]:  # row (people)
            if title is None:
                continue

            tds = tr.find_all("td")
            assert len(tds) == 11
            tds = [t.get_text() for t in tds]
            (
                _discipline,
                _distance,
                lastname,
                firstname,
                gender,
                birthyear,
                _club,
                _,
                registrationdate,
                _,
                _,
            ) = tds

            row_key = "%s %s" % (firstname, lastname)
            assert row_key not in data[title], "Unexpected key '%s' found" % row_key

            age = birth2age(int(birthyear))

            data[title][row_key] = [(gender, age, registrationdate), None]

        elif klass == ["zeile6"]:  # header
            pass
        else:
            raise Exception("CSS class '%s' not handled" % klass)


def parse_results(filepath, data_key, data):
    soup = open_and_parse(filepath)

    for tr in soup.find("table").find("tbody").find_all("tr"):
        tds = tr.find_all("td")
        assert len(tds) == 11
        tds = [t.get_text() for t in tds]
        (
            _,
            place_global,
            firstname,
            lastname,
            _club,
            _nb,
            _age_group,
            place_age,
            time_raw,
            speed,
            _pace,
        ) = tds

        row_key = "%s %s" % (firstname, lastname)
        if row_key not in data[data_key]:
            print("WARN: runner '%s' not found in Meldeliste" % row_key)
            row_key = "%s %s" % (firstname, lastname)
            data[data_key][row_key] = [(None, None, None), None]

        assert row_key in data[data_key]

        if speed:
            speed = float(speed.replace(",", "."))
        else:
            speed = 0.0

        data[data_key][row_key][1] = (place_global, place_age, time_raw, speed)


def main():
    # {
    #   "firstname lastname": [
    #     (gender, age, registrationdate),
    #     (place_global, place_age, time_raw, speed),
    #   ],
    # }
    data = {
        "21": {},
        "42": {},
    }

    # Parse the participants file

    parse_participants(FILEPATH_PARTICIPANTS, data)

    # Parse the result files

    parse_results(FILEPATH_RESULTS_21, "21", data)
    parse_results(FILEPATH_RESULTS_42, "42", data)

    def conv_time(time_raw):
        time_raw = time_raw.split(":")
        time_raw = 3600*int(time_raw[0]) + 60*int(time_raw[1]) + int(time_raw[2])
        return time_raw

    data_21 = []
    for k, d in data["21"].items():
        # fix registered but not running
        if (d[1] is None) or (d[1][0] is ''):
            continue

        t = conv_time(d[1][2])

        # fix edge cases
        if (t == 15) or (t == 103):
            continue

        data_21.append({
            "name": k,
            "gender": d[0][0],
            "time_raw": t,
            "place_global": int(d[1][0]),
        })

    data_21 = sorted(data_21, key=lambda d: d["place_global"])

    # Save to json

    with open(FILEPATH_OUT_OLD, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)

    with open(FILEPATH_OUT_21, "w") as f:
        json.dump(data_21, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
