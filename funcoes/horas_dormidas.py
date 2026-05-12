# Calcular horas dormidas com o uso do return

def horas_dormidas(hora_dormiu, hora_acordou):
  if hora_acordou < hora_dormiu:
    return(24 - hora_dormiu) + hora_acordou
  else:
    return hora_acordou - hora_dormiu

hora_dormiu = int(input("DIgite o horário que dormiu: "))  
hora_acordou = int(input("Digite o horário que acordou: "))

resultado = horas_dormidas(hora_dormiu, hora_acordou)
print(f"Você dormiu {resultado} horas.")

