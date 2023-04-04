"""
Takes <1 sec to run.
"""

import datetime
import json
import re


FILEPATH_IN = "data/participants?groupId=988396&routeId=173931&offset={offset}&limit=100"
FILEPATH_OUT = "./data.json"
MAX = 50756


def open_and_parse(filepath):
    with open(filepath, "rb") as f:
        print("Reading the file %s..." % filepath)
        json_raw = f.read()
    print("Parsing JSON...")

    return json.loads(json_raw)


def parse_time(string):
    matches = re.findall(r"PT(\d+)H(?:(\d+)M)?(?:(\d+)S)?", string)
    assert len(matches) == 1
    assert len(matches[0]) == 3

    h, m, s = matches[0]
    if m == '': m = 0
    if s == '': s = 0

    return int(h)*3600 + int(m)*60 + int(s)


def parse_results(data):
    results = []

    for item in data["items"]:
        ident = item["id"]
        time_raw = parse_time(item["finalResult"]["chipTimeResult"])
        name = "%s %s" % (item["person"]["lastName"], item["person"]["firstName"].upper())
        gender = item["person"]["gender"]
        age = item["person"]["age"]

        results.append({
            "id": ident,
            "time_raw": time_raw,
            "name": name,
            "gender": gender,
            "age": age,
            # TODO others
        })

    return results


def main():

    data = []
    for off in range(0, MAX+1, 100):
        f = FILEPATH_IN.format(offset=off)
        data_parsed = open_and_parse(f)
        r = parse_results(data_parsed)
        data.extend(r)

    # Save to json

    with open(FILEPATH_OUT, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
