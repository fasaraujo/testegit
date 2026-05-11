import requests
import os
import platform
import time

def limpa():
    x = platform.system()
    if (x == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def arnaLatLong():
    arnaLat = float(input('Latitude  ..: '))
    arnaLong = float(input('Longitude ..: '))
    return arnaLat,arnaLong

limpa()
arnaCoordenadas = arnaLatLong()
url = f'https://api.open-meteo.com/v1/forecast?latitude={arnaCoordenadas[0]}&longitude={arnaCoordenadas[1]}&current=temperature_2m&current=relative_humidity_2m&current=precipitation_probability&current=rain'

try:
    print('Comunicando com a api da Open Meteo...')
    time.sleep(2)
    res = requests.get(url, timeout=10)
    if res.status_code == 200:
        print('Ready Ok')
        time.sleep(1)
        dados = res.json()
        print('--------------------------------')
        print('-     Dados Coletados          -')
        print('--------------------------------')
        print('    - AGORA NA REGIÃO -         ')
        print(f'Latitude: {dados['latitude']}')
        print(f'Longitude: {dados['longitude']}')
        print(f'Elevação: {dados['elevation']}')
        print(f'Temperatura: {dados['current']['temperature_2m']} {dados['current_units']['temperature_2m']}')
        print(f'Umidade: {dados['current']['relative_humidity_2m']} {dados['current_units']['relative_humidity_2m']}')
        print(f'Precipitação prob: {dados['current']['precipitation_probability']} {dados['current_units']['precipitation_probability']}')
        print(f'Chuva:  {dados['current']['rain']} {dados['current_units']['rain']}')
        print('--------------------------------')
    else:
        arnaOutro = res.status_code
        print(f'Erro retornado pela api {arnaOutro}')
except Exception as e:
    print(f'Erro -> {e}')

