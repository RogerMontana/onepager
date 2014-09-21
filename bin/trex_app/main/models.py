from django.db import models
import json

# Create your models here.
class Main(models.Model):

    class Meta:
        db_table = "main info"

    main_hello = models.CharField(max_length=20, verbose_name='Hello text on main page')
    main_button_url = models.CharField(max_length=20,verbose_name='Facebook URL')
    main_button_url2 = models.TextField(max_length=20,verbose_name='Twitter URL')
    main_button_url3 = models.TextField(max_length=20,verbose_name='Google+ URL')
    main_button_url4 = models.TextField(max_length=20,verbose_name='Skype URL')
    main_button_text = models.TextField(max_length=20,verbose_name='News block 1')
    main_button_text2 = models.TextField(max_length=20,verbose_name='News block 2')
    main_button_text3 = models.TextField(max_length=20,verbose_name='News block 3')
    main_button_text4 = models.TextField(max_length=20,verbose_name='News block 4 - not used')
    main_about_us = models.TextField(max_length=20,verbose_name='about us page section text')
    main_contacts = models.TextField(max_length=20,verbose_name='contacts page section text')

class News(models.Model):
    """docstring for Article"""

    class Meta:  # add
        """additon extends for databases"""
        db_table = "news"

    news_title = models.CharField(max_length=200)  # uses for name of article or smth
    news_text = models.TextField()  # for big mas of text
    article_date = models.DateTimeField()  # date and time field

def dumps(value):
    return json.dumps(value,default=lambda o:None)

