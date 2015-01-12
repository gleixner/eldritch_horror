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

	probability = {'1' : [0.33,0.67], '2' : [0.56,0.44], '3' : [0.7,0.3], '4' : [0.8,0.2]}
	skills = {}

	def __init__ (this, data):
		this.name = data[0]
		skills['lore'] = data[1]
		skills['influence'] = data[2]
		skills['observation'] = data[3]
		skills['strength'] = data[4]
		skills['will'] = data[5]

	def success (expedition):
		return passTest(expedition[2], expedition[3]) * passTest(expedition[4], expedition[5])

	def _passTest (skill, modifier):
		return probability[(dice(skills[skill.lower()]) + modifier)][0]

	def failure (expedition):
		return failTest(expedition[2], expedition[3]) * failTest(expedition[6], expedition[7])

	def _failTest(skill, modifier):
		return probability[(dice(skills[skill.lower()]) + modifier)][1]
