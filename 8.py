q = input("Digite algo: ")
print("Isso é um valor númerico", q.isnumeric()) 
print("Isso é uma letra ",q.isalpha()) #verifica se é letra
print("Tem algum espaço",q.isspace()) #se é só espaço
print("É um alpha ",q.isalnum()) # se é alpha numerico por exemplo 3a
print("Está em letras maiúsculas",q.isupper()) # se esta em letras maiusculas
print("Está em letras minúsculas",q.islower()) # se esta em letras minuscula
print("Está com a primeira letra maiúscula",q.istitle())