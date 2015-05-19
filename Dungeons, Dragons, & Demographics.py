from random import randint
    
def newSettlement():
    theSettlement = {}
    sizepop = determineSizePop()
    theSettlement['size'] = sizepop['size']
    theSettlement['population'] = sizepop['population']
    theSettlement['classes'] = determineClassesLevels(theSettlement['size'], theSettlement['population'])
    theSettlement['races'] = determineRacialMix(theSettlement['population'])
    return theSettlement
    
def determineSizePop():
    dper = randint(1,100)
    if dper < 11:
        return {'size': "thorp", 'population': randint(20,80)}
    elif dper < 31:
        return {'size': "hamlet", 'population': randint(81, 400)}
    elif dper < 51:
        return {'size': "village", 'population': randint(401, 900)}
    elif dper < 71:
        return {'size': "small town", 'population': randint(901, 2000)}
    elif dper < 86:
        return {'size': "large town", 'population': randint(2001, 5000)}
    elif dper < 96:
        return {'size': "small city", 'population': randint(5001, 12000)}
    elif dper < 100:
        return {'size': "large city", 'population': randint(12001, 25000)}
    elif dper == 100:
        return {'size': "metropolis", 'population': randint(25001, 50000)}
    return {'size': "", 'population': 0}
    
def determineClassesLevels(size, population):
	modifier = 0
	numHighest = 1
	modifierRgrDrd = 0
	if size == "thorp":
		modifier = -3
		if randint(1,20) == 20:
			modifierRgrDrd = modifier + 10
		else: 
			modifierRgrDrd = modifier
	elif size == "hamlet":
		modifier = -2
		if randint(1,20) == 20:
			modifierRgrDrd = modifier + 10
		else: 
			modifierRgrDrd = modifier
	elif size == "village":
		modifier = -1
		modifierRgrDrd = modifier
	elif size == "large town":
		modifier = 3
		modifierRgrDrd = modifier
	elif size == "small city":
		modifier = 6
		numHighest = 2
		modifierRgrDrd = modifier
	elif size  == "large city":
		modifier = 9
		numHighest = 3
		modifierRgrDrd = modifier
	elif size == "metropolis":
		modifier = 12
		numHighest = 4
		modifierRgrDrd = modifier
	pcClasses = {
		'barbarian': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'bard': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'cleric': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'druid': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'fighter': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'monk': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'paladin': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'ranger': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'rogue': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'sorcerer': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'wizard': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		}
	pcClasses['barbarian'] = determineClassLevels(1,4,modifier,numHighest)
	pcClasses['bard'] = determineClassLevels(1,6,modifier,numHighest)
	pcClasses['cleric'] = determineClassLevels(1,6,modifier,numHighest)
	pcClasses['druid'] = determineClassLevels(1,6,modifierRgrDrd,numHighest)
	pcClasses['fighter'] = determineClassLevels(1,8,modifier,numHighest)
	pcClasses['monk'] = determineClassLevels(1,4,modifier,numHighest)
	pcClasses['paladin'] = determineClassLevels(1,3,modifier,numHighest)
	pcClasses['ranger'] = determineClassLevels(1,3,modifierRgrDrd,numHighest)
	pcClasses['rogue'] = determineClassLevels(1,8,modifier,numHighest)
	pcClasses['sorcerer'] = determineClassLevels(1,4,modifier,numHighest)
	pcClasses['wizard'] = determineClassLevels(1,4,modifier,numHighest)
	npcClasses = {
		'adept': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'aristocrat': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'commoner': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'expert': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'warrior': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		}
	npcClasses['adept'] = determineClassLevels(1,6,modifier,numHighest)
	npcClasses['aristocrat'] = determineClassLevels(1,4,modifier,numHighest)
	npcClasses['commoner'] = determineClassLevels(4,4,modifier,numHighest)
	npcClasses['expert'] = determineClassLevels(3,4,modifier,numHighest)
	npcClasses['warrior'] = determineClassLevels(2,4,modifier,numHighest)
	for npcClass in npcClasses:
		npcClasses[npcClass][1] = 0
	classes = dict(pcClasses.items() + npcClasses.items())
	subtotal = 0
	for theClass in classes:
		for level in classes[theClass]:
			subtotal += classes[theClass][level]
	remaining = population - subtotal
	classes['warrior'][1] = int(round(remaining * .05))
	classes['expert'][1] = int(round(remaining * .03))
	classes['adept'][1] = int(round(remaining * .005))
	classes['aristocrat'][1] = int(round(remaining * .005))
	subtotal += classes['warrior'][1] + classes['expert'][1] + classes['adept'][1] + classes['aristocrat'][1]
	classes['commoner'][1] = population - subtotal
	return classes

