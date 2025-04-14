import json

fileJ = '{"nome": "tommaso", "cogn": "muraca"}'
dizionario = json.loads(fileJ)
print(dizionario["nome"])

dizMio = {'nome': 'tommaso'}
x = json.dumps(dizMio)
print(x)


