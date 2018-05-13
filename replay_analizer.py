# -*- coding: iso-8859-1 -*-
# kurnik

import re

j = 1

start_id = 60896519
end_id   = 60901118

for i in range(start_id, end_id):
    
    matchfile = open('wszystkie_partie/'+ str(i) +'.txt', 'r')
    matchfile_lines = matchfile.readlines()
    matchfile.close()
    
    # dodane: 17.05.2015, problem w przypadku turnieji, gdy nie ma jednego gracza
    # jesli ta linia jest pusta, to oznacza, ze brak jednego gracza
    tmp_elo_tur = matchfile_lines[10].strip()
    tmp_elo_tur_formatted = re.sub(r'\[(.+?)Elo \"(\d{1,4})\"\]', r'\1', tmp_elo_tur)
    
    if not (tmp_elo_tur_formatted == '' or tmp_elo_tur_formatted == '1-0' or tmp_elo_tur_formatted == '0-1'):
    
        elo1 = matchfile_lines[9].strip()
        elo1_formatted = re.sub(r'\[BlackElo \"(\d{1,4})\"\]', r'\1', elo1)

        elo2 = matchfile_lines[10].strip()
        elo2_formatted = re.sub(r'\[WhiteElo \"(\d{1,4})\"\]', r'\1', elo2)
        
        #is_event = matchfile_lines[0].strip()
        #if not is_event == '[Event "?"]':
            #print 'TUR ' + str(i)
        
        if (int(elo1_formatted) > 1700 and int(elo2_formatted) > 1700):
            # mecz dwóch dobrych graczy
            
            date = matchfile_lines[2].strip()
            date_formatted = re.sub(r'\[Date \"(\d{4}).(\d{2}).(\d{2})\"\]', r'\1-\2-\3', date)
            
            player1 = matchfile_lines[4].strip()
            player1_formatted = re.sub(r'\[Black \"(.+?)\"\]', r'\1', player1)

            player2 = matchfile_lines[5].strip()
            player2_formatted = re.sub(r'\[White \"(.+?)\"\]', r'\1', player2)
        
            time = matchfile_lines[7].strip()
            time_formatted = re.sub(r'\[Time \"(\d{2}):(\d{2}):(\d{2})\"\]', r'\1:\2:\3', time)

            round_time = matchfile_lines[8].strip()
            round_time_formatted = re.sub(r'\[TimeControl \"(\d{1,3})\"\]', r'\1', round_time)

            file = open('spis_ciekawych_partii/'+ date_formatted +'.txt', 'a')
            
            file.write(str(j) + ' - #'+ str(i) + '\n')
            file.write('Termin: ' + date_formatted + ', ' + time_formatted + '\n')
            file.write('Mecz: ' + player1_formatted + ' (' + elo1_formatted + ') vs ' + player2_formatted + ' (' + elo2_formatted + ')' + '\n')
            file.write('System: ' + str(int(round_time_formatted)/60) + 'm' + '\n\n')
            file.close()
            
            print j, i
            
            j += 1

