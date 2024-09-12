from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User

from . models import Student,BlogPost,Gallery,PDFDocument

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))



class CustomerRegistrationForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete': 'current-password','class':'form-control'}))
  new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
  new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
  new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
  new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Student
    fields=['name','university_name','department','batch','roll','address','phone','student_img']
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control'}),'university_name':forms.TextInput(attrs={'class':'form-control'}),'department':forms.TextInput(attrs={'class':'form-control'}),'batch':forms.TextInput(attrs={'class':'form-control'}),'roll':forms.NumberInput(attrs={'class':'form-control'}),
      'address':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.TextInput(attrs={'class':'form-control'}),
      'student_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      
    }


#post
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
        widgets={
          'title':forms.TextInput(attrs={'class':'form-control'}),'content':forms.Textarea(attrs={'class':'form-control'}),
          'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      
    }
        

#gallery
class AddGalleryForm(forms.ModelForm):
  class Meta:
    model = Gallery
    fields=['gallery_img']
    widgets={
      'gallery_img':forms.ClearableFileInput(attrs={'class':'form-control'}),
    }

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'document']
        widgets={
          'title':forms.TextInput(attrs={'class':'form-control'}),
          'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      
    }

        

