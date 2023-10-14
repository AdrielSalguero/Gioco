import json 
import csv
import random
import math 
from datetime import datetime  
import sys
import mysql.connector
import time

def mostrar_menu(opciones):
    
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
    

def elegir_menu(opciones):
    
    mostrar_menu(opciones)
    opcion = input('\n Su opcion es... ')

    while opcion not in opciones:
        print('\nUpss.. hubo algun error de tipeo recuerda:')
        elegir_menu(opciones)
    
    accion = opciones[opcion][1]
    accion()

def configuration():

    players_num = int(input('Seleziona il numero di giocatori: '))
    players= []
    for i in range(players_num):
        players.append(input('Nome e cognome: '))

    return players


def backup(games_records):

    file_path = 'C:\\Users\\Usuario\\OneDrive\\Escritorio\\Italiano\\Gioco\\BD\\records.csv'


    with open(file_path, mode='r+', newline='') as records:
                
        lector_csv = csv.reader(records)
        
        # Contar el número de filas en el archivo
        numero_filas = sum(1 for fila in lector_csv)

        games_records.append(numero_filas)
        escritor_csv = csv.writer(records)
        escritor_csv.writerow(games_records)



def comparador(real, ingresado, points):

    if real == ingresado: 
        points+=2
        print(f'+ + + È corretto + + + \n')
        return points

    else: 
        print(f" - - - Oops, ti sbagliavi, l'opzione corretta è **{real.upper()}** - - - \n ")
        return points


def verbos():


    file_path =  'C:\\Users\\Usuario\\OneDrive\\Escritorio\\Italiano\\Gioco\\BD\\verbos.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        rawdata = json.load(file)

    data = rawdata['verbs']     
    game= 'verbos'
    players = configuration()

    continue_playing = ''
    decorado= '- -'*10


    print('\n \nBENVENUTI GIOCHIAMO CON I VERBI  \n \n')


    while continue_playing == '':
        
        for player in players:
            playtime = datetime.now()
            points = 0
            verbo_aleatorio = random.choice(data)
            personas = random.choice(['Io', 'Tu','Lui/Lei','Noi'])
            persona = verbo_aleatorio['persona'][personas]
            
            print(f'{decorado} \n Ricorda che dovresti rispondere con la persona {personas} \n')

            print('Turno del giocatore', player.upper())
            levels = {'traduzione':'translation',
                    'presente': 'presente',
                    'passato prosimo':'passato_prossimo',
                    'passato imperfetto':'passato_imperfetto',
                    'futuro semplice':'futuro_semplice',
                    'futuro anteriore':'futuro_anteriore'}

            infinitive = verbo_aleatorio['infinitive'].upper()
            for key,value in levels.items(): 

                if key == 'traduzione':
                    player_input = input(f'Scrivi {key.upper()} del verbo {infinitive}: ').lower()
                    points = comparador(verbo_aleatorio[value],player_input, points)
                    
                else:
                    player_input = input(f'Scrivi {key.upper()} del verbo {infinitive}: ').lower()
                    points = comparador(persona[value],player_input, points)      
            print(f'{decorado} \n {decorado}  HAI AGGIUNTO IN TOTALE {points} PUNTI \n {decorado}')

            new_game_info = [playtime, player, game, points]
            backup(new_game_info)
        continue_playing = input('\nPremi "*Invio*" per il prossimo verbo \nPremi "*Finire*" per finire  ').lower()
    
    elegir_menu()




def conectores(): 
    
    file_path =  'C:\\Users\\Usuario\\OneDrive\\Escritorio\\Italiano\\Gioco\\BD\\conectores.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        rawdata = json.load(file)

    data = rawdata['connettori']     
    game= 'conectores'
    players = configuration()

    continue_playing = ''
    decorado= '- -'*10


    print('\n \n BENVENUTI GIOCHIAMO CON I CONNETORI  \n \n')

    while continue_playing == '':
        
        for player in players:
            
            playtime = datetime.now()
            points = 0
        
            for i in range(5):

                aleatorio = random.choice(data) 

                print(f'Turno del giocatore {player.upper()}, volta {i+1}/5')
                levels = {'traduzione':'translation'}

                connetore = aleatorio['italiano'].upper()

                for key,value in levels.items(): 

                    player_input = input(f'Scrivi {key.upper()} del connetore {connetore}: ').lower()
                    points = comparador(aleatorio[value],player_input, points)

            new_game_info = [playtime, player, game, points]
            backup(new_game_info)


        continue_playing = input('\n \n"*Invio*" per il prossimo conectori \nPremi "*Finire*" per finire  ').lower()
    
    elegir_menu()



def terminate():

    print('Grazie per aver giocato!\n\nIl programma si chiuderà tra 5 secondi\n')
    termination_list = ['Saving 20%', 'Saving 40%','Saving 60%','Saving 80%','Saving 99%']


    for i in termination_list:
        print(i)
        time.sleep(1) 

    #sys.exit()

if __name__ == "__main__":

    opciones = {
        '1': ('Practicar verbos', verbos),
        '2': ('Practicar conectores', conectores),
        '3': ('Salir', terminate)
    }

    elegir_menu(opciones)
