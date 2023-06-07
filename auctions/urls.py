from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("category", views.category, name="category"),
    path("createlist", views.createlist, name="createlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("add_watchlist/<int:listing_id>/", views.add_watchlist, name="add_watchlist"),
]
