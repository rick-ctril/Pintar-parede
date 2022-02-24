width = float(input('Largura da prede:'))
#Altura da parede
height = float(input('Altura da parede:'))
#Largura da parede
area = width * height
#area é a soma de width (altura) e height (largura)
print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m2' .format(width, height, area))
dye = area / 2
#dye (tinta) vai dividir a area por 2 
print('Para pintar essa parede você presisa de {}l de tinta.' .format(dye))
