def converter_dolar_para_real(valor_dolar, taxa_cambio):
  
  valor_real = valor_dolar * taxa_cambio
  return valor_real

valor_dolar = float(input("Digite o valor em dólar: "))
taxa_cambio = float(input("Digite a taxa de câmbio dólar-real: "))

valor_real = converter_dolar_para_real(valor_dolar, taxa_cambio)

print("Valor em real brasileiro: R$", valor_real)
