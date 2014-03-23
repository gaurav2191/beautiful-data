## images.py
import sys
import fourch

def main():
    # Display usage and help if they've mucked up.
    if len(sys.argv) is not 3:
        print "usage: python {0} <board> <thread>".format(sys.argv[0])
        return
	
    str = " "	
    b = fourch.board(sys.argv[1])
    t = b.thread(sys.argv[2])
    for i in t.replies:
        str = str + i.comment_text.encode(sys.getdefaultencoding(), 'replace')
	print i.comment_text.encode(sys.getdefaultencoding(), 'replace')	
	with open('data20.txt', 'w') as myFile:
		myFile.write(str)

if __name__ == "__main__":
    main()
