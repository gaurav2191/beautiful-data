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

def read(readFlag):
    print(readFlag);
    if (readFlag == True):
        targetFile = config.targetFile.strip()
        targetDirectory = config.targetDirectory.strip()
        targetPath = config.targetPath
        
        print(targetPath)
        
        # instantiate hadoop
        hdfs.hdfs()
        
        # read from hadoop
        fileToRead = hdfs.open(targetPath)
        print(fileToRead.read())

if __name__ == "__main__":
    read(True);

#files = hdfs.lsl("test4")
#print (files)
#hdfs.get("test4/hello.txt", "/tmp/hello.txt")
#with open("/tmp/hello.txt") as f:
#	print f.read()