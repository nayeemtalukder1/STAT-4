from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm


urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('gallery/', views.gallery,name="gallery"),
    path('addgallery/', views.AddGallery,name="addgallery"),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('models/', views.models_list, name='models_list'),
    path('models/<int:id>/', views.models_details, name='models_details'),

     path('add/', views.add_numbers, name='add_numbers'),
    path('view/<int:pk>/', views.view_numbers, name='view_numbers'),
    path('list/', views.list_numbers, name='list_numbers'),

    
     path('registration/', views.CustomerRegistrationView.as_view(),name="customerregistration"),
     path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name="login"),

     path('profile/', views.ProfileView.as_view(),name="profile"),
    path('address/', views.address,name="address"),
    path('updateaddress/<int:pk>', views.updateAddress.as_view(),name="updateaddress"),
     

     path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name="passwordchange"),
     path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="passwordchangedone"),
      path('logout/',views.LogoutPage, name='logout'),


      path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm),name="password_reset"),

     path('password-reset/done',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),

     path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name="password_reset_confirm"),

     path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password_reset_complete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

