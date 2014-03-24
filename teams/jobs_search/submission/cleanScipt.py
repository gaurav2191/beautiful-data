import csv


def cleanTXT():
    read = open('/Users/rodthungsudrung/Desktop/craigList2.txt', 'r')
    index = 0
    for row in read:
        index += 1
        each_row = row.strip().split(';');
        title = each_row[2]
        location = each_row[3][8:each_row[3].index(".")]
        skill = each_row[4]
        dataFile = open('/Users/rodthungsudrung/Desktop/CleanData.txt', 'a')
        if len(skill.strip()) == 0:
            dataFile.write(title.strip()+";"+location.strip()+";*\n" )
            dataFile.close()
        if len(skill.strip()) != 0:
            dataFile.write(title.strip()+";"+location.strip()+";"+skill.strip()+"\n" )
            dataFile.close()
        
       

def cleanCVS():
    with open('/Users/rodthungsudrung/Documents/workspace/Test.Python/job2.csv', 'rb') as f:
        read = csv.reader(f, delimiter=";")
        num = 0
        for row in read:
            num += 1
            if row[0].count("(") == 1:
                print str(num) +" ; "+ row[0][row[0].index("("):]
            if (row[0].count("(") > 1):
                if "allow" in row[0]:
                    print "***********************"
                    print str(num) +" ; "+row[0][row[0].index("("):row[0].index(")")+1]
                if "allow" not in row[0]:
                    index = 0;
                    high = 0;
                    while index < len(row[0]):
                        index = row[0].find("(",index)
                        if index == -1:
                            print str(num) +" ; "+row[0][high:]
                            break;
                        high = index
                        index += 1;
                

if __name__ == '__main__':
    cleanTXT();
    #cleanCVS();
    