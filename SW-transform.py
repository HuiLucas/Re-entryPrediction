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


############ Kp #############################################
lines = kp_indeces.readlines()
last_15_chars_list = []
for line in lines[2:26]:      #23719 +3 for right range
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

for i in range(0, 23):  
    observed_data_list[i].kp = seperate_row[i]
print(seperate_row[0])
print (last_15_chars_list[0])

'''
############ Ap #############################################

observed_data_list[0].Ap = [0,0,0,0,0,0,0,0]

print(last_15_chars_list[0:2])

seperate_AP = []
for item in last_15_chars_list:
        new_row = [item[i:i+2] for i in range(0, len(item), 2)]
        seperate_AP.append(new_row)

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
        for i in range(len(row)):
            row[i] = int(row[i])

print(seperate_AP[0:2])
print(len(seperate_AP))
for i in range(0, 23):  
    observed_data_list[i].Ap = seperate_AP[i]

#print (observed_data_list[0].Ap)
#print (seperate_row[0])
#print (last_15_chars_list[0])

'''


######################### F10.7 ########################################
with open('SW-kp-indeces.txt', 'r') as kp_indeces2:
    lines2 = kp_indeces2.readlines()
    f107_list = []
    for i in range(185, 23904):
        f107 = list(lines2[i])[11:14]
        for j in range(len(f107)):
            f107[j] = int(f107[j])
        f107num = f107[0]*100 + f107[1]*10 + f107[2]    
        f107_list.append(f107num)
        observed_data_list[i-185].F10_7_obs=f107num

    with open('SW-All.txt', 'r') as swall:
        lines3 = swall.readlines()
        f107ratiolist = []
        for i in range(0, 23719):
            f107ratioa = list(lines3[i+17])[93:98]
            for j in range(len(f107ratioa)):
                if f107ratioa[j] != "." and f107ratioa[j] != " ":
                    #print(j, f107ratioa[j], i)
                    f107ratioa[j] = int(f107ratioa[j])
                else:
                    f107ratioa[j] = 0
            f107ratioanum = f107ratioa[0]*100 + f107ratioa[1]*10 + f107ratioa[2] + f107ratioa[4]/10
            f107ratiob = list(lines3[i+17])[113:118]
            for j in range(len(f107ratiob)):
                if f107ratiob[j] != "." and f107ratiob[j] != " ":
                    f107ratiob[j] = int(f107ratiob[j])
                else:
                    f107ratiob[j] = 0
            f107ratiobnum = f107ratiob[0]*100 + f107ratiob[1]*10 + f107ratiob[2] + f107ratiob[4]/10
            ratio = f107ratioanum/f107ratiobnum
            observed_data_list[i].F10_7_adj = f107_list[i]*ratio
            #print(f107ratioanum, f107ratiobnum)

    print(f107_list[0:10])
    print(f107_list[-10:])
    print(observed_data_list[19].F10_7_obs)

