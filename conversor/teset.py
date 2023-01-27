from datetime import datetime

while True:
    nascimento = int(input ( 'Em que ano você nasceu? '))
    data =  datetime.today().year
    idade = data - nascimento 
    print (f'Você tem {idade} anos')

    if idade < 0 or idade > 120:
        print('Idade inválida')
    else:
        break

print('Você é', end=' ')

print('Criança' if idade < 10 else 'Pré-adolescente' if idade == 13 else 'Adolescente' if idade <= 18 else 'Adulto' if idade >= 18 else 'Velho' if idade >= 60 else 'Idoso')