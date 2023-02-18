from django.urls import path
from . import consumers 


websocket_urlpatterns=[
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()),
    path('ws/rsc/',consumers.MyRealSyncConsumer.as_asgi()),
    path('ws/rac/',consumers.MyRealAsyncConsumer.as_asgi()),
     
]