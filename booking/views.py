from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth as authe
from logins import views as v
user = {}

# Create your views here.
config = {
    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com/",
    'projectId': "software-engineering-6e9a7",
    'storageBucket': "software-engineering-6e9a7.appspot.com",
    'messagingSenderId': "329135496498"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
def book(request):
    return render(request,'flight_bookings/book.html')
def postbooking(request):
    begin = request.POST.get("from")
    to = request.POST.get("to")
    date = request.POST.get("Date")
    passengers = request.POST.get("pass")
    data = { 'from' :begin,
              'to' :to,
              'date': date,
              'passengers': passengers
            }
    if 'uid' in request.session :
        print("\n\n\n\n")
        print()
        request.session['b_no']+=1
        db.child("users").child(request.session['key']).child("journey").push(data)
        j=0
        d={}
        for i in db.child('available').get().each():
            print(i.val())
            d[j]=i.val()
            j+=1
        return render(request, 'flight_bookings/show.html',{'all': d})
    else:
        return redirect(reverse(v.signin))
def seat(request):
    return render(request,'seat.html')
def details(request):
    print(request.session['key'])
    x = db.child('users').child(request.session['key']).child('journey').get()
    w ={}
    for i in x.each():
        w=(i.val())


    print('x value \n\n\n\n\n\n')
    print('hello \n',w)
    return render(request,'details.html', w)
def done(request):
    seats=[]
    for i in range(1,13):
        y = request.POST.get(str(i))
        if y=='on':
            seats.append(i)
    db.child('users').child(request.session['key']).child('journey').child('seats').set(seats)
    print(y)
    return HttpResponse(y)
