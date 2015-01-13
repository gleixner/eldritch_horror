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

result = "name,"

i = 0
while i < len( expeditions ):
	result = result + expeditions[i][0] + ","
	i = i + 3
stats.append( result )

for i in investigators:
		result = ""
		i = Investigator( i )
		result = result + i.name + ","
		current = "Amazon"
		cumulative = 0
		for exp in expeditions:
				if exp[0] != current:
						result = result + "{0:.2f}".format(cumulative) + ","
						cumulative = 0
						current = exp[0]

				cumulative = cumulative + (i.success( exp )/3)
		result = result + "{0:.2f}".format(cumulative) + ","
		stats.append( result )


for line in stats:
		print line
