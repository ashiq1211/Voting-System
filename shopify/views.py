from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import pandas as pd
import csv
from calc.models import Destination
# Create your views here.
def home(request):
     df=pd.read_csv("/Users/hashiqmohammed/Desktop/shopifynew.csv")
     df=df.loc[df.Size=="S"]
     print(df)
     
     item=df.values.tolist()
     print(item)
     return render(request, 'allDress.html', {"items": item })
    
def viewProduct(request):
     selectedItem=[]  
     itemId = request.GET.get('productId')
     itemNameAndSize=request.GET.get('productNameAndSize')
     print(itemId)
     print(itemNameAndSize)
     if itemId is not None:

          print(itemId)
          r = csv.reader(open("/Users/hashiqmohammed/Desktop/shopifynew.csv")) # Here your csv file
          item= list(r) 
          
          for product in item:
               if product[0]==itemId:
                    selectedItem=product
          return render(request, 'viewProduct.html',{"item":selectedItem} )
     elif itemNameAndSize is not None:
          
          r = csv.reader(open("/Users/hashiqmohammed/Desktop/shopifynew.csv")) # Here your csv file
          item= list(r)

          # if itemNameAndSize
          print(itemNameAndSize.split(" ",1))
          for product in item:
               if  itemNameAndSize.split(" ",1)[0]==product[2] and itemNameAndSize.split(" ",1)[1]==product[1]:
                    selectedItem=product


          return render(request, 'viewProduct.html',{"item":selectedItem} )

  
     
