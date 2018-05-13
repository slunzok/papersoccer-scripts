import re
import textwrap

matchfile = open('61972037.txt', 'r')
matchfile_lines = matchfile.readlines()
matchfile.close()

moves = ''
for i in range(12,len(matchfile_lines)-1):
    moves += matchfile_lines[i].strip() + ' '
        
moves_formatted = re.sub(r'\d{1,2}\.', r'', moves)
moves_array  = moves_formatted.split()

array_size = len(moves_array)
new_element = ''

for j in range(array_size-1): #nie wliczajac wyniku koncowego np. 1-0, 0-1
    elements = len(moves_array[j])
    for i in range(elements):
        if int(moves_array[j][i]) < 4:
            new_element += str(int(moves_array[j][i])+4)
        else:
            new_element += str(int(moves_array[j][i])-4)
            
    moves_array[j] = new_element
    new_element = ''
            
file = open('61972037_rotate.txt', 'a')

for i in range(12):
    file.write(matchfile_lines[i])
    
one_line = ''
for k in range(array_size-1):
    if k%2 == 0:
        one_line += str((k/2)+1) + '. ' + moves_array[k] + ' '
        #file.write(str(k+1) + '. ' + moves_array[k] + ' ')
    else:
        one_line += moves_array[k] + ' '
        
# wynik koncowy - osobno, bo wynik moze pojawic sie jako np. 33 5 1-0
one_line += moves_array[array_size-1]
        
lines = textwrap.fill(one_line, width=79)
file.write(lines)
file.write('\n \n \n')
    
file.close()
