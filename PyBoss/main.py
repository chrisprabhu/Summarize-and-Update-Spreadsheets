
# coding: utf-8

# In[249]:


import os
import csv
import string
import datetime


# In[250]:


csvpath = os.path.join("Resources", "employee_data1.csv")


# In[251]:


stateAb = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine', 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',    
         'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming']


# In[252]:


names = []
newSocial = []
newState = []
first_name = []
last_name = []
emp_id = []
new_dob = []
cleaned_csv = []
with open(csvpath) as csvfile:
    csvobject = csv.reader(csvfile)
    next(csvobject, None)
    
    for row in csvobject:
        names.append(row[1].split(" "))
        oldDateFormat = datetime.datetime.strptime(row[2],'%Y-%m-%d')
        new_dob.append(datetime.datetime.strftime(oldDateFormat,'%m/%d/%Y'))
        newSocial.append("***-**" + row[3][6:11])
        newState.append(stateAb[states.index(row[4])])
        emp_id.append(row[0])


# In[253]:


first_name, last_name = zip(*names)


# In[254]:


cleaned_csv = zip(emp_id, first_name, last_name, new_dob, newSocial, newState)


# In[255]:


output_file = os.path.join("cleaned_csv.csv")


# In[256]:


with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(cleaned_csv)

