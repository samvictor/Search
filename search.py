#Search Script
from os import walk, path

s_path = input('Search where? (enter "~" for user directory)\n')

walk_data = ()
if s_path == '~':
    walk_data = next(walk (path.expanduser('~')))
else:
    walk_data = next(walk(path))

print ('Looking in: ')
print('\t' + walk_data[0])
print ('\nFolders:')
print ('\t' + ', '.join(walk_data[1]))
print ('\nFiles:')
print ('\t' + ', '.join(walk_data[2]))
