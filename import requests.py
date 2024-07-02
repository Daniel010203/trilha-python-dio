import requests

# Pegando a cotação do dolar hoje pela API do Banco Central
url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='06-09-2023'&$top=100&$format=json&$select=cotacaoCompra"
response = requests.get(url)
data = response.json()

# Extraindo a cotação de compra do dolar
cotacao_dolar = data['value'][0]['cotacaoCompra']

def converter_dolar_para_real(valor_em_dolar):
  valor_em_real = valor_em_dolar * cotacao_dolar
  return valor_em_real

# Loop principal do programa
while True:
  try:
    valor_em_dolar = float(input("Digite o valor em dólar a ser convertido: "))
    valor_em_real = converter_dolar_para_real(valor_em_dolar)
    print(f"O valor em reais é: R$ {valor_em_real:.2f}")
    break
  except ValueError:
    print("Valor inválido. Digite um número.")
