import random
from colorama import Fore, Style

tablero=[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

pos_jugador_1=[0,0]
pos_jugador_2=[0,0]
pos_ignorancia_1=[0,0]
pos_ignorancia_2=[0,0]
  
def pintar_tablero():
  for i in range(len(tablero)):
    for j in range(len(tablero[i])):
      print("[",end="")
      if pos_jugador_1[0]==j and pos_jugador_1[1]==i:
        print(Fore.RED +Style.BRIGHT +"P1",end=" " + Style.RESET_ALL)
      else:
        print(Fore.YELLOW + Style.DIM + "#",end=" " + Style.RESET_ALL)
      if pos_jugador_2[0]==j and pos_jugador_2[1]==i:
        print(Fore.BLUE + Style.BRIGHT +"P2",end="" + Style.RESET_ALL)
      else:
        print(Fore.YELLOW + Style.DIM + "#",end="" + Style.RESET_ALL )
      if pos_ignorancia_1[0]==j and pos_ignorancia_1[1]==i:
        print(Fore.MAGENTA +Style.BRIGHT +"I1",end=" " + Style.RESET_ALL)
      else:
        print(Fore.YELLOW + Style.DIM + "#",end=" " + Style.RESET_ALL)
      if pos_ignorancia_2[0]==j and pos_ignorancia_2[1]==i:
        print(Fore.CYAN + Style.BRIGHT +"I2",end="" + Style.RESET_ALL)
      else:
        print(Fore.YELLOW + Style.DIM + "#",end="" + Style.RESET_ALL )   
      print("]",end=" ")     

    print("")


print("Este es el tablero de juego:\n")

pintar_tablero()

print("\n\nA continuación se muestra la lectura que se podría ocupar en algunas preguntas de español\n\nÉrase una vez una mujercita que vivía en una  casita. Una noche, cuando estaba en su camita, oyó un ruido. Salió de la camita y encendió su velita. Miró bajo su camita. Miró bajo su mesita. Miró   bajo su sillita. No había nada. Así que apagó su velita y regresó a su camita. La mujercita cerró los ojitos. Ya iba a dormirse cuando... ¡oyó un ruido! Así que salió de la camita y encendió la velita  y bajó la escalerita. Entró en su salita. Miró bajo la mesita. Miró    bajo las sillitas. No había nada. Así que subió la escalerita, apagó la velita y   regresó a su camita. La mujercita cerró los ojitos. Ya iba a dormirse cuando... ¡oyó un ruido! Salió de la cama. Encendió la vela. Bajo la escalera. Entró en el comedor. Subió a la mesa. Levantó el mantel. Miró debajo. Y en eso salió...   ¡bu!. -Vaya, vaya -dijo la mujercita-, ¡qué te parece! Asustarse de un simple ¡bu! \n\n       James H. Van Sickle, Mujercita\n\n")

preguntas_español=[
  ["1. ¿Qué escuchó la mujercita en su cama?",["1) Un ruido "," 2) El despertador "," 3) Un jilguero. "],1],
  ["2. Miró bajo su...",["1) Armario, su mesita, su maquinita. "," 2) Su camita, su mesita, su sillita. "," 3) Su sillita, su maquinita, su armarito."],2],
  ["3. ¿Qué salió debajo del mantel?", ["1) ¡bu, bu! "," 2) ¡pío, pío! ","3) ¡bu! "],3],
  ["4. ¿Cuál es la oración correcta?", ["1) No se que hacer "," 2) No sé qué hacer"],2],
  ["5. Es la falta de sosiego...", ["1) Deshasosiego "," 2) Desasosiego "," 3) Desasociego"],2],
  ["6. ¿Cuál se ocupa para hacer una pregunta?", ["1) Porqué "," 2) Porque "," 3) Por qué"],3],
  ["7. Sinónimo de razón", ["1) Entendimiento "," 2) Locura"],1],
  ["8. Ella le ........... la comida a los cerdos.", ["1) hecho "," 2) echo "," 3) echó "],3],
  ["9. Sinónimo de Imprudencia", ["1) Temeridad "," 2) Réplica "," 3) Rareza "],1],
  ["10. Y entonces, de repente, él me ......... un beso.", ["1) Dio"," 2)Dió"],2],
]

esp=9

def preguntar_esp(numero_jugador):
  global esp
  pregunta=random.choice(preguntas_español)
  print(pregunta[0])
  for i in range(len(pregunta[1])):
    print(pregunta[1][i],end=" ")
  print("Si es necesario, recuerda revisar la lectura")
  respuesta=int(input())
  if respuesta==pregunta[2]:
    if numero_jugador==1:
      esp=1
    elif numero_jugador==2:
      esp=1
  elif respuesta!=pregunta[2]:
    if numero_jugador==1:
      esp=0
    elif numero_jugador==2:
      esp=0
    
preguntas_mate=[
  ["1. ¿Cuánto es la cuarta parte de la tercera parte de 84?",7],
  ["2. Tengo 20 metros de cinta roja para hacer lazos en unos paquetes de regalo idénticos. Para cada lazo necesito 50 centímetros de cinta. ¿Cuántos lazos puedo hacer?",[40],1],
  ["3. Tengo que viajar en autobús durante 1,5 horas y luego esperar 45 minutos hasta tomar un tren que me dejará en mi destino dos horas y media después. ¿Cuánto dura mi trayecto en minutos?",285],
  ["4. (-5)(-9) te da...",45],
  ["5. ¿Cuánto es la raíz de dos al cuadrado?",2],
  ["6. (-3,4) ¿En qué cuadrante se ubica?",2],
  ["7. Resuelve para x en '5x+3=18'",3],
  ["8. El supervisor de producción de una empresa que se dedica a la fabricación de tornillos de acero, decide verificar la producción; la maquina debe producir tornillos de 3.2 pulgadas. Como no se dispone de tiempo para medir las 950 piezas que produce la maquina en un día, elije un grupo de 70 piezas para comprobar la confiabilidad o no de las maquinas. ¿Cuál es el tamaño de la población al cuadrado menos la muestra?",902430],
  ["9. Aproxima el número 58 a la siguiente docena y escíbela.",60],
  ["10. Si en una carrera adelantas al segundo lugar, ¿en qué número de posición quedas? (Escribe el número)",2]
]

mat=9

def preguntar_mate(numero_jugador):
  global mat
  pregunta=random.choice(preguntas_mate)
  print(pregunta[0])
  respuesta=int(input())
  if respuesta==pregunta[1]:
    if numero_jugador==1:
      mat=1
    elif numero_jugador==2:
      mat=1
  elif respuesta!=pregunta[1]:
    if numero_jugador==1:
      mat=0
    elif numero_jugador==2:
      mat=0

preguntas_ciencias=[
 ["1. La información genética en las células se localiza", ["1) En el núcleo "," 2) En la membrana "," 3) En el citoplasma "],[1],"núcleo"],
 ["2. Los cromosomas están formados por .....", ["1) ADN "," 2) Proteínas "," 3) ARN"],1],
 ["3. La fuerza física que la tierra ejerce sobre los cuerpos hacia su centro es la: ", ["1) Normal "," 2) Rozamiento","3) Gravedad"],3],
 ["4. La columna más a la derecha de la tabla periódica esta compuesta por:", ["1) Metales ","2) Gases Nobles","3) Tierras Raras"],2],
 ["5. ¿Cómo se llama la teoría que considera que todos los organismos descendemos del mismo ancestro?", ["1) Creacionismo "," 2) Darwinismo "," 3) Gradualismo"],2],
 ["6. ¿Qué expulsan las plantas por la noche?", ["1) Oxígeno","2) Dióxido de carbono","3) Glucosa"],2],
 ["7. ¿Cómo se llama el conjunto de montañas alineadas que forman una unidad.",["1) Alpes","2) Sierra","3) Cordillera"],3],
 ["8. ¿Cuál es la parte del cuerpo humano donde hay más huesos?",["1) El pie","2) El torso","3) La mano"],3],
 ["9. Los astronautas tienen mayor masa en la Tierra que en la Luna",["1) Sí","2) No"],2],
 ["10. ¿Cómo se llaman las partículas elementales sin masa que componen la luz?",["1) Gravitones","2) Electrones","3) Fotones"],1]
]

print(preguntas_ciencias[0][3])

ciencias=9

def preguntar_ciencias(numero_jugador):
  global ciencias
  pregunta=random.choice(preguntas_ciencias)
  print(pregunta[0])
  for i in range(len(pregunta[1])):
    print(pregunta[1][i],end=" ")
  respuesta=int(input())
  if respuesta==pregunta[2]:
    if numero_jugador==1: 
      ciencias=1
    elif numero_jugador==2:
      ciencias=1
  elif respuesta!=pregunta[2]:
    if numero_jugador==1:
      ciencias=0
    elif numero_jugador==2:
      ciencias=0
  
def ahorcado(numero_jugador):
  global ciencias
  pregunta=random.choice(preguntas_ciencias)
  print(pregunta[0])
  input("Tendras que resolver este ahorcado con 6 intentos. Para que no sea injusto te daremos una pequeña pista que sabemos te ayudará para poder completar este reto: ")
  palabra = pregunta[3]
  palabra_clave = []
  for i in range(len(palabra)):
    palabra_clave.append("_")
    print(palabra_clave)
  vidas = 6
  while "_" in palabra_clave and vidas > 0:
    print("Escribe una letra y completa la palabra:\n")
    letra = input()
    encontrar = False
    for i in range(len(palabra)):
      if palabra[i] == letra:
        palabra_clave[i] = letra
        encontrar=True
    if not encontrar:
      vidas -= 1
    print(palabra_clave)
    print("Te quedan " + str(vidas) + " intentos.")
    if vidas > 0:
      print("¡Lo lograste!\nFelicidades!")
      ciencias=1
  else:
    print("No lo lograste...")
    ciencias=0



archivo_salida=open("Puntos.txt","w")

turno=1
ahorcado(turno)
while True:
  print("Jugador "+ str(turno)+" es tu turno, estás listo? 1)Si 2)Salir")
  respuesta=input()
  if(respuesta=="2"):
    break
  else:
    if turno==1:
      for i in range(0,10):
        if pos_jugador_1==[i,0]:
          preguntar_esp(turno)
        if pos_jugador_1==[i,1]:
          preguntar_mate(turno)
        if pos_jugador_1==[i,2]:
          preguntar_ciencias(turno)
        if pos_jugador_1==[i,3]:
          preguntar_esp(turno)
        if pos_jugador_1==[i,4]:
          preguntar_mate(turno)
        if pos_jugador_1==[i,5]:
          preguntar_ciencias(turno)
    if turno==2:
      for i in range(0,10):
        if pos_jugador_2==[i,0]:
          preguntar_esp(turno)
        if pos_jugador_2==[i,1]:
          preguntar_mate(turno)
        if pos_jugador_2==[i,2]:
          preguntar_ciencias(turno) 
        if pos_jugador_2==[i,3]:
          preguntar_esp(turno)
        if pos_jugador_2==[i,4]:
          preguntar_mate(turno)
        if pos_jugador_2==[i,5]:
          preguntar_ciencias(turno)     
    if (turno==1 and (esp==1 or mat==1 or ciencias==1)):
      numero_dado=random.randint(1,6)
      pos_jugador_1[0]=pos_jugador_1[0]+numero_dado
      print("Tiraste: "+str(numero_dado)+" en tus dados")
      if(pos_jugador_1[0]>9):
        pos_jugador_1[0]=pos_jugador_1[0]-10
        pos_jugador_1[1]+=1
    elif (turno==2 and (esp==1 or mat==1 or ciencias==1)):
      numero_dado=random.randint(1,6)
      pos_jugador_2[0]=pos_jugador_2[0]+numero_dado
      print("Tiraste: "+str(numero_dado)+" en tus dados")
      if(pos_jugador_2[0]>9):
        pos_jugador_2[0]=pos_jugador_2[0]-10
        pos_jugador_2[1]+=1
    elif(turno==1 and (esp==0 or mat==0 or ciencias==0)):
      print("Lo siento, respuesta equivocada")
      numero_dado=random.randint(1,6)
      pos_ignorancia_1[0]=pos_ignorancia_1[0]+numero_dado
      print("La ignorancia del jugador 1 avanzó "+str(numero_dado)+" posiciones")
      if(pos_ignorancia_1[0]>9):
        pos_ignorancia_1[0]=pos_ignorancia_1[0]-10
        pos_ignorancia_1[1]+=1
    elif(turno==2 and (esp==0 or mat==0 or ciencias==0)):
      print("Lo siento, respuesta equivocada")
      numero_dado=random.randint(1,6)
      pos_ignorancia_2[0]=pos_ignorancia_2[0]+numero_dado
      print("La ignorancia del jugador 2 avanzó "+str(numero_dado)+" posiciones")
      if(pos_ignorancia_2[0]>9):
        pos_ignorancia_2[0]=pos_ignorancia_2[0]-10
        pos_ignorancia_2[1]+=1
    for i in range(0,7):
      if pos_jugador_1==[2,i]:
        pos_jugador_1[0]=pos_jugador_1[0]+3
        print(Fore.YELLOW+"¡Caíste en la casilla especial, avanzaste 3 lugares más!"+Style.RESET_ALL)
      elif pos_jugador_2==[2,i]:
        pos_jugador_2[0]=pos_jugador_2[0]+3
        print(Fore.YELLOW+"¡Caíste en la casilla especial, avanzaste 3 lugares más!"+Style.RESET_ALL)
    for i in range(0,7):
      if pos_jugador_1==[8,i]:
        pos_jugador_1[0]=pos_jugador_1[0]-8
        print(Fore.RED+"Caíste en la casilla maldita, regresas al inicio de la fila..."+Style.RESET_ALL)
      elif pos_jugador_2==[8,i]:
        pos_jugador_2[0]=pos_jugador_2[0]-8
        print(Fore.RED+"Caíste en la casilla maldita, regresas al incio de la fila..."+Style.RESET_ALL)
    pintar_tablero()
    if(turno==1):
      turno=2
    else:
      turno=1 
    if pos_jugador_1[1]>=6:
      ganador="¡Ganó el jugador 1!"
      print("El juego ha terminado ..... ¡Gana el jugador 1!")
      print(Fore.YELLOW + Style.BRIGHT + r"""

          _______________
         |@@@@|     |####|
         |@@@@|     |####|
         |@@@@|     |####|
         \@@@@|     |####/
          \@@@|     |###/
           `@@|_____|##'
                (O)
             .-'''''-.
           .'  * * *  `.
          :  *       *  :
         :    JUGADOR    :
         :       1       :
         :   *       *   :
          `.   * * *   .'
              `-.....-'       """+ Style.RESET_ALL)
      break
    elif pos_jugador_2[1]>=6:
      ganador="¡Ganó el jugador 2!"
      print("El juego ha terminado ..... ¡Gana el jugador 2!")
      print(Fore.YELLOW + Style.BRIGHT + r"""
      
          _______________
         |@@@@|     |####|
         |@@@@|     |####|
         |@@@@|     |####|
         \@@@@|     |####/
          \@@@|     |###/
           `@@|_____|##'
                (O)
             .-'''''-.
           .'  * * *  `.
          :  *       *  :
         :    JUGADOR    :
         :       2       :
         :   *       *   :
          `.   * * *   .'
             `-.....-'       """+ Style.RESET_ALL)
      break
    elif pos_ignorancia_1[1]>=6: 
     ganador="Ganó la ignorancia del jugador 1... Estúdiale más"
     print("El juego ha terminado ..... Ganó la ignorancia del jugador 1...")
     print(Fore.YELLOW + Style.BRIGHT + r'''
                        uuuuuuu
                    uu$$$$$$$$$$$uu
                 uu$$$$$$$$$$$$$$$$$uu
                u$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$"   "$$$"   "$$$$$$u
              "$$$$"      u$u       $$$$"
               $$$u       u$u       u$$$
               $$$u      u$$$u      u$$$
                "$$$$uu$$$   $$$uu$$$$"
                 "$$$$$$$"   "$$$$$$$"
                   u$$$$$$$u$$$$$$$u
                    u$"$"$"$"$"$"$u
         uuu        $$u$ $ $ $ $u$$       uuu
        u$$$$        $$$$$u$u$u$$$       u$$$$
        $$$$$uu      "$$$$$$$$$"     uu$$$$$$
        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
        """      ""$$$$$$$$$$$uu ""$"""
                uuuu ""$$$$$$$$$$uuu
         u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
         $$$$$$$$$$""""           ""$$$$$$$$$$$"
         "$$$$$"                      ""$$$$""
         $$$"                         $$$$"
     '''+ Style.RESET_ALL)
     break
    elif pos_ignorancia_2[1]>=6: 
     ganador="Ganó la ignorancia del jugador 2... Estúdiale más"
     print("El juego ha terminado ..... Ganó la ignorancia del jugador 2...")
     print(Fore.YELLOW + Style.BRIGHT + r'''
                        uuuuuuu
                    uu$$$$$$$$$$$uu
                 uu$$$$$$$$$$$$$$$$$uu
                u$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$$$$$$$$$$$$$$$$$$$$u
              u$$$$$$"   "$$$"   "$$$$$$u
              "$$$$"      u$u       $$$$"
               $$$u       u$u       u$$$
               $$$u      u$$$u      u$$$
                "$$$$uu$$$   $$$uu$$$$"
                 "$$$$$$$"   "$$$$$$$"
                   u$$$$$$$u$$$$$$$u
                    u$"$"$"$"$"$"$u
         uuu        $$u$ $ $ $ $u$$       uuu
        u$$$$        $$$$$u$u$u$$$       u$$$$
        $$$$$uu      "$$$$$$$$$"     uu$$$$$$
        u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
        """      ""$$$$$$$$$$$uu ""$"""
                uuuu ""$$$$$$$$$$uuu
         u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
         $$$$$$$$$$""""           ""$$$$$$$$$$$"
         "$$$$$"                      ""$$$$""
         $$$"                         $$$$"
     '''+ Style.RESET_ALL)
     break

archivo_salida.write(ganador)
archivo_salida.close()
