
from bs4 import BeautifulSoup
import urllib2
import re
import string

def replace_word(infile,old_word,new_word):
    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)

m_score_list, final_score = [], []
open('metacritic_score_list.txt', 'w').close()
fn = open("game_list")
del m_score_list[:]
for line in fn:
    url = "http://www.metacritic.com/game/xbox-360/"+line
    print url
    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
        
    # Get Name
    result = soup.find('span',{'itemprop':'name'})
    for r in result:
        if (r.string is None):
            r.string = ' '
    a = result.get_text()
    new_name = a.strip()
    
        
    # Get Release Date
    result = soup.find('span',{'itemprop':'datePublished'})
    for r in result:
        if (r.string is None):
            r.string = ' '
    b = result.get_text()
    datePublished = b.strip()
        
    # Get Meta Score
    result = soup.find('span',{'itemprop':'ratingValue'})
    for r in result:
        if (r.string is None):
            r.string = ' '
    c = result.get_text()
    ratingValue = c.strip()
    
    for div in soup.findAll('a',attrs={'class':'metascore_anchor'}):
        if div.find('div',attrs={'class':'metascore_w user large game positive'}):
            for rr in div:
                print rr
                if (rr.string is None):
                    rr.string = ' '
            d = div.get_text()
            metascore = d.strip()
            m_score_list = [str(new_name),str(datePublished), str(ratingValue), str(metascore)]
        elif div.find('div',attrs={'class':'metascore_w user large game negative'}):
            for rr in div:
                print rr
                if (rr.string is None):
                    rr.string = ' '
            d = div.get_text()
            metascore = d.strip()
            m_score_list = [str(new_name),str(datePublished), str(ratingValue), str(metascore)]
        elif div.find('div',attrs={'class':'metascore_w user large game mixed'}):
            for rr in div:
                print rr
                if (rr.string is None):
                    rr.string = ' '
            d = div.get_text()
            metascore = d.strip()
            m_score_list = [str(new_name),str(datePublished), str(ratingValue), str(metascore)]
            
    final_score.append(m_score_list)
with open('metacritic_score_list.txt', 'w') as file:
    file.write(str(final_score))
    
replace_word('metacritic_score_list.txt', '], [','\n')
replace_word('metacritic_score_list.txt', '[','')
replace_word('metacritic_score_list.txt', ']','')      
replace_word('metacritic_score_list.txt', ',','')
replace_word('metacritic_score_list.txt', ' ','_')
replace_word('metacritic_score_list.txt', chr(34),chr(39)) 
replace_word('metacritic_score_list.txt', chr(39)+'_'+chr(39),' ') 
replace_word('metacritic_score_list.txt', '__','_') 
replace_word('metacritic_score_list.txt', chr(39),'')

