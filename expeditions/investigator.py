class Investigator:
	'A character in Eldritch Horror that has certain skills with varying levels of competence.'

	# chance of success and failure for the number of dice rolled
	probability = {1 : [0.33,0.67], 2 : [0.56,0.44], 3 : [0.7,0.3], 4 : [0.8,0.2], 5 : [0.87, 0.13]}
	# how many dice the investigator can roll for each skill
	skills = {}

	def __init__ (this, data):
		this.name = data[0]
		this.skills['lore'] = int(data[1])
		this.skills['influence'] = int(data[2])
		this.skills['observation'] = int(data[3])
		this.skills['strength'] = int(data[4])
		this.skills['will'] = int(data[5])

	# 	Test of Skill 1  
	# 		-- pass --> Test of Skill 2 
	# 						  -- pass --> good outcome <-- success returns chance of this
	# 						  -- fail --> bad outcome
	# 		-- fail --> Test of Skill 3
	# 						  -- pass --> eh outcome
	# 						  -- fail --> bad outcome <-- failure returns chance of this

	# returns the investigator's chance of succeeding at both tests
	def success (this, expedition):
		passFirstTest = this._skillCheck(expedition[2], expedition[3], 0)
		passSecondTest = this._skillCheck(expedition[4], expedition[5], 0)
		return passFirstTest * passSecondTest

	# returns the investigator's chance of failing at both tests
	def failure (this, expedition):
		failFirstTest = this._skillCheck(expedition[2], expedition[3], 1)
		failThirdTest = this._skillCheck(expedition[6], expedition[7], 1)
		return failFirstTest * failThirdTest

	# skill: the skill being tested for the expedition
	# modifier: may add or subtract number of dice allowed
	# outcome: 0 for success, 1 for failure
	def _skillCheck (this, skill, modifier, outcome):
		numberOfDice = this.skills[skill.lower()] + int(modifier)
		if numberOfDice == 0:
				numberOfDice = 1
		return this.probability[numberOfDice][outcome]
