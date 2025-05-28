from django.urls import path
from .import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('faq',views.faq,name='faq'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('profile',views.profile,name='profile'),
    path('bookings',views.bookings,name='booking'),
    path('check-username/', views.check_username, name='check_username'),
    path('check-email/', views.check_email, name='check_email'),
    path('dashboard',views.dashboard,name='dashboard'),
    path("query/places/<str:q>", views.query, name="query"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path("flight/ticket/payment", views.payment, name="payment"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('flight/ticket/print',views.get_ticket, name="getticket"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('ticket/cancel', views.cancel_ticket, name="cancelticket"),
    path('flight/ticket/resume', views.resume_booking, name="resumebooking"),


]

