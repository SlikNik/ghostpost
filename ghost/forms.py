from django import forms
from ghost.models import GhostPost


TRUE_FALSE_CHOICES = (
    (True, 'Boast'),
    (False, 'Roast')
)
class GhostPostForm(forms.ModelForm):
    class Meta:
        model = GhostPost
        exclude = ('up_votes', 'down_votes', 'post_date', 'secret')
        widgets = {
            'type_of_post': forms.Select(choices=TRUE_FALSE_CHOICES)
        }

