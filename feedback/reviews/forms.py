from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name",
        max_length=200,
        error_messages={
            "required": "Xour name must not be empty!",
            "max_length": "Please enter a shorter name!",
        })
