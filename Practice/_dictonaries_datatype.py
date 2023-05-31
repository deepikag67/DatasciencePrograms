# Dictonaries = are changable unordered collection of unique key value pair.
# we use colon (:) to follow key and add some value.
# we use comma ( , ) to separate the key value pair.
# we use curly brackets ( { })

_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams)

_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams ['csk'])

# To check or to get something we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams.get('dc'))
print(_ipl_teams.get('mi'))

# To get only key we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams.keys())

# To check omnly values we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams.values())

# To check both key and value we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
print(_ipl_teams.items())

# To check update or to change we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
_ipl_teams.update( {'Dc':'warner'})
_ipl_teams.update({'csk':'rituraj'})
print(_ipl_teams)

# To remove any key value pair we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
_ipl_teams.pop('rcb')
print(_ipl_teams)

# To clear all key value we use
_ipl_teams = {'csk' : 'msd', 'gt' : 'pandya', 'mi' : 'rohit', 'rcb' : 'faf'}
_ipl_teams.clear()
print(_ipl_teams)

# ur very beautiful

