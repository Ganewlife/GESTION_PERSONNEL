from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from . import forms, models

# Create your views here
class LoginPageView(View):
    template_name = 'stagiaire_app/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
def logout_user(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)# on connect l'utilisateur
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'stagiaire_app/signup.html', context={'form': form})

@login_required
def user_profil(request):
    return render(request, 'stagiaire_app/user_profil.html')

# Decorator don't forget it
@login_required
def stagiaire_and_files_upload(request):
    stagiaire_form = forms.StagiaireForm(use_required_attribute=False)
    if request.method == 'POST':
        stagiaire_form = forms.StagiaireForm(request.POST, request.FILES)
        if stagiaire_form.is_valid():
            stagiaire = stagiaire_form.save()
            return redirect('home')
    context = {
        'stagiaire_form': stagiaire_form}
    return render(request, 'stagiaire_app/create.html', context=context)

@login_required
def home(request):
    stagiaires = models.StagiaireInfo.objects.all()
    context={'stagiaires': stagiaires}
    return render(request, 'stagiaire_app/home.html', context=context)

@login_required
def view_stagiaire_info(request, stagiaire_info_id):
    infos = get_object_or_404(models.StagiaireInfo, id=stagiaire_info_id)
    return render(request, 'stagiaire_app/home.html', {'infos': infos})

@login_required
def edit_stagiaire_info(request, stagiaire_info_id):
    stagiaire_info = get_object_or_404(models.StagiaireInfo, id=stagiaire_info_id)
    edit_form = forms.StagiaireForm(instance=stagiaire_info)
    delete_form = forms.DeleteStagiaireForm()
    if request.method == 'POST':
        if 'edit_stagiaire' in request.POST:
            edit_form = forms.StagiaireForm(request.POST,request.FILES, instance=stagiaire_info)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_stagiaire' in request.POST:
            delete_form = forms.DeleteStagiaireForm(request.POST, request.FILES)
            if delete_form.is_valid():
                stagiaire_info.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'stagiaire_info':stagiaire_info}
    return render(request, 'stagiaire_app/update.html', context=context)
    