"""URLS Config of Pages Main"""

# Libraries
from django.urls import path, include

# View
from .views import home_page

app_name = "pages"
urlpatterns = [
    path("", home_page, name="home"),
]