def determineClassLevels(numRolls, dieSize, modifier, numHighest):
	levels = {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
	for i in range(numHighest):
		roll = modifier
		for j in range(numRolls):
			roll += randint(1,dieSize)
		if roll > 20:
			roll = 20
		elif roll < 1:
			return levels
		curLevel = roll
		curQuant = 1
		levels[curLevel] += 1
		while curLevel / 2 > 0:
			curLevel = curLevel / 2
			curQuant = curQuant * 2
			levels[curLevel] += curQuant
	return levels

def determineRacialMix(population):
    races = {
    	'human': 0, 
    	'halfling': 0, 
    	'elf': 0, 
    	'dwarf': 0, 
    	'gnome': 0, 
    	'half-elf': 0, 
    	'half-orc': 0, 
    	'other': 0,
    	}
    if population > 12000:
        races['halfling'] = int(round(population * .2))
        races['elf'] = int(round(population * .18))
        races['dwarf'] = int(round(population * .1))
        races['gnome'] = int(round(population * .07))
        races['half-elf'] = int(round(population * .05))
        races['half-orc'] = int(round(population * .03))
    elif population > 900:
        races['halfling'] = int(round(population * .09))
        races['elf'] = int(round(population * .05))
        races['dwarf'] = int(round(population * .03))
        races['gnome'] = int(round(population * .02))
        races['half-elf'] = int(round(population * .01))
        races['half-orc'] = int(round(population * .01))
    else:
        races['halfling'] = int(round(population * .02))
        races['elf'] = int(round(population * .01))
        races['other'] = int(round(population * .01))
    minoritySubtotal = 0
    for race in races:
    	minoritySubtotal += races[race]
    races['human'] = population - minoritySubtotal
    return races
    
def newRuralSettlement():
	theSettlement = {}
	sizepop = determineRuralSizePop()
	theSettlement['size'] = sizepop['size']
	theSettlement['population'] = sizepop['population']
	theSettlement['classes'] = determineClassesLevels(theSettlement['size'], theSettlement['population'])
	theSettlement['races'] = determineRacialMix(theSettlement['population'])
	return theSettlement

def determineRuralSizePop():
	dper = randint(1,50)
	if dper < 11:
		return {'size': "thorp", 'population': randint(20,80)}
	elif dper < 31:
		return {'size': "hamlet", 'population': randint(81, 400)}
	elif dper < 51:
		return {'size': "village", 'population': randint(401, 900)}
	return {'size': "", 'population': 0}
    
numSettlements = int(raw_input("How many settlements? "))

totals = {
	'population': 0,
	'classes': {
		'barbarian': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'bard': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'cleric': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'druid': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'fighter': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'monk': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'paladin': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'ranger': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'rogue': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'sorcerer': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'wizard': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'adept': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'aristocrat': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'commoner': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'expert': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		'warrior': {20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
		},
	'races': {
    	'human': 0, 
    	'halfling': 0, 
    	'elf': 0, 
    	'dwarf': 0, 
    	'gnome': 0, 
    	'half-elf': 0, 
    	'half-orc': 0, 
    	'other': 0,
    	},
    'types': {
    	'thorp': 0,
    	'village': 0,
    	'hamlet': 0,
    	'small town': 0,
    	'large town': 0,
    	'small city': 0,
    	'large city': 0,
    	'metropolis': 0,
    	}
	}

for i in range(numSettlements):
    curSettlement = newSettlement()
    totals['population'] += curSettlement['population']
    for theClass in totals['classes']:
    	for level in totals['classes'][theClass]:
    		totals['classes'][theClass][level] += curSettlement['classes'][theClass][level]
    for k in totals['races']:
    	totals['races'][k] += curSettlement['races'][k]
    totals['types'][curSettlement['size']] += curSettlement['population']

ruralPop = totals['types']['thorp'] + totals['types']['hamlet'] + totals['types']['village']
print "Rural population is currently " + str(ruralPop/float(totals['population'])*100) + "% of total."
ruralize = str(raw_input("Generate rural settlements until rural population is >90% of total? (y/n) "))
if ruralize.lower() == "y":
	while ruralPop/float(totals['population']) < .9:
		curSettlement = newRuralSettlement()
		totals['population'] += curSettlement['population']
		for theClass in totals['classes']:
			for level in totals['classes'][theClass]:
				totals['classes'][theClass][level] += curSettlement['classes'][theClass][level]
		for k in totals['races']:
			totals['races'][k] += curSettlement['races'][k]
		totals['types'][curSettlement['size']] += curSettlement['population']
		ruralPop += curSettlement['population']

for theClass in totals['classes']:
	print theClass + " " + str(totals['classes'][theClass])
for race in totals['races']:
	print race + ": " + str(totals['races'][race])
for size in totals['types']:
	print size + ": " + str(totals['types'][size])
