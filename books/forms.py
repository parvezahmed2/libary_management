from django import forms
from .models import Review




class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [  'comment']


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())


