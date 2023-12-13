from django.urls import path
from .views import contact_list, create_contact, contact_details, edit_contact, delete_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('create', create_contact, name='create_contact'),
    path('contact_details/<int:pk>/', contact_details, name='contact_details'),
    path('edit_contact/<int:pk>/edit/', edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/delete/', delete_contact, name='delete_contact'),
]