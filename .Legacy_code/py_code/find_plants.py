import json
import urllib.request

url = "https://data.elexon.co.uk/bmrs/api/v1/reference/bmunits/all"

with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())

# NPSHYD = non-pumped-storage hydro, PS = pumped storage
hydro_types = ["NPSHYD", "PS"]
hydro = [u for u in data if u.get("fuelType") in hydro_types]

print(f"{'NGBmUnitName':25s}  {'Type':8s}  bmUnitName")

for u in hydro:
    print(
        f"{u.get('nationalGridBmUnit', '?'):25s}  {u.get('fuelType', '?'):8s}  {u.get('bmUnitName', '?')}"
    )

print(f"\ntotal hydro units found: {len(hydro)}")
