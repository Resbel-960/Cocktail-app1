from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
import json
from asgiref.sync import async_to_sync

#synch to asynch when to use?
#groups when to use?



class NotificationConsumer(WebsocketConsumer):
    
     # Function to connect to the websocket
    def connect(self):
        if self.scope["user"].is_anonymous:
            self.close()
        else:
            self.group_name = str(self.scope["user"].pk)  # Setting the group name as the pk of the user primary key as it is unique to each user. The group name is used to communicate with the user.
            async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
            self.accept()

    def disconnect(self, close_code):
        self.close()

    # Custom Notify Function which can be called from Views or api to send message to the frontend
    def notify(self, event):
        self.send(text_data=json.dumps(event))
