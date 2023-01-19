ano = int(input ( ' em que ano você nasceu? '))
print (' você tem ')
idade = 2023 - ano 
if idade >= 18:
    print ('você é adulto')

elif idade >= 14: 
    print ('você é um adolecente')

elif idade >= 13: 
    print ('você é um pré-adolecente')

elif idade > 120:
    print ('idade invalida!')

elif idade >= 60: 
    print (' você é velho')

elif idade >= 80:
    print (' você é idoso ')

elif idade < 10:
    print ('você é uma criança ')

else: 
    print (' tente digitar novamente!')