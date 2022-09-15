from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import wishlist_xml
from wishlist.views import wishlist_json
from wishlist.views import wishlist_xml_by_id
from wishlist.views import wishlist_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', wishlist_xml, name='wishlist_xml'),
    path('json/', wishlist_json, name='wishlist_json'),
    path('xml/<int:id>', wishlist_xml_by_id, name='wishlist_xml_by_id'),
    path('json/<int:id>', wishlist_json_by_id, name='wishlist_json_by_id'),
]