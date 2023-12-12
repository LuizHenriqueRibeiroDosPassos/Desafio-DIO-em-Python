# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões

# ## Objetivo

# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 6.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"

nome = input("Digite o nome de seu guerreiro : ")
nivel = int(input("Digite aqui o nível de experiência : "))


if nivel < 1000:
    print(f"\n O Herói {nome} está na maestria Ferro \n")
elif nivel >= 1001 and nivel <= 2000:
    print(f"\n O Herói {nome} está na maestria Bronze \n")
elif nivel >= 2001 and nivel <= 5000:
    print(f"\n O Herói {nome} está na maestria Prata \n")
elif nivel >= 5001 and nivel <= 7000:
    print(f"\n O Herói {nome} está na maestria Ouro \n")
elif nivel >= 7001 and nivel <= 8000:
    print(f"\n O Herói {nome} está na maestria Platina \n")
elif nivel >= 8001 and nivel <= 9000:
    print(f"\n O Herói {nome} está na maestria Ascendente \n")
elif nivel >= 9001 and nivel <= 1000:
    print(f"\n O Herói {nome} está na maestria Imortal \n")
else:
    print(f"\n O Herói {nome} está na maestria Radiante \n")
