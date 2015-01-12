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
		print i.name
		print i.skills
		for exp in expeditions:
				answer = ""

				print exp

				answer = answer + i.success( exp )
				answer = answer + "/"
				answer = answer + i.fail( exp )
				result.append( answer )
		stats.append( result )

print stats
