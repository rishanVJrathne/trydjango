from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


    def clean(self):
        title = self.cleaned_data.get('title')
        if title == "office":
            self.add_error('title', "office for title is not valid")
            raise forms.ValidationError("office for title is not valid")
