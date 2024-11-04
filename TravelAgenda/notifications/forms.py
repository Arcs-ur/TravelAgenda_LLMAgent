from django import forms

class NotificationForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='消息内容', max_length=500)
