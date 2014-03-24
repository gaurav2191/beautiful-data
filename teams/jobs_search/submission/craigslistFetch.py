# Suren Abrahamyan
from bs4 import BeautifulSoup, NavigableString
import urllib2
import time

"""
Crawler pseudo-code
--------------------------------------
procedure CRAWLER_THREAD (frontier)
    while not function.done() do
        webSite = frontier.nextSite()
        url = webSite.nextUrl()
        if (webSite.permitsCrawl(url))
            text = retrieveUrl(url)
            storeDocument(url, text)
            for each url in parse(text) do
                frontier.addUrl(url)
            end for
        end if
        frontier.releaseSite(webSite)
    end while
end procedure
--------------------------------------
"""


# the function removes all HTML tags leaving only plain text
def strip_all_tags(html_content):
    if html_content is None:
        return None
    return ''.join(BeautifulSoup(html_content).findAll(text=True))


def build_craigslist_city_link(city_name, job_link):

    if "http" in job_link:
        return job_link
    else:
        host_url = str("http://")
        end_url = str(".craigslist.org")
        full_url = host_url + str(city_name) + end_url + str(job_link)
        return full_url

# seed
baseUrl = "http://losangeles.craigslist.org/sof/"

# computer science base usr
craigListBaseUrl = "http://losangeles.craigslist.org"

# main seeds, job post pages with all links to the jobs, dynamically append more pages at runtime
frontierLinks = [baseUrl]

# since Craigslist only keeps 300/400 links in history, control the depth of pagination
depthOfPagination = 4
currentPagination = 0

# open files to operate in
outputFile = open("craigList.txt", "a+")
techListFile = open("techList.txt",'r')
techListArray = techListFile.read().split(':')

# main craigslist site
mainCraigslistSiteRoot = "http://www.craigslist.org/about/sites"

mainCraigslistSiteRootHtml = BeautifulSoup(urllib2.urlopen(mainCraigslistSiteRoot).read())
usCitiesDiv = mainCraigslistSiteRootHtml.findAll("div", {"class": "colmask"}, limit=1)
usCitiesDiv = BeautifulSoup(str(usCitiesDiv))('a')

# map that holds the city link as key and city name
cityLinkMapFrontier = {}

totalRecordCounter = 0

# fill the frontier map for the cities
for link in usCitiesDiv:
    href = unicode(link['href']).decode('ascii', 'ignore')
    title = unicode(link.string).decode('ascii', 'ignore')
    cityLinkMapFrontier.update({str(href) + str("/sof/"): str(title)})
    #print href

