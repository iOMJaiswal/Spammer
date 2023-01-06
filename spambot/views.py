from django.http import HttpResponse
from django.shortcuts import render
from .forms import RadioModelForm
from .models import RadioModel
from django.views import View
import random
import time
import pyautogui as pg


class RadioView(View):
    def get(self, request):
        form = RadioModelForm()
        return render(request, 'spambot/index.html', {'form':form} )
    def post(self, request):
        form = RadioModelForm(request.POST)
        if form.is_valid():
            form.save()

            # Getting value of radio button
            selected = form.cleaned_data.get('spam')

            # Calling to start spam
            # Here value of selected is type(str)
            startSpam(request,selected)
            # print(selected)
            return render(request, 'spambot/index.html', {'form':form} )

def about(request):
    return render(request, 'spambot/about.html')


def startSpam(request,selected):
    textArea = list(str(request.POST.get('text', 'default')).split(','))
   
    # Writing Entered words in file    
    f = open("spambot\\static\\Keywords\\Keywords.txt", "a")
    for text in textArea:
        f.write(f'{text} {selected} \n')
    f.close()

    # spam00 = request.POST.get('spam00', 'default')
    # print(textArea)
    # print(spam00)

    time.sleep(20)

    for i in range(int(selected)):
        pg.write(random.choice(textArea))
        pg.press('enter')

