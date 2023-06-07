from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from .forms import NewListingForm, NewBidForm
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Category, Bid, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "listing": Listing.objects.all()
    })

def category(request):
    pass

def listing(request, listing_id):

    if request.method == "POST":
        bid_form = Bid.objects.get(id=listing_id)
        bid_form.currentbid = request.POST["currentbid"]
        #if bid_form.is_valid():
        bid_form.save()
        return HttpResponseRedirect(reverse("index"))

    listing = Listing.objects.get(id=listing_id)
    #bids = Bid.objects.get(id=listing_id)
    bid_form = NewBidForm()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bids": bid_form
    })


def createlist(request):
    if request.method == "POST":
        listing_form = NewListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            listing_form.save()
            
        return HttpResponseRedirect(reverse("index"))
    listing_form = NewListingForm()
    return render(request, "auctions/createlist.html", context={'listing_form':listing_form })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



@login_required
def add_watchlist(request, listing_id):
    item_to_save = Listing.objects.get(id=listing_id)
    watched = Watchlist.objects.filter(user=request.user, item=listing_id)

    if request.method == 'POST':
        if watched.exists():
            watched.delete()
            messages.success(request, 'Listing removed from watchlist')
            # messages.add_message(request, messages.ERROR, "Successfully deleted from your watchlist")
            return HttpResponseRedirect(reverse("watchlist"))
            
        else:
            watched, created = Watchlist.objects.get_or_create(user=request.user)
            watched.item.add(item_to_save)
            messages.success(request, 'Listing removed from watchlist')
            # messages.add_message(request, messages.SUCCESS, "Successfully added to your watchlist")
            return redirect('index')
    else:
        return HttpResponseRedirect(reverse("watchlist")) 




@login_required
def watchlist(request):
    watchlists = Watchlist.objects.all()
    context = {'watchlists':watchlists}
    return render(request, 'auctions/watchlist.html', context) 

