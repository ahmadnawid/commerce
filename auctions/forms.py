from django import forms
from .models import Listing, Bid

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"

class NewBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('currentbid',)