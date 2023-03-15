from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from posts.forms import CommentForm, PostForm
from posts.models import Post, Comment


def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek TEST</title>
    #         </head>
    #         <body>
    #
    #             <h1>Заголовок первого уровня</h1>
    #             <p>Параграф</p>
    #
    #         </body>
    #     </html>
    # """
    headers = {
        "name": "Alex",
    }
    # "Content-Type": "application/vnd.ms-excel",
    # "Content-Disposition": "attachment; filename=file.xls"}
    return HttpResponse(body, headers=headers, status=500)


# def get_index(request):
#     posts = Post.objects.filter(status=True)
#     context = {
#         "title": "Main page",
#         "posts": posts,
#     }
#     return render(request, "posts/index.html", context=context)

class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    # model = Post
    template_name = "posts/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Главная страница"

        return context


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"

    def post(self, request, pk):
        # post_id = request.POST.get("post_id", None)

        post = Post.objects.get(pk=pk)  # Или post_id, если бы не было pk, нужен input hidden
        form = CommentForm(request.POST)

        # name = request.POST.get("name", None)
        # text = request.POST.get("text", None)

        # if name and text:
        #     comment = Comment.objects.create(name=name, text=text, post=post)
        #     comment.save()

        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()

        return redirect("post-detail", pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["title"] = "Просмотр поста"
        return context


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("index-page")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }


# CRUD - Create, Retrieve, Update, Delete

# def get_about(request):
#     context = {
#         "title": "Страница о нас",
#     }
#     return render(request, "posts/about.html", context=context)


def get_contacts(request):
    return render(request, "posts/contacts.html", {"title": "Контакты"})