
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csvpath = os.path.join('Resources', 'budget_data_1.csv')


# In[3]:


numberofmonths = 0
totalrevenue = 0
changeinrevenuelist = []
namelist = []
temp = 0

with open(csvpath) as csvfile:
    csvobject = csv.reader(csvfile)
    next(csvobject, None) 
    
    for row in csvobject:
            numberofmonths = numberofmonths + 1
            totalrevenue = totalrevenue + int(row[1])
            changeinrevenuelist.append(int(row[1]) - temp)
            temp = int(row[1])  
            namelist.append(row[0])        


# In[4]:


absValChangeInRevenue = []
for x in changeinrevenuelist:
        absValChangeInRevenue.append(abs(x))


# In[5]:


averagechange = sum(absValChangeInRevenue) / len(changeinrevenuelist)


# In[6]:


print("Financial Analysis")
print('--------------------------')
print('Total Months:' + str(numberofmonths))
print('Total Revenue:' + str(totalrevenue))
print('Average Revenue Change:' + str(averagechange))
print('Greatest Increase in Revenue:' + namelist[changeinrevenuelist.index(max(changeinrevenuelist))] + " (" + str(changeinrevenuelist[changeinrevenuelist.index(max(changeinrevenuelist))]) + ")" )
print('Greatest Decrease in Revenue:' + namelist[changeinrevenuelist.index(min(changeinrevenuelist))] + " (" + str(changeinrevenuelist[changeinrevenuelist.index(min(changeinrevenuelist))]) + ")" )


# In[7]:


file = open('Financial_Analysis.txt','w')
file.write(
"Financial Analysis\n" +
'--------------------------\n' +
'Total Months:' + str(numberofmonths) + '\n' +
'Total Revenue:' + str(totalrevenue) + '\n' +
'Average Revenue Change:' + str(averagechange) + '\n' +
'Greatest Increase in Revenue:' + namelist[changeinrevenuelist.index(max(changeinrevenuelist))] + " (" + str(changeinrevenuelist[changeinrevenuelist.index(max(changeinrevenuelist))]) + ")" + '\n' + 
'Greatest Decrease in Revenue:' + namelist[changeinrevenuelist.index(min(changeinrevenuelist))] + " (" + str(changeinrevenuelist[changeinrevenuelist.index(min(changeinrevenuelist))]) + ")"
)
file.close()

