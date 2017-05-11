#Search Script
from os import walk, path

input_str = input('Search where? (enter "~" for user directory)\n')

walk_data = ([''])
while True:
    try:
        if input_str == '~':
            walk_data = next(walk (path.expanduser('~')))
        else:
            walk_data = next(walk(input_str))
    except StopIteration:
        print ('\nNot found, please try again')
        input_str = input('\nSearch where? (enter path name or -s to search, enter ~ for user directory, enter c:/ for root)\n')
        if input_str == '-s':
            break
        elif input_str == '~':
            pass
        elif input_str in ['c:/', 'C:/']:
            pass
        else:
            input_str = walk_data[0] +'\\'+ input_str
        continue
        
    print('----------------------------------------------------------------------------------------------')
    print ('Looking in: ')
    print ('\t' + walk_data[0])
    print ('\nFolders:')
    print ('\t' + ', '.join(walk_data[1]))
    print ('\nFiles:')
    print ('\t' + ', '.join(walk_data[2]))

    input_str = input('\nNext? (enter path name or -s to search, enter ~ for user directory, enter c:/ for root)\n')
    if input_str == '-s':
        break
    elif input_str == '~':
        pass
    elif input_str in ['c:/', 'C:/']:
        pass
    else:
        input_str = walk_data[0] +'\\'+ input_str

s_term = input('\nEnter search term:\n')
s_path = walk_data[0]
print ('\nSearching for ' +s_term+ ' in ' +s_path+ ' and subdirectories')
found = []

if s_term in s_path.lower():
    found += [s_path]

for root, dirs, files in walk(s_path):
    for d in dirs:
        if s_term in d.lower():
            found += [root + '\\' + d + '\\']
    
    for f in files:
        if s_term in f.lower():
            found += [root + '\\' + f]
            
print ('\nThe following files and folders matched your search:')
print('\t' + '\n\t'.join(found))

input('\n')
