kp_indeces = open('SW-kp-indeces.txt', 'r')
SW_F10_predicted = open('SW-F10-predicted.txt', 'r')
import numpy as np

import datetime
from dateutil.relativedelta import relativedelta



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

q = 23719 # 10 #2000 #23719 #23 #change for the number of lines in the file

############ Kp #############################################
lines = kp_indeces.readlines()
last_15_chars_list = []
for counter, line in enumerate(lines[185:q+185]):      #23719 +3 for right range
    print(counter)
    
    last_15_chars = line[-17:].strip()
    last_15_chars_list.append(last_15_chars)
    seperate_row = []
    for item in last_15_chars_list:
        new_row = [item[i:i+2] for i in range(0, len(item), 2)]
        seperate_row.append(new_row)

    if True:
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
    print(i)
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
    print(i)

#print (observed_data_list[5].kp)
#print (observed_data_list[5].Ap)
#print (seperate_row[0])
#sprint (last_15_chars_list[0])

############ SUM #############################################

for i in range(0, q):      #23719
    observed_data_list[i].sum = sum(observed_data_list[i].kp)
    print(i)

#print (observed_data_list[5].sum)

############ AVG #############################################

for i in range(0, q-1):     #23719 
    observed_data_list[i].avg = int(np.mean(observed_data_list[i].Ap))
    print(i)

#print(observed_data_list[5].Ap)
#print (observed_data_list[5].avg)

############ CP #############################################

average_Ap = []
for i in range(0, q):      #23719
    average_Ap.append(np.sum(observed_data_list[i].Ap))
    print(i)

#print(observed_data_list[0].Ap,observed_data_list[1].Ap,observed_data_list[2].Ap,observed_data_list[3].Ap,observed_data_list[4].Ap)
#print (average_Ap[5])

for i in range(len(average_Ap)):
        print(i)
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
        elif 562 <= average_Ap[i] <= 729:
            average_Ap[i] = 1.8
        elif 730 <= average_Ap[i] <= 1119:
            average_Ap[i] = 1.9
        elif 1120 <= average_Ap[i] <= 1399:
            average_Ap[i] = 2.0
        elif 1400 <= average_Ap[i] <= 1699:
            average_Ap[i] = 2.1
        elif 1700 <= average_Ap[i] <= 1999:
            average_Ap[i] = 2.2
        elif 2000 <= average_Ap[i] <= 2399:
            average_Ap[i] = 2.3
        elif 2400 <= average_Ap[i] <= 3199:
            average_Ap[i] = 2.4
        elif 3200 <= average_Ap[i]: 
            average_Ap[i] = 2.5



for i in range(0, q-1):      #23719
    observed_data_list[i].cp = average_Ap[i]
    print(i)

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
    print(i)

# for i in range(0, q):      #23719
#     observed_data_list[i].cp = np.round(average_Ap[i],2)

sum_Ap = []
for i in range(0, q):      #23719
    sum_Ap.append(np.sum(observed_data_list[i].Ap))
    print(i)

#k = 236
#print(f'sum={sum_Ap[k]}, cp={observed_data_list[k].cp},c9={observed_data_list[k].c9}')


######################### F10.7 ########################################
with open('SW-kp-indeces.txt', 'r') as kp_indeces2:
    lines2 = kp_indeces2.readlines()
    f107_list = []
    ISN_list = []
    for i in range(185, 23904):
        f107 = list(lines2[i])[11:14]
        for j in range(len(f107)):
            f107[j] = int(f107[j])
        f107num = f107[0]*100 + f107[1]*10 + f107[2]    
        f107_list.append(f107num)
        observed_data_list[i-185].F10_7_obs=f107num
        ISN = list(lines2[i])[19:22]
        for j in range(len(ISN)):
            ISN[j] = int(ISN[j])
        ISNnum = ISN[0]*100 + ISN[1]*10 + ISN[2]
        ISN_list.append(ISNnum)
        observed_data_list[i-185].ISN = ISNnum
    mm=0
    for i in range(23904, 23931):
        ISN = list(lines2[i])[19:22]
        for j in range(len(ISN)):
            ISN[j] = int(ISN[j])
        ISNnum = ISN[0]*100 + ISN[1]*10 + ISN[2]
        ISN_list.append(ISNnum)
        daily_predicted_data_list[mm].ISN = ISNnum
        mm+=1

    for i in range(0, 18):
        # interpolate
        with open('SW-montlypred', 'r') as monthlypred:
            lines4 = monthlypred.readlines()
            ISNa = list(lines4[794-1])[17:22]	# ISN at 1-10-2022
            ISNb = list(lines4[794])[17:22]	# ISN at 1-11-2022
            for j in range(len(ISNa)):
                if ISNa[j] != "." and ISNa[j] != " ":
                    ISNa[j] = int(ISNa[j])
                else:
                    ISNa[j] = 0
            ISNanum = ISNa[0]*100 + ISNa[1]*10 + ISNa[2] + ISNa[4]/10
            for j in range(len(ISNb)):
                if ISNb[j] != "." and ISNb[j] != " ":
                    ISNb[j] = int(ISNb[j])
                else:
                    ISNb[j] = 0
            ISNbnum = ISNb[0]*100 + ISNb[1]*10 + ISNb[2] + ISNb[4]/10
            dayshift = 6
            daily_predicted_data_list[mm].ISN=int(np.round(ISNanum + (ISNbnum-ISNanum)/(31) * (i + dayshift),1))
        mm+=1



    with open('SW-All.txt', 'r') as swall:
        lines3 = swall.readlines()
        f107ratiolist = []
        for i in range(0, 23719): # lines from which the ratios are calculated
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

    f107predicted_list = []
    k=0
    for i in range(0, 45):
        if i + 23904 < len(lines2):
            f107predicted = list(lines2[i+23904])[11:14]
            for j in range(len(f107predicted)):
                f107predicted[j] = int(f107predicted[j])
            f107predictednum = f107predicted[0]*100 + f107predicted[1]*10 + f107predicted[2]    
            f107predicted_list.append(f107predictednum)
        else :
            with open('SW-montlypred', 'r') as monthlypred:
                lines4 = monthlypred.readlines()
                f107predicteda = list(lines4[len(lines2)-23904-794-520])[31:36] # f107 at 1-10-2022
                f107predictedb = list(lines4[len(lines2)-23904-794-520+1])[31:36]   # f107 at 1-11-2022
                
                for j in range(len(f107predicteda)):
                    if f107predicteda[j] != "." and f107predicteda[j] != " ":
                        f107predicteda[j] = int(f107predicteda[j])
                    else:
                        f107predicteda[j] = 0
                f107predicteda = f107predicteda[0]*100 + f107predicteda[1]*10 + f107predicteda[2] + f107predicteda[4]/10
                for j in range(len(f107predictedb)):
                    if f107predictedb[j] != "." and f107predictedb[j] != " ":
                        f107predictedb[j] = int(f107predictedb[j])
                    else:
                        f107predictedb[j] = 0
                f107predictedb = f107predictedb[0]*100 + f107predictedb[1]*10 + f107predictedb[2] + f107predictedb[4]/10
                #print('pred', f107predicteda, f107predictedb)
                #interpolate:
                day1 = 6 # 6-1-2022 (First interpolated day)
                f107predicted_list.append(np.round(f107predicteda + (f107predictedb-f107predicteda)/(31) * (k + day1-1),1))
                k+=1

