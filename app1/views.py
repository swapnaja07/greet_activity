from django.shortcuts import render
from datetime import datetime
# Create your views here.
def greet(request):
    date=datetime.now()
    #print(date)
    msg="Hello Guest !!! Very Good"
    h=int(date.strftime("%H"))
    if h<12:
        msg += "Morning!!!"
    elif h<16:
        msg += "Afternoon!!!"
    else:
        msg += "Evening !!!"
    return render(request, "greet.html",{"data":msg, "date":date})