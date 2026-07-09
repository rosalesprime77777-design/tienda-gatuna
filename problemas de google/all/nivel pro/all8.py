equipo = [
    {"usuario": "GatoPro", "level": 85},
    {"usuario": "MichiHacker", "level": 45}, # <-- No pasa los 50
    {"usuario": "CarlosTk", "level": 90}
]

validar=any([
    all(i["level"] > 50 for i in equipo),
    sum(i["level"] for i in equipo)/len(equipo) > 70#el sum biene con un +=
    ])
print(validar)
