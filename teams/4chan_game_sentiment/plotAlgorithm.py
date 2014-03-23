import sys

sys.path.append("C:OpenCV2.2Python2.7Libsite-packages")

import cv2
import random
import numpy as np

import matplotlib.pyplot as plt


def goto(linenum):
    global line
    line = linenum

    
data = [line.strip() for line in open("success_score.txt", 'r')]

trainData = np.array(data[0], data[1]).astype(np.float32)


responses = np.array(data[3]).astype(np.float32)
print responses

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('4Chan Game Rating')
ax.set_xlabel('Month')
ax.set_ylabel('Genre')

for item in data:
    if float(item) <= 0.4:
        color = 'r'
        # Take Red families and plot them
        red = trainData[responses.ravel() == 0]
        color_red = plt.scatter(red[:, 0], red[:, 1], 80, color, 'o')
    if float(item) <= 0.8:
        color = 'b'
        # Take Blue families and plot them
        blue = trainData[responses.ravel() == 1]
        color_blue = plt.scatter(blue[:, 0], blue[:, 1], 80, color, 'o')
    if float(item) == 1.0:
        color = 'y'
        # Take Yellow families and plot them
        yellow = trainData[responses.ravel() == 2]
        color_yellow = plt.scatter(yellow[:, 0], yellow[:, 1], 80, color, 'o')
    if float(item) < 1.2:
        color = 'g'
        # Take Green families and plot them
        green = trainData[responses.ravel() == 3]
        color_green = plt.scatter(green[:, 0], green[:, 1], 80, color, 'o')
    if float(item) > 1.2:
        color = 'k'
        # Take Black families and plot them
        black = trainData[responses.ravel() == 4]
        color_black = plt.scatter(black[:, 0], black[:, 1], 80, color, 'o')
    
newcomer1 = np.array([[7, 90]]).astype(np.float32)
color_white = plt.scatter(newcomer1[:, 0], newcomer1[:, 1], 80, 'w', 'o')
knn = cv2.KNearest()
knn.train(trainData, responses)
ret, results, neighbours , dist = knn.find_nearest(newcomer1, 4)

newcomer2 = np.array([[2, 50]]).astype(np.float32)
color_white = plt.scatter(newcomer2[:, 0], newcomer2[:, 1], 80, 'w', 'o')
knn = cv2.KNearest()
knn.train(trainData, responses)
ret1, results1, neighbours1 , dist1 = knn.find_nearest(newcomer2, 4)


newcomer3 = np.array([[10, 30]]).astype(np.float32)
color_white = plt.scatter(newcomer3[:, 0], newcomer3[:, 1], 80, 'w', 'o')
knn = cv2.KNearest()
knn.train(trainData, responses)
ret2, results2, neighbours2 , dist2 = knn.find_nearest(newcomer3, 4)

newcomer4 = np.array([[6, 50]]).astype(np.float32)
color_white = plt.scatter(newcomer4[:, 0], newcomer4[:, 1], 80, 'w', 'o')
knn = cv2.KNearest()
knn.train(trainData, responses)
ret3, results3, neighbours3 , dist3 = knn.find_nearest(newcomer4, 4)

newcomer5 = np.array([[9, 90]]).astype(np.float32)
color_white = plt.scatter(newcomer5[:, 0], newcomer5[:, 1], 80, 'w', 'o')
knn = cv2.KNearest()
knn.train(trainData, responses)
ret4, results4, neighbours4 , dist4 = knn.find_nearest(newcomer5, 4)


plt.legend((color_red, color_blue, color_yellow, color_green, color_black, color_white),
           ('Horrible', 'Bad', 'Average', 'Good', 'Great', 'New'),
           scatterpoints=1,
           loc='right right',
           ncol=3,
           fontsize=12)
print "Result: ", results, "\n"
print "Neighbours: ", neighbours, "\n"
print "Distance: ", dist, "\n"

print "Result: ", results1, "\n"
print "Neighbours: ", neighbours1, "\n"
print "Distance: ", dist1

print "Result: ", results2, "\n"
print "Neighbours: ", neighbours2, "\n"
print "Distance: ", dist2

print "Result: ", results3, "\n"
print "Neighbours: ", neighbours3, "\n"
print "Distance: ", dist3

print "Result: ", results4, "\n"
print "Neighbours: ", neighbours4, "\n"
print "Distance: ", dist4
plt.show()
