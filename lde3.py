def metros_para_centimetros(metros):
    centimetros = metros * 100 
    return centimetros 

metros = float(input("Digite a quantidade de metros:"))

resultado = metros_para_centimetros(metros)

print(f"{metros} metros equivalem a {resultado} centímetros.")