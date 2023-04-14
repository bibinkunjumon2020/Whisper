from channels.generic.websocket import AsyncWebsocketConsumer 
import json 

class ChatConsumer(AsyncWebsocketConsumer):  
    async def connect(self):
        await self.channel_layer.group_add('chat', self.channel_name)  # Add this WebSocket connection to the 'chat' group
        await self.accept()  # Accept the WebSocket connection

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('chat', self.channel_name)  # Remove this WebSocket connection from the 'chat' group

    async def receive(self, text_data):
        data = json.loads(text_data)  # Parse the received JSON text data into a dictionary
        message = data['message']  # Extract the 'message' value from the dictionary

        await self.channel_layer.group_send(
            'chat',
            {
                'type': 'chat_message',
                'message': message
            }
        )  # Send a group message with the extracted message to all WebSocket connections in the 'chat' group

    async def chat_message(self, event):
        message = event['message']  # Extract the 'message' value from the event dictionary

        await self.send(text_data=json.dumps({
            'message': message
        }))  # Send a message containing the extracted message back to the WebSocket client as JSON
