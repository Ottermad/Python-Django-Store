from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

import sendgrid

from .models import Shirt
from .forms import ContactForm


def listing(request):
    shirts = Shirt.objects.all()
    return render(request, 'shirts/listing.html', {'shirts': shirts})


def home(request):
    shirts = Shirt.objects.all().order_by('-id')[:4]
    return render(request, 'shirts/home.html', {'shirts': shirts})


def detail(request, pk):
    shirt = get_object_or_404(Shirt, pk=pk)
    return render(request, 'shirts/detail.html', {'shirt': shirt})


def contact(request):
    if request.POST:
        sg = sendgrid.SendGridClient("", "", raise_errors=True)

        subject = request.POST['name']
        text = request.POST['message']
        email = request.POST['email']

        message = sendgrid.Mail()
        message.add_to('charlie.thomas@attwoodthomas.net')
        message.set_subject(subject)
        message.set_text(text)
        message.set_from(email)

        try:
            sg.send(message)
            print("SENT")
        except sendgrid.SendGridClientError:
            None
        except sendgrid.SendGridServerError:
            None
        return redirect(reverse("shirts:home"))
    form = ContactForm(auto_id='%s')
    return render(request, 'shirts/contact.html', {'form': form})