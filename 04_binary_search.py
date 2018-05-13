#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from operator import itemgetter
import csv
import sys
import os
import re

# mkdir labs
# ./01_unpack_and_remove.sh
# ./02_directory_info.sh
# ./03_analyze_replay.sh

# 1. Open a file, merge all lines to one line and save to list
def main():
    stats_file = 'users.csv'

    if os.stat(stats_file).st_size == 0:
        i = 0
        players = []
        new_players = []
        keys = []
        new_keys = []
        broken_replays = []

    else:
        #1. sposob
        with open(stats_file) as csvfile:
            reader = csv.DictReader(csvfile)
            players_unsorted = list(reader)

        players = sorted(players_unsorted, key=itemgetter('name'))
        keys = [r['name'] for r in players]

        i = len(players)
        new_players = []
        new_keys = []
        broken_replays = []

    # 2. Replay

    date = sys.argv[1]
    start_id = int(sys.argv[2])
    end_id   = int(sys.argv[3])+1

    for id in range(start_id,end_id):

        replay = open('labs/' + date + '/' + str(id) + '.txt', 'r')
        replay_lines = replay.readlines()
        replay.close()

        # turnieje troche psujo :(
        #is_second_player_tmp = replay_lines[10].strip()
        #is_second_player = re.sub(r'\[(.+?)Elo \"(\d{1,4})\"\]', r'\1', is_second_player_tmp)
        is_second_player = replay_lines[10].strip()

        """
        Bardzo dyskusyjna sprawa, dlatego te powtorki nie beda uzwgledniane w statystykach
        if is_second_player == '':
            elo0_tmp = replay_lines[9].strip()
            elo0 = re.sub(r'\[(.+?)Elo \"(\d{1,4})\"\]', r'\2', elo0_tmp)
        else:

            elo1_tmp = replay_lines[9].strip()
            elo1 = re.sub(r'\[BlackElo \"(\d{1,4})\"\]', r'\1', elo1_tmp)

            elo2_tmp = replay_lines[10].strip()
            elo2 = re.sub(r'\[WhiteElo \"(\d{1,4})\"\]', r'\1', elo2_tmp)
        """
        
        """
        player1 = 'kuba'
        player2 = 'jazz'
        elo1 = '1600'
        elo2 = '2200'
        result = '0-1'
        """

        """
        Tydzien 27:
        Puste: 62024123.txt, Black, 1622
        Puste: 62029500.txt, Black, 1548
        Puste: 62029583.txt, Black, 1535
        Puste: 62029655.txt, Black, 1533
        Puste: 62029689.txt, White, 1527
        Puste: 62029848.txt, Black, 1857
        Puste: 62042130.txt, White, 1797
        Puste: 62042202.txt, White, 1773
        """

        if (is_second_player == '' or is_second_player == '1-0' or is_second_player == '0-1'):
            
            """
            Tydzien 25: 30
            Tydzien 26: 18
            Tydzien 27:  8
            Tydzien 28:  7
            Tydzien 29:  3
            Tydzien 30:  2
            Tydzien 31:  4
            Tydzien 32:  2
            Tydzien 33:  3
            Tydzien 34:  0
            Tydzien 35:  0
            Tydzien 36:  0
            ---- Razem: 77
            """

            broken_replays.append(str(id))

        else:

            player1_tmp = replay_lines[4].strip()
            player1 = re.sub(r'\[Black \"(.+?)\"\]', r'\1', player1_tmp)

            player2_tmp = replay_lines[5].strip()
            player2 = re.sub(r'\[White \"(.+?)\"\]', r'\1', player2_tmp)

            result_tmp = replay_lines[6].strip()
            result = re.sub(r'\[Result \"(.+?)\"\]', r'\1', result_tmp)

            elo1_tmp = replay_lines[9].strip()
            elo1 = re.sub(r'\[BlackElo \"(\d{1,4})\"\]', r'\1', elo1_tmp)

            elo2_tmp = replay_lines[10].strip()
            elo2 = re.sub(r'\[WhiteElo \"(\d{1,4})\"\]', r'\1', elo2_tmp)

            if result == '0-1':

                # A - winner (player2)
                is_player2 = search_binary(keys, player2)
                is_new_player2 = search_binary(new_keys, player2)

                if is_player2 >=0:

                    position = int(keys.index(player2))
                    #players[position+2] += int(elo2)                                #Sums
                    #players[position+3] += 1                                        #Games
                    #players[position+4] += 1                                        #Wins
                    #players[position+1] = players[position+2]/players[position+3]   #Rank

                    players[position]['sums'] = str(int(players[position]['sums']) + int(elo2))                     #Sums
                    players[position]['games'] = str(int(players[position]['games']) + 1)                           #Games
                    players[position]['wins'] = str(int(players[position]['wins']) + 1)                             #Wins
                    players[position]['rank'] = str(int(players[position]['sums'])/int(players[position]['games'])) #Rank

                elif is_new_player2 >=0:

                    position = int(new_keys.index(player2))
                    #players[position+2] += int(elo2)                                #Sums
                    #players[position+3] += 1                                        #Games
                    #players[position+4] += 1                                        #Wins
                    #players[position+1] = players[position+2]/players[position+3]   #Rank

                    new_players[position]['sums'] = str(int(new_players[position]['sums']) + int(elo2))                     #Sums
                    new_players[position]['games'] = str(int(new_players[position]['games']) + 1)                           #Games
                    new_players[position]['wins'] = str(int(new_players[position]['wins']) + 1)                             #Wins
                    new_players[position]['rank'] = str(int(new_players[position]['sums'])/int(new_players[position]['games'])) #Rank
          
                else:
                    #players.append({'id': len(players)+1, 'name': player2, 'rank': elo2, 'sums': elo2, 'games': '1', 'wins': '1', 'losses': '0'})
                    #players = sorted(players, key=itemgetter('name'))
                    #keys = [r['name'] for r in players]
                    i += 1
                    new_players.append({'id': str(i), 'name': player2, 'rank': elo2, 'sums': elo2, 'games': '1', 'wins': '1', 'losses': '0'})
                    new_players = sorted(new_players, key=itemgetter('name'))
                    new_keys = [r['name'] for r in new_players]

                # B - loser (player1)

                is_player1 = search_binary(keys, player1)
                is_new_player1 = search_binary(new_keys, player1)

                if is_player1 >=0:

                    position = int(keys.index(player1))
                    #players[position+2] += int(elo1)                                    #Sums
                    #players[position+3] += 1                                            #Games
                    #players[position+5] += 1                                            #Losses
                    #players[position+1] = players[position+2]/players[position+3]       #Rank

                    players[position]['sums'] = str(int(players[position]['sums']) + int(elo1))                     #Sums
                    players[position]['games'] = str(int(players[position]['games']) + 1)                           #Games
                    players[position]['losses'] = str(int(players[position]['losses']) + 1)                         #Losses
                    players[position]['rank'] = str(int(players[position]['sums'])/int(players[position]['games'])) #Rank

                elif is_new_player1 >=0:

                    position = int(new_keys.index(player1))
                    #players[position+2] += int(elo1)                                    #Sums
                    #players[position+3] += 1                                            #Games
                    #players[position+5] += 1                                            #Losses
                    #players[position+1] = players[position+2]/players[position+3]       #Rank

                    new_players[position]['sums'] = str(int(new_players[position]['sums']) + int(elo1))                     #Sums
                    new_players[position]['games'] = str(int(new_players[position]['games']) + 1)                           #Games
                    new_players[position]['losses'] = str(int(new_players[position]['losses']) + 1)                         #Losses
                    new_players[position]['rank'] = str(int(new_players[position]['sums'])/int(new_players[position]['games'])) #Rank

                else:
                    #players.append({'id': len(players)+1, 'name': player1, 'rank': elo1, 'sums': elo1, 'games': '1', 'wins': '0', 'losses': '1'})
                    #players = sorted(players, key=itemgetter('name'))
                    #keys = [r['name'] for r in players]
                    i += 1
                    new_players.append({'id': str(i), 'name': player1, 'rank': elo1, 'sums': elo1, 'games': '1', 'wins': '0', 'losses': '1'})
                    new_players = sorted(new_players, key=itemgetter('name'))
                    new_keys = [r['name'] for r in new_players]
            else:

                # C - winner (player1)
                is_player1 = search_binary(keys, player1)
                is_new_player1 = search_binary(new_keys, player1)

                if is_player1 >=0:

                    position = int(keys.index(player1))
                    #players[position+2] += int(elo1)                                    #Sums
                    #players[position+3] += 1                                            #Games
                    #players[position+5] += 1                                            #Losses
                    #players[position+1] = players[position+2]/players[position+3]       #Rank

                    players[position]['sums'] = str(int(players[position]['sums']) + int(elo1))                     #Sums
                    players[position]['games'] = str(int(players[position]['games']) + 1)                           #Games
                    players[position]['wins'] = str(int(players[position]['wins']) + 1)                             #Wins
                    players[position]['rank'] = str(int(players[position]['sums'])/int(players[position]['games'])) #Rank

                elif is_new_player1 >=0:

                    position = int(new_keys.index(player1))
                    #players[position+2] += int(elo1)                                    #Sums
                    #players[position+3] += 1                                            #Games
                    #players[position+5] += 1                                            #Losses
                    #players[position+1] = players[position+2]/players[position+3]       #Rank

                    new_players[position]['sums'] = str(int(new_players[position]['sums']) + int(elo1))                     #Sums
                    new_players[position]['games'] = str(int(new_players[position]['games']) + 1)                           #Games
                    new_players[position]['wins'] = str(int(new_players[position]['wins']) + 1)                             #Wins
                    new_players[position]['rank'] = str(int(new_players[position]['sums'])/int(new_players[position]['games'])) #Rank
          
                else:
                    #players.append({'id': len(players)+1, 'name': player1, 'rank': elo1, 'sums': elo1, 'games': '1', 'wins': '1', 'losses': '0'})
                    #players = sorted(players, key=itemgetter('name'))
                    #keys = [r['name'] for r in players]
                    i += 1
                    new_players.append({'id': str(i), 'name': player1, 'rank': elo1, 'sums': elo1, 'games': '1', 'wins': '1', 'losses': '0'})
                    new_players = sorted(new_players, key=itemgetter('name'))
                    new_keys = [r['name'] for r in new_players]

                # D - loser (player2)
                is_player2 = search_binary(keys, player2)
                is_new_player2 = search_binary(new_keys, player2)

                if is_player2 >=0:

                    position = int(keys.index(player2))
                    #players[position+2] += int(elo2)                                #Sums
                    #players[position+3] += 1                                        #Games
                    #players[position+4] += 1                                        #Wins
                    #players[position+1] = players[position+2]/players[position+3]   #Rank

                    players[position]['sums'] = str(int(players[position]['sums']) + int(elo2))                     #Sums
                    players[position]['games'] = str(int(players[position]['games']) + 1)                           #Games
                    players[position]['losses'] = str(int(players[position]['losses']) + 1)                         #Losses
                    players[position]['rank'] = str(int(players[position]['sums'])/int(players[position]['games'])) #Rank

                elif is_new_player2 >=0:

                    position = int(new_keys.index(player2))
                    #players[position+2] += int(elo2)                                #Sums
                    #players[position+3] += 1                                        #Games
                    #players[position+4] += 1                                        #Wins
                    #players[position+1] = players[position+2]/players[position+3]   #Rank

                    new_players[position]['sums'] = str(int(new_players[position]['sums']) + int(elo2))                     #Sums
                    new_players[position]['games'] = str(int(new_players[position]['games']) + 1)                           #Games
                    new_players[position]['losses'] = str(int(new_players[position]['losses']) + 1)                         #Losses
                    new_players[position]['rank'] = str(int(new_players[position]['sums'])/int(new_players[position]['games'])) #Rank
          
                else:
                    #players.append({'id': len(players)+1, 'name': player2, 'rank': elo2, 'sums': elo2, 'games': '1', 'wins': '0', 'losses': '1'})
                    #players = sorted(players, key=itemgetter('name'))
                    #keys = [r['name'] for r in players]
                    i += 1
                    new_players.append({'id': str(i), 'name': player2, 'rank': elo2, 'sums': elo2, 'games': '1', 'wins': '0', 'losses': '1'})
                    new_players = sorted(new_players, key=itemgetter('name'))
                    new_keys = [r['name'] for r in new_players]

    """
    print players
    print '\n'
    print new_players
    print '\n'

    all_players = players + new_players
    print all_players
    print '\n'
    all_players = sorted(all_players, key=itemgetter('name'))
    print all_players
    """

    # 3

    all_players = players + new_players
    all_players = sorted(all_players, key=itemgetter('name'))

    print '--> Zapisywanie do pliku'

    with open(stats_file, 'w') as csvfile:
        fieldnames = ['id', 'name', 'rank', 'sums', 'games', 'wins', 'losses']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # hack python 2.5, in normal case just use: writer.writeheader()
        headers = {}
        for n in writer.fieldnames:
            headers[n] = n
        writer.writerow(headers)

        for i in range(len(all_players)):
            writer.writerow({'id': all_players[i]['id'], 'name': all_players[i]['name'], 'rank': all_players[i]['rank'], 'sums': all_players[i]['sums'], 'games': all_players[i]['games'], 'wins': all_players[i]['wins'], 'losses': all_players[i]['losses']})

    # turnieje :(
    file = open('broken_replays.txt', 'a')

    for i in range(len(broken_replays)):
        file.write(broken_replays[i])
        file.write('\n')

    file.close()

def search_binary(xs, target):
    #Find and return the index of key in sequence xs
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

if __name__ == '__main__':
    main()
