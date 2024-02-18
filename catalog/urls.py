from django.urls import path

from catalog.views import index, home, contacts

urlpatterns = [
    # path("", index, name='catalog'),
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]