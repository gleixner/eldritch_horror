import investigator

def get(filename):
		file = open(filename, 'r')
		file = file.readlines()
		file.pop(0)
		return [line.split(',') for line in file]

exp_file = "../data/expeditions.dat"
expeditions = get( exp_file )

inv_file = "../data/investigators.dat"
investigators = get( inv_file )

stats = []

for i in investigators:
		result = []
		i = investigator( i )
		result.append( i.getName() )
		for exp in expeditions:
				answer = ""
				answer = answer + i.success( exp )
				answer = answer + "/"
				answer = answer + i.fail( exp )
				result.append( answer )
		stats.append( result )

print stats
