import time
import random

user = 0
pc = 0
psb = ["gooool! ","parata super del portier ", "palooo ", "palla sotto al 7 incredibileee ", "palla fuori ", "che gooool! "]
#vincita dell attacante
psbW = psb[0]
psbW2 = psb[3]
psbW3 = psb[5]
#perdita dell attacante
psbL = psb[1]
psbL2 = psb[2]
psbL3 = psb[4]
psbL4 = psb[5]

while True:
    squadre = ["benevento", "juventus", "inter", "milan", "real madrid", "sassuolo", "chelsea", "bologna", "napoli", "roma", "lazio"]
    nazionali = ["italia", "argentina", "messico", "qatar", "brasile", "giappone", "belgio", "germania", "russia", "spania"]

    print("Benvenuto al campetto di calcio piu famoso al mondo... ")
    time.sleep(2)
    print("scegli il nome della tua squadra!")
    sqd = input().lower()

    print("perfetto benvenuto",sqd)
    print("contro che squadra vuoi giocare ?\n")
    print("hai a disposizione queste squadre! digita la squadra che vuoi oppure NAZIONALI se vuoi andare contro una nazionale")
    print(squadre)
    choose = input().lower()

    if choose in squadre:
        print("perfetto preparati a:",sqd,"VS",choose+"\n")
        print("si sente la tensione nell aria per i rigori...")
        time.sleep(5)
        print("la",choose,"è pronta a vincere ma ne sara degna?...")
        time.sleep(2)
        gol = random.choice(psb)
        print("l'attacante della",choose,"si prepara sul dischetto")
        print("....")
        time.sleep(4)
        if gol == psbW or gol == psbW2 or gol == psbW3:
            user += 1
            print(gol + "la squadra di casa ha segnato: [" + str(user) + "]")
        elif gol == psbL or gol == psbL2 or gol == psbL3 or gol == psbL4:
            pc += 1
            print()
            print("la squadra avversaria ora è ad",pc,"gol")


    elif choose == "nazionali":
        print("ecco tute le nazionali che hai a disposizione")
        print(nazionali)
        choose2 = input()
        if choose2 in nazionali:
            print("perfetto preparati a:",sqd,"VS",choose2)
            print("si sente la tensione per la finale dei mondiali...!")
            time.sleep(5)
            print("la",choose2,"fara di tutto per vincere ma se lo meritera?..")
            time.sleep(2)
            gol = random.choice(psb)
            print("il rigorista della",choose2,"sistema il pallone sul dischetto..")
            time.sleep(3)
            print("il fischio dell'arbitro")
            time.sleep(4)
            if gol == psbW or gol == psbW2 or gol == psbW3:
                user += 1
                print(gol + "la squadra di casa ha vintooo: [" + str(user) + "]")
            elif gol == psbL or gol == psbL2 or gol == psbL3 or gol == psbL4:
                pc += 1
                print()
                print("la squadra avversaria ha perso di", pc, "gol")
        else:
            print("devi scegliere una delle nazionali in lista!")
            continue
    else:
        print("devi scegliere  una squadra o nazionali !\n")
        continue