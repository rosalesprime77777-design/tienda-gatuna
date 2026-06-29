import json
personaje = {
    "nombre": "Goku",
    "nivel": 99,
    "transformaciones": ["Saya", "God", "Blue"],
    "activo": True
}

with open("goku.json","w") as f:
    json.dump(personaje,f,indent=4)
    