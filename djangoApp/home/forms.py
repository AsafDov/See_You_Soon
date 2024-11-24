from django import forms
from home.models import User, Friend, Meeting

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Create new user", max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'Create new user',  # Grayed-out text
            }))
    
    class Meta:
        model = User
        fields = ["username"]

class FriendForm(forms.ModelForm):
	name = forms.CharField(label="Create new friend", max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'Create new friend'  # Grayed-out text
    }))

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user", None)
		super().__init__(*args, **kwargs)
		if self.user:
			self.fields["username"] = user
	
	class Meta:
		model = Friend
		fields = ['name']
        
	

class MeetingForm(forms.ModelForm):

	friend = forms.ModelChoiceField(
		queryset=Friend.objects.none(),  # Default to an empty queryset
		empty_label="Add a meeting with",
		widget=forms.Select(attrs={'class': 'form-control'}))  # Optional styling)


	date = forms.DateField(label="Create new", widget=forms.DateInput(attrs={
		"type" : "date",
		'placeholder': 'When did you meet?',  # Grayed-out text
		'class': 'form-control'
	}))
	def __init__(self, *args, **kwargs):
	# Capture the user instance passed during form initialization
		user = kwargs.pop('user', None) 
		# print(user)
		super().__init__(*args, **kwargs)
		if user:
		# Filter the category queryset to only include categories for the given user
			self.fields['friend'].queryset = Friend.objects.filter(username=user)

	class Meta:
		model = Meeting
		fields = ["friend","date"]

class FriendForm(forms.ModelForm):
	name = forms.CharField(label="Create new friend", max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'Create new friend'  # Grayed-out text
    }))

	def __init__(self, *args, **kwargs):
		user = kwargs.pop("user", None)
		super().__init__(*args, **kwargs)
		if user:
			self.fields["username"] = user
	
	class Meta:
		model = Friend
		fields = ['name']


class AddFriendForm(forms.ModelForm):
	name = forms.CharField(label="Create new friend", max_length=100, widget=forms.TextInput(attrs={
            'placeholder': '',  # Grayed-out text
			'class': 'form-control'
    }))

	date = forms.DateField(label="Last meeting date" , widget=forms.DateInput(attrs={
		"type" : "date",
		'placeholder': 'When did you meet?',  # Grayed-out text
		'class': 'form-control'
	}))
	details = forms.CharField(label="Details",required=False,widget=forms.Textarea(attrs={'class': 'form-control'}))
			

	class Meta:
		model = Meeting
		fields = ["date"]