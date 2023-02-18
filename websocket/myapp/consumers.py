#for syncconsumer

from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import json
import asyncio

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Webshocket connected",event)
        self.send({
             'type':'websocket.accept'
            })
        

    def websocket_receive(self,event):
        print("Message received from client",event)
        print(event['text'])
        self.send({'type':'websocket.send',
        'text':"Message from server to client"})
    
    def websocket_disconnect(self,event):
        print("Websocket disconnected",event)
        raise StopConsumer()




#for Asyncconsumer

from channels.consumer import AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket connected",event)
        await self.send({'type':'websocket.accept'})

    async def websocket_receive(self,event):
        print("Welsocket received",event)
        print(event['text'])
        
        
        await self.send({'type':'websocket.send',
          'text':'Message sent to client by server'})
        
    
    async def websocket_disconnect(self,event):
        print("Websocket disconnected",event)
        raise StopConsumer()



        #Fetching real time data




class MyRealSyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Webshocket sanga jodiyeko xa aba",event)
        self.send({
             'type':'websocket.accept'
            })
        

    def websocket_receive(self,event):
        print("Message received from client",event)
        print(event['text'])
        for i in  range(10):
            self.send({'type':'websocket.send',
                        'text':json.dumps({'count':i})
                        })
            sleep(5)
    
    def websocket_disconnect(self,event):
        print("Websocket disconnected",event)
        raise StopConsumer()


class MyRealAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket connected",event)
        await self.send({'type':'websocket.accept'})

    async def websocket_receive(self,event):
        print("Welsocket received",event)
        print(event['text'])
        
        for i in  range(5):
            await self.send({'type':'websocket.send',
                        'text':str(i)+ "No data "})
            await asyncio.sleep(5)
        
    
    async def websocket_disconnect(self,event):
        print("Websocket disconnected",event)
        raise StopConsumer()

