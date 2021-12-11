from django.forms import ModelForm
from .models import Article

class CreateArticle(ModelForm) :
    class Meta :
        model = Article
        fields = ["name", "image_post"]
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["name"].label=''
        self.fields["image_post"].label=''
        self.fields["name"].widget.attrs.update({"placeholder":"Create Article Now!", "rows":"5","cols":"10","class":"form-control","class":"mb-3"})
        self.fields["image_post"].widget.attrs.update({"class":"mb-3", "class" :"form-control"})