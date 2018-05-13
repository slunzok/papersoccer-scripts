# -*- coding: iso-8859-1 -*-
# kurnik

import urllib

def beep():
    print "\a"

start_id = 66370784
end_id   = 66373457
    
for i in range(start_id, end_id):
    # 22.03.2015
    # urllib.urlretrieve('http://www.kurnik.pl/prze.phtml/' + str(i) + '.txt?sc', 'wszystkie_partie/' + str(i) + '.txt')
    # 20.05.2017 - nowy format adresu wyświetlania podglądu partii w .txt
    # urllib.urlretrieve('https://www.kurnik.pl/prze.phtml?gid=sc&pid=' + str(i) + '&txt', 'wszystkie_partie/' + str(i) + '.txt')
    # 03.05.2018 - kolejny nowy format adresu :P
    urllib.urlretrieve('https://www.kurnik.pl/p/?g=sc' + str(i) + '&txt', 'wszystkie_partie/' + str(i) + '.txt')
    #print i
    #for j in range(1,9):
        #if start_id+j*1000 == i:
            #print str(j*1000) + '/' + str(end_id-start_id)
    if i%1000 == 0:
        print str(i-start_id) + '/' + str(end_id-start_id)

beep()
