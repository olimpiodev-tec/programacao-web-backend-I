cidades = ['Saltinho']
cidades.append('Piracicaba')
print(cidades)

apps = ['orkut']
apps.insert(0, 'mirc messenger')
print(apps)

bolos = ['chocolate', 'prestígio', 'morango']
bolos.pop(1)
print(bolos)

chinelos = ['havaianas', 'rider', 'ipanema', 'rider']
chinelos.remove('rider')
print(chinelos)

bairros = [
    'Jaraguá', 'Santa Inês', 'Jupiá', 'Bosques',
    'Parque Orlândia', 'Santa Terezinha',
    'Mário Dedini', 'Cantagalo', 'Vida Nova',
    'Cecap', 'Campestre', 'Artemis', 'Boa Esperança',
    'Bongue', 'Água Branca', 'Paulicéia', 'Jd. Oriente'
]

print(len(bairros))

# Altera a lista original
bairros.sort()
print(bairros)

bairros.sort(reverse=True)
print(bairros)
