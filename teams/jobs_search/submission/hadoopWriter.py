# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 13:28:20 2014

@author: suren
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:04:45 2014

@author: suren
"""
import pydoop.hdfs as hdfs
import os
import Config as config

MB = 2**20
TEST_ROOT = os.getenv("TEST_ROOT", "facebook")

def write(writeFlag):
    if (writeFlag == True):
        # instantiate hadoop
        hdfs.hdfs()
        
        targetPath = config.targetPath;
        targetDirectory = config.targetDirectory;
        sourceFile = config.sourceFile;
        
        print("Target Path: " + targetPath);
        print("Target Directory: " + targetDirectory);
        print("Source Path: " + sourceFile);
        
        dumpFile = open(sourceFile, "r");
        fullText = dumpFile.read();
        dumpFile.close();
        
        # write to hadoop
        #hdfs.mkdir(targetDirectory)
        hdfs.dump(fullText, targetPath)
#hdfs.cp(sourceFile, targetPath)

#print (hdfs.ls("test4"))
#files = hdfs.ls("test4")

# read from hadoop
#hdfs.get("test4/hello.txt", "/tmp/hello.txt")
#with open("/tmp/hello.txt") as f:
#	print f.read()

#print(hdfs.ls("test", "hduser1"))
#text = hdfs.load("test/hello.txt")
#print text