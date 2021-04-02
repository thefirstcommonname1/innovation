import pprint
from pick import pick 

from beem import Hive

h = Hive()

title = 'Please choose filter: '

options = ['trending', 'hot', 'active', 'created', 'promoted']

option, index = pick(options, title)

