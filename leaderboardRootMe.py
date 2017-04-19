# -*- coding: utf-8 -*-
# Python v3.6

from urllib.request import urlopen
import re

def getScore(string): 
    html = urlopen("https://www.root-me.org/" + string )
    result = html.read().decode()
    
    match = re.findall(r'(Scor.*)', result)
    if match:
        if len(match) > 2:
            match = re.findall(r'.*span>(.*)</span', match[2])
            if match:
                result = match[0]
            else:
                result = None
        else : 
            result = 0
    else:
        result = None

    return result

def maxSize(array):
    maxS = -1
    for user in array:
        if maxS < len(user[0]):
            maxS = len(user[0])
    return maxS

def sortScore(array):
    a = {}; b = []
    for i in range(0, len(array)):
        if not array[i][1] in list(a.keys()):
            a.update({array[i][1]:[]})
        a[array[i][1]].append(i)

    keyA = list(a.keys())
    keyA.sort()

    for i in keyA[::-1]:
        for index in a[i]:
            b.append(array[index])

    return b

def printScore(array):
    maxS = maxSize(array)
    for user in array:
        sizeSpace = maxS - len(user[0]) + 3
        space =  ' '*sizeSpace
        print(user[0], space, '|', user[1])

def JsonScore(array):
    myJson = {} #nom original
    for user in array:
        myJson.update({user[0]:user[1]})
    return myJson

#nameList = ['pseudo',...]
nameList = []
leaderBoard= []
jsonLead = {}

for name in nameList:
    score = getScore(name)
    if not score == None:
        leaderBoard.append([name, int(score)])
sortLeaderboard = sortScore(leaderBoard)
printScore(sortLeaderboard)

