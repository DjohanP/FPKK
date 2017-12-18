# CART on the Bank Note dataset
from random import seed
from random import randrange
from csv import reader
import math

dataTypes = 0
impurityNodes = 0

# Load a CSV file
def load_csv(filename):
	file = open(filename, "rb")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	counter = 1
	dummydict = {} #buat nyimpen konversi string ke float
	for row in dataset:
		try:
			row[column] = float(row[column].strip())
		except ValueError:
			if dummydict.has_key(str(row[column])) == True:
				row[column] = float(dummydict[str(row[column].strip())])
			else:
				dummydict[str(row[column])] = counter
				row[column] = float(counter)
				counter = counter + 1


# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Calculate precision percentage
def counting_reliability(actual, predicted):
	TP = 0
	TN = 0
	FP = 0
	FN = 0
	counter = {}
	for i in range(len(actual)):
		if actual[i] in counter:
			counter[actual[i]] += 1
		else:
			counter[actual[i]] = 1
		if (actual[i] == predicted[i]):
			if actual[i] == 0:
				TP += 1
			else:
				TN += 1
		else:
			if actual[i] == 0:
				FP += 1
			else:
				FN += 1
	# TP disini adalah ketika actual 0 predicted 0.
	try:
		precision = TP / float((TP+FP)) * 100
	except:
		precision = 100
	try:
		recall = TP / float((TP + FN)) * 100
	except:
		recall = 100
	try :
		accuracy = (TP + TN) / float((TP + TN + FP + FN)) * 100
	except :
		accuracy = 100
	return precision, recall, accuracy

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	accuration_scores = list()
	precision_scores = list()
	recall_scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted =algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		print dataTypes
		if dataTypes == 2:
			for i in range(len(predicted)):
				print 'Predicted : %.2f, Actual : %.2f' %(predicted[i], actual[i])
		elif dataTypes == 1:
			precision, recall, accuracy = counting_reliability(actual, predicted)
			for i in range(len(predicted)):
				print 'Predicted : %.2f, Actual : %.2f' %(predicted[i], actual[i])
			precision_scores.append(precision)
			recall_scores.append(recall)
			accuration_scores.append(accuracy)
	return accuration_scores, precision_scores, recall_scores

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini

def misclasification_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	misclas = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score = max(p, score)
		# weight the group score by its relative size
		misclas = max(score, misclas)
	return 1.0-misclas

def gain_index(groups, classes, dataset):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gain = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			if p != 0:
				score += - (p * math.log(p, 2))
		# weight the group score by its relative size
		gain += score * (size / n_instances)
	counter = {0:0, 1:0}
	for i in range(len(dataset)):
		if dataset[i][-1] == 0:
			counter[0] += 1
		else:
			counter[1] += 1
	information = 0.0
	for i in range(2):
		if p != 0:
			information += - (counter[i]/n_instances * math.log(counter[i], 2))
	return gain

# Select the best split point for a dataset
def get_split(dataset):
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	for index in range(len(dataset[0])-1):
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			if impurityNodes == 1:
				gini = gini_index(groups, class_values)
				if gini < b_score:
					b_index, b_value, b_score, b_groups = index, row[index], gini, groups
			elif impurityNodes == 2:
				b_score = 0
				gain = gain_index(groups, class_values, dataset)
				if gain > b_score:
					b_index, b_value, b_score, b_groups = index, row[index], gain, groups
			elif impurityNodes == 3:
				misclas = misclasification_index(groups, class_values)
				if misclas <b_score:
					b_index, b_value, b_score, b_groups = index, row[index], misclas, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
	root = get_split(train)
	split(root, max_depth, min_size, 1)
	return root

# Make a prediction with a decision tree
def predict(node, row):
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']

# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):
	tree = build_tree(train, max_depth, min_size)
	predictions = list()
	for row in test:
		prediction = predict(tree, row)
		predictions.append(prediction)
	return(predictions)

def main():
	# Test CART on Bank Note dataset
	seed(1)
	# load and prepare data
	global dataTypes
	dataTypes = input("1. Iris\n2. Housing Data Forecast\nInput Your Choices : ")
	if dataTypes == 1:
		dataset = load_csv('iris.data')
	elif dataTypes == 2:
		dataset = load_csv('housingdata.csv')
	global impurityNodes
	impurityNodes = input("1. GINI Method\n2. Entropy\n3. Misclasification Error\nInput Your Choices : ")

	# convert string attributes to integers
	for i in range(len(dataset[0])):
		str_column_to_float(dataset, i)
	# evaluate algorithm
	n_folds = 5
	max_depth = 5
	min_size = 10
	accuration_scores, precision_scores, recall_scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
	if dataTypes == 1:
		print'Accuration : %.2f\nPrecision : %.2f\nRecall : %.2f' % (sum(accuration_scores)/float(len(accuration_scores)),
														   sum(precision_scores)/float(len(precision_scores)),
														   sum(recall_scores) / float(len(recall_scores)))
	#print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

main()