# README.md

https://resultscui.active.com/api/results/events/SchneiderElectricMarathondeParis2023/participants?groupId=988396&routeId=173931&offset=0&limit=1


## Part 1

https://resultscui.active.com/events/SchneiderElectricMarathondeParis2023
https://resultscui.active.com/api/results/participants/43618855/splits

```python

# Basic results

import subprocess
import time

URL = "https://resultscui.active.com/api/results/events/SchneiderElectricMarathondeParis2023/participants?groupId=988396&routeId=173931&offset={offset}&limit={limit}"

MAX = int(subprocess.check_output("curl 'https://resultscui.active.com/api/results/events/SchneiderElectricMarathondeParis2023/participants?groupId=988396&routeId=173931&offset=0&limit=1' | jq '.meta.totalCount'", shell=True))
LIMIT = 100
print("MAX=%d" % MAX)
for off in range(0, MAX+1, LIMIT):
    print("=== file %d/%d" % (off, MAX))
    url = URL.format(offset=off, limit=LIMIT)
    subprocess.check_call("wget '%s'" % url, shell=True)
    time.sleep(1.000)

# Splits

import os
import subprocess
import time

URL = "https://resultscui.active.com/api/results/participants/{ident}/splits"

files_raw = subprocess.check_output("ls data/participants*", shell=True).decode('utf8')
files = files_raw.strip().split("\n")
for i, file in enumerate(files):
    print("=== file %d/%d" % (i, len(files)))
    idents = subprocess.check_output("jq '.items[].id' '%s'" % file, shell=True).decode('utf8')
    for ident in idents.strip().split("\n"):
        print("=== file %d/%d - ident %s" % (i, len(files), ident))
        url = URL.format(ident=ident)
        file_out = "data-splits/splits.%s" % ident
        if not os.path.isfile(file_out):
            subprocess.check_call("wget --output-document %s '%s'" % (file_out, url), shell=True)
            time.sleep(0.100)  # a bit short, but we have 50k to download...
```
