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
import cv2

from PIL import Image
from io import StringIO
import numpy as np
from django.contrib.staticfiles.templatetags.staticfiles import static
hc = static("haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(hc)


def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

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
#    if request:
        print ("post called")
        form = PostForm(request.POST or None, request.FILES or None)
        Gender = request.POST.get('Gender','')
        image = request.POST.get('image', '')
        imgstr = re.search(r'base64,(.*)', image).group(1)
        #filename = 'media/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.png'
        filename = datetime.now().strftime("%Y%m%d-%H%M%S") + '.png'
        #output = open(filename, 'wb')
        # imgstr = imgstr.codecs.decode()
        t = imgstr
        imgstr = base64.b64decode(imgstr)
        #output.write(imgstr)
        formobj = Image_Chart()
        formobj.Gender = Gender
        #formobj.image.save(filename, File(output))
        cnt = ContentFile(imgstr)


        gray = data_uri_to_cv2_img(image)
        print(type(gray),gray)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (0, 20)
        fontScale = 1
        fontColor = (0, 0, 255)
        lineType = 2

        cv2.putText(gray, 'People Count:-'+str(len(faces)),
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)

        cnt = gray
        formobj.image.save(filename, cnt)

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
        print ("Not called")
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

# def Model_Form_tmp(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             Gender = request.POST.get('Gender','')
#             formobj = Image_Chart(image = canvas, Gender = Gender)
#             formobj.save()
#             return HttpResponse("Submitted !!")
#     else:
#         form = DetailsForm()
#
#     return render(request, 'model.html')