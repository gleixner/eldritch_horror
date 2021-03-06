from investigator import Investigator

def get(filename):
		file = open(filename, 'r')
		file = file.readlines()
		file.pop(0)
		file = map( lambda x: x.strip(), file )
		return [line.split(',') for line in file]

exp_file = "../data/expeditions.dat"
expeditions = get( exp_file )

inv_file = "../data/investigators.dat"
investigators = get( inv_file )

stats = []



for i in investigators:
		result = []
		i = Investigator( i )
		result.append( i.name )
		for exp in expeditions:
				answer = ""
				answer = answer + str( i.success( exp ) )
				answer = answer + "/"
				answer = answer + str( i.failure( exp ) )
				result.append( answer )
		stats.append( result )

for line in stats:
		print line
