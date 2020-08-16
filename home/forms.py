from .models import Post,Comments, Video
from django import forms

class HomeForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('post',)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('text',)


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ("name", "videofile")
        # fields= '__all__'
