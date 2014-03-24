import matplotlib.pyplot as plt
import numpy as np

def percentage(data):
        total = sum(data)
        print total
        return [each * 100 / float(total) for each in data]

def MaxCatagories():
    #read Categories
    readCat =  open('/Users/rodthungsudrung/Desktop/Categories.txt', 'r')
    allCat = []
    cat_name = []
    for row in readCat:
        catagories = []
        eachCat = row.strip().split(";") 
        cat_name.append(eachCat[0])
        eachSkill  = eachCat[1].split(":")
        for skill in eachSkill:
            catagories.append(skill)
        allCat.append(catagories)
    
    print len(allCat)
    print cat_name
    
    
    
    #raad skill
    readSkill =  open('/Users/rodthungsudrung/Desktop/CleanData.txt', 'r')
    
    count_cat = []
    #initialze count_cat
    for x in range(0,15):
        count_cat.insert(x,0)
    
    temp = count_cat[2]
    print temp
    
    for row in readSkill:
        each_row = row.strip().split(";")
        each_skill = each_row[2].split(",")
        each_skill = map(lambda x: x.strip(), each_skill)
        if "*" not in each_skill:
            for skill in each_skill:
                if skill != "Bachelor" or skill != "BA/BS":
                    for index,eachCat in enumerate(allCat):
                        if skill in eachCat:
                            count_cat[index] += 1
                            
    zipper = zip(cat_name,count_cat)
    b = sorted(zipper, key=lambda x:x[1], reverse=True)                                           
    
    new_name = []
    new_num = []
    for x in b:
        new_name.append(x[0])
        new_num.append(x[1])
        
    print new_name
    print new_num  
    
    plotPie(new_name[:5],new_num[:5])
    
     
def plotPie( name, data):
        # Data as percentage to fill in a pie chart
        #data = np.array(data).astype(np.float)
        
        percents = percentage(data)
        #fig = plt.figure()
    # Labels
        # Y = ['Y' + str(i) for i in xrange(1, len(percents))]
        # labels = ['X'] + Y

    # Random colors and explode at maximum value
        colors = [np.random.rand(3) for _ in xrange(0, len(percents))]
        #explode = tuple([0.1 if percents[i] == max(percents) else 0 for i in xrange(0, len(percents))])
        #plt.title("Teacnology Skills")
    # Plot
        plt.pie(percents, labels=name, colors=colors, autopct='%1.1f%%', shadow=True)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.show()
        #fig.savefig(title+'.png')  
           

def MaxArea():
    '''
    What state require most job in computer science ?
    Analyst : count the frequency 
    Display : Bar Chart
    '''
    read = open('/Users/rodthungsudrung/Desktop/CleanData.txt', 'r')
    
    location_list = []
    location_num = []
    index = 0
    for row in read:
        element = row.strip().split(";")
        if element[1] not in location_list:
            location_list.insert(index, element[1])
            location_num.insert(index, 1)
        else:
            temp = location_list.index(element[1])                                        
            location_num[temp] = location_num[temp] + 1
            
    zipper1 = zip(location_list,location_num)
    b = sorted(zipper1, key=lambda x:x[1], reverse=True)
    
    print b
    new_list = []
    new_num = []
    for e in b:
        new_list.append(e[0])
        new_num.append(e[1])  
        
    show_list = new_list[:11]
    show_number = new_num[:11]
    plotBar(show_list,show_number)


def MaxTag():
    
    '''
    What is the most popular required skill in computer science ? 
        Analyst : count the frequency 
        - Popular = the most appare skill tag in data
        Display : Bar Chart  
    '''   
    
    read = open('/Users/rodthungsudrung/Desktop/CleanData.txt', 'r')
    job = []
    location = []
    skill = [] 
    list_of_skill = []
    skill_number = []
    
    index = 0
    for row in read:
        element = row.strip().split(";")
        job.append(element[0]) #collect Job Title
        location.append(element[1]) #collect Location
        #skill 
        each_skill = element[2].strip().split(",")
        each_skill = map(lambda x: x.strip(), each_skill)
        if "*" not in each_skill:
            for skill in each_skill:
                if skill not in list_of_skill:
                    if skill != "Bachelor":
                        list_of_skill.insert(index,skill)
                        skill_number.insert(index, 1)
                        index = index + 1
                else:
                    temp = list_of_skill.index(skill)                                        
                    skill_number[temp] = skill_number[temp] + 1

    zipper1 = zip(list_of_skill,skill_number)
    b = sorted(zipper1, key=lambda x:x[1], reverse=True)
    
    #print list_of_skill
    
    print b
    new_list = []
    new_num = []
    for e in b:
        new_list.append(e[0])
        new_num.append(e[1])
    
   
    show_list = new_list[:11]
    show_number = new_num[:11]
    plotBar(show_list,show_number)
    
def plotBar(list_of_skill,skill_number):
    
    n_groups = len(list_of_skill)
    means_men = skill_number
    index = np.arange(n_groups)
    bar_width = 0.8
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    plt.bar(index + 0.4, means_men, bar_width,
                 alpha=opacity,
                 color='g',
                 error_kw=error_config)
    plt.xlabel('Skill')
    plt.ylabel('Job Frequency')
    #plt.title('Number of appeared tag')
    plt.xticks(index + bar_width, list_of_skill)
    plt.legend()

    plt.tight_layout()
    plt.show() 
    
if __name__ == '__main__':
    MaxTag()
    #MaxArea()
    #MaxCatagories()