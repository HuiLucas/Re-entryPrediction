kp_indeces = open('SW-kp-indeces.txt', 'r')
SW_F10_predicted = open('SW-F10-predicted.txt', 'r')
import numpy as np


class observed_data:
    def __init__(self):
        self.kp = [0,0,0,0,0,0,0,0]
        self.sum = 0
        self.Ap = [0,0,0,0,0,0,0,0]
        self.avg = 0
        self.cp = 0
        self.c9 = 0
        self.ISN = 0
        self.F10_7_adj = 0
        self.Q = 0
        self.ctr81_adj = 0
        self.lst81_adj = 0
        self.F10_7_obs = 0
        self.ctr81_obs = 0
        self.lst81_obs = 0
class daily_predicted_data:
    def __init__(self):
        self.kp = [0,0,0,0,0,0,0,0]
        self.sum = 0
        self.Ap = [0,0,0,0,0,0,0,0]
        self.avg = 0
        self.cp = 0
        self.c9 = 0
        self.ISN = 0
        self.F10_7_adj = 0
        self.Q = ""
        self.ctr81_adj = 0
        self.lst81_adj = 0
        self.F10_7_obs = 0
        self.ctr81_obs = 0
        self.lst81_obs = 0

class monthly_predicted_data:
    def __init__(self):
        self.ISN = 0
        self.F10_7_adj = 0
        self.Q = ""
        self.ctr81_adj = 0
        self.lst81_adj = 0
        self.F10_7_obs = 0
        self.ctr81_obs = 0
        self.lst81_obs = 0

observed_data_list = [observed_data() for i in range(0, 23719)]

daily_predicted_data_list = [daily_predicted_data() for i in range(0, 45)]

monthly_predicted_data_list = [monthly_predicted_data() for i in range(0, 209)]

observed_data_list[0].kp = [0,0,0,0,0,0,0,0]

q = 237  #change for the number of lines in the file

############ Kp #############################################
lines = kp_indeces.readlines()
last_15_chars_list = []
for line in lines[2:q+3]:      #23719 +3 for right range
    last_15_chars = line[-17:].strip()
    last_15_chars_list.append(last_15_chars)
    seperate_row = []
    for item in last_15_chars_list:
        new_row = [item[i:i+2] for i in range(0, len(item), 2)]
        seperate_row.append(new_row)

    
    for row in seperate_row:
        for i in range(len(row)):
            row[i] = row[i].replace("o", "0")
            row[i] = row[i].replace("+", "3")
            row[i] = row[i].replace("4-", "37")
            row[i] = row[i].replace("5-", "47")
            row[i] = row[i].replace("6-", "57")
            row[i] = row[i].replace("7-", "67")
            row[i] = row[i].replace("8-", "77")
            row[i] = row[i].replace("9-", "87")
            row[i] = row[i].replace("2-", "17")
            row[i] = row[i].replace("3-", "27")
            row[i] = row[i].replace("1-", "7")
    
    for row in seperate_row:
        for i in range(len(row)):
            row[i] = int(row[i])

for i in range(0, q):         #23719
    observed_data_list[i].kp = seperate_row[i]
#print(seperate_row[0])
#print (last_15_chars_list[0])


############ Ap #############################################

observed_data_list[0].Ap = [0,0,0,0,0,0,0,0]

#print(last_15_chars_list[0:2])

seperate_AP = []
for item in last_15_chars_list:
        new_row = [item[i:i+2] for i in range(0, len(item), 2)]
        seperate_AP.append(new_row)
#print (seperate_AP[0:3])

for row in seperate_AP:
    for i in range(len(row)):
        row[i] = row[i].replace("0o", "0")
        row[i] = row[i].replace("0+", "2")
        row[i] = row[i].replace("1-", "3")
        row[i] = row[i].replace("1o", "4")
        row[i] = row[i].replace("1+", "5")
        row[i] = row[i].replace("2-", "6")
        row[i] = row[i].replace("2o", "7")
        row[i] = row[i].replace("2+", "9")
        row[i] = row[i].replace("3-", "12")
        row[i] = row[i].replace("3o", "15")
        row[i] = row[i].replace("3+", "18")
        row[i] = row[i].replace("4-", "22")
        row[i] = row[i].replace("4o", "27")
        row[i] = row[i].replace("4+", "32")
        row[i] = row[i].replace("5-", "39")
        row[i] = row[i].replace("5o", "48")
        row[i] = row[i].replace("5+", "56")
        row[i] = row[i].replace("6-", "67")
        row[i] = row[i].replace("6o", "80")
        row[i] = row[i].replace("6+", "94")
        row[i] = row[i].replace("7-", "111")
        row[i] = row[i].replace("7o", "132")
        row[i] = row[i].replace("7+", "154")
        row[i] = row[i].replace("8-", "179")
        row[i] = row[i].replace("8o", "207")
        row[i] = row[i].replace("8+", "236")
        row[i] = row[i].replace("9-", "300")
        row[i] = row[i].replace("9o", "400")
        row[i] = row[i].replace("9+", "500")
  
