import json
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone


def elexon_find_plants():
    url = "https://data.elexon.co.uk/bmrs/api/v1/reference/bmunits/all"

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())

    # NPSHYD = non-pumped-storage hydro, PS = pumped storage
    hydro_types = ["NPSHYD", "PS"]
    hydro = [u for u in data if u.get("fuelType") in hydro_types]

    unit_dict = {}

    for u in hydro:
        name = u.get("bmUnitName") or "Unknown"
        id = u.get("nationalGridBmUnit")
        unit_dict[id] = name

    return unit_dict


def fetch_output(bmu_id):
    # Physical Notis = What the plant says it is doing RN
    now = datetime.now(timezone.utc)
    fr = (now - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    to = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    url = (
        f"https://data.elexon.co.uk/bmrs/api/v1/datasets/PN"
        f"?bmUnit={bmu_id}&from={fr}&to={to}"
    )

    print(url)

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            records = data.get("data", [])
            if not records:
                return "No data"
            return records[-1].get("levelTo")
    except urllib.error.HTTPError as e:
        return f"HTTP Error {e.code}"


unit_dict = elexon_find_plants()

for bmu_id, name in unit_dict.items():
    # Now we pass the api_id (the value) to the function
    mw = fetch_output(bmu_id)
    print(f"{name:25s} | {mw} MW")
