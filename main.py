import random #05/03/2025 // 21:17 // 2:01 horas de programacao

hp = int(random.randint(7, 16))
xp = 0
level = 0
batalha = False

def level_up():
    global level, xp
    if xp >= (level + 1) * 100:  
        while xp >= (level + 1) * 100:  
            level += 1
            print(f"Você subiu para o nível {level}!")
        return True
    return False

def turno_jogador():
    global hp, xp, level, escolha_jogador, defesa_jogador, dano
    print("-----------------------------------------")
    print(f"|Inimigo -> HP = {hp_inimigo} - XP = {xp_inimigo}|")
    print("-----------------------------------------")
    print(f"|Jogador -> HP = {hp} - XP = {xp} - LEVEL = {level}|")
    print("|ATK = 1 --- ATK PESADO = 2 --- DEF = 3 |")
    print("|ESPECIAL = 4 --- CURA = 5 --- HELP = 99|")
    print("-----------------------------------------")
    escolha_jogador = int(input(""))

    if escolha_jogador == 99:
        print("ATK = Ataque o inimigo com um dano comum")
        print("ATK PESADO = Ataque o inimigo com um dano mais alto que o comum porem com maior chance de errar")
        print("DEF = Tente defender um ataque com uma chance de nao conseguir defender")
        print("ESPECIAL = Um golpe com habilidades especiais com pouca chance de acerto")
        print("CURA = Cure um determinado numero de ponto de HP, variando entre 0 - 10")
        turno_jogador()

    elif escolha_jogador == 1:
        if xp <= 120:
            dano = random.randint(2, 7)
        elif xp >= 121:
            dano = random.randint(3, 9)
        elif xp >= 240:
            dano = random.randint(5, 11)
        elif xp >= 330:
            dano = random.randint(9, 11)
        elif xp >= 500:
            dano = 15

    elif escolha_jogador == 2:
        if xp <= 120:
            n = [1, 2, 3, 4, 5]
            acerto = random.choice(n)
            if acerto > 4:
                dano = random.randint(5, 7) + (level * 2)
            else:
                print("Voce errou o golpe")
        elif xp >= 121:
            n = [1, 2, 3, 4, 5]
            acerto = random.choice(n)
            if acerto >= 4:           
                dano = random.randint(8, 9) + (level * 2)
            else:
                print("Voce errou o golpe")
        elif xp >= 240:
            n = [1, 2]
            acerto = random.choice(n)
            if acerto == 2: 
                dano = random.randint(8, 11) + (level * 3)
            else:
                print("Voce errou o golpe")
        elif xp >= 330:
            dano = random.randint(9, 13) + (level * 2)
        elif xp >= 500:
            dano = 15 + (level * 2)

    elif escolha_jogador == 3:
        defesa_jogador = 1
        print("Jogador defendera!")

    elif escolha_jogador == 4:
        if xp <= 120:
            n = [1, 2, 3, 4, 5]
            acerto = random.choice(n)
            if acerto > 4:
                dano = 10
                print("Especial executado!")
            else:
                print("Voce errou o golpe")
        elif xp >= 121:
            n = [1, 2, 3, 4, 5]
            acerto = random.choice(n)
            if acerto >= 4:           
                dano = 5
                print("Especial executado!")
            else:
                print("Voce errou o golpe")
        elif xp >= 240:
            n = [1, 2]
            acerto = random.choice(n)
            if acerto == 2: 
                dano = 20
                cura = random.randint(5, 7)
                hp += cura
                print(f"Jogador curou {cura} de HP!")
                print("Especial executado!")
            else:
                print("Voce errou o golpe")
        elif xp >= 330:
            dano = 25
        elif xp >= 500:
            cura = random.randint(9, 15)
            hp += cura
            print(f"Jogador curou {cura} de HP!")
            print("Especial executado!")
            dano = 15

    elif escolha_jogador == 5:
        if xp <= 120:
            hp += 3
            print("Jogador curou 3 de HP!")
        elif xp >= 121:
            hp += 5
            print("Jogador curou 5 de HP!")
        elif xp >= 240:
            hp += 8
            print("Jogador curou 8 de HP!")
        elif xp >= 330:
            hp += 11
            print("Jogador curou 11 de HP!")
        elif xp >= 500:
            cura = random.randint(9, 15)
            hp += cura
            print(f"Jogador curou {cura} de HP!")

