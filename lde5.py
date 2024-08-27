def calcular_area_e_dobrar(lado):

  area = lado * lado
  dobro_area = area * 2
  return dobro_area

lado = float(input("Digite o comprimento do lado do quadrado: "))

resultado = calcular_area_e_dobrar(lado)

print(f"O dobro da área do quadrado é: {resultado}")