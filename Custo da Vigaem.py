distância= float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma vigem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))