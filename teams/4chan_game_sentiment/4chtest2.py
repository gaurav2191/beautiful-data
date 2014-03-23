## all_threads.py
import sys
import fourch
import json
import csv

def main():
    if len(sys.argv) is not 3:
        print "usage: python {0} <board> <page>".format(sys.argv[0])
        return

    
    #unicodeData.encode('ascii', 'ignore')
    #sys.stdout.encoding='utf-8'
    data = " "
    thread_url = []
    thread_op = []
    page_number=int(sys.argv[2])
    str = " "
    b = fourch.board(sys.argv[1])
    #view = b.page(0)
	
    for page_number in range (0, 10):
	thr = b.page(page_number)
    	for t in thr:
	    print page_number
	    print t.op.now.encode('utf-8')
	    print t.op.url.encode('utf-8')
            print t.op.comment_text.encode(sys.getdefaultencoding(), 'replace')
	    print "\n"
	    print "-------------------------------------"
	    str = str + t.op.now.encode('utf-8') + "\n" + t.op.url.encode('utf-8') + "\n" + t.op.comment_text.encode('utf-8')  + "\n"
            thread_url.append(t.op.url.encode('utf-8'))
            thread_op.append(t.op.comment_text.encode('utf-8'))
	    with open('mymy.txt', 'w') as myFile:
	      	    myFile.write(str)
	page_number = page_number + 1

    with open('mymy.json', 'w') as outfile:
		json.dump(str, outfile)
		
    c = csv.writer(open("MYFILE.csv", "wb"))
    c.writerow(["Thread URL","Thread OP"])
    for row in zip(thread_url, thread_op):
    		c.writerow(row)

if __name__ == "__main__":
    main()
