#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from operator import itemgetter
import csv
import sys
import os
import re
import shutil
from datetime import date

def main():

    now = date.today()
    search_player = sys.argv[1]

    # gracze/trabka/trabka_stats.csv
    stats_file = 'gracze/'+ search_player +'/'+ search_player+'_stats.csv'

    with open(stats_file) as csvfile:
        reader = csv.DictReader(csvfile)
        players_unsorted = list(reader)

    players = sorted(players_unsorted, key=lambda k: int(k['losses']), reverse=True)
    keys = [r['name'] for r in players]

    number = keys.index(search_player)

    # gracze/trabka/trabka_details.txt
    logfile = open('gracze/'+ search_player +'/'+ search_player+'_details.txt', 'a')
    logfile.write('00_'+ search_player + ': \n')
    logfile.write('    --> ' + players[number]['games'] + ' partii \n')
    logfile.write('    --> wynik: ' + players[number]['wins'] + '-' + players[number]['losses'] + '\n')
    logfile.write('    --> ' + now.strftime("%d.%m.%Y") + ' - rank ' + players[number]['rank'] + '\n\n')
    logfile.close()

    # delete search_player from lists
    del players[number]
    del keys[number]

    for i in range(len(keys)):
        if i < 9:
            os.mkdir('gracze/'+ search_player +'/0'+ str(i+1) + '_' + keys[i], 0755);
        else:
            os.mkdir('gracze/'+ search_player +'/'+ str(i+1) + '_' + keys[i], 0755);

    # gracze/trabka/trabka_replays.txt
    all_replays = open('gracze/'+ search_player +'/'+ search_player+'_replays.txt', 'r')
    all_replays_lines = all_replays.readlines()
    all_replays.close()

    for i in range(len(all_replays_lines)):

        replay_id = all_replays_lines[i][0:8]

        # gracze/trabka/00_trabka/61096194.txt
        replay = open('gracze/'+ search_player + '/00_'+ search_player+'/'+ replay_id + '.txt', 'r')
        replay_lines = replay.readlines()
        replay.close()

        player1_tmp = replay_lines[4].strip()
        player1 = re.sub(r'\[Black \"(.+?)\"\]', r'\1', player1_tmp)

        player2_tmp = replay_lines[5].strip()
        player2 = re.sub(r'\[White \"(.+?)\"\]', r'\1', player2_tmp)

        if not player1 == search_player:
            opponent = keys.index(player1)
            if opponent < 9:
                # gracze/trabka/00_trabka/61096194.txt --> gracze/trabka/03_gramnafonie/61096194.txt
                shutil.copy2('gracze/'+ search_player +'/00_'+ search_player+'/'+ replay_id + '.txt', 'gracze/' + search_player + '/0' + str(opponent+1) + '_' + player1 + '/' + replay_id + '.txt')
            else:
                shutil.copy2('gracze/'+ search_player +'/00_'+ search_player+'/'+ replay_id + '.txt', 'gracze/' + search_player + '/' + str(opponent+1) + '_' + player1 + '/' + replay_id + '.txt')
        elif not player2 == search_player:
            opponent = keys.index(player2)
            if opponent < 9:
                # gracze/trabka/00_trabka/61096194.txt --> gracze/trabka/03_gramnafonie/61096194.txt
                shutil.copy2('gracze/'+ search_player +'/00_'+ search_player+'/'+ replay_id + '.txt', 'gracze/' + search_player + '/0' + str(opponent+1) + '_' + player2 + '/' + replay_id + '.txt')
            else:
                shutil.copy2('gracze/'+ search_player +'/00_'+ search_player+'/'+ replay_id + '.txt', 'gracze/' + search_player + '/' + str(opponent+1) + '_' + player2 + '/' + replay_id + '.txt')


    print '--> Zapisywanie do pliku'

    # save to details file
    logfile = open('gracze/'+ search_player +'/'+ search_player+'_details.txt', 'a')

    for i in range(len(keys)):
        if i < 9:
            logfile.write('0'+ str(i+1) + '_' + players[i]['name'] + ': \n')
        else:
            logfile.write(str(i+1) + '_' + players[i]['name'] + ': \n')
        logfile.write('    --> ' + players[i]['games'] + ' partii \n')
        logfile.write('    --> wynik: ' + players[i]['losses'] + '-' + players[i]['wins'] + '\n')
        logfile.write('    --> ' + now.strftime("%d.%m.%Y") + ' - rank ' + players[i]['rank'] + '\n\n')

    logfile.close()


if __name__ == '__main__':
    main()

