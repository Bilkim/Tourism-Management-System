from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from vacations.models import MemberUsers, Packages
from vacations.forms import PackageForm
from django.contrib.auth.models import User
from hotels.models import SpecialRooms, HotelMembers
from dashboard.models import CustomerChoice
from hotels.forms import RoomForm
from hotels.models import HotelMembers, SpecialRooms
from hotels.forms import UserFilter

# Create your views here.

def payment(request, packages_id):
    package = Packages.objects.get(pk=packages_id)
    price = package.latestPrice 
    user = User.objects.all() 
    
    user = request.user
    user.save()
    
    members_list = MemberUsers.objects.all()       
    memb_filter = UserFilter(request.GET, queryset = members_list)  
    
    
    attendees = members_list[0].members    
    totalPrice = price * attendees       
    dollarPrice = totalPrice/100 
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
       dis =  PackageForm(request.POST or None)
       if dis.is_valid():
           instance = dis.save(commit=False)
           instance.user = request.user
           instance.save()
       return redirect('payment:payment')
    else:
        instance= PackageForm
        
    context={'instance':instance}     
    

    
    return render (request, 'paymbase.html',
           {'package': package, 'user': user, 'context' : context, 'filter': memb_filter, 'att': attendees,'price': totalPrice, 'price2': dollarPrice})


def hotelPayment(request, hotel_id):
    hotel = SpecialRooms.objects.get(pk=hotel_id)
    price = SpecialRooms.price  
    
    users = request.user
    users.save()
    
    hotel_list = HotelMembers.objects.all()
    hotel_filter = UserFilter(request.GET, queryset = hotel_list)    
    members_list = MemberUsers.objects.all()         

    totalFamily = members_list[0].members
    totalPrice = price     
    dollarPrice = totalPrice
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
       dis =  RoomForm(request.POST or None)
       if dis.is_valid():
           instance = dis.save(commit=False)
           instance.user = request.user
           instance.save()
       return redirect('payment:payment')
    else:
        instance= RoomForm
        
    context={'instance':instance}  
    

    
    return render (request, 'hotelPayment.html',
           {'hotels': hotel,'hotelList': hotel_list, 'user': users,'family': totalFamily, 'hotelFilter': hotel_filter ,'roomPrice': totalPrice, 'roomPrice2': dollarPrice, 'context':context})

