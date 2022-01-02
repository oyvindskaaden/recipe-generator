#!/usr/bin/env python3

from domonic.html import *

import json

file = open("examples/pizzadeig.json")

data = json.load(file)

file.close()

#print(data)

print(f"## {data['title']}")
print(f"> Porsjoner {data['portions']}")
print()
print("### Ingridienser:")

#rows = [[td(b(f"{ingredient['amount']} {ingredient['unit']}")), td(ingredient['ingredient'])] for ingredient in data['ingredients']]
#rows = [f"{td(b(str(ingredient['amount']) + ' ' + str(ingredient['unit'])))}{td(ingredient['ingredient'])}" for ingredient in data["ingredients"]]
rows = [
    tr(
        td(b(f"{ingredient['amount']} {ingredient['unit']}"), _style="text-align: right; padding-right: 1em; padding-right: 1em"),
        td(ingredient['ingredient'])
    ) for ingredient in data["ingredients"]
]

table = table(
    # tr(
    #     td(b(f"{data['ingredients'][1]['amount']} {data['ingredients'][1]['unit']}")),
    #     td(f"{data['ingredients'][1]['ingredient']}")
    # )
    ''.join([str(row) for row in rows])
)
print(table)

script = script(f"var ingredients = {data['ingredients']};")
#for ingredient in data["ingredients"]:
#    print(f"\t{ingredient['amount']} {ingredient['unit']} {ingredient['ingredient']}")
print(script)
print()
print("### Fremgangsmåte")
for i, step in enumerate(data["steps"]):
    print(f"{i + 1}. {step}")

