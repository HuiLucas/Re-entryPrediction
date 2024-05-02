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

observed_data_list = [observed_data() for i in range(0, 23719)]

observed_data_list[0].kp = [0,0,0,0,0,0,0,0]


############ Kp #############################################
lines = kp_indeces.readlines()
last_15_chars_list = []
for line in lines[2:23722]:      #23719 +3 for right range
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

for i in range(0, 23719):  
    observed_data_list[i].kp = seperate_row[i]

    
# Open the file for reading and writing
with open('SW-NEW.txt', 'r+') as file:
    # Read the contents of the file
    lines = file.readlines()
    # Iterate over each line
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
            linelist[48:50] = [f"{observed_data_list[j].Ap[0]//10 if observed_data_list[j].Ap[0]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[0]%10}"]
            linelist[52:54] = [f"{observed_data_list[j].Ap[1]//10 if observed_data_list[j].Ap[1]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[1]%10}"]
            linelist[56:58] = [f"{observed_data_list[j].Ap[2]//10 if observed_data_list[j].Ap[2]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[2]%10}"]
            linelist[60:62] = [f"{observed_data_list[j].Ap[3]//10 if observed_data_list[j].Ap[3]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[3]%10}"]
            linelist[64:66] = [f"{observed_data_list[j].Ap[4]//10 if observed_data_list[j].Ap[4]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[4]%10}"]
            linelist[68:70] = [f"{observed_data_list[j].Ap[5]//10 if observed_data_list[j].Ap[5]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[5]%10}"]
            linelist[72:74] = [f"{observed_data_list[j].Ap[6]//10 if observed_data_list[j].Ap[6]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[6]%10}"]
            linelist[76:78] = [f"{observed_data_list[j].Ap[7]//10 if observed_data_list[j].Ap[7]//10 !=0 else nostring}", f"{observed_data_list[j].Ap[7]%10}"]
            linelist[80:82] = [f"{observed_data_list[j].avg//10 if observed_data_list[j].avg//10 !=0 else nostring}", f"{observed_data_list[j].avg%10}"]
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

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Write the modified lines back to the file
    file.writelines(lines)

# Close the file
file.close()




# Close files

kp_indeces.close()
SW_F10_predicted.close()
