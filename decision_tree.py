#-------------------------------------------------------------------------
# AUTHOR: Joshua Ho
# FILENAME: decision_tree.py
# SPECIFICATION: Plot a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment Start: 9:50 PM Programming
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

attributes = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)
      else:
         attributes = row

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
num_features = len(row) - 1
d = [dict() for x in range(num_features)]
for i, row in enumerate(db):
   X.append([])
   for x in range(num_features):
      if row[x] in d[x]:
         X[i].append(d[x].get(row[x]))
      else:
         X[i].append(len(d[x]))
         d[x][row[x]] = len(d[x])
# print(d)
# print(X)
# for(row in )

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
d2 = {}
for row in db:
  if row[-1] in d2:
    Y.append(d2.get(row[-1]))
  else:
    Y.append(len(d2))
    d2[row[-1]] = len(d2)

# print(d2)
# print(Y)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
# tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)

# Allows code to work for different datasets
tree.plot_tree(clf, feature_names=attributes, class_names=list(d2.keys()), filled=True, rounded=True)

plt.show()