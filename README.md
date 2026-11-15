# Ex.03 Design a Website for Server Side Processing
## Date: 10.11.2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
math.html
<html>
    <head><title>calculator</title></head>
    <body>
        <h1 align="center"> Dinesh 26019310</h1>
        <h2 align="center"> GST Calculator</h2>
        <form method="POST">{%csrf_token%}<br><br>
            <label>Price </label>
            <input type="text"  name="price" value="{{P1}}"><br><br>
            <label>GST </label>
            <input type="text"  name="gst" value="{{G1}}"><br><br>
            <input type="submit" value="Calculate"><br><br>
            <label>Bill Amount</label>
            <label>Bill Amount : {{bill1}}</label>

        </form>
    </body>
</html>

views.py

from django.shortcuts import render
def calculate(request):
    P = float(request.POST.get('price', '0'))
    G = float(request.POST.get('gst', '0'))
    bill = P + (P * G / 100) if request.method == 'POST' else 0
    print("Price : ",P)
    print("GST : ",G)
    print("Bill Amount : ",bill)
    return render(request, 'areaapp/math.html',{ 'P1' : P, "G1" : G, 'bill1' : bill})

urls.py

from django.contrib import admin
from django.urls import path
from areaapp import views

urlpatterns = [path('', views.calculate, name='calculate')]



```



## OUTPUT - SERVER SIDE:
![alt text](<server side ss.png>)

## OUTPUT - WEBPAGE:
![alt text](<homepage ss.png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
