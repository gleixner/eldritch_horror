# need a constructor that takes a line of the data, just sets the data and name
# need get methods for the stats and name. 
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

	def __init__ (this, data){
		this.name = data[0]
		this.lore = data[1]
		this.influence = data[2]
		this.observation = data[3]
		this.strength = data[4]
		this.will = data[4]
	}