for row in seperate_AP:
    # print(row)
    for i in range(len(row)):
        row[i] = int(row[i])

#print(seperate_AP[0:3])
#print(len(seperate_AP))
for i in range(0, q):      #23719
    observed_data_list[i].Ap = seperate_AP[i]

#print (observed_data_list[5].kp)
#print (observed_data_list[5].Ap)
#print (seperate_row[0])
#sprint (last_15_chars_list[0])

############ SUM #############################################

for i in range(0, q):      #23719
    observed_data_list[i].sum = sum(observed_data_list[i].kp)

#print (observed_data_list[5].sum)

############ AVG #############################################

for i in range(0, q):     #23719 
    observed_data_list[i].avg = np.mean(observed_data_list[i].Ap)

#print(observed_data_list[5].Ap)
#print (observed_data_list[5].avg)

############ CP #############################################

average_Ap = []
for i in range(0, q):      #23719
    average_Ap.append(np.sum(observed_data_list[i].Ap))

#print(observed_data_list[0].Ap,observed_data_list[1].Ap,observed_data_list[2].Ap,observed_data_list[3].Ap,observed_data_list[4].Ap)
#print (average_Ap[5])

for i in range(len(average_Ap)):
        
        if 0 <= average_Ap[i] <= 22:
            average_Ap[i] = 0.0
        elif 23 <= average_Ap[i] <= 34:
            average_Ap[i] = 0.1
        elif 35 <= average_Ap[i] <= 44: 
            average_Ap[i] = 0.2
        elif 45 <= average_Ap[i] <= 55:
            average_Ap[i] = 0.3
        elif 56 <= average_Ap[i] <= 66:
            average_Ap[i] = 0.4
        elif 67 <= average_Ap[i] <= 78:
            average_Ap[i] = 0.5
        elif 79 <= average_Ap[i] <= 90:
            average_Ap[i] = 0.6
        elif 91 <= average_Ap[i] <= 104:
            average_Ap[i] = 0.7
        elif 105 <= average_Ap[i] <= 120:
            average_Ap[i] = 0.8
        elif 121 <= average_Ap[i] <= 139:
            average_Ap[i] = 0.9
        elif 140 <= average_Ap[i] <= 164:
            average_Ap[i] = 1.0
        elif 165 <= average_Ap[i] <= 190:
            average_Ap[i] = 1.1
        elif 191 <= average_Ap[i] <= 228:
            average_Ap[i] = 1.2
        elif 229 <= average_Ap[i] <= 273:
            average_Ap[i] = 1.3
        elif 274 <= average_Ap[i] <= 320:
            average_Ap[i] = 1.4
        elif 321 <= average_Ap[i] <= 379:
            average_Ap[i] = 1.5
        elif 380 <= average_Ap[i] <= 453:
            average_Ap[i] = 1.6
        elif 454 <= average_Ap[i] <= 561:
            average_Ap[i] = 1.7



for i in range(0, q):      #23719
    observed_data_list[i].cp = average_Ap[i]

############ C9 ############################################

for i in range(0, q):      #23719
    if 0.0 <= observed_data_list[i].cp <= 0.1:
        observed_data_list[i].c9 = 0
    if 0.2 <= observed_data_list[i].cp <= 0.3:
        observed_data_list[i].c9 = 1
    if 0.4 <= observed_data_list[i].cp <= 0.5:
        observed_data_list[i].c9 = 2
    if 0.6 <= observed_data_list[i].cp <= 0.7:
        observed_data_list[i].c9 = 3
    if 0.8 <= observed_data_list[i].cp <= 0.9:
        observed_data_list[i].c9 = 4
    if 1.0 <= observed_data_list[i].cp <= 1.1:
        observed_data_list[i].c9 = 5
    if 1.2 <= observed_data_list[i].cp <= 1.4:
        observed_data_list[i].c9 = 6
    if 1.5 <= observed_data_list[i].cp <= 1.8:
        observed_data_list[i].c9 = 7
    if observed_data_list[i].cp == 1.9:
        observed_data_list[i].c9 = 8
    if 2.0 <= observed_data_list[i].cp <= 2.5:
        observed_data_list[i].c9 = 9

