from django import forms
from .models import BarangWishlist

class BarangWishlistForm(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']

    def __str__(self):
        return ""