# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm
from .models import Size_Chart, Image_Chart

from PIL import Image
from base64 import decodestring
import base64
import re
from io import StringIO
import os
from datetime import datetime
from django.core.files.base import ContentFile
from django.core.files import File
from decimal import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#def Model_Form(request):
#	form = PostForm(request.POST or None, request.FILES or None)
#	if form.is_valid():
#		instance = form.save(commit=False)
#		instance.save()
#		message.success(request, "Successfully Created")
#		return HttpResponseRedirect(instance.get_absolute_url())
#	context = {
#		"form": form,
#	}
#
#	return render(request, 'model.html', context)

def Model_Form(request):
    now = datetime.now()
    len_id = 23
    len1 = 26.10
    min_dist = 50
    min_id = -1
    #find the nearest Length_ID
    all_entries = Size_Chart.objects.all()
    for entry in all_entries:
        if min_dist > (entry.Length - Decimal(len1)) and (entry.Length - Decimal(len1)) >= 0:
            min_dist = entry.Length - Decimal(len1)
            min_id = entry.Length_ID
    results = Size_Chart.objects.get(Length_ID=min_id)

    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        Gender = request.POST.get('Gender','')
        image = request.POST.get('image', '')
        imgstr = re.search(r'base64,(.*)', image).group(1)
        #filename = 'media/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.png'
        filename = datetime.now().strftime("%Y%m%d-%H%M%S") + '.png'
        #output = open(filename, 'wb')
        imgstr = imgstr.decode('base64')
        #output.write(imgstr)
        formobj = Image_Chart()
        formobj.Gender = Gender
        #formobj.image.save(filename, File(output))
        formobj.image.save(filename, ContentFile(imgstr))
        formobj.save()
        #output.close()
        #tempimg = cStringIO.StringIO(imgstr)
        #im = Image.open(tempimg)
        #formobj = PostForm()
        #form.Gender = Gender
        #form.image = imgstr
        #instance = form.save(commit=False)
        #instance.save()
        

        #get the length_ID and initialize it to a variable
        # get len1
        
        
        
        return render(request, 'modal1.html',{'results': results }, {'form': form}, )
        #return HttpResponse(status=204)
    else:
        form = PostForm()
    return render(request, 'modal1.html',  {'results': results}, {'form': form})

def Model_Form_tmp1(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponse("Uploaded Successfully")
    else:
        form = PostForm()
    return render(request, 'model.html', {'form': form})

def Model_Form_tmp(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Gender = request.POST.get('Gender','')        
            formobj = Image_Chart(image = canvas, Gender = Gender)
            formobj.save()
            return HttpResponse("Submitted !!")
    else:
        form = DetailsForm()

    return render(request, 'model.html')