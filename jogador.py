'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dicionario = {}
dicionario['Nome:'] = str(input('Digite o nome do jogador: ')).strip().title()
dicionario['Partidas:'] = int(input(f'Quantas partidas {dicionario["Nome:"]} jogou? '))
gols = []
for p in range(1, dicionario['Partidas:'] + 1):
    gols.append(int(input(f'    Quantos gols na {p}° partida? ')))
dicionario['Gols:'] = gols
print()
for k, v in dicionario.items():
    print(k, v)
print()
print(f'O jogador {dicionario["Nome:"]} jogou {dicionario["Partidas:"]} partidas.')
for partidas in range(1, dicionario['Partidas:'] + 1):
    print(f'    Na {partidas}° partida fez {gols[partidas - 1]} gols')