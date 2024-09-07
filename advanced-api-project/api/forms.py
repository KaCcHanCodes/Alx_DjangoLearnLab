from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    author = forms.CharField(label='author', max_length=100)
    publication_year = forms.IntegerField(label='publication_year', max_length=100)