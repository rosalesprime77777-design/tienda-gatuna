import json

clan_gerreros = [
    {"nombre": "Goku", "nivel": 99, "activo": True},
    {"nombre": "Vegeta", "nivel": 95, "activo": True},
    {"nombre": "Krillin", "nivel": 40, "activo": False}
]


with open("clan.json","w") as f :
    json.dump(clan_gerreros,f,indent=4)

with open("clan.json","r") as f:
    datos = json.load(f)
    
print("mis pendejos de la logia del michi")
for pendejos in datos:
    print(f"nombre;{pendejos['nombre']}")
    print(f"nivel;{pendejos['nivel']}")
    print(f"nivel: {pendejos['activo']}")
    
print("el pelonchas revive y entrena con drogasama")
for i in datos:
    if i['nombre'] == "Krillin":
        i['activo'] = True
        i['nivel'] += 10
        break
with open("clan.json","w") as f:
    json.dump(datos,f,indent=4)
    
for pendejos in datos:
    print(f"nombre;{pendejos['nombre']}")
    print(f"nivel;{pendejos['nivel']}")
    print(f"nivel: {pendejos['activo']}")
    