# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 15:02:33 2014

@author: suren
"""
import Classifier as classifier
configFile = open("config.txt", "r");

url = configFile.readline().split("=")[1].strip();
targetFile = configFile.readline().split("=")[1].strip();
statsFile = configFile.readline().split("=")[1].strip();

configFile.close();

classifier.doSomething()