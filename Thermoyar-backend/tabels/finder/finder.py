# This function finds the nearest "upper" and "lower" value of the given one, in a target list

# Example target_dictationary = [1,2,3,4,5] target_value = 2
# returns 1 as lower and 3 as upper

def find_nearest_values(target_list, target_value):

	lowerValues = []
	upperValues = []

	#creates array of higher and lower values than the target value
	for value in target_list:
		if value < target_value:
			lowerValues.append(value)
		elif value > target_value:
			upperValues.append(value)

	# target_value is on the end of the list
	if target_list[len(target_list) - 1] == target_value:
		lower_target_value = findLowerValue(lowerValues, target_value)
		return [lower_target_value, None]

	# target_value is on the beginning of the list
	if target_list[0] == target_value:
		upper_target_value = findUpperValue(upperValues, target_value)
		return [None, upper_target_value]
	
	# target value is between the beginning and the end of the list
	lower_target_value = findLowerValue(lowerValues, target_value)
	upper_target_value = findUpperValue(upperValues, target_value)
	
	return [lower_target_value, upper_target_value]




def findLowerValue(lowerValues, target_value):
	for lowerValue in lowerValues:
		lowerValueDifference = abs(lowerValue - target_value)
		for otherLowerValue in lowerValues:
			otherLowerValuesDifference = abs(otherLowerValue - target_value)
			if lowerValueDifference <= otherLowerValuesDifference:
				lower_target_value = lowerValue
			elif lowerValueDifference > otherLowerValuesDifference:
				break
	return lower_target_value


def findUpperValue(upperValues, target_value):
	for upperValue in upperValues:
		upperValueDifference = abs(upperValue - target_value)
		for otherUpperValue in upperValues:
			otherUpperValuesDifference = abs(otherUpperValue - target_value)
			if upperValueDifference <= otherUpperValuesDifference:
				upper_target_value = upperValue
			elif upperValueDifference > otherUpperValuesDifference:
				break
	return upper_target_value


def interpolate(firstX, firstY, secondX, thirdX, thirdY):
	secondX = firstY + (secondX - firstX) * ((thirdY - firstY)/(thirdX - firstX))
	return secondX