from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, home, contacts, product, product_item, confections, condiments, beverages

#app_name = CatalogConfig

urlpatterns = [
    # path("", index, name='catalog'),
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/", product, name="product"),
    path("product/<int:pk>/", product_item, name="product_<int:pk>"),
    path("beverages/", beverages, name="beverages"),
    path("condiments/", condiments, name="condiments"),
    path("confections/", confections, name="confections"),
]