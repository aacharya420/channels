
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import myapp.routing
from myapp import routing
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        myapp.routing.websocket_urlpatterns
    )
    
})


 