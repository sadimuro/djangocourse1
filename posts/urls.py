from django.urls import path

from posts.views import hello, get_index, get_about, get_contacts

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path("about/", get_about, name="about-page"),
    path("contacts/", get_contacts, name="contacts-page"),
]