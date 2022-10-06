import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Ied Mubaraque Sultan Salahuddine El Ayyubie',
    'last_login': request.COOKIES['last_login']
    }
    return render(request, "wishlist.html", context)

@login_required(login_url='/wishlist/login/')
@csrf_exempt
def add_wishlist(request):
    data_wishlist = BarangWishlist.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        nama_barang = request.POST.get('nama_barang')
        harga_barang =  request.POST.get('harga_barang')
        deskripsi = request.POST.get('deskripsi')

        response_data['nama_barang'] = nama_barang
        response_data['harga_barang'] = harga_barang
        response_data['deskripsi'] = deskripsi

        BarangWishlist.objects.create(
            nama_barang = nama_barang,
            harga_barang = harga_barang,
            deskripsi = deskripsi,
            )
        return JsonResponse(response_data)

    return render(request, 'wishlist_ajax.html', {'data_wishlist':data_wishlist}) 
def wishlist_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def wishlist_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def wishlist_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def wishlist_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response

def wishlist_ajax(req):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Ied Mubaraque Sultan Salahuddine El Ayyubie',
        'last_login': req.COOKIES['last_login'],
    }
    return render(req, "wishlist_ajax.html", context)