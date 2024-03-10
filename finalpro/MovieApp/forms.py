from django import forms

from .models import Movie,MovieComment


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','image','description']

class CommentMovieForm(forms.ModelForm):
    class Meta:
        model=MovieComment
        fields=['comment']