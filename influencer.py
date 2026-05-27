#Christina Y

import pandas as pd

data=pd.read_csv('influence.csv')

months=data['Month'].tolist()
views=data['Views'].tolist()
dislikes=data['Dislikes'].tolist()
subs=data['Subscriber(+-)'].tolist()
revenue=data['Revenue'].tolist()

filter=[]

def find_views(number_views):
    for i in range(len(views)):
        if views[i]<= number_views:
            filter.append([i])
    print(filter)
    filter.clear()

def golden(subscribes):
    for i in range(len(subs)):
        if subs[i]>= subscribes:
            filter.append([i])
    print(filter)
    filter.clear()

def scandal(down):
    for i in range(len(revenue)):
        if revenue[i]<=down:
            filter.append([i])
    print(filter)
    filter.clear()

#Main

find_views(2000)
print(data.loc[[0,1,2,3,4,5,6,7,8,9,10]])
golden(50000)
print(data.loc[[54,65,66,67,68,69,70,71,72]])
scandal(0)
print(data.loc[[64,65,66,67,68,69,70,71,72,98,10]])
