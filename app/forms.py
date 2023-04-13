from django.forms import ModelForm
from .models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'image',
            'detail',
            'category',
)

class CommentsForm(ModelForm):
    class Meta:
        model=Comments
        fields=('text',)
        def init(self, *args,**kwargs) :
            super().init(self, *args,**kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'    
