from django.forms import ModelForm, Textarea, RadioSelect
from .models import Review
from django_lookup_table_rating_widget.widgets import DjangoLookupTableRatingWidget

class ReviewForm(ModelForm):
    class Meta:
        RATING_CHOICES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
        model = Review
        fields = ['rating', 'title', 'summary', 'ipAddress' , 'company']
        widgets = {
            'summary': Textarea(attrs={'cols': 80, 'rows': 20}),
            'rating':RadioSelect(choices=RATING_CHOICES)   
        }