with open('SW-montlypred', 'r') as monthlypred:
    lines4 = monthlypred.readlines()
    for i in range(0, 209):
        f107predicted = list(lines4[i+795-1])[31:36] # f107 at 1-11-2022
        
        for j in range(len(f107predicted)):
            if f107predicted[j] != "." and f107predicted[j] != " ":
                f107predicted[j] = int(f107predicted[j])
            else:
                f107predicted[j] = 0
        f107predictednum = f107predicted[0]*100 + f107predicted[1]*10 + f107predicted[2] + f107predicted[4]/10
        #print(f107predictednum)
        monthly_predicted_data_list[i].F10_7_obs = f107predictednum
        SSN_pred = list(lines4[i+795-1])[17:22] 
        for j in range(len(SSN_pred)):
            if SSN_pred[j] != "." and SSN_pred[j] != " ":
                SSN_pred[j] = int(SSN_pred[j])
            else:
                SSN_pred[j] = 0
        SSN_prednum = SSN_pred[0]*100 + SSN_pred[1]*10 + SSN_pred[2] + SSN_pred[4]/10
        monthly_predicted_data_list[i].ISN = int(SSN_prednum)

    with open('SW-all.txt', 'r') as swall:
        lines3 = swall.readlines()
        f107ratiolist = []
        for m in range(0,209): 
            i = 23790 + int(m *30.4375) -1 # lines from which the ratios are calculated
            if i <= 24300:
                f107ratioa = list(lines3[i])[93:98]
                #print(f107ratioa, i, m, list(lines3[i])[0:10])
                for j in range(len(f107ratioa)):
                    if f107ratioa[j] != "." and f107ratioa[j] != " ":
                        f107ratioa[j] = int(f107ratioa[j])
                    else:
                        f107ratioa[j] = 0
                f107ratioanum = f107ratioa[0]*100 + f107ratioa[1]*10 + f107ratioa[2] + f107ratioa[4]/10
                f107ratiob = list(lines3[i])[113:118]
                for j in range(len(f107ratiob)):
                    if f107ratiob[j] != "." and f107ratiob[j] != " ":
                        f107ratiob[j] = int(f107ratiob[j])
                    else:
                        f107ratiob[j] = 0
                f107ratiobnum = f107ratiob[0]*100 + f107ratiob[1]*10 + f107ratiob[2] + f107ratiob[4]/10
                ratio = f107ratioanum/f107ratiobnum
                monthly_predicted_data_list[m].F10_7_adj = monthly_predicted_data_list[m].F10_7_obs*ratio
                #print(f107ratioanum, f107ratiobnum)
            elif i > 24305:
                if i < 24350:
                    f107ratioa = list(lines3[i+5])[93:98]
                    for j in range(len(f107ratioa)):
                        if f107ratioa[j] != "." and f107ratioa[j] != " ":
                            f107ratioa[j] = int(f107ratioa[j])
                        else:
                            f107ratioa[j] = 0
                    f107ratioanum = f107ratioa[0]*100 + f107ratioa[1]*10 + f107ratioa[2] + f107ratioa[4]/10
                    f107ratiob = list(lines3[i+5])[113:118]
                    for j in range(len(f107ratiob)):
                        if f107ratiob[j] != "." and f107ratiob[j] != " ":
                            f107ratiob[j] = int(f107ratiob[j])
                        else:
                            f107ratiob[j] = 0
                    f107ratiobnum = f107ratiob[0]*100 + f107ratiob[1]*10 + f107ratiob[2] + f107ratiob[4]/10
                    ratio = f107ratioanum/f107ratiobnum
                    monthly_predicted_data_list[m].F10_7_adj = monthly_predicted_data_list[m].F10_7_obs*ratio
                    #print(m, list(lines3[i+5])[0:10])
                else:
                    f107ratioa = list(lines3[len(lines3)-8 - (209 -m)])[93:98] # last line in SW-new in SW-all
                    for j in range(len(f107ratioa)):
                        if f107ratioa[j] != "." and f107ratioa[j] != " ":
                            f107ratioa[j] = int(f107ratioa[j])
                        else:
                            f107ratioa[j] = 0
                    #print(f107ratioa, len(lines3)-8 - (209 - m), m, list(lines3[len(lines3)-8 - (209 - m)])[0:10])
                    f107ratioanum = f107ratioa[0]*100 + f107ratioa[1]*10 + f107ratioa[2] + f107ratioa[4]/10
                    f107ratiob = list(lines3[len(lines3)-8 - (209 - m)])[113:118]
                    #print(f107ratiob, len(lines3)-8 - (209 - m), m)
                    for j in range(len(f107ratiob)):
                        if f107ratiob[j] != "." and f107ratiob[j] != " ":
                            f107ratiob[j] = int(f107ratiob[j])
                        else:
                            f107ratiob[j] = 0
                    f107ratiobnum = f107ratiob[0]*100 + f107ratiob[1]*10 + f107ratiob[2] + f107ratiob[4]/10
                    ratio = f107ratioanum/f107ratiobnum
                    monthly_predicted_data_list[m].F10_7_adj = monthly_predicted_data_list[m].F10_7_obs*ratio
                    #print(f107ratioanum, f107ratiobnum)

