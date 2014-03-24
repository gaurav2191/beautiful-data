from lxml import etree
import csv
import sys

##### How to run #####
#>python soCollect.py xml_file_name
# 
#Example
#>python soCollect.py 'big data.xml'
#######################

def scrapXML(xml_input_file, csv_output_file):
	with open(csv_output_file,'w') as fout:
		writer = csv.writer(fout, delimiter=';', quoting=csv.QUOTE_ALL)
		for _, element in etree.iterparse(xml_input_file, tag='item'):
			data = [element.findtext('title').encode("utf8"),
					element.findtext('link').encode("utf8"),
					element.findtext('pubDate').encode("utf8"),
					element.findtext('a10:updated',  namespaces={'a10':'http://www.w3.org/2005/Atom'}).encode('utf8'),
					' '.join([item.text for item in element.findall('category')]),]
			writer.writerow(data)
			element.clear()
		fout.close()			

if __name__ == '__main__':
	cmdargs = sys.argv
	xml_input_file = cmdargs[1]
	csv_output_file = xml_input_file.split('.')[0] + '.csv'
	print xml_input_file, csv_output_file
	scrapXML(xml_input_file, csv_output_file)