for j in range(90, 23719):
    average1 = 0
    if j<23719-40:
        for k in range(-40, 41):
            average1 += observed_data_list[j+k].F10_7_obs/81
    else:
        for k in range(-40, 23719-j):
            average1 += observed_data_list[j+k].F10_7_obs/(40+23719-j)
            #print(j+k, k, 23719-j)
    observed_data_list[j].ctr81_obs = average1
    average2 = 0
    for k in range(-80, 1):
        average2 += observed_data_list[j+k].F10_7_obs/81
    observed_data_list[j].lst81_obs = average2   

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
            linelist[43:46] = [f"{(observed_data_list[j].sum)//100 if observed_data_list[j].sum//100 !=0 else nostring}", f"{(observed_data_list[j].sum)%100//10 if (observed_data_list[j].sum)%100//10 !=0 or observed_data_list[j].sum//100 !=0 else nostring}", f"{(observed_data_list[j].sum)%10}"]
            linelist[47:50] = [f"{observed_data_list[j].Ap[0]//100 if observed_data_list[j].Ap[0]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[0])%100//10 if (observed_data_list[j].Ap[0])%100//10 !=0 or observed_data_list[j].Ap[0]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[0]%10}"]
            linelist[51:54] = [f"{observed_data_list[j].Ap[1]//100 if observed_data_list[j].Ap[1]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[1])%100//10 if (observed_data_list[j].Ap[1])%100//10 !=0 or observed_data_list[j].Ap[1]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[1]%10}"]
            linelist[55:58] = [f"{observed_data_list[j].Ap[2]//100 if observed_data_list[j].Ap[2]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[2])%100//10 if (observed_data_list[j].Ap[2])%100//10 !=0 or observed_data_list[j].Ap[2]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[2]%10}"]
            linelist[59:62] = [f"{observed_data_list[j].Ap[3]//100 if observed_data_list[j].Ap[3]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[3])%100//10 if (observed_data_list[j].Ap[3])%100//10 !=0 or observed_data_list[j].Ap[3]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[3]%10}"]
            linelist[63:66] = [f"{observed_data_list[j].Ap[4]//100 if observed_data_list[j].Ap[4]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[4])%100//10 if (observed_data_list[j].Ap[4])%100//10 !=0 or observed_data_list[j].Ap[4]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[4]%10}"]
            linelist[67:70] = [f"{observed_data_list[j].Ap[5]//100 if observed_data_list[j].Ap[5]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[5])%100//10 if (observed_data_list[j].Ap[5])%100//10 !=0 or observed_data_list[j].Ap[5]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[5]%10}"]
            linelist[71:74] = [f"{observed_data_list[j].Ap[6]//100 if observed_data_list[j].Ap[6]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[6])%100//10 if (observed_data_list[j].Ap[6])%100//10 !=0 or observed_data_list[j].Ap[6]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[6]%10}"]
            linelist[75:78] = [f"{observed_data_list[j].Ap[7]//100 if observed_data_list[j].Ap[7]//100 != 0 else nostring}",f"{(observed_data_list[j].Ap[7])%100//10 if (observed_data_list[j].Ap[7])%100//10 !=0 or observed_data_list[j].Ap[7]//100 != 0 else nostring}", f"{observed_data_list[j].Ap[7]%10}"]
            linelist[79:82] = [f"{observed_data_list[j].avg//100 if observed_data_list[j].avg//100 !=0 else nostring}", f"{observed_data_list[j].avg%100//10 if observed_data_list[j].avg%100//10 !=0 or observed_data_list[j].avg//100 !=0 else nostring}", f"{observed_data_list[j].avg%10}" ]
            linelist[83:86] = [f"{observed_data_list[j].cp//1}",".", f"{np.round(observed_data_list[j].cp-observed_data_list[j].cp-int(observed_data_list[j].cp), decimals=1)}"]
            linelist[87] = f"{observed_data_list[j].c9//1}"
            linelist[89:92] = [f"{observed_data_list[j].ISN//100 if observed_data_list[j].ISN//100 !=0 else nostring}", f"{observed_data_list[j].ISN%100//10 if (observed_data_list[j].ISN)%100//10 !=0 or observed_data_list[j].ISN//100 !=0 else nostring}", f"{(observed_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{int(observed_data_list[j].F10_7_adj//100) if int(observed_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int(observed_data_list[j].F10_7_adj%100//10) if int((observed_data_list[j].F10_7_adj)%100//10) !=0 or int(observed_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int((observed_data_list[j].F10_7_adj)%10)}",".", f"{int((observed_data_list[j].F10_7_adj-int(observed_data_list[j].F10_7_adj))*10)}"]
            linelist[99] = f"{observed_data_list[j].Q//1 if type(observed_data_list[j].Q) == int else nostring}"
            if j>100:
                linelist[101:106] = [f"{int(observed_data_list[j].ctr81_adj//100) if int(observed_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int(observed_data_list[j].ctr81_adj%100//10) if int((observed_data_list[j].ctr81_adj)%100//10) !=0 or int(observed_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int((observed_data_list[j].ctr81_adj)%10)}",".", f"{int((observed_data_list[j].ctr81_adj-int(observed_data_list[j].ctr81_adj))*10)}"]
                linelist[107:112] = [f"{int(observed_data_list[j].lst81_adj//100) if int(observed_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int(observed_data_list[j].lst81_adj%100//10) if int((observed_data_list[j].lst81_adj)%100//10) !=0 or int(observed_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int((observed_data_list[j].lst81_adj)%10)}",".", f"{int((observed_data_list[j].lst81_adj-int(observed_data_list[j].lst81_adj))*10)}"]
            linelist[113:118] = [f"{int(observed_data_list[j].F10_7_obs//100) if int(observed_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int(observed_data_list[j].F10_7_obs%100//10) if (int(observed_data_list[j].F10_7_obs)%100//10) !=0 or int(observed_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int((observed_data_list[j].F10_7_obs)%10)}",".", f"{int((observed_data_list[j].F10_7_obs-int(observed_data_list[j].F10_7_obs))*10)}"]
            if j>100:
                linelist[119:124] = [f"{int(observed_data_list[j].ctr81_obs//100) if int(observed_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int(observed_data_list[j].ctr81_obs%100//10) if int((observed_data_list[j].ctr81_obs)%100//10) !=0 or int(observed_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int((observed_data_list[j].ctr81_obs)%10)}",".", f"{int((observed_data_list[j].ctr81_obs-int(observed_data_list[j].ctr81_obs))*10)}"]
                linelist[125:130] = [f"{int(observed_data_list[j].lst81_obs//100) if int(observed_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int(observed_data_list[j].lst81_obs%100//10) if int((observed_data_list[j].lst81_obs)%100//10) !=0 or int(observed_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int((observed_data_list[j].lst81_obs)%10)}",".", f"{int((observed_data_list[j].lst81_obs-int(observed_data_list[j].lst81_obs))*10)}"]
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
            linelist[43:46] = [f"{(daily_predicted_data_list[j].sum)//100 if daily_predicted_data_list[j].sum//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%100//10 if (daily_predicted_data_list[j].sum)%100//10 !=0 or daily_predicted_data_list[j].sum//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%10}"]
            linelist[47:50] = [f"{daily_predicted_data_list[j].Ap[0]//100 if daily_predicted_data_list[j].Ap[0]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[0])%100//10 if (daily_predicted_data_list[j].Ap[0])%100//10 !=0 or daily_predicted_data_list[j].Ap[0]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[0]%10}"]
            linelist[51:54] = [f"{daily_predicted_data_list[j].Ap[1]//100 if daily_predicted_data_list[j].Ap[1]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[1])%100//10 if (daily_predicted_data_list[j].Ap[1])%100//10 !=0 or daily_predicted_data_list[j].Ap[1]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[1]%10}"]
            linelist[55:58] = [f"{daily_predicted_data_list[j].Ap[2]//100 if daily_predicted_data_list[j].Ap[2]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[2])%100//10 if (daily_predicted_data_list[j].Ap[2])%100//10 !=0 or daily_predicted_data_list[j].Ap[2]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[2]%10}"]
            linelist[59:62] = [f"{daily_predicted_data_list[j].Ap[3]//100 if daily_predicted_data_list[j].Ap[3]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[3])%100//10 if (daily_predicted_data_list[j].Ap[3])%100//10 !=0 or daily_predicted_data_list[j].Ap[3]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[3]%10}"]
            linelist[63:66] = [f"{daily_predicted_data_list[j].Ap[4]//100 if daily_predicted_data_list[j].Ap[4]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[4])%100//10 if (daily_predicted_data_list[j].Ap[4])%100//10 !=0 or daily_predicted_data_list[j].Ap[4]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[4]%10}"]
            linelist[67:70] = [f"{daily_predicted_data_list[j].Ap[5]//100 if daily_predicted_data_list[j].Ap[5]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[5])%100//10 if (daily_predicted_data_list[j].Ap[5])%100//10 !=0 or daily_predicted_data_list[j].Ap[5]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[5]%10}"]
            linelist[71:74] = [f"{daily_predicted_data_list[j].Ap[6]//100 if daily_predicted_data_list[j].Ap[6]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[6])%100//10 if (daily_predicted_data_list[j].Ap[6])%100//10 !=0 or daily_predicted_data_list[j].Ap[6]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[6]%10}"]
            linelist[75:78] = [f"{daily_predicted_data_list[j].Ap[7]//100 if daily_predicted_data_list[j].Ap[7]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[7])%100//10 if (daily_predicted_data_list[j].Ap[7])%100//10 !=0 or daily_predicted_data_list[j].Ap[7]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[7]%10}"]
            linelist[79:82] = [f"{daily_predicted_data_list[j].avg//100 if daily_predicted_data_list[j].avg//100 !=0 else nostring}", f"{daily_predicted_data_list[j].avg%100//10 if daily_predicted_data_list[j].avg%100//10 !=0 or daily_predicted_data_list[j].avg//100 !=0 else nostring}", f"{daily_predicted_data_list[j].avg%10}" ]
            linelist[83:86] = [f"{daily_predicted_data_list[j].cp//1}",".", f"{np.round(daily_predicted_data_list[j].cp-daily_predicted_data_list[j].cp-int(daily_predicted_data_list[j].cp), decimals=1)}"]
            linelist[87] = f"{daily_predicted_data_list[j].c9//1}"
            linelist[89:92] = [f"{daily_predicted_data_list[j].ISN//100 if daily_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{daily_predicted_data_list[j].ISN%100//10 if (daily_predicted_data_list[j].ISN)%100//10 !=0 or daily_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{int(daily_predicted_data_list[j].F10_7_adj//100) if int(daily_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].F10_7_adj%100//10) if int((daily_predicted_data_list[j].F10_7_adj)%100//10) !=0 or int(daily_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].F10_7_adj)%10)}",".", f"{int((daily_predicted_data_list[j].F10_7_adj-int(daily_predicted_data_list[j].F10_7_adj))*10)}"]
            linelist[99] = f"{daily_predicted_data_list[j].Q//1 if type(daily_predicted_data_list[j].Q) == int else nostring}"
            if j>100:
                linelist[101:106] = [f"{int(daily_predicted_data_list[j].ctr81_adj//100) if int(daily_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].ctr81_adj%100//10) if int((daily_predicted_data_list[j].ctr81_adj)%100//10) !=0 or int(daily_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].ctr81_adj)%10)}",".", f"{int((daily_predicted_data_list[j].ctr81_adj-int(daily_predicted_data_list[j].ctr81_adj))*10)}"]
                linelist[107:112] = [f"{int(daily_predicted_data_list[j].lst81_adj//100) if int(daily_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].lst81_adj%100//10) if int((daily_predicted_data_list[j].lst81_adj)%100//10) !=0 or int(daily_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].lst81_adj)%10)}",".", f"{int((daily_predicted_data_list[j].lst81_adj-int(daily_predicted_data_list[j].lst81_adj))*10)}"]
            linelist[113:118] = [f"{int(daily_predicted_data_list[j].F10_7_obs//100) if int(daily_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].F10_7_obs%100//10) if (int(daily_predicted_data_list[j].F10_7_obs)%100//10) !=0 or int(daily_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].F10_7_obs)%10)}",".", f"{int((daily_predicted_data_list[j].F10_7_obs-int(daily_predicted_data_list[j].F10_7_obs))*10)}"]
            if j>100:
                linelist[119:124] = [f"{int(daily_predicted_data_list[j].ctr81_obs//100) if int(daily_predicted_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].ctr81_obs%100//10) if int((daily_predicted_data_list[j].ctr81_obs)%100//10) !=0 or int(daily_predicted_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].ctr81_obs)%10)}",".", f"{int((daily_predicted_data_list[j].ctr81_obs-int(daily_predicted_data_list[j].ctr81_obs))*10)}"]
                linelist[125:130] = [f"{int(daily_predicted_data_list[j].lst81_obs//100) if int(daily_predicted_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].lst81_obs%100//10) if int((daily_predicted_data_list[j].lst81_obs)%100//10) !=0 or int(daily_predicted_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].lst81_obs)%10)}",".", f"{int((daily_predicted_data_list[j].lst81_obs-int(daily_predicted_data_list[j].lst81_obs))*10)}"]
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
            linelist[89:92] = [f"{monthly_predicted_data_list[j].ISN//100 if monthly_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].ISN%100//10 if (monthly_predicted_data_list[j].ISN)%100//10 !=0 or monthly_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{(monthly_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{int(monthly_predicted_data_list[j].F10_7_adj//100) if int(monthly_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].F10_7_adj%100//10) if int((monthly_predicted_data_list[j].F10_7_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].F10_7_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].F10_7_adj-int(monthly_predicted_data_list[j].F10_7_adj))*10)}"]
            #linelist[99] = f"{monthly_predicted_data_list[j].Q//1 if type(monthly_predicted_data_list[j].Q) == int else nostring}"
            if j>100:
                linelist[101:106] = [f"{int(monthly_predicted_data_list[j].ctr81_adj//100) if int(monthly_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].ctr81_adj%100//10) if int((monthly_predicted_data_list[j].ctr81_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].ctr81_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].ctr81_adj-int(monthly_predicted_data_list[j].ctr81_adj))*10)}"]
                linelist[107:112] = [f"{int(monthly_predicted_data_list[j].lst81_adj//100) if int(monthly_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].lst81_adj%100//10) if int((monthly_predicted_data_list[j].lst81_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].lst81_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].lst81_adj-int(monthly_predicted_data_list[j].lst81_adj))*10)}"]
            linelist[113:118] = [f"{int(monthly_predicted_data_list[j].F10_7_obs//100) if int(monthly_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].F10_7_obs%100//10) if (int(monthly_predicted_data_list[j].F10_7_obs)%100//10) !=0 or int(monthly_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].F10_7_obs)%10)}",".", f"{int((monthly_predicted_data_list[j].F10_7_obs-int(monthly_predicted_data_list[j].F10_7_obs))*10)}"]
            if j>100:
                linelist[119:124] = [f"{int(monthly_predicted_data_list[j].ctr81_obs//100) if int(monthly_predicted_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].ctr81_obs%100//10) if int((monthly_predicted_data_list[j].ctr81_obs)%100//10) !=0 or int(monthly_predicted_data_list[j].ctr81_obs//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].ctr81_obs)%10)}",".", f"{int((monthly_predicted_data_list[j].ctr81_obs-int(monthly_predicted_data_list[j].ctr81_obs))*10)}"]
                linelist[125:130] = [f"{int(monthly_predicted_data_list[j].lst81_obs//100) if int(monthly_predicted_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].lst81_obs%100//10) if int((monthly_predicted_data_list[j].lst81_obs)%100//10) !=0 or int(monthly_predicted_data_list[j].lst81_obs//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].lst81_obs)%10)}",".", f"{int((monthly_predicted_data_list[j].lst81_obs-int(monthly_predicted_data_list[j].lst81_obs))*10)}"]
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
file.close()




# Close files

kp_indeces.close()
SW_F10_predicted.close()
