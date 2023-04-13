
# Whisper

This project is a chat application built using Django Channels and WebSocket protocol. It allows multiple users to join a chat room and send and receive messages in real-time.



## Working

When a user joins the chat room, the user is assigned a unique WebSocket channel, and the user's messages are sent through this channel. Other users in the same chat room can listen to this channel and receive the messages.
## Tools

The tools used in this project are Django, Django Channels, WebSocket, JavaScript, HTML, and CSS. Django is a high-level Python web framework used for rapid development, and Django Channels is an extension that allows the use of WebSockets and asynchronous code in Django. WebSocket is a protocol that provides a two-way communication channel between a client and a server over a single TCP connection. JavaScript, HTML, and CSS are used to create the frontend of the chat application.
## Commands to Run 'Whisper'

Clone the repository from GitHub using the command:

```bash

git clone https://github.com/bibinkunjumon2020/Whisper.git

```
Create a virtual environment using the command:
```bash

python -m venv env


```
Activate the virtual environment using the command:

```bash

source env/bin/activate


```

Install the required Python packages using the command:

```bash

pip install -r requirements.txt


```

Navigate to the project directory using the command:

```bash

cd Django-Chat-Application

```
Apply the migrations using the command:
```bash

python manage.py migrate


```
Run the Django development server using the command:

```bash

python manage.py runserver


```
Open another terminal window and activate the virtual environment again.

Run the Daphne server using the command:

```bash

daphne chat_mallu.asgi:application --port 8080


```

Open your web browser and navigate to http://localhost:8000/.

Enter a username and click on the "Enter Chatroom" button.

Open another browser window or tab and navigate to the same URL.

Enter another username and click on the "Enter Chatroom" button.

You should now be able to see both users in the chatroom. Type a message in one window and it should appear in the other window.

That's it! You should now have a working chat application.

## Screenshot:

<img width="388" alt="image" src="https://user-images.githubusercontent.com/104210649/231892620-7b9d5c39-f179-4a75-bf92-52a06c646a6a.png">


## 🚀 About Me

I am a skilled software developer with over three years of experience in delivering secure and reliable applications. My expertise lies in back-end user development and AI-related work. Currently, I am employed as an AI and Full Stack Django Web Developer at Sayone Technology Ltd., a US-based IT firm. I have a strong background in Python programming and am dedicated to continuously improving my skills and knowledge in the field.

