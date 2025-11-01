from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Сохрани в базу
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Отправь email (настроим позже)
        try:
            send_mail(
                f'Новое сообщение: {subject}',
                f'От: {name} ({email})\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except:
            pass
        
        messages.success(request, 'Ваше сообщение успешно отправлено!')
        return redirect('contact:index')
    
    return render(request, 'contact/index.html')