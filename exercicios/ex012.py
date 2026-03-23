largura = float(input('largura da parede'))
altura = float(input('altura da parede'))
área = largura*altura
print('sua parede tem a dimensão de {} x {} e a sua área é de {}m quadradros;'.format(largura,altura,
largura*altura))
print('para pintar essa parede, vocẽ precisa de{}L de tinta'.format(área/2))
