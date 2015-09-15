
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden
from main.models import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from main.forms import *
from task.views import *
from med3Dmodel.tasks import *

# Create your views here.


def home(request):
	return render(request,'home.html')


def register(request):
	return render(request, 'main/register.html')

def register2(request):
	user=User()
	user.username=request.POST['login']
	user.set_password(request.POST['pwd'])
	user.first_name=request.POST['fn']
	user.last_name=request.POST['ln']
	user.email=request.POST['email']
	user.save()
	return render(request,'home.html')



# @login_required(login_url='/login')
def navigation(request):
	if request.user.is_authenticated():
		return render(request, 'main/navigation.html')
	else:
		return render(request,'/')


def upload(request):
	if request.user.is_authenticated():
		return render(request, 'main/upload.html')
	else:
		return render(request,'/')




def upload_medimg(request):
	if request.user.is_authenticated():
		user=get_user(request)
		context=user
		id = user.pk
		imgcontainer = ImgContainer()
		if request.method == 'POST':
			form = UploadMedImgForm(request.POST, request.FILES)
			if form.is_valid():
				imgcontainer.file = form.cleaned_data['imgcontainer']
				imgcontainer.user = context
				imgcontainer.save()
				return render(request,'main/navigation.html')



		return HttpResponseForbidden('allowed only via post')


def upload_model(request):
	if request.user.is_authenticated():
		user=get_user(request)
		context=user
		id = user.pk
		model = Model()
		if request.method == 'POST':
			form = UploadModelForm(request.POST, request.FILES)
			if form.is_valid():
				model.model_file = form.cleaned_data['model']

				model.user = context
				model.save()
				return render(request,'main/navigation.html')


		return HttpResponseForbidden('allowed only via post')

def upload_form(request):
	if request.user.is_authenticated():
		user = get_user(request)
		context = user
		id = user.pk



		if request.method == "POST":
			# form = ImgOptions(request.POST)
			# form.imgOptions = imgOptions
			imgOptions = request.POST.get("imgOptions")
			if imgOptions == "model":
				model = Model()
				form = UploadModelForm(request.POST, request.FILES)
				if form.is_valid():
					model.model_file = form.cleaned_data['file']
					model.name = form.cleaned_data['name']
					model.user = context
					model.save()
					return render(request,'main/navigation.html')

			if imgOptions == "medimg":
				imgcontainer = ImgContainer()
				form = UploadMedImgForm(request.POST, request.FILES)
				if form.is_valid():
					imgcontainer.file = form.cleaned_data['file']
					imgcontainer.name = form.cleaned_data['name']
					imgcontainer.user = context
					imgcontainer.save()
					return render(request,'main/navigation.html')



		return HttpResponseForbidden('allowed only via post')

def viewer(request, id):
	if request.user.is_authenticated():
		user = get_user(request)
		imgcontainer = ImgContainer.objects.get(pk=id)
		if(imgcontainer.user_id == user.id and imgcontainer.active == True):
			return render(request, 'main/viewer.html', {'imgcontainer': imgcontainer})
		else:
			return HttpResponse('File not found')





def  files(request):
	if request.user.is_authenticated():
		user=get_user(request)


		lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')

		lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
		c1 = {'lista' : lista}
		c2 = {'lista2' : lista2}

		context = {}
		context.update(c1)
		context.update(c2)



		return render(request, 'main/files.html', context)


def delete(request,id):
	if request.user.is_authenticated():
		user=get_user(request)
		a=ImgContainer.objects.get(pk=id)
		if (a.user_id == user.id):
			a.active = False
			a.save()
			lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')

			lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
			c1 = {'lista' : lista}
			c2 = {'lista2' : lista2}

			context = {}
			context.update(c1)
			context.update(c2)
			return render(request, 'main/files.html', context)
		else:
			return HttpResponse('File not found')

def deletemodel(request,id):
	if request.user.is_authenticated():
		user=get_user(request)
		a=Model.objects.get(pk=id)
		if (a.user_id == user.id):
			a.active = False
			a.save()
			lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')

			lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
			c1 = {'lista' : lista}
			c2 = {'lista2' : lista2}

			context = {}
			context.update(c1)
			context.update(c2)
			return render(request, 'main/files.html', context)
		else:
			return HttpResponse('File not found')

def generate(request,id):

	return render(request,'main/generate.html')

def browser(request,id):
	return render(request,'main/browser.html')

def converter(request, id):
	#llamar a funcion de conversion
	if request.user.is_authenticated():
		user=get_user(request)
		# archivo = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).filter(id=id)


		# a=archivo.id
		nhdr2nrrd(id)


	return render(request, 'main/converter.html' )



def settings(request, id):
	if request.user.is_authenticated():
		user=get_user(request)
		lista = User.objects.all()

		c1 = {'lista' : lista}

		context = {}
		context.update(c1)

	return render(request, 'main/settings.html',context)

def order(request):
	if request.user.is_authenticated():
		user=get_user(request)
		lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
		lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
		c1 = {'lista' : lista}
		c2 = {'lista2' : lista2}
		context = {}
		context.update(c1)
		context.update(c2)

		return render(request, 'main/order.html',context)
	else:
		return render(request,'/')


def viewermod(request, id):
	if request.user.is_authenticated():
		user = get_user(request)
		model = Model.objects.get(pk=id)
		if(model.user_id == user.id and model.active == True):
			return render(request, 'main/viewermod.html', {'model': model})
		else:
			return HttpResponse('File not found')


def roi(request):
#	if request.is_ajax():
		form = ROIForm(request.GET)
		if request.method == 'GET':
			if form.is_valid():
				roi = Roi()
				roi.x1 = form.cleaned_data['x1']
				roi.y1 = form.cleaned_data['y1']
				roi.x2 = form.cleaned_data['x2']
				roi.y2 = form.cleaned_data['y2']
				roi.save()
				return HttpResponse('%s' % request.GET.get('y1') )
			else:
				return HttpResponse('Wrong format')
		else:
			return HttpReponse('No GET')
#	else:
#		return HttpResponse("No Ajax request")

def comp(request):
		if request.user.is_authenticated():
			user = get_user(request)
			lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
			lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
			c1 = {'lista' : lista}
			c2 = {'lista2' : lista2}

			context = {}
			context.update(c1)
			context.update(c2)

			return render(request, 'main/comp.html', context)

		else:
			return HttpResponse('Sign in first')

