from django.shortcuts import render
import pandas as pd
import csv
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def vote(request):
     return  render(request,'vote.html')
def poll(request):
    user_index=0
    if request.method=='POST':
        name=request.POST['name']
        userid=request.POST['id']
        df=pd.read_csv('/Users/hashiqmohammed/Desktop/people.csv')
        if name in df.values:
            df1=df.loc[df.name == name]
            print(df1)

            if int(userid) in df1.values:
                if int(df1["voted"])==0:
                    r = csv.reader(open('/Users/hashiqmohammed/Desktop/people.csv')) # Here your csv file
                    lines = list(r)
                    print(lines)
                    for sub_list in lines:
                        if name in sub_list:
                            user_index=lines.index(sub_list)
                    lines[user_index][2]=1
                    writer = csv.writer(open('/Users/hashiqmohammed/Desktop/people.csv', 'w'))
                    writer.writerows(lines) 
                    return  render(request,'poll.html')
                else:
                    messages.info(request,'Already voted')
                    return redirect('/')
            else:
                messages.info(request,'You have no vote')
                return redirect('/')
        else:
            messages.info(request,'You have no vote')
            return redirect('/')
    else:  
        return  render(request,'vote.html')
def ended(request):
     voted = request.GET.get('polledtowhom')
     print(voted)
     r = csv.reader(open('/Users/hashiqmohammed/Desktop/result.csv')) # Here your csv file
     lines = list(r)
     print(lines)
     lines[int(voted)][2]=int(lines[int(voted)][2])+1
     writer = csv.writer(open('/Users/hashiqmohammed/Desktop/result.csv', 'w'))
     writer.writerows(lines) 
     return  render(request,'end.html')