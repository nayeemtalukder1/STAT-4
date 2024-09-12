class ProfileView(View):
  def get(self,request):
    form = CustomerProfileForm(request.POST, request.FILES)
    return render(request, 'app/profile.html',locals())
  def post(self,request):
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

      reg = Student.objects.create(user=user,name=name,university_name=university_name,department=department,batch=batch,roll=roll,address=address,student_img=student_img)
      reg.save()
      messages.success(request, "Congratulation! Profils Save Success")

    else:
      print(form.errors)
      messages.warning(request,"invalid Input Data")
    return render(request, 'app/profile.html',locals())
  