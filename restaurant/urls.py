from django.urls import path, include
from . import views
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet


router = DefaultRouter()
router.register('', BookingViewSet)

urlpatterns = [
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('bookings', views.bookings, name='bookings'), 
    path('', views.index, name="home"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('reservations/', views.reservations, name="reservations"),

    # API paths
    path('api-token-auth/', obtain_auth_token),
    path('booking/tables/', include(router.urls)),
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
]