from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget= forms.widgets.Textarea(
            attrs={
                'placeholder': "Write something cool...",
                "class":"textarea is-success is-medium",
            }
        ),
        label='',
    )

    class Meta:
        model = Post
        exclude = ("user",'likes')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)