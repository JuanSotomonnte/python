import random

def elegiropciones():
    opciones=('piedra','papel','tijera')
    opciones_de_usuario=input('piedra , papel o tijera => ')
    opciones_de_usuario=opciones_de_usuario.lower()

    if not opciones_de_usuario in opciones:
        print('no es valido')
     #continue
        return None, None

    opciones_de_computador=random.choice(opciones)

    print('=> ', opciones_de_usuario)
    print('=> ', opciones_de_computador)
    return opciones_de_usuario,opciones_de_computador

def reglas(opciones_de_usuario,opciones_de_computador,user_wins,computer_wins):
   
    if opciones_de_usuario==opciones_de_computador:
        print("empate!")
    elif opciones_de_usuario=='piedra':
        if opciones_de_computador == 'tijera':
            print('piedra gana a tijera')
            print ('usuario gano')
            user_wins+=1
        else :
            print ('papel pierde con tijera')
            print('computador gano')
            computer_wins+=1
    elif opciones_de_usuario=='papel':
        if opciones_de_computador=='piedra':
            print("papel gana a piedra")
            print('usuario gana')
            user_wins+=1
        else:
            print('tijera gana a papel')
            print('computador gano')
            computer_wins+=1

    elif opciones_de_usuario=='tijera': 
        if  opciones_de_computador=='papel':
            print('papel pierde contra tijera')
            print('usuario gana')
            user_wins+=1
        else:   
            print("piedra gana a tijera")
        print('computador gana')
        computer_wins+=1

    return user_wins,computer_wins

def ganador(user_wins, computer_wins):
            if user_wins == 3:
                print(' El ganador es User ')
                exit()
                
            if computer_wins == 3:
                print(' El ganador es Computer ')
                exit()

def juego():
    user_wins = 0
    computer_wins = 0
    Rounds=1
    while True:
        print('***'*10 )
        print ('ROUND',Rounds)
        print('***'*10 )


        print('puntaje computador: ', computer_wins)
        print('puntaje Usuario: ', user_wins)
        Rounds +=1

        opciones_de_usuario,opciones_de_computador=elegiropciones()
        user_wins, computer_wins = reglas(opciones_de_usuario, opciones_de_computador, user_wins, computer_wins)
        ganador(user_wins,computer_wins)

juego()