from django.urls import path

from posts.views import hello, IndexView, AboutView, get_contacts, PostDetailView, PostCreateView, PostDeleteView, \
    PostUpdateView

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", IndexView.as_view(), name="index-page"),
    path("about/", AboutView.as_view(), name="about-page"),
    path("contacts/", get_contacts, name="contacts-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
]