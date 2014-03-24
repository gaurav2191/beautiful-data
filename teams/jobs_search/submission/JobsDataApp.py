# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 15:17:02 2014

@author: suren
"""
import hadoopWriter as toHadoop
import hadoopReader as fromHadoop

# ignore this block, cant get it to work
def defSwitch(x):
    return {
        1 : toHadoop.write(True),
        2 : fromHadoop.read(True),
        3 : "Not hooked in yet",
        4 : 4
        }.get(x, "Command not found") 
        
userInput = 0;
menuOptions = [];
menuOptions.append("1. Run Hadoop writer");
menuOptions.append("2. Run Hadoop reader");
menuOptions.append("3. Run Facebook scrapper");
menuOptions.append("4. Exit");
menuText = ''.join(menuOptions);

while (userInput < 4):
    for index in range(len(menuOptions)):
        print menuOptions[index]
    userInput = input("Enter option: ");
    if (userInput < 4):
        #print (defSwitch(userInput));
        if (userInput == 1):
            toHadoop.write(True);
        if (userInput == 2):
            fromHadoop.read(True);
        if (userInput == 3):
            print ("Scrapping not hooked in yet.");

print ("Done");

    



#str1 = raw_input("Enter anything:")
#print "raw_input =", str1
# input() actually uses raw_input() and then tries to
# convert the input data to a number using eval()
# hence you could enter a math expression
# gives an error if input is not numeric eg. $34.95
#x = input("Enter a number:")
#print "input =", x

