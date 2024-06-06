from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
