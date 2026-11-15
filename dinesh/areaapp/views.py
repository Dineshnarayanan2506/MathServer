from django.shortcuts import render
def calculate(request):
    P = float(request.POST.get('price', '0'))
    G = float(request.POST.get('gst', '0'))
    bill = P + (P * G / 100) if request.method == 'POST' else 0
    print("Price : ",P)
    print("GST : ",G)
    print("Bill Amount : ",bill)
    return render(request, 'areaapp/math.html',{ 'P1' : P, "G1" : G, 'bill1' : bill})



