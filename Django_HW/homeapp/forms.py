from django.forms import ModelForm
from .models import Article


class Articleform(ModelForm): 
    class Meta:
        model = Article
        fields = ['title', 'description', 'views', 'is_published', 'create_date']