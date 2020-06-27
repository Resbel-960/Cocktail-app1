from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from notifications.consumers import NotificationConsumer

#allowed hosts?
# Session Authentication, required to use if we want to access the user details in the consumer 


application = ProtocolTypeRouter({ 
    
    'websocket': AllowedHostsOriginValidator( 
        AuthMiddlewareStack(  
            URLRouter(
                [
                    path("notifications/", NotificationConsumer),    
                ]
            )
        ),
    ),
})