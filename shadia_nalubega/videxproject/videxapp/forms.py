from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'quality', 'date_of_publishing', 'video_file', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Video Title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'input-field',
                'placeholder': 'Description (Optional)',
                'rows': 5,
            }),
            'quality': forms.Select(attrs={
                'class': 'quality-select',
            }),
            'date_of_publishing': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date',
            }),
            'video_file': forms.FileInput(attrs={
                'id': 'inp-video',
                'accept': 'video/*',
                'style': 'display:none',
            }),
            'thumbnail': forms.FileInput(attrs={
                'id': 'inp-thumb',
                'accept': 'image/*',
                'style': 'display:none',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['quality'].empty_label = 'Video quality'