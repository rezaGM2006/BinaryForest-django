from django.shortcuts import render, redirect
from .forms import ChatForm
from .models import Chat
# Create your views here.


def main(request):

    return render(request, 'chatroom/main.html')

def chat(request):
    chats = Chat.objects.all()
    
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = request.user.username
            chat = Chat(username=username, text=cd['text'])
            chat.save()
            return redirect('chatroom:ChatCity')  # فرض بر اینکه URL شما نیاز به topic_id دارد
    else:
        form = ChatForm()

    
    return render(request, 'chatroom/ChatCity.html', {"form": form, "chats": chats})


