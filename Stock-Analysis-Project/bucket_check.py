from pylab import plot,show

linecount = 0
sym = '';
y_l = '';
y_h = '';
c_p = '';
year_low = 1;
year_high = 1;
current_rate = 1;
rank5 = []
rank4 = []
rank3 = []
rank2 = []
rank1 = []

a = [1,2,3]
print a[2]
file = open('data_set_1/Company_Info_numbers.txt', 'r+')
for line in file:
    key_val = line.split('#')
    sym = sym + "#" + key_val[1].split(' ')[3]
    y_l = y_l + "#" + key_val[6].split(' ')[3]
    y_h = y_h + "#" + key_val[7].split(' ')[3]
    c_p = c_p + "#" + key_val[9].split(' ')[3]
    linecount = linecount + 1

sy = sym.split('#')
yl = y_l.split('#')
yh = y_h.split('#')
cp = c_p.split('#')

for i in range(1, linecount):
    symbol =  sy[i]
    year_low =  float(yl[i])
    year_high =  float(yh[i])
    current_rate =  float(cp[i])
    if current_rate == 0:
        current_rate = 1
    percent_down = year_low*100/current_rate
    percent_decrease = 100 - percent_down
    
    percent_high = year_high*100/current_rate
    percent_increase = percent_high - 100

    if(100 < percent_increase):
        suggestion = 'Never Purchase this'
        rank5.append(percent_increase)
    elif ( 25 < percent_increase < 100):
        suggestion = 'Not a good investment'
        rank4.append(percent_increase)

    elif (50 < percent_decrease):
        suggestion = 'Very Good to take'
        rank2.append(percent_decrease * -1)
    elif (10 < percent_decrease < 50):
        suggestion = 'Good to take'
        rank1.append(percent_decrease * -1)
    else:
        suggestion = 'Moderate kind'
        rank3.append(percent_increase - percent_decrease)


file.close()

plot(rank5[:],'ob',
     rank4[:],'or',
     rank3[:],'oy',
     rank2[:],'ok',
     rank1[:],'og',markersize=8)
show()