sum_Ap = []
for i in range(0, q):      #23719
    sum_Ap.append(np.sum(observed_data_list[i].Ap))

#k = 236
#print(f'sum={sum_Ap[k]}, cp={observed_data_list[k].cp},c9={observed_data_list[k].c9}')


######################### F10.7 ########################################
lines2 = kp_indeces.readlines()
f107_list = []
for i in range(186, 23904):
    f107 = list(lines2[i])[10:13]
    for i in range(len(f107)):
        f107[i] = int(f107[i])
    f107num = f107[0]*100 + f107[1]*10 + f107[2]    
    f107_list.append(f107num)

print(f107_list[0:10])

# Open the file for reading and writing
with open('SW-NEW.txt', 'r+') as file:
    # Read the contents of the file
    lines = file.readlines()
    # Iterate over each line
    dum=0
    removalarray = []
    for i, line in enumerate(lines):
        # Check if the line has at least 46 characters
        if i >= 17 and i <= 17+23718:
            #print(line)
            linelist = list(line)
            j=i-17
            nostring = " "
            linelist[19:21] = [f"{observed_data_list[j].kp[0]//10 if observed_data_list[j].kp[0]//10 !=0 else nostring}", f"{observed_data_list[j].kp[0]%10}"]
            linelist[22:24] = [f"{observed_data_list[j].kp[1]//10  if observed_data_list[j].kp[1]//10 !=0 else nostring}", f"{observed_data_list[j].kp[1]%10}"]
            linelist[25:27] = [f"{observed_data_list[j].kp[2]//10  if observed_data_list[j].kp[2]//10 !=0 else nostring}", f"{observed_data_list[j].kp[2]%10}"]
            linelist[28:30] = [f"{observed_data_list[j].kp[3]//10  if observed_data_list[j].kp[3]//10 !=0 else nostring}", f"{observed_data_list[j].kp[3]%10}"]
            linelist[31:33] = [f"{observed_data_list[j].kp[4]//10  if observed_data_list[j].kp[4]//10 !=0 else nostring}", f"{observed_data_list[j].kp[4]%10}"]
            linelist[34:36] = [f"{observed_data_list[j].kp[5]//10  if observed_data_list[j].kp[5]//10 !=0 else nostring}", f"{observed_data_list[j].kp[5]%10}"]
            linelist[37:39] = [f"{observed_data_list[j].kp[6]//10  if observed_data_list[j].kp[6]//10 !=0 else nostring}", f"{observed_data_list[j].kp[6]%10}"]
            linelist[40:42] = [f"{observed_data_list[j].kp[7]//10  if observed_data_list[j].kp[7]//10 !=0 else nostring}", f"{observed_data_list[j].kp[7]%10}"]
            linelist[43:46] = [f"{(observed_data_list[j].sum)//100 if observed_data_list[j].sum//100 !=0 else nostring}", f"{(observed_data_list[j].sum)%100//10 if (observed_data_list[j].sum)%100//10 !=0 else nostring}", f"{(observed_data_list[j].sum)%10}"]
            linelist[47:50] = [f"{observed_data_list[j].Ap[0]//100 if observed_data_list[j].Ap[0]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[0])%100//10 if (observed_data_list[j].Ap[0])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[0]%10}"]
            linelist[51:54] = [f"{observed_data_list[j].Ap[1]//100 if observed_data_list[j].Ap[1]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[1])%100//10 if (observed_data_list[j].Ap[1])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[1]%10}"]
            linelist[55:58] = [f"{observed_data_list[j].Ap[2]//100 if observed_data_list[j].Ap[2]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[2])%100//10 if (observed_data_list[j].Ap[2])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[2]%10}"]
            linelist[59:62] = [f"{observed_data_list[j].Ap[3]//100 if observed_data_list[j].Ap[3]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[3])%100//10 if (observed_data_list[j].Ap[3])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[3]%10}"]
            linelist[63:66] = [f"{observed_data_list[j].Ap[4]//100 if observed_data_list[j].Ap[4]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[4])%100//10 if (observed_data_list[j].Ap[4])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[4]%10}"]
            linelist[67:70] = [f"{observed_data_list[j].Ap[5]//100 if observed_data_list[j].Ap[5]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[5])%100//10 if (observed_data_list[j].Ap[5])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[5]%10}"]
            linelist[71:74] = [f"{observed_data_list[j].Ap[6]//100 if observed_data_list[j].Ap[6]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[6])%100//10 if (observed_data_list[j].Ap[6])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[6]%10}"]
            linelist[75:78] = [f"{observed_data_list[j].Ap[7]//100 if observed_data_list[j].Ap[7]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[7])%100//10 if (observed_data_list[j].Ap[7])%100//10 !=0 else nostring}", f"{observed_data_list[j].Ap[7]%10}"]
            linelist[79:82] = [f"{observed_data_list[j].avg//100 if observed_data_list[j].avg//100 !=0 else nostring}", f"{observed_data_list[j].avg%100//10 if observed_data_list[j].avg%100//10 !=0 else nostring}", f"{observed_data_list[j].avg%10}" ]
            linelist[83:86] = [f"{observed_data_list[j].cp//1}",".", f"{np.round(observed_data_list[j].cp-observed_data_list[j].cp-int(observed_data_list[j].cp), decimals=1)}"]
            linelist[87] = f"{observed_data_list[j].c9//1}"
            linelist[89:92] = [f"{observed_data_list[j].ISN//100 if observed_data_list[j].ISN//100 !=0 else nostring}", f"{observed_data_list[j].ISN%100//10 if (observed_data_list[j].ISN)%100//10 !=0 else nostring}", f"{(observed_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{observed_data_list[j].F10_7_adj//100 if observed_data_list[j].F10_7_adj//100 !=0 else nostring}", f"{observed_data_list[j].F10_7_adj%100//10 if (observed_data_list[j].F10_7_adj)%100//10 !=0 else nostring}", f"{(observed_data_list[j].F10_7_adj)%10}",".", f"{np.round(observed_data_list[j].F10_7_adj-int(observed_data_list[j].F10_7_adj), decimals=1)}"]
            linelist[99] = f"{observed_data_list[j].Q//1 if type(observed_data_list[j].Q) == int else nostring}"
            linelist[101:106] = [f"{observed_data_list[j].ctr81_adj//100 if observed_data_list[j].ctr81_adj//100 !=0 else nostring}", f"{observed_data_list[j].ctr81_adj%100//10 if (observed_data_list[j].ctr81_adj)%100//10 !=0 else nostring}", f"{(observed_data_list[j].ctr81_adj)%10}",".", f"{np.round(observed_data_list[j].ctr81_adj-int(observed_data_list[j].ctr81_adj), decimals=1)}"]
            linelist[107:112] = [f"{observed_data_list[j].lst81_adj//100 if observed_data_list[j].lst81_adj//100 !=0 else nostring}", f"{observed_data_list[j].lst81_adj%100//10 if (observed_data_list[j].lst81_adj)%100//10 !=0 else nostring}", f"{(observed_data_list[j].lst81_adj)%10}",".", f"{np.round(observed_data_list[j].lst81_adj-int(observed_data_list[j].lst81_adj), decimals=1)}"]
            linelist[113:118] = [f"{observed_data_list[j].F10_7_obs//100 if observed_data_list[j].F10_7_obs//100 !=0 else nostring}", f"{observed_data_list[j].F10_7_obs%100//10 if (observed_data_list[j].F10_7_obs)%100//10 !=0 else nostring}", f"{(observed_data_list[j].F10_7_obs)%10}",".", f"{np.round(observed_data_list[j].F10_7_obs-int(observed_data_list[j].F10_7_obs), decimals=1)}"]
            linelist[119:124] = [f"{observed_data_list[j].ctr81_obs//100 if observed_data_list[j].ctr81_obs//100 !=0 else nostring}", f"{observed_data_list[j].ctr81_obs%100//10 if (observed_data_list[j].ctr81_obs)%100//10 !=0 else nostring}", f"{(observed_data_list[j].ctr81_obs)%10}",".", f"{np.round(observed_data_list[j].ctr81_obs-int(observed_data_list[j].ctr81_obs), decimals=1)}"]
            linelist[125:130] = [f"{observed_data_list[j].lst81_obs//100 if observed_data_list[j].lst81_obs//100 !=0 else nostring}", f"{observed_data_list[j].lst81_obs%100//10 if (observed_data_list[j].lst81_obs)%100//10 !=0 else nostring}", f"{(observed_data_list[j].lst81_obs)%10}",".", f"{np.round(observed_data_list[j].lst81_obs-int(observed_data_list[j].lst81_obs), decimals=1)}"]
            line = ''.join(linelist)
            

            # Update the line in the list of lines
            lines[i] = line
        
        if i>17+23719 and dum==0:
            if list(lines[i]) != ['E', 'N', 'D', ' ', 'O', 'B', 'S', 'E', 'R', 'V', 'E', 'D', '\n']:
                removalarray.append(i-1)
            else:
                removalarray.append(i-1)
                dum=1
    # Move the file pointer to the beginning of the file
    #print(removalarray)
    
    
    for i in sorted(removalarray, reverse=True):
        del lines[i]

    dum2=0
    count1=0
    dum3=0
    #print(list(lines[23739]))
    j=0
    for i, line in enumerate(lines):
        #print(count1)
        if dum2==0:
            if list(line) == ['B', 'E', 'G', 'I', 'N', ' ', 'D', 'A', 'I', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
                dum2=1
                count1=i
        elif list(line) == ['E', 'N', 'D', ' ', 'D', 'A', 'I', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
            dum3=1
        if i > count1  and dum3==0 and dum2==1:
            #print(line)
            linelist = list(line)
            nostring = " "
            #print(linelist[19:21], [f"{daily_predicted_data_list[j].kp[0]//10 if daily_predicted_data_list[j].kp[0]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[0]%10}"])
            linelist[19:21] = [f"{daily_predicted_data_list[j].kp[0]//10 if daily_predicted_data_list[j].kp[0]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[0]%10}"]
            linelist[22:24] = [f"{daily_predicted_data_list[j].kp[1]//10  if daily_predicted_data_list[j].kp[1]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[1]%10}"]
            linelist[25:27] = [f"{daily_predicted_data_list[j].kp[2]//10  if daily_predicted_data_list[j].kp[2]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[2]%10}"]
            linelist[28:30] = [f"{daily_predicted_data_list[j].kp[3]//10  if daily_predicted_data_list[j].kp[3]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[3]%10}"]
            linelist[31:33] = [f"{daily_predicted_data_list[j].kp[4]//10  if daily_predicted_data_list[j].kp[4]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[4]%10}"]
            linelist[34:36] = [f"{daily_predicted_data_list[j].kp[5]//10  if daily_predicted_data_list[j].kp[5]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[5]%10}"]
            linelist[37:39] = [f"{daily_predicted_data_list[j].kp[6]//10  if daily_predicted_data_list[j].kp[6]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[6]%10}"]
            linelist[40:42] = [f"{daily_predicted_data_list[j].kp[7]//10  if daily_predicted_data_list[j].kp[7]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[7]%10}"]
            linelist[43:46] = [f"{(daily_predicted_data_list[j].sum)//100 if daily_predicted_data_list[j].sum//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%100//10 if (daily_predicted_data_list[j].sum)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%10}"]
            linelist[47:50] = [f"{daily_predicted_data_list[j].Ap[0]//100 if daily_predicted_data_list[j].Ap[0]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[0])%100//10 if (daily_predicted_data_list[j].Ap[0])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[0]%10}"]
            linelist[51:54] = [f"{daily_predicted_data_list[j].Ap[1]//100 if daily_predicted_data_list[j].Ap[1]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[1])%100//10 if (daily_predicted_data_list[j].Ap[1])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[1]%10}"]
            linelist[55:58] = [f"{daily_predicted_data_list[j].Ap[2]//100 if daily_predicted_data_list[j].Ap[2]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[2])%100//10 if (daily_predicted_data_list[j].Ap[2])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[2]%10}"]
            linelist[59:62] = [f"{daily_predicted_data_list[j].Ap[3]//100 if daily_predicted_data_list[j].Ap[3]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[3])%100//10 if (daily_predicted_data_list[j].Ap[3])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[3]%10}"]
            linelist[63:66] = [f"{daily_predicted_data_list[j].Ap[4]//100 if daily_predicted_data_list[j].Ap[4]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[4])%100//10 if (daily_predicted_data_list[j].Ap[4])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[4]%10}"]
            linelist[67:70] = [f"{daily_predicted_data_list[j].Ap[5]//100 if daily_predicted_data_list[j].Ap[5]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[5])%100//10 if (daily_predicted_data_list[j].Ap[5])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[5]%10}"]
            linelist[71:74] = [f"{daily_predicted_data_list[j].Ap[6]//100 if daily_predicted_data_list[j].Ap[6]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[6])%100//10 if (daily_predicted_data_list[j].Ap[6])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[6]%10}"]
            linelist[75:78] = [f"{daily_predicted_data_list[j].Ap[7]//100 if daily_predicted_data_list[j].Ap[7]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[7])%100//10 if (daily_predicted_data_list[j].Ap[7])%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].Ap[7]%10}"]
            linelist[79:82] = [f"{daily_predicted_data_list[j].avg//100 if daily_predicted_data_list[j].avg//100 !=0 else nostring}", f"{daily_predicted_data_list[j].avg%100//10 if daily_predicted_data_list[j].avg%100//10 !=0 else nostring}", f"{daily_predicted_data_list[j].avg%10}" ]
            linelist[83:86] = [f"{daily_predicted_data_list[j].cp//1}",".", f"{np.round(daily_predicted_data_list[j].cp-daily_predicted_data_list[j].cp-int(daily_predicted_data_list[j].cp), decimals=1)}"]
            linelist[87] = f"{daily_predicted_data_list[j].c9//1}"
            linelist[89:92] = [f"{daily_predicted_data_list[j].ISN//100 if daily_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{daily_predicted_data_list[j].ISN%100//10 if (daily_predicted_data_list[j].ISN)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{daily_predicted_data_list[j].F10_7_adj//100 if daily_predicted_data_list[j].F10_7_adj//100 !=0 else nostring}", f"{daily_predicted_data_list[j].F10_7_adj%100//10 if (daily_predicted_data_list[j].F10_7_adj)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].F10_7_adj)%10}",".", f"{np.round(daily_predicted_data_list[j].F10_7_adj-int(daily_predicted_data_list[j].F10_7_adj), decimals=1)}"]
            linelist[99] = f"{daily_predicted_data_list[j].Q//1 if type(daily_predicted_data_list[j].Q) == int else nostring}"
            linelist[101:106] = [f"{daily_predicted_data_list[j].ctr81_adj//100 if daily_predicted_data_list[j].ctr81_adj//100 !=0 else nostring}", f"{daily_predicted_data_list[j].ctr81_adj%100//10 if (daily_predicted_data_list[j].ctr81_adj)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].ctr81_adj)%10}",".", f"{np.round(daily_predicted_data_list[j].ctr81_adj-int(daily_predicted_data_list[j].ctr81_adj), decimals=1)}"]
            linelist[107:112] = [f"{daily_predicted_data_list[j].lst81_adj//100 if daily_predicted_data_list[j].lst81_adj//100 !=0 else nostring}", f"{daily_predicted_data_list[j].lst81_adj%100//10 if (daily_predicted_data_list[j].lst81_adj)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].lst81_adj)%10}",".", f"{np.round(daily_predicted_data_list[j].lst81_adj-int(daily_predicted_data_list[j].lst81_adj), decimals=1)}"]
            linelist[113:118] = [f"{daily_predicted_data_list[j].F10_7_obs//100 if daily_predicted_data_list[j].F10_7_obs//100 !=0 else nostring}", f"{daily_predicted_data_list[j].F10_7_obs%100//10 if (daily_predicted_data_list[j].F10_7_obs)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].F10_7_obs)%10}",".", f"{np.round(daily_predicted_data_list[j].F10_7_obs-int(daily_predicted_data_list[j].F10_7_obs), decimals=1)}"]
            linelist[119:124] = [f"{daily_predicted_data_list[j].ctr81_obs//100 if daily_predicted_data_list[j].ctr81_obs//100 !=0 else nostring}", f"{daily_predicted_data_list[j].ctr81_obs%100//10 if (daily_predicted_data_list[j].ctr81_obs)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].ctr81_obs)%10}",".", f"{np.round(daily_predicted_data_list[j].ctr81_obs-int(daily_predicted_data_list[j].ctr81_obs), decimals=1)}"]
            linelist[125:130] = [f"{daily_predicted_data_list[j].lst81_obs//100 if daily_predicted_data_list[j].lst81_obs//100 !=0 else nostring}", f"{daily_predicted_data_list[j].lst81_obs%100//10 if (daily_predicted_data_list[j].lst81_obs)%100//10 !=0 else nostring}", f"{(daily_predicted_data_list[j].lst81_obs)%10}",".", f"{np.round(daily_predicted_data_list[j].lst81_obs-int(daily_predicted_data_list[j].lst81_obs), decimals=1)}"]
            line = ''.join(linelist)
            j+=1
            

            # Update the line in the list of lines
            lines[i] = line

    print(lines[23734:23742])
    

    dum4=0
    count3=0
    dum5=0
    j=0
    for i, line in enumerate(lines):
        if dum4==0:
            if list(line) == ['B', 'E', 'G', 'I', 'N', ' ', 'M', 'O', 'N', 'T', 'H', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
                dum4=1
                count3=i
        elif list(line) == ['E', 'N', 'D', ' ', 'M', 'O', 'N', 'T', 'H', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
            dum5=1
        if i > count3  and dum5==0 and dum4==1:
            linelist = list(line)
            nostring = " "
            linelist[89:92] = [f"{monthly_predicted_data_list[j].ISN//100 if monthly_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].ISN%100//10 if (monthly_predicted_data_list[j].ISN)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{monthly_predicted_data_list[j].F10_7_adj//100 if monthly_predicted_data_list[j].F10_7_adj//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].F10_7_adj%100//10 if (monthly_predicted_data_list[j].F10_7_adj)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].F10_7_adj)%10}",".", f"{np.round(monthly_predicted_data_list[j].F10_7_adj-int(monthly_predicted_data_list[j].F10_7_adj), decimals=1)}"]
            #linelist[99] = f"{daily_predicted_data_list[j].Q//1 if type(daily_predicted_data_list[j].Q) == int else nostring}"
            linelist[101:106] = [f"{monthly_predicted_data_list[j].ctr81_adj//100 if monthly_predicted_data_list[j].ctr81_adj//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].ctr81_adj%100//10 if (monthly_predicted_data_list[j].ctr81_adj)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].ctr81_adj)%10}",".", f"{np.round(monthly_predicted_data_list[j].ctr81_adj-int(monthly_predicted_data_list[j].ctr81_adj), decimals=1)}"]
            linelist[107:112] = [f"{monthly_predicted_data_list[j].lst81_adj//100 if monthly_predicted_data_list[j].lst81_adj//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].lst81_adj%100//10 if (monthly_predicted_data_list[j].lst81_adj)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].lst81_adj)%10}",".", f"{np.round(monthly_predicted_data_list[j].lst81_adj-int(monthly_predicted_data_list[j].lst81_adj), decimals=1)}"]
            linelist[113:118] = [f"{monthly_predicted_data_list[j].F10_7_obs//100 if monthly_predicted_data_list[j].F10_7_obs//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].F10_7_obs%100//10 if (monthly_predicted_data_list[j].F10_7_obs)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].F10_7_obs)%10}",".", f"{np.round(monthly_predicted_data_list[j].F10_7_obs-int(monthly_predicted_data_list[j].F10_7_obs), decimals=1)}"]
            linelist[119:124] = [f"{monthly_predicted_data_list[j].ctr81_obs//100 if monthly_predicted_data_list[j].ctr81_obs//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].ctr81_obs%100//10 if (monthly_predicted_data_list[j].ctr81_obs)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].ctr81_obs)%10}",".", f"{np.round(monthly_predicted_data_list[j].ctr81_obs-int(monthly_predicted_data_list[j].ctr81_obs), decimals=1)}"]
            linelist[125:130] = [f"{monthly_predicted_data_list[j].lst81_obs//100 if monthly_predicted_data_list[j].lst81_obs//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].lst81_obs%100//10 if (monthly_predicted_data_list[j].lst81_obs)%100//10 !=0 else nostring}", f"{(monthly_predicted_data_list[j].lst81_obs)%10}",".", f"{np.round(monthly_predicted_data_list[j].lst81_obs-int(monthly_predicted_data_list[j].lst81_obs), decimals=1)}"]
            line = ''.join(linelist)
            j+=1
            #print(line)

            # Update the line in the list of lines
            lines[i] = line
    print(lines[23734+46:23748+46])
    print(lines[23734+46+211:23742+46+211])
    # Write the modified lines back to the file
    file.seek(0)
    file.truncate(0)
    file.writelines(lines)


# Close the file
#file.close()




# Close files

kp_indeces.close()
SW_F10_predicted.close()
