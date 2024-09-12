from django.db.models import Count
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import logout

from . forms import CustomerRegistrationForm,CustomerProfileForm,AddGalleryForm,BlogPostForm
from . models import Student,Gallery,NumberArray,Model
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


from django.http import JsonResponse
from statistics import mean, median, mode, StatisticsError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




def models_list(request):
    models = Model.objects.all()
    return render(request, 'app/models_list.html', {'models': models})

def models_details(request, id):
    model = get_object_or_404(Model, id=id)
    return render(request, 'app/models_details.html', {'model': model})



def add_numbers(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        data = request.POST.get('data', '[]')
        numbers = list(map(int, data.strip('[]').split(',')))

        number_array = NumberArray.objects.create(name=name, data=numbers)
        return JsonResponse({'id': number_array.id, 'name': number_array.name, 'data': number_array.data})

    return render(request, 'app/add_numbers.html')

def view_numbers(request, pk):
    number_array = get_object_or_404(NumberArray, pk=pk)
    numbers = number_array.data

    try:
        stats = {
            'mean': mean(numbers),
            'median': median(numbers),
            'mode': mode(numbers),
            'count': len(numbers),
        }
    except StatisticsError as e:
        stats = {'error': str(e)}

    return JsonResponse({'id': number_array.id, 'name': number_array.name, 'data': number_array.data, 'stats': stats})

def list_numbers(request):
    number_arrays = NumberArray.objects.all()
    paginator = Paginator(number_arrays, 10)  # Show 10 arrays per page

    page = request.GET.get('page')
    try:
        arrays = paginator.page(page)
    except PageNotAnInteger:
        arrays = paginator.page(1)
    except EmptyPage:
        arrays = paginator.page(paginator.num_pages)

    return render(request, 'app/list_numbers.html', {'arrays': arrays})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # Assuming you have user authentication
            new_post.save()
            return redirect('blog_list')  # Redirect to blog list page
    else:
        form = BlogPostForm()
    return render(request, 'app/blog_create.html', {'form': form})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'app/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'app/blog_detail.html', {'post': post})



def home(request):
  return render(request,"app/home.html")


def about(request):
  return render(request,"app/about.html")

def LogoutPage(request):
  logout(request)
  return redirect('login')

def gallery(request):
  image = Gallery.objects.all()
  return render(request,'app/gallery.html',locals())

def AddGallery(request):
  if request.method == "POST":
    form = AddGalleryForm(request.POST, request.FILES)
    
    if form.is_valid():
        image_upload = form.save(commit=False)
        image_upload.user = request.user
        image_upload.save()
        return redirect('gallery')
  else:
    form = AddGalleryForm()
  return render(request,'app/addgallery.html',locals())
  
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            university_name = form.cleaned_data['university_name']
            department = form.cleaned_data['department']
            batch = form.cleaned_data['batch']
            roll = form.cleaned_data['roll']
            address = form.cleaned_data['address']
            student_img = form.cleaned_data['student_img']

            reg = Student.objects.create(user=user, name=name, university_name=university_name, department=department, batch=batch, roll=roll, address=address, student_img=student_img)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        return render(request, 'app/profile.html', locals())

  


class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html',locals())
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Congrations ! User Register Successfully")
    else:
      messages.warning(request,"Invalid Input Data")

    return render(request, 'app/customerregistration.html',locals())
  

def address(request):
  add = Student.objects.filter(user=request.user)
  return render(request, 'app/address.html',locals())


class updateAddress(View):
  def get(self,request,pk):
    add = Student.objects.get(pk=pk)
    form = CustomerProfileForm(instance=add)
    return render(request, 'app/updateaddress.html',locals())
  def post(self,request,pk):
    form = CustomerProfileForm(request.POST, request.FILES)
    if form.is_valid():
      add = Student.objects.get(pk=pk)
      add.name = form.cleaned_data['name']
      add.university_name = form.cleaned_data['university_name']
      add.department = form.cleaned_data['department']
      add.batch = form.cleaned_data['batch']
      add.roll = form.cleaned_data['roll']
      add.address = form.cleaned_data['address']
      add.student_img = form.cleaned_data['student_img']
      add.save()
      messages.success(request,"Congratulations! Profile Update Successfully")
    else:
      messages.warning(request,"Invalid Input Data")
    return redirect("address")
  