for cityLink in cityLinkMapFrontier:

    # grab the name of the city to be crawled
    cityName = unicode(cityLinkMapFrontier[cityLink]).decode('ascii', 'ignore').strip()
    cityName = str(cityName).strip().replace(" ", "")

    #print "1." + cityName
    #print "2." + cityLink
    frontierLinks = [cityLink]
   # print "3. "
    print frontierLinks

    # start looping over the frontier links
    for postPage in frontierLinks:

        print str(postPage) + str(" @ depth: ") + str(currentPagination)

        # pagination control, stop when the depth limit reached
        if currentPagination == depthOfPagination:
            # -- IMPORTANT--
            # here we have an opportunity to change the base url from losangeles.craigslist.org to some other city,
            # reset the currentPagination to 0, and crawl the other cities postings, or even have a list of cities
            currentPagination = 0
            break

        # open the seed url, and put inside BeautifulSoup for parsing

        try:
            postPageResponse = urllib2.urlopen(postPage)
        except urllib2.HTTPError, e:
            print e.code
            continue
        except urllib2.URLError, e:
            print e.args
            print "Unable to connect to " + str(fullJobLink)
            continue
        postPageHtml = postPageResponse.read()
        postPageBeautifulSoup = BeautifulSoup(postPageHtml)

        # jobsMap is a mpa that holds [link, jobTitle] as key value pair
        jobsMap = {}

        # loop through every link on the page
        for anchor in postPageBeautifulSoup('a'):
            # in Craigslist, next > contains a link to the next 100 pots, capture that next page link and put in frontier
            if unicode(anchor.string).strip() == "next >":
                if not frontierLinks.__contains__(str(postPage) + str(anchor["href"])):
                    print str("Adding Next Post Page to frontier @ ") + str(anchor["href"])
                    frontierLinks.append(str(postPage) + str(anchor["href"]))
                else:
                    print ("Continue @" + str(anchor["href"]))
                    continue

            # Get relevant links by parsing Craigslist job links.
            # conditions that need to be met:
            # 1. the link must contain href attribute that ends with '.html'
            # 2. the string content of the link must not be 'None'
            elif unicode(anchor['href']).find(".html") != -1 and unicode(anchor.string) != "None":
                # update the 'jobsMap' with link as the key, and the job title as the value
                #print "4." + anchor['href']
                jobsMap.update({unicode(anchor['href']): unicode(anchor.string)})


        print len(frontierLinks)
        print len(jobsMap)
        # use the throttle to work with small set of links at first, set to -1 to turn it off
        throttleLinkCount = -1
        counter = 0

        # loop through every job listing
        for jobLink in jobsMap:

            if throttleLinkCount == -1 or counter < throttleLinkCount:

                # build full job url by appending the relative href extracted from job links
                #fullJobLink = str(craigListBaseUrl) + str(jobLink)
                #fullJobLink = str(cityLink).strip() + str(jobLink)
                fullJobLink = build_craigslist_city_link(cityName, jobLink)

                print fullJobLink

                # put the job page into BeautifulSoup Soup for parsing
                # jobHtmlContent = BeautifulSoup(urllib2.urlopen(fullJobLink).read())

                try:
                    jobHtmlContent = BeautifulSoup(urllib2.urlopen(fullJobLink).read())
                except urllib2.HTTPError, e:
                    print e.code
                    continue
                except urllib2.URLError, e:
                    print e.args
                    print "Unable to connect to " + str(fullJobLink)
                    continue

                # extract 'body' class that contains all the job posting text
                bodyContent = jobHtmlContent.findAll("section", {"id": "postingbody"})

                # strip all HTML tags, leaving plain text
                stripedBodyContent = strip_all_tags(str(bodyContent))

                # convert the full text into array of text
                bodyContentArray = stripedBodyContent.split()

                # for keeping track of runtime
                start_time = time.time()

                # placeholder for all job tags that are found in the job post
                foundJobTags = set()

                # check for the job tags and compare to every piece of string in the job post
                for jobTag in techListArray:
                    for stringInPost in bodyContentArray:
                        # convert to lower case to avoid missing keywords that are spelled differently
                        if unicode(stringInPost).lower() == unicode(jobTag).lower():
                            foundJobTags.add(unicode(jobTag) + str(","))
                            #print jobTag

                # there are few listings that contains special character that cannot be parsed, thus try/catch to rescue
                try:
                    # grab the job title from the map
                    jobTitle = unicode(jobsMap[jobLink]).decode('ascii', 'ignore')
                except ValueError:
                    print "ERROR"
                    jobTitle = "n/a"

                # create a unique id for this job post, might be useful in the future when checking for duplicates
                jobId = hash(jobTitle)

                # extract the set of skill and separate by space into a string
                skills = ' '.join(foundJobTags).decode('ascii', 'ignore')

                totalRecordCounter += 1

                # build a job data that will go into the text file, remove the last comma of the skill set
                jobData = str(totalRecordCounter) + " ; " + str(jobId) + str(" ; ") + str(jobTitle) + str(" ; ") + \
                    str(fullJobLink) + str(" ; ") + str(skills).rstrip(",") + str("\n")

                # finally append the job posting data to the file
                outputFile.writelines(str(jobData))

                # track the runtime of every job posting scan
                #print time.time() - start_time, "seconds"

                # increment the throttle counter
                counter += 1

        currentPagination += 1

outputFile.close()
techListFile.close()
