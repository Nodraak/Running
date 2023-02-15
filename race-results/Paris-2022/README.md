# README.md

https://resultscui.active.com/events/SchneiderElectricMarathondeParis2022

```python
import subprocess
import time

URL = "https://resultscui.active.com/api/results/events/SchneiderElectricMarathondeParis2022/participants?groupId=947610&routeId=170632&offset={offset}&limit={limit}"

LIMIT = 100
for off in range(0, 34365+1, LIMIT):
    url = URL.format(offset=off, limit=LIMIT)
    subprocess.check_call("wget '%s'" % url, shell=True)
    time.sleep(1.000)
```
