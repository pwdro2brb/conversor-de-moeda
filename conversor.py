import requests

API_KEY = 'fca_live_RAQo8NPgouxFZvyEgrx7wID5sCw1fouLcFiy4XjD'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

# Moedas suportadas 
SUPPORTED_CURRENCIES = ["USD", "BRL", "EUR", "CAD", "AUD", "CNY"]

def converte_valor(base):
    currencies = ",".join(SUPPORTED_CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se houver um status de erro HTTP
        data = response.json()
        return data["data"]
    except Exception as e:
        print(f"Erro: {e}")
        return None

while True:
    base = input("Digite a moeda padrão (q é para sair): ").upper()

    # Verifica se a moeda base está na lista das suportadas
    if base == "Q":
        break

    if base not in SUPPORTED_CURRENCIES:
        print("Moeda não suportada ou inválida.")
        continue
    
    try:
        quantidade = float(input(f"Digite a quantidade de {base} que você deseja converter: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue   

    data = converte_valor(base)
    if not data:
        continue
    
    del data[base]
    # Imprime o valor convertido multiplicado pela quantidade inserida
    for ticker, value in data.items():
        valor_convertido = quantidade * value
        print(f"{quantidade} {base} = {valor_convertido:.2f} {ticker}")
