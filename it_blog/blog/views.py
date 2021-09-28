from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormView
from blog.forms import CreatePost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Post


# def blogs_page(request):
#     return render(request, "all_blogs.html", {})


class AllPosts(ListView):
    paginate_by = 2
    model = Post
    template_name = "all_blogs.html"




class NewPost(LoginRequiredMixin, FormView):
    template_name = "create_blog.html"
    form_class = CreatePost
    login_url = '/user/login/'
    success_url = "/blog/"

    def form_valid(self, form):
        if form.cleaned_data["author"] == self.request.user:
            form.save()
            return super().form_valid(form)
        return HttpResponseForbidden()