def gerar_inimigo():
    global hp_inimigo, dano_inimigo, hp_inimigo, xp_inimigo
    xp_inimigo = random.randint(1, 273)
    if xp_inimigo >= 150:
        hp_inimigo = random.randint(12, 20)
        dano_inimigo = random.randint(5, 10)
    elif xp_inimigo >= 350:
        hp_inimigo = random.randint(20, 35)
        dano_inimigo = random.randint(10, 15)   
    else:
        hp_inimigo = random.randint(2, 10)
        dano_inimigo = random.randint(1, 6)

def turno_inimigo():
    global escolha_inimigo, hp_inimigo
    if hp_inimigo <= 7:
        escolhas = [1, 3, 5] #ATK, DEF, CURA
    elif hp_inimigo >= 8 and hp_inimigo <= 14:
        escolhas = [1, 2, 3] #ATK, ATK PESADO, DEF

    elif hp_inimigo >= 15 and hp_inimigo <= 26:
        escolhas = [1, 2, 3, 4] #ATK, ATK PESADO, DEF, ESP
    elif hp_inimigo >= 27 and hp_inimigo <= 35:
         escolhas = [2, 3, 4] #ATK PESADO, DEF, ESP
    escolha_inimigo = random.choice(escolhas)
    print(escolha_inimigo)

def comparacao_escolhas():
    global hp, hp_inimigo, escolha_inimigo, escolha_jogador, dano_inimigo, dano
    defesa_jogador = 0
    defesa_inimigo = 0
    if escolha_jogador == 1 and escolha_inimigo == 3:
        print("O inimigo defendeu o seu ataque!")
        defesa_inimigo = 1
    if escolha_jogador == 2 and escolha_inimigo == 3:
        print("O inimigo defendeu o seu ataque!")
    if escolha_jogador == 3 and escolha_inimigo == 1:
        print("Jogador defendeu o ataque")
    if escolha_jogador == 3 and escolha_inimigo == 2:
        print("Jogador defendeu o ataque")
 
    if escolha_jogador == 1:
        if defesa_inimigo == 1:
            print("O inimigo defendeu o seu ataque!")
        else:
            hp_inimigo = hp_inimigo - dano
            print(f"Jogador causou {dano} de dano!")
    if escolha_jogador == 2:
        if defesa_inimigo == 1:
            print("O inimigo defendeu o seu ataque!")
        else:
            hp_inimigo = hp_inimigo - dano
            print(f"Jogador causou {dano} de dano!")

    if escolha_inimigo == 1:
        if defesa_jogador == 1:
            print("Jogador defendeu o ataque")
        else:
            hp = hp - dano_inimigo
            print(f"Inimigo causou {dano_inimigo} de dano !")

    if escolha_inimigo == 2:
        if defesa_jogador == 1:
            print("Jogador defendeu o ataque")
        else:
            hp = hp - dano_inimigo
            print(f"Inimigo causou {dano_inimigo} de dano !")

    if escolha_inimigo == 4:
        hp = hp - 15
        print("Inimigo usou um especial!")
    if escolha_inimigo == 5:
        hp_inimigo = hp_inimigo + 8
        print("Inimigo curou 8 de vida!")

    if escolha_jogador == 4:
        hp = hp - dano
        print("Jogador usou um especial!")

def combate(): 
    global batalha, xp
    gerar_inimigo()
    while batalha == True: 
        turno_jogador()
        turno_inimigo()
        comparacao_escolhas()
        if hp <= 0:
            print("Jogador morreu! Fim de jogo.")
            batalha = input("Deseja jogar novamente?")
            if batalha == "s":
                batalha = True
                combate()
            else:
                exit()
        if hp_inimigo <= 0:
            print("Inimigo morreu! Fim de jogo.")
            xp += xp_inimigo
            level_up()
            batalha = input("Deseja batalhar mais uma vez?")
            if batalha == "s":
                batalha = True
                combate()
            else:
                exit()
            



batalha = input("Deseja batalhar?")
if batalha == "s":
    batalha = True
    combate()
else:
    exit()



