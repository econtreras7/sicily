from django import forms

class ContactForm(forms.Form):
  #  name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class BookForm(BSModalForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']