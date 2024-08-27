def contar_caracteres(string, caractere):

  contagem = string.count(caractere)
  print(f"O caractere '{caractere}' aparece {contagem} vezes na string.")


minha_string = "Olá, mundo! Python é divertido."
caractere_procurado = 'o'

contar_caracteres(minha_string, caractere_procurado)