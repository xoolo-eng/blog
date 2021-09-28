from django import forms
from blog.models import Post


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "text", "tags", "author")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "id": "title",
                    "class": "form-control",
                    "placeholder": "Post Title",
                    "onfocus": "this.placeholder = ''",
                    "onblur": "this.placeholder = 'Post Title'",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "id": "text",
                    "class": "form-control",
                    "placeholder": "Post Content",
                    "onfocus": "this.placeholder = ''",
                    "onblur": "this.placeholder = 'Post Content'",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "id": "tags",
                    "class": "form-control",
                }
            ),
        }
