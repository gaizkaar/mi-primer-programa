pokemon_elegido = input('Contra que Pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur):')

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0
nombre_enemigo = 0

if pokemon_elegido == 'Squirtle':
    vida_enemigo = 90
    nombre_enemigo = 'Squirtle'
    ataque_enemigo = 8

elif pokemon_elegido == 'Charmander':
    vida_enemigo = 80
    nombre_enemigo = 'Charmander'
    ataque_enemigo = 7

elif pokemon_elegido == 'Bulbasaur':
    vida_enemigo = 100
    nombre_enemigo = 'Bulbasaur'
    ataque_enemigo = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input('Que ateque vamos a usar? (Chispazo / Bola Voltio) :')
    if ataque_elegido == 'Chispazo':
        vida_enemigo -= 10
    elif ataque_elegido == 'Bola Voltio':
        vida_enemigo -= 12

    print('La vida de {} ahora es {}'.format(nombre_enemigo, vida_enemigo))

    print('{} te hace un ataque'.format(nombre_enemigo))
    vida_pikachu -= ataque_enemigo

    print('La vida de Pikachu es de {}'.format(vida_pikachu))

if vida_enemigo <= 0:
    print('Has ganado')

elif vida_pikachu <= 0:
    print('Has perdido')

print('El combate ha terminado')

