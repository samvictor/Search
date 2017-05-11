#Search Script
from os import walk, path

input_str = input('Search where? (enter "~" for user directory)\n')

walk_data = ()
while True:
    if input_str == '~':
        walk_data = next(walk (path.expanduser('~')))
    else:
        walk_data = next(walk(input_str))

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
    elif input_str in ['c:/', 'C:/', 'c:', 'C:']:
        pass
    else:
        input_str = walk_data[0] + input_str

input('\nEnter search term:\n')