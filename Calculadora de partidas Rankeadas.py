 # Calculadora de partidas Rankeadas
# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

# Objetivo:

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

# Se vitórias for menor do que 10 = Ferro
# Se vitórias for entre 11 e 20 = Bronze
# Se vitórias for entre 21 e 50 = Prata
# Se vitórias for entre 51 e 80 = Ouro
# Se vitórias for entre 81 e 90 = Diamante
# Se vitórias for entre 91 e 100= Lendário
# Se vitórias for maior ou igual a 101 = Imortal

# Saída

# Ao final deve se exibir uma mensagem:
# "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

# saldo = 0



def calculoDeRankeadas (vitorias, derrotas):
    saldo = vitorias - derrotas
    
    if vitorias <= 10:
        nivel = " Ferro "
    elif vitorias >= 11 and vitorias <= 20:
        nivel = " Bronze "
    elif vitorias >= 21 and vitorias <= 50:
        nivel = " Prata "
    elif vitorias >= 51 and vitorias <= 80:
        nivel = " Ouro "
    elif vitorias >= 81 and vitorias <= 90:
        nivel = " Diamante "
    elif vitorias >= 91 and vitorias <= 100:
        nivel = " Lendário "
    else:
        nivel = " Imortal "
    
    return saldo, nivel

vitorias = int(input("Me diga o número de vitórias de sua conta : "))
derrotas = int(input("\nMe diga o número de derrotas de sua conta : "))

saldoVitorias, nivel = calculoDeRankeadas(vitorias, derrotas)

print(f"\nO Herói tem um saldo de {saldoVitorias} está no nível de {nivel}.\n")
