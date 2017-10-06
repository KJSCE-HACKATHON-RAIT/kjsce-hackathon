# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Size_Chart(models.Model):
	Length_ID = models.IntegerField(blank=True, null=True)
	Gender_Choices = (
		('M', 'Male'),
		('F', 'Female'),
	)
	Gender = models.CharField(max_length=1, choices=Gender_Choices)
	Length = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	UK = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	EU = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

	def __str__(self):
		return u'%d %s %0.2f %0.2f %0.2f' % (self.Length_ID, self.Gender, self.Length,  self.UK, self.EU)

class Image_Chart(models.Model):
	image = models.FileField(null = True, blank = True)
	Gender_Choices = (
		('M', 'Male'),
		('F','Female'),
	)
	Gender = models.CharField(max_length=1, choices=Gender_Choices)

	
	#def save(self, commit=True):
	#	instance = super(Image_Chart, self).save(commit=False)
	#	f = self['image'].value() # actual file object
		# process the file in a way you need
	#	if commit:
	#		instance.save()
	#	return instance
	#Length_ID = models.IntegerField(blank=True, null=True)   
	#Length = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

	#def __str__(self):
	#    return u'%d %s %0.2f %0.2f %0.2f' % (self.Length_ID, self.Gender, self.Length,  self.UK, self.EU)