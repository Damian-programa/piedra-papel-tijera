import random
f= open('puntaje.txt', 'a', encoding= 'utf8')
for i in range(1,4):
    user_action= input("seleccione (piedra-papel-tijera)")
    possible_actions= ["piedra","papel","tijera"]
    computer_action= random.choice(possible_actions)
    #print(computer_action)
    print("\n Tú elegiste: ", user_action,", la computadora eligió: ", computer_action,"\n")
    if user_action==computer_action:
        print("Empate!!",user_action,". Ambos ganaron")
        f.write("Empate. \n")
    elif user_action=="piedra"and computer_action== "paper":
        print("Gano la computadora . \n")
        f.write("Gano la computadora. \n")
    elif user_action=="piedra" and computer_action== "tijera":
        print("Ganaste!!!! . \n")
        f.write("Ganaste!!. \n")
    elif user_action=="papel" and computer_action=="piedra":
        print("Ganaste!!!! . \n")
        f.write("Ganaste!!.\n")
    elif user_action=="papel" and computer_action=="tijera":
        print("Gano la computadora . \n")
        f.write("Gano la computadora.\n")
    elif user_action=="tijera" and computer_action=="piedra":
        print("Gano la computadora . \n")
        f.write("Gano la computadora.\n")
    elif user_action=="tijera" and computer_action=="papel":
        print("Ganaste!!!! .\n")
        f.write("Ganaste!!.\n")
    else:
        print("Error seleccione correctamente!")