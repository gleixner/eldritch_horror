# need a constructor that takes a line of the data, just sets the data and name
# need a method that takes in a line of expedition and calculates the probability of success and failure in that expedition.
# Structure of expeditions:

# 	Test of Skill 1  
# 		-- pass --> Test of Skill 2 
# 						  -- pass --> good outcome
# 						  -- fail --> bad outcome
# 		-- fail --> Test of Skill 3
# 						  -- pass --> eh outcome
# 						  -- fail --> bad outcome
#
# Calculate the success for the first * success for the second.  
# Calculate the failure of the first test * failure of the third test
#
class Investigator:
	'A character in Eldritch Horror that has certain skills with varying levels of competence.'

	def __init__ (this, data):
		this.name = data[0]
		this.lore = data[1]
		this.influence = data[2]
		this.observation = data[3]
		this.strength = data[4]
		this.will = data[5]

	def success (expedition):
		return passTest(expedition[2], expedition[3]) * passTest(expedition[4], expedition[5])

	def passTest (skill, modifier):
		return probability(dice(skill) - modifier)[0]

	def failure (expedition):
		return failTest(expedition[2], expedition[3]) * failTest(expedition[6], expedition[7])

	def failTest(skill, modifier):
		return probability(dice(skill) - modifier)[1]

	def probability (dice):
		stat = []
		if(dice == 1)
			stat[0] = 0.33
			stat[1] = 0.67
		else if (dice == 2)
			stat[0] = 0.56
			stat[1] = 0.44
		else if (dice == 3)	
			stat[0] = 0.7
			stat[1] = 0.3
		else
			stat[0] = 0.8
			stat[1] = 0.2
		return stat

	def dice (skillString):
		skill = skillString.lower()
		if(skill == "lore")
			return this.lore
		else if(skill == "influence")
			return this.influence
		else if(skill == "observation")
			return this.observation
		else if(skill == "strength")
			return this.strength
		else return this.will
	