with open('SW-kp-indeces.txt', 'r') as kp_indeces2:
    mmm=0
    lines5 = kp_indeces2.readlines()
    for j in range(23904, 23931):
        ap_avg = list(lines5[j])[22:26]
        for i in range(len(ap_avg)):
            if ap_avg[i] != "." and ap_avg[i] != " ":
                ap_avg[i] = int(ap_avg[i])
            else:
                ap_avg[i] = 0
        ap_avgnum = ap_avg[0]*1000 + ap_avg[1]*100 + ap_avg[2]*10 + ap_avg[3]
        daily_predicted_data_list[mmm].avg = int(ap_avgnum)
        for k in range(8): 
            daily_predicted_data_list[mmm].Ap[k] = ap_avgnum
        
        ### KP berekenen:
        for k in range(8):
            daily_predicted_data_list[mmm].kp[k] = daily_predicted_data_list[mmm].Ap[k]  

        for i2, row in enumerate(daily_predicted_data_list[mmm].kp):
            row = [str(row)]
            rownew = row
            print("first", row)
            for i in range(len(row)):
                row = ["0" if r == "0" else r for r in row]
                if row != rownew : print('row', row); break
                row = ["0" if r == "1" else r for r in row]
                if row != rownew : print('row', row); break
                row = ["3" if r == "2" else r for r in   row]
                if row != rownew : print('row', row); break 
                row = ["7" if r == "3" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["10" if r == "4" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["13" if r == "5" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["17" if r == "6" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["20" if r == "7" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "8" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "9" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "10" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "11" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "12" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "13" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "14" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "15" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "16" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "17" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "18" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "19" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "20" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "21" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "22" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "23" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "24" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "25" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "26" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "27" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "28" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "29" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "30" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "31" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "32" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "33" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "34" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "35" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "36" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "37" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "38" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "39" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "40" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "41" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "42" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "43" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "44" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "45" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "46" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "47" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "48" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "49" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "50" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "51" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "52" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "53" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "54" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "55" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "56" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(57, 60):
                    row = ["53" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(60, 67):
                    row = ["57" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["57" if r == "67" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(68, 74):
                    row = ["57" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(74, 80):
                    row = ["60" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["60" if r == "80" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(81, 87):
                    row = ["60" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(87, 94):
                    row = ["63" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["63" if r == "94" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(95, 103):
                    row = ["63" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(103, 111):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["67" if r == "111" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(112, 122):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(122, 132):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["70" if r == "132" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(133, 144):
                    row = ["70" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(144, 154):
                    row = ["73" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["73" if r == "154" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(155, 166):
                    row = ["73" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(166, 179):
                    row = ["77" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["77" if r == "179" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(180, 193):
                    row = ["77" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(193, 207):
                    row = ["80" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["80" if r == "207" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(208, 223):
                    row = ["80" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(223, 236):
                    row = ["83" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["83" if r == "236" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(237, 269):
                    row = ["83" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(269, 300):
                    row = ["87" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["87" if r == "300" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(301, 350):
                    row = ["87" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(350, 400):
                    row = ["90" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["90" if r == "400" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(401, 450):
                    row = ["90" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(450, 500):
                    row = ["93" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["93" if r == "500" else r for r in  row]
                if row != rownew : print('row', row); break
            print("second", row)
            row = list(row[0])
            for j in range(len(row)):
                if row[j] != "." and row[j] != " ":
                    row[j] = int(row[j])
                else:
                    row[j] = 0
            rownum = row[0]*10 + row[1]
            daily_predicted_data_list[mmm].kp[i2] = rownum
            print('print', daily_predicted_data_list[mmm].kp[i2], daily_predicted_data_list[mmm].Ap[i2] , rownum, )
            
            ### Cp & C9 berekenen:
        

        ### Cp & C9 berekenen:
        if 0 <= daily_predicted_data_list[mmm].avg <= 22:
            Cp_new = 0.0
        elif 23 <= daily_predicted_data_list[mmm].avg <= 34:
            Cp_new = 0.1
        elif 35 <= daily_predicted_data_list[mmm].avg <= 44: 
            Cp_new = 0.2
        elif 45 <= daily_predicted_data_list[mmm].avg <= 55:
            Cp_new = 0.3
        elif 56 <= daily_predicted_data_list[mmm].avg <= 66:
            Cp_new = 0.4
        elif 67 <= daily_predicted_data_list[mmm].avg <= 78:
            Cp_new = 0.5
        elif 79 <= daily_predicted_data_list[mmm].avg <= 90:
            Cp_new = 0.6
        elif 91 <= daily_predicted_data_list[mmm].avg <= 104:
            Cp_new = 0.7
        elif 105 <= daily_predicted_data_list[mmm].avg <= 120:
            Cp_new = 0.8
        elif 121 <= daily_predicted_data_list[mmm].avg <= 139:
            Cp_new = 0.9
        elif 140 <= daily_predicted_data_list[mmm].avg <= 164:
            Cp_new = 1.0
        elif 165 <= daily_predicted_data_list[mmm].avg <= 190:
            Cp_new = 1.1
        elif 191 <= daily_predicted_data_list[mmm].avg <= 228:
            Cp_new = 1.2
        elif 229 <= daily_predicted_data_list[mmm].avg <= 273:
            Cp_new = 1.3
        elif 274 <= daily_predicted_data_list[mmm].avg <= 320:
            Cp_new = 1.4
        elif 321 <= daily_predicted_data_list[mmm].avg <= 379:
            Cp_new = 1.5
        elif 380 <= daily_predicted_data_list[mmm].avg <= 453:
            Cp_new = 1.6
        elif 454 <= daily_predicted_data_list[mmm].avg <= 561:
            Cp_new = 1.7
        elif 562 <= daily_predicted_data_list[mmm].avg <= 729:
            Cp_new = 1.8
        elif 730 <= daily_predicted_data_list[mmm].avg <= 1119:
            Cp_new = 1.9
        elif 1120 <= daily_predicted_data_list[mmm].avg <= 1399:
            Cp_new = 2.0
        elif 1400 <= daily_predicted_data_list[mmm].avg <= 1699:
            Cp_new = 2.1
        elif 1700 <= daily_predicted_data_list[mmm].avg <= 1999:
            Cp_new = 2.2
        elif 2000 <= daily_predicted_data_list[mmm].avg <= 2399:
            Cp_new = 2.3
        elif 2400 <= daily_predicted_data_list[mmm].avg <= 3199:
            Cp_new = 2.4
        elif 3200 <= daily_predicted_data_list[mmm].avg: 
            Cp_new = 2.5
        daily_predicted_data_list[mmm].cp = np.round(Cp_new, decimals=1)
        if 0.0 <= daily_predicted_data_list[mmm].cp <= 0.1:
            daily_predicted_data_list[mmm].c9 = 0
        if 0.2 <= daily_predicted_data_list[mmm].cp <= 0.3:
            daily_predicted_data_list[mmm].c9 = 1
        if 0.4 <= daily_predicted_data_list[mmm].cp <= 0.5:
            daily_predicted_data_list[mmm].c9 = 2
        if 0.6 <= daily_predicted_data_list[mmm].cp <= 0.7:
            daily_predicted_data_list[mmm].c9 = 3
        if 0.8 <= daily_predicted_data_list[mmm].cp <= 0.9:
            daily_predicted_data_list[mmm].c9 = 4
        if 1.0 <= daily_predicted_data_list[mmm].cp <= 1.1:
            daily_predicted_data_list[mmm].c9 = 5
        if 1.2 <= daily_predicted_data_list[mmm].cp <= 1.4:
            daily_predicted_data_list[mmm].c9 = 6
        if 1.5 <= daily_predicted_data_list[mmm].cp <= 1.8:
            daily_predicted_data_list[mmm].c9 = 7
        if daily_predicted_data_list[mmm].cp == 1.9:
            daily_predicted_data_list[mmm].c9 = 8
        if 2.0 <= daily_predicted_data_list[mmm].cp <= 2.5:
            daily_predicted_data_list[mmm].c9 = 9
        mmm+=1
        print('mmm', mmm)


for jj in range(0, 18):
    print('jj', jj)   
    #interpolation
    with open('SW-montlypred') as monthlypred:
        lines4 = monthlypred.readlines()
        avga = list(lines4[794-1])[66:71]	# avg at 1-10-2022
        avgb = list(lines4[794])[66:71]	# avg at 1-11-2022
        for i in range(len(avga)):
            if avga[i] != "." and avga[i] != " ":
                avga[i] = int(avga[i])
            else:
                avga[i] = 0
        avganum = avga[0]*100 + avga[1]*10 + avga[2] + avga[4]/10
        for i in range(len(avgb)):
            if avgb[i] != "." and avgb[i] != " ":
                avgb[i] = int(avgb[i])
            else:
                avgb[i] = 0
        avgbnum = avgb[0]*100 + avgb[1]*10 + avgb[2] + avgb[4]/10
        dayshift = 6
        #print(avganum, avgbnum,'avg')
        daily_predicted_data_list[mmm+jj].avg=int(np.round(avganum + (avgbnum-avganum)/(31) * (jj + dayshift),1))
        for k in range(8):
            daily_predicted_data_list[mmm+jj].Ap[k] = daily_predicted_data_list[mmm+jj].avg
         ### KP berekenen:
        for k in range(8):
            daily_predicted_data_list[mmm+jj].kp[k] = daily_predicted_data_list[mmm+jj].Ap[k]  

        for i2, row in enumerate(daily_predicted_data_list[mmm+jj].kp):
            
            row = [str(row)]
            rownew = row
            print("first", row)
            for i in range(len(row)):
                row = ["0" if r == "0" else r for r in row]
                if row != rownew : print('row', row); break
                row = ["0" if r == "1" else r for r in row]
                if row != rownew : print('row', row); break
                row = ["3" if r == "2" else r for r in   row]
                if row != rownew : print('row', row); break 
                row = ["7" if r == "3" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["10" if r == "4" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["13" if r == "5" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["17" if r == "6" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["20" if r == "7" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "8" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "9" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["23" if r == "10" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "11" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "12" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["27" if r == "13" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "14" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "15" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["30" if r == "16" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "17" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "18" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "19" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["33" if r == "20" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "21" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "22" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "23" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["37" if r == "24" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "25" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "26" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "27" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "28" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["40" if r == "29" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "30" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "31" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "32" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "33" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "34" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "35" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["43" if r == "36" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "37" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "38" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "39" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "40" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "41" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "42" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["47" if r == "43" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "44" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "45" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "46" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "47" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "48" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "49" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "50" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "51" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "52" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["50" if r == "53" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "54" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "55" else r for r in  row]
                if row != rownew : print('row', row); break
                row = ["53" if r == "56" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(57, 60):
                    row = ["53" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(60, 67):
                    row = ["57" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["57" if r == "67" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(68, 74):
                    row = ["57" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(74, 80):
                    row = ["60" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["60" if r == "80" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(81, 87):
                    row = ["60" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(87, 94):
                    row = ["63" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["63" if r == "94" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(95, 103):
                    row = ["63" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(103, 111):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["67" if r == "111" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(112, 122):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(122, 132):
                    row = ["67" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["70" if r == "132" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(133, 144):
                    row = ["70" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(144, 154):
                    row = ["73" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["73" if r == "154" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(155, 166):
                    row = ["73" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(166, 179):
                    row = ["77" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["77" if r == "179" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(180, 193):
                    row = ["77" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(193, 207):
                    row = ["80" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["80" if r == "207" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(208, 223):
                    row = ["80" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(223, 236):
                    row = ["83" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["83" if r == "236" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(237, 269):
                    row = ["83" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(269, 300):
                    row = ["87" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["87" if r == "300" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(301, 350):
                    row = ["87" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(350, 400):
                    row = ["90" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["90" if r == "400" else r for r in  row]
                if row != rownew : print('row', row); break
                for n in range(401, 450):
                    row = ["90" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                for n in range(450, 500):
                    row = ["93" if r == str(n) else r for r in  row]
                    if row != rownew : print('row', row); break
                row = ["93" if r == "500" else r for r in  row]
                if row != rownew : print('row', row); break
            print("second", row)
            row = list(row[0])
            for j in range(len(row)):
                if row[j] != "." and row[j] != " ":
                    row[j] = int(row[j])
                else:
                    row[j] = 0
            if len(row) == 1:
                rownum = row[0]
            else:
                rownum = row[0]*10 + row[1]
            
            daily_predicted_data_list[mmm+jj].kp[i2] = rownum
            print('rownum', daily_predicted_data_list[mmm+jj].kp[i2])

        ### Cp & C9 berekenen:
        if 0 <= daily_predicted_data_list[mmm+jj].avg <= 22:
            Cp_new = 0.0
        elif 23 <= daily_predicted_data_list[mmm+jj].avg <= 34:
            Cp_new = 0.1
        elif 35 <= daily_predicted_data_list[mmm+jj].avg <= 44: 
            Cp_new = 0.2
        elif 45 <= daily_predicted_data_list[mmm+jj].avg <= 55:
            Cp_new = 0.3
        elif 56 <= daily_predicted_data_list[mmm+jj].avg <= 66:
            Cp_new = 0.4
        elif 67 <= daily_predicted_data_list[mmm+jj].avg <= 78:
            Cp_new = 0.5
        elif 79 <= daily_predicted_data_list[mmm+jj].avg <= 90:
            Cp_new = 0.6
        elif 91 <= daily_predicted_data_list[mmm+jj].avg <= 104:
            Cp_new = 0.7
        elif 105 <= daily_predicted_data_list[mmm+jj].avg <= 120:
            Cp_new = 0.8
        elif 121 <= daily_predicted_data_list[mmm+jj].avg <= 139:
            Cp_new = 0.9
        elif 140 <= daily_predicted_data_list[mmm+jj].avg <= 164:
            Cp_new = 1.0
        elif 165 <= daily_predicted_data_list[mmm+jj].avg <= 190:
            Cp_new = 1.1
        elif 191 <= daily_predicted_data_list[mmm+jj].avg <= 228:
            Cp_new = 1.2
        elif 229 <= daily_predicted_data_list[mmm+jj].avg <= 273:
            Cp_new = 1.3
        elif 274 <= daily_predicted_data_list[mmm+jj].avg <= 320:
            Cp_new = 1.4
        elif 321 <= daily_predicted_data_list[mmm+jj].avg <= 379:
            Cp_new = 1.5
        elif 380 <= daily_predicted_data_list[mmm+jj].avg <= 453:
            Cp_new = 1.6
        elif 454 <= daily_predicted_data_list[mmm+jj].avg <= 561:
            Cp_new = 1.7
        elif 562 <= daily_predicted_data_list[mmm+jj].avg <= 729:
            Cp_new = 1.8
        elif 730 <= daily_predicted_data_list[mmm+jj].avg <= 1119:
            Cp_new = 1.9
        elif 1120 <= daily_predicted_data_list[mmm+jj].avg <= 1399:
            Cp_new = 2.0
        elif 1400 <= daily_predicted_data_list[mmm+jj].avg <= 1699:
            Cp_new = 2.1
        elif 1700 <= daily_predicted_data_list[mmm+jj].avg <= 1999:
            Cp_new = 2.2
        elif 2000 <= daily_predicted_data_list[mmm+jj].avg <= 2399:
            Cp_new = 2.3
        elif 2400 <= daily_predicted_data_list[mmm+jj].avg <= 3199:
            Cp_new = 2.4
        elif 3200 <= daily_predicted_data_list[mmm+jj].avg: 
            Cp_new = 2.5
        daily_predicted_data_list[mmm+jj].cp = np.round(Cp_new, decimals=1)
        if 0.0 <= daily_predicted_data_list[mmm+jj].cp <= 0.1:
            daily_predicted_data_list[mmm+jj].c9 = 0
        if 0.2 <= daily_predicted_data_list[mmm+jj].cp <= 0.3:
            daily_predicted_data_list[mmm+jj].c9 = 1
        if 0.4 <= daily_predicted_data_list[mmm+jj].cp <= 0.5:
            daily_predicted_data_list[mmm+jj].c9 = 2
        if 0.6 <= daily_predicted_data_list[mmm+jj].cp <= 0.7:
            daily_predicted_data_list[mmm+jj].c9 = 3
        if 0.8 <= daily_predicted_data_list[mmm+jj].cp <= 0.9:
            daily_predicted_data_list[mmm+jj].c9 = 4
        if 1.0 <= daily_predicted_data_list[mmm+jj].cp <= 1.1:
            daily_predicted_data_list[mmm+jj].c9 = 5
        if 1.2 <= daily_predicted_data_list[mmm+jj].cp <= 1.4:
            daily_predicted_data_list[mmm+jj].c9 = 6
        if 1.5 <= daily_predicted_data_list[mmm+jj].cp <= 1.8:
            daily_predicted_data_list[mmm+jj].c9 = 7
        if daily_predicted_data_list[mmm+jj].cp == 1.9:
            daily_predicted_data_list[mmm+jj].c9 = 8
        if 2.0 <= daily_predicted_data_list[mmm+jj].cp <= 2.5:
            daily_predicted_data_list[mmm+jj].c9 = 9
    print('rownum2', daily_predicted_data_list[mmm+j].kp, mmm+jj, j)

#print('rownum2', daily_predicted_data_list[45].kp, 45)
#print('list', f107predicted_list)
for i, f107 in enumerate(f107predicted_list):
    daily_predicted_data_list[i].F10_7_obs = f107

with open('SW-all.txt', 'r') as swall:
    lines3 = swall.readlines()
    f107ratiolist = []
    k=0
    for i in range(23736, 23781): # lines from which the ratios are calculated
        #print(lines3[i])
        f107ratioa = list(lines3[i])[93:98]
        for j in range(len(f107ratioa)):
            if f107ratioa[j] != "." and f107ratioa[j] != " ":
                #print(j, f107ratioa[j], i)
                f107ratioa[j] = int(f107ratioa[j])
            else:
                f107ratioa[j] = 0
        f107ratioanum = f107ratioa[0]*100 + f107ratioa[1]*10 + f107ratioa[2] + f107ratioa[4]/10
        f107ratiob = list(lines3[i])[113:118]
        for j in range(len(f107ratiob)):
            if f107ratiob[j] != "." and f107ratiob[j] != " ":
                f107ratiob[j] = int(f107ratiob[j])
            else:
                f107ratiob[j] = 0
        f107ratiobnum = f107ratiob[0]*100 + f107ratiob[1]*10 + f107ratiob[2] + f107ratiob[4]/10
        ratio = f107ratioanum/f107ratiobnum
        daily_predicted_data_list[k].F10_7_adj = daily_predicted_data_list[k].F10_7_obs*ratio
        k+=1
        #print(f107ratioanum, f107ratiobnum)


###### Averaging stuff:

for i in range(0, 45):
    daily_predicted_data_list[i].sum = 8 * daily_predicted_data_list[i].kp[0]

for i in range(0, 45):
    average1 = 0
    if i<45-40:
        for j in range(-40, 41):
            if i+j>=0:
                average1 += daily_predicted_data_list[i+j].F10_7_obs/81
            else:
                average1 += observed_data_list[i+j+23719].F10_7_obs/81 # 23719 is the index of the last on the observed data list
    else:
        for j in range(-40, 45-i):
            if i+j>=0:
                average1 += daily_predicted_data_list[i+j].F10_7_obs/(40+45-i)
            else:
                average1 += observed_data_list[i+j+23719].F10_7_obs/(40+45-i)
    daily_predicted_data_list[i].ctr81_obs = average1
    average2 = 0
    for j in range(-80, 1):
        if i+j>=0:
            average2 += daily_predicted_data_list[i+j].F10_7_obs/81
        else:
            average2 += observed_data_list[i+j+23719].F10_7_obs/81
    daily_predicted_data_list[i].lst81_obs = average2
        
for i in range(0, 45):
    average1 = 0
    if i<45-40:
        for j in range(-40, 41):
            if i+j>=0:
                average1 += daily_predicted_data_list[i+j].F10_7_adj/81
            else:
                average1 += observed_data_list[i+j+23719].F10_7_adj/81
    else:
        for j in range(-40, 45-i):
            if i+j>=0:
                average1 += daily_predicted_data_list[i+j].F10_7_adj/(40+45-i)
            else:
                average1 += observed_data_list[i+j+23719].F10_7_adj/(40+45-i)
    daily_predicted_data_list[i].ctr81_adj = average1
    average2 = 0
    for j in range(-80, 1):
        if i+j>=0:
            average2 += daily_predicted_data_list[i+j].F10_7_adj/81
        else:
            average2 += observed_data_list[i+j+23719].F10_7_adj/81
    daily_predicted_data_list[i].lst81_adj = average2

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

for j in range(90, 23719):
    average1 = 0
    if j<23719-40:
        for k in range(-40, 41):
            average1 += observed_data_list[j+k].F10_7_adj/81
    else:
        for k in range(-40, 23719-j):
            average1 += observed_data_list[j+k].F10_7_adj/(40+23719-j)
            #print(j+k, k, 23719-j)
    observed_data_list[j].ctr81_adj = average1
    average2 = 0
    for k in range(-80, 1):
        average2 += observed_data_list[j+k].F10_7_adj/81
    observed_data_list[j].lst81_adj = average2

for i in range(0, 209):
    average1 = 0
    if i<209-40:
        for j in range(-40, 41):
            if i+j>=0:
                average1 += monthly_predicted_data_list[i+j].F10_7_obs/81
            else:
                average1 += daily_predicted_data_list[i+j+45].F10_7_obs/81
    else:
        for j in range(-40, 209-i):
            if i+j>=0:
                average1 += monthly_predicted_data_list[i+j].F10_7_obs/(40+209-i)
            else:
                average1 += daily_predicted_data_list[i+j+45].F10_7_obs/(40+209-i)
    monthly_predicted_data_list[i].ctr81_obs = average1
    average2 = 0
    for j in range(-80, 1):
        if i+j>=0:
            average2 += monthly_predicted_data_list[i+j].F10_7_obs/81
        else:
            average2 += observed_data_list[i+j+23719].F10_7_obs/81
    monthly_predicted_data_list[i].lst81_obs = average2

for i in range(0, 209): 
    average1 = 0
    if i<209-40:
        for j in range(-40, 41):
            if i+j>=0:
                average1 += monthly_predicted_data_list[i+j].F10_7_adj/81
            else:
                average1 += daily_predicted_data_list[i+j+45].F10_7_adj/81
    else:
        for j in range(-40, 209-i):
            if i+j>=0:
                average1 += monthly_predicted_data_list[i+j].F10_7_adj/(40+209-i)
            else:
                average1 += daily_predicted_data_list[i+j+45].F10_7_adj/(40+209-i)
    monthly_predicted_data_list[i].ctr81_adj = average1
    average2 = 0
    for j in range(-80, 1):
        if i+j>=0:
            average2 += monthly_predicted_data_list[i+j].F10_7_adj/81
        else:
            average2 += observed_data_list[i+j+23719].F10_7_adj/81
    monthly_predicted_data_list[i].lst81_adj = average2




# Open the file for reading and writing
with open('SW-NEW.txt', 'r+') as file:
    # Read the contents of the file
    lines = file.readlines()
    # Iterate over each line
    dum=0
    removalarray = []
    saveline1 = 0
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
            linelist[83:86] = [f"{int(observed_data_list[j].cp//1)}",".", f"{int(10*(observed_data_list[j].cp-int(observed_data_list[j].cp)))}"]
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
                saveline1 = i
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
    saveline2=0
    for i, line in enumerate(lines):
        #print(count1)
        if dum2==0:
            if list(line) == ['B', 'E', 'G', 'I', 'N', ' ', 'D', 'A', 'I', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
                dum2=1
                count1=i
                lastdate = lines[i-4]
                lastyear = int(lastdate[0:4])
                lastmonth = int(lastdate[5:7])
                lastday = int(lastdate[8:10])
                lastdatetime = datetime.datetime(lastyear, lastmonth, lastday)
                lastND = int(lastdate[16:19])
                lastNDyear = int(lastdate[11:15])
                #print('lastdate', lastdatetime.year, lastdatetime.month, lastdatetime.day, lastND, lastNDyear)
        elif list(line) == ['E', 'N', 'D', ' ', 'D', 'A', 'I', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
            saveline2=i
            dum3=1
        if i > count1  and dum3==0 and dum2==1:
            #print(line)
            linelist = list(line)
            nostring = " "
            newdatetime = (lastdatetime+datetime.timedelta(days=j+1))
            newND = (lastND+j)%27 + 1
            newNDyear = lastNDyear + (lastND+j)//27 
            #print(newdatetime.year, newdatetime.month, newdatetime.day, newND)
            #print(linelist[19:21], [f"{daily_predicted_data_list[j].kp[0]//10 if daily_predicted_data_list[j].kp[0]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[0]%10}"])
            linelist[0:4] = [f"{newdatetime.year//1000}", f"{newdatetime.year%1000//100}", f"{newdatetime.year%100//10}", f"{newdatetime.year%10}"]
            linelist[5:7] = [f"{newdatetime.month//10}", f"{newdatetime.month%10}"]
            linelist[8:10] = [f"{newdatetime.day//10}", f"{newdatetime.day%10}"]
            linelist[16:18] = [f"{newND//10  if newND//10 != 0 else nostring}", f"{newND%10}"]
            linelist[11:15] = [f"{newNDyear//1000}", f"{newNDyear%1000//100}", f"{newNDyear%100//10}", f"{newNDyear%10}"]
            linelist[19:21] = [f"{daily_predicted_data_list[j].kp[0]//10 if daily_predicted_data_list[j].kp[0]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[0]%10}"]
            linelist[22:24] = [f"{daily_predicted_data_list[j].kp[1]//10  if daily_predicted_data_list[j].kp[1]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[1]%10}"]
            linelist[25:27] = [f"{daily_predicted_data_list[j].kp[2]//10  if daily_predicted_data_list[j].kp[2]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[2]%10}"]
            linelist[28:30] = [f"{daily_predicted_data_list[j].kp[3]//10  if daily_predicted_data_list[j].kp[3]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[3]%10}"]
            linelist[31:33] = [f"{daily_predicted_data_list[j].kp[4]//10  if daily_predicted_data_list[j].kp[4]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[4]%10}"]
            linelist[34:36] = [f"{daily_predicted_data_list[j].kp[5]//10  if daily_predicted_data_list[j].kp[5]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[5]%10}"]
            linelist[37:39] = [f"{daily_predicted_data_list[j].kp[6]//10  if daily_predicted_data_list[j].kp[6]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[6]%10}"]
            linelist[40:42] = [f"{daily_predicted_data_list[j].kp[7]//10  if daily_predicted_data_list[j].kp[7]//10 !=0 else nostring}", f"{daily_predicted_data_list[j].kp[7]%10}"]
            linelist[43:46] = [f"{(daily_predicted_data_list[j].sum)//100 if daily_predicted_data_list[j].sum//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%100//10 if (daily_predicted_data_list[j].sum)%100//10 !=0 or daily_predicted_data_list[j].sum//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].sum)%10}"]
            linelist[51:54] = [f"{daily_predicted_data_list[j].Ap[1]//100 if daily_predicted_data_list[j].Ap[1]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[1])%100//10 if (daily_predicted_data_list[j].Ap[1])%100//10 !=0 or daily_predicted_data_list[j].Ap[1]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[1]%10}"]
            linelist[47:50] = [f"{daily_predicted_data_list[j].Ap[0]//100 if daily_predicted_data_list[j].Ap[0]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[0])%100//10 if (daily_predicted_data_list[j].Ap[0])%100//10 !=0 or daily_predicted_data_list[j].Ap[0]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[0]%10}"]
            linelist[55:58] = [f"{daily_predicted_data_list[j].Ap[2]//100 if daily_predicted_data_list[j].Ap[2]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[2])%100//10 if (daily_predicted_data_list[j].Ap[2])%100//10 !=0 or daily_predicted_data_list[j].Ap[2]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[2]%10}"]
            linelist[59:62] = [f"{daily_predicted_data_list[j].Ap[3]//100 if daily_predicted_data_list[j].Ap[3]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[3])%100//10 if (daily_predicted_data_list[j].Ap[3])%100//10 !=0 or daily_predicted_data_list[j].Ap[3]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[3]%10}"]
            linelist[63:66] = [f"{daily_predicted_data_list[j].Ap[4]//100 if daily_predicted_data_list[j].Ap[4]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[4])%100//10 if (daily_predicted_data_list[j].Ap[4])%100//10 !=0 or daily_predicted_data_list[j].Ap[4]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[4]%10}"]
            linelist[67:70] = [f"{daily_predicted_data_list[j].Ap[5]//100 if daily_predicted_data_list[j].Ap[5]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[5])%100//10 if (daily_predicted_data_list[j].Ap[5])%100//10 !=0 or daily_predicted_data_list[j].Ap[5]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[5]%10}"]
            linelist[71:74] = [f"{daily_predicted_data_list[j].Ap[6]//100 if daily_predicted_data_list[j].Ap[6]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[6])%100//10 if (daily_predicted_data_list[j].Ap[6])%100//10 !=0 or daily_predicted_data_list[j].Ap[6]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[6]%10}"]
            linelist[75:78] = [f"{daily_predicted_data_list[j].Ap[7]//100 if daily_predicted_data_list[j].Ap[7]//100 != 0 else nostring}",f"{(daily_predicted_data_list[j].Ap[7])%100//10 if (daily_predicted_data_list[j].Ap[7])%100//10 !=0 or daily_predicted_data_list[j].Ap[7]//100 != 0 else nostring}", f"{daily_predicted_data_list[j].Ap[7]%10}"]
            linelist[79:82] = [f"{daily_predicted_data_list[j].avg//100 if daily_predicted_data_list[j].avg//100 !=0 else nostring}", f"{(int(daily_predicted_data_list[j].avg))%100//10 if daily_predicted_data_list[j].avg%100//10 !=0 or daily_predicted_data_list[j].avg//100 !=0 else nostring}", f"{(int(daily_predicted_data_list[j].avg))%10}" ]
            linelist[83:86] = [f"{int(daily_predicted_data_list[j].cp//1)}",".", f"{int(10*(daily_predicted_data_list[j].cp-int(daily_predicted_data_list[j].cp)))}"]
            linelist[87] = f"{daily_predicted_data_list[j].c9//1}"
            linelist[89:92] = [f"{daily_predicted_data_list[j].ISN//100 if daily_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{daily_predicted_data_list[j].ISN%100//10 if (daily_predicted_data_list[j].ISN)%100//10 !=0 or daily_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{(daily_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{int(daily_predicted_data_list[j].F10_7_adj//100) if int(daily_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].F10_7_adj%100//10) if int((daily_predicted_data_list[j].F10_7_adj)%100//10) !=0 or int(daily_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].F10_7_adj)%10)}",".", f"{int((daily_predicted_data_list[j].F10_7_adj-int(daily_predicted_data_list[j].F10_7_adj))*10)}"]
            linelist[99] = f"{daily_predicted_data_list[j].Q//1 if type(daily_predicted_data_list[j].Q) == int else nostring}"
            
            linelist[101:106] = [f"{int(daily_predicted_data_list[j].ctr81_adj//100) if int(daily_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].ctr81_adj%100//10) if int((daily_predicted_data_list[j].ctr81_adj)%100//10) !=0 or int(daily_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].ctr81_adj)%10)}",".", f"{int((daily_predicted_data_list[j].ctr81_adj-int(daily_predicted_data_list[j].ctr81_adj))*10)}"]
            linelist[107:112] = [f"{int(daily_predicted_data_list[j].lst81_adj//100) if int(daily_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].lst81_adj%100//10) if int((daily_predicted_data_list[j].lst81_adj)%100//10) !=0 or int(daily_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].lst81_adj)%10)}",".", f"{int((daily_predicted_data_list[j].lst81_adj-int(daily_predicted_data_list[j].lst81_adj))*10)}"]
            linelist[113:118] = [f"{int(daily_predicted_data_list[j].F10_7_obs//100) if int(daily_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int(daily_predicted_data_list[j].F10_7_obs%100//10) if (int(daily_predicted_data_list[j].F10_7_obs)%100//10) !=0 or int(daily_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int((daily_predicted_data_list[j].F10_7_obs)%10)}",".", f"{int((daily_predicted_data_list[j].F10_7_obs-int(daily_predicted_data_list[j].F10_7_obs))*10)}"]
            
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
                lastdate = lines[i-4]
                lastyear = int(lastdate[0:4])
                lastmonth = int(lastdate[5:7])
                lastday = int(lastdate[8:10])
                lastdatetime = datetime.datetime(lastyear, lastmonth, lastday)
                lastND = int(lastdate[16:19])
                lastNDyear = int(lastdate[11:15])
                #print('lastdate', lastdatetime.year, lastdatetime.month, lastdatetime.day, lastND, lastNDyear)
        elif list(line) == ['E', 'N', 'D', ' ', 'M', 'O', 'N', 'T', 'H', 'L', 'Y', '_', 'P', 'R', 'E', 'D', 'I', 'C', 'T', 'E', 'D', '\n']:
            dum5=1
        if i > count3  and dum5==0 and dum4==1:
            linelist = list(line)
            nostring = " "
            newdatetime = (lastdatetime+relativedelta(months=j+1)+relativedelta(days=-lastdatetime.day+1))
            newND = ((newdatetime-lastdatetime).days + lastND - 1)%27 +1
            newNDyear = lastNDyear + ((newdatetime-lastdatetime).days + lastND)//27
            #print(newdatetime.year, newdatetime.month, newdatetime.day, newND)
            linelist[0:4] = [f"{newdatetime.year//1000}", f"{newdatetime.year%1000//100}", f"{newdatetime.year%100//10}", f"{newdatetime.year%10}"]
            linelist[5:7] = [f"{newdatetime.month//10}", f"{newdatetime.month%10}"]
            linelist[8:10] = [f"{newdatetime.day//10}", f"{newdatetime.day%10}"]
            linelist[16:18] = [f"{newND//10  if newND//10 != 0 else nostring}", f"{newND%10}"]
            linelist[11:15] = [f"{newNDyear//1000}", f"{newNDyear%1000//100}", f"{newNDyear%100//10}", f"{newNDyear%10}"]


            linelist[89:92] = [f"{monthly_predicted_data_list[j].ISN//100 if monthly_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{monthly_predicted_data_list[j].ISN%100//10 if (monthly_predicted_data_list[j].ISN)%100//10 !=0 or monthly_predicted_data_list[j].ISN//100 !=0 else nostring}", f"{(monthly_predicted_data_list[j].ISN)%10}"]
            linelist[93:98] = [f"{int(monthly_predicted_data_list[j].F10_7_adj//100) if int(monthly_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].F10_7_adj%100//10) if int((monthly_predicted_data_list[j].F10_7_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].F10_7_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].F10_7_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].F10_7_adj-int(monthly_predicted_data_list[j].F10_7_adj))*10)}"]
            #linelist[99] = f"{monthly_predicted_data_list[j].Q//1 if type(monthly_predicted_data_list[j].Q) == int else nostring}"
            
            linelist[101:106] = [f"{int(monthly_predicted_data_list[j].ctr81_adj//100) if int(monthly_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].ctr81_adj%100//10) if int((monthly_predicted_data_list[j].ctr81_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].ctr81_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].ctr81_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].ctr81_adj-int(monthly_predicted_data_list[j].ctr81_adj))*10)}"]
            linelist[107:112] = [f"{int(monthly_predicted_data_list[j].lst81_adj//100) if int(monthly_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].lst81_adj%100//10) if int((monthly_predicted_data_list[j].lst81_adj)%100//10) !=0 or int(monthly_predicted_data_list[j].lst81_adj//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].lst81_adj)%10)}",".", f"{int((monthly_predicted_data_list[j].lst81_adj-int(monthly_predicted_data_list[j].lst81_adj))*10)}"]
            linelist[113:118] = [f"{int(monthly_predicted_data_list[j].F10_7_obs//100) if int(monthly_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int(monthly_predicted_data_list[j].F10_7_obs%100//10) if (int(monthly_predicted_data_list[j].F10_7_obs)%100//10) !=0 or int(monthly_predicted_data_list[j].F10_7_obs//100) !=0 else nostring}", f"{int((monthly_predicted_data_list[j].F10_7_obs)%10)}",".", f"{int((monthly_predicted_data_list[j].F10_7_obs-int(monthly_predicted_data_list[j].F10_7_obs))*10)}"]
            
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
#file.close()




# Close files

kp_indeces.close()
SW_F10_predicted.close()

