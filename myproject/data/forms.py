from django.forms import ModelForm, Textarea
from .models import Review
from django_lookup_table_rating_widget.widgets import DjangoLookupTableRatingWidget

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'summary', 'ipAddress' , 'company']
        widgets = {
            'summary': Textarea(attrs={'cols': 80, 'rows': 20}),
            
        }