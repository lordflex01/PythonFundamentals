import random
from turtle import *

x = 0
y = 0
posPlayer = 0
posComputer = 0

print("Bienvenue sur Battlefield");

def PlayerMove():
    print ("Entrez vos coordonnées : \n");
    x = int(input("x = "));
    y = int(input("y = "));
    posPlayer = x*y;
    print("Vous êtes à la position "+str(posPlayer));
    return posPlayer

def ComputerMove():
    x = random.randint(0,5);
    y = random.randint(0,5);
    posComputer = x*y;
    print("Votre ennemi est à la position "+str(posComputer));
    return posComputer

def Plan(posPlayer, posComputer):
    if (posPlayer == posComputer):
        print("")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠊⠉⠉⠉⠉⢉⠝⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⡴⣋⠀⠀⣤⣒⡠⢀⠀⠐⠂⠀⠤⠤⠈⠓⢦⡀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⣰⢋⢬⠀⡄⣀⠤⠄⠀⠓⢧⠐⠥⢃⣴⠤⣤⠀⢀⡙⣆⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢠⡣⢨⠁⡘⠉⠀⢀⣤⡀⠀⢸⠀⢀⡏⠑⠢⣈⠦⠃⠦⡘⡆⠀⠀⠀")
        print("⠀⠀⠀⠀⢸⡠⠊⠀⣇⠀⠀⢿⣿⠇⠀⡼⠀⢸⡀⠠⣶⡎⠳⣸⡠⠃⡇⠀⠀⠀")
        print("⢀⠔⠒⠢⢜⡆⡆⠀⢿⢦⣤⠖⠒⢂⣽⢁⢀⠸⣿⣦⡀⢀⡼⠁⠀⠀⡇⠒⠑⡆")
        print("⡇⠀⠐⠰⢦⠱⡤⠀⠈⠑⠪⢭⠩⠕⢁⣾⢸⣧⠙⡯⣿⠏⠠⡌⠁⡼⢣⠁⡜⠁")
        print("⠈⠉⠻⡜⠚⢀⡏⠢⢆⠀⠀⢠⡆⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⣼⠾⢬⣹⡾⠀⠀")
        print("⠀⠀⠀⠉⠀⠉⠀⠀⠈⣇⠀⠀⠀⣴⡟⢣⣀⡔⡭⣳⡈⠃⣼⠀⠀⠀⣼⣧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⣸⣿⣿⣿⡿⣷⣿⣿⣷⠀⡇⠀⠀⠀⠙⠊⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣠⠀⢻⠛⠭⢏⣑⣛⣙⣛⠏⠀⡇⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠠⠜⠓⠉⠉⠀⠐⢒⡒⡍⠐⡇⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠢⠤⣀⣀⣀⣀⣘⠧⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀")
        print("\nBOOM! Vous avez tous les deux perdu")
    elif (posPlayer < posComputer):
        print("")
        print("⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⡴⠋⠉⡊⢁⠀⠀⢬⠀⠉⠋⠈⠥⠤⢍⡛⠒⠶⣄⡀⠀⠀⠀")
        print("⠀⠀⠀⠀⣾⠥⠀⠀⠊⢭⣾⣿⣷⡤⠀⣠⡀⡅⢠⣶⣮⣄⠉⠢⠙⡆⠀⠀")
        print("⠀⠀⣠⡾⣁⡨⠴⠢⡤⣿⣿⣿⣿⣿⠸⡷⠙⣟⠻⣯⣿⣟⣃⣠⡁⢷⣄⠀")
        print("⠀⡼⡙⣜⡕⠻⣷⣦⡀⢙⠝⠛⡫⢵⠒⣀⡀⠳⡲⢄⣀⢰⣫⣶⡇⡂⠙⡇")
        print("⢸⡅⡇⠈⠀⠀⠹⣿⣿⣷⣷⣾⣄⣀⣬⣩⣷⠶⠧⣶⣾⣿⣿⣿⡷⠁⣇⡇")
        print("⠀⠳⣅⢀⢢⠡⠀⡜⢿⣿⣿⡏⠑⡴⠙⣤⠊⠑⡴⠁⢻⣿⣿⣿⠇⢀⡞⠀")
        print("⠀⠀⠘⢯⠀⡆⠀⠐⡨⡻⣿⣧⣤⣇⣀⣧⣀⣀⣷⣠⣼⣿⣿⣿⠀⢿⠀⠀")
        print("⠀⠀⠀⠈⢧⡐⡄⠀⠐⢌⠪⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⠀⠀")
        print("⠀⠀⠀⠀⠀⠙⢾⣆⠠⠀⡁⠘⢌⠻⣿⣿⠻⠹⠁⢃⢹⣿⣿⣿⡇⡘⡇⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⢴⣄⠀⢭⡊⠛⠿⠿⠵⠯⡭⠽⣛⠟⢡⠃⡇⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⠬⣥⣀⡀⠀⢀⠀⠀⣠⡲⢄⡼⠃⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⠒⠒⠒⠋⠉⠀⠀⠀")
        print("\nWow! Vous avez dégommée votre adversaire")
    else:
        print("")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠤⠤⠒⠖⠒⠦⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⡠⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢄⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀")
        print("⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⠀")
        print("⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀")
        print("⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⢀⡴⠾⠆⠀⠀⠀⠈⠈⠁⠀⠀⠀ ⠈⡆")
        print("⠀⡾⠀⠀⠀⠀⠀⠐⢛⡿⠿⠟⠻⠿⡿⠛⠀⠀⠀⠛⣿⠿⠛⠛⠻⠂⠀⠀ ⢸")
        print("⢰⡇⠀⠀⠀⠀⠀⣀⣾⣗⠦⠀⠀⠈⡿⠀⠀⣼⠀⠀⣿⡀⠀⠐⢄⠆⠀⠀ ⠸")
        print("⢸⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣶⣴⢞⠕⠀⠀⣹⡆⠀⠙⣿⣷⣾⡟⠀⠀⠀ ⢸")
        print("⢸⡀⠀⣀⠤⠀⠄⠀⠀⠙⠟⠋⢁⣤⣼⣅⣶⣾⡿⣶⡶⢏⠉⠉⠀⠐⠢  ⡇")
        print("⠈⢧⠰⠁⠀⣀⢠⡔⠒⢾⠿⢿⣿⣿⡿⠭⠭⡭⠦⠦⠭⠿⢿⡶⠆⣠  ⢠⠃")
        print("⠀⠈⢆⠀⠀⢏⡉⠀⠀⠀⠀⠀⠈⠉⠛⢛⡿⠯⠭⠙⠛⠉⠁⠀⡤⠜  ⡜⠀")
        print("⠀⠀⠀⠳⣄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠓⡄⠀⠀⠀⠀⠀⠀ ⢀⠎⠀⠀")
        print("⠀⠀⠀⠀⠈⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀ ⢀⡤⠁⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⠉⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("\nAie! C'est fini pour vous...")

posPlayer = PlayerMove()
posComputer = ComputerMove()

Plan(posPlayer, posComputer)