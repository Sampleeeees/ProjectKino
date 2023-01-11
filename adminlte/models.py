from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
import datetime
# Create your models here.

# User Block

class Mailing(models.Model):
    template = models.FileField()


# SEO Block

class SeoBlock(models.Model):
    url_seo = models.URLField()
    tittle_seo = models.CharField(max_length=150)
    keywords_seo = models.CharField(max_length=50)
    description_seo = models.TextField()


# Image Block

class Gallery(models.Model):
    text = models.CharField(max_length=100)


class Image(models.Model):
    image = models.ImageField(upload_to='images/gallery_image/', blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, null=True)



# Cinema Block

class Film(models.Model):
    name_uk = models.CharField(max_length=50, blank=True)
    description_uk = models.TextField(blank=True)
    name_eng = models.CharField(max_length=50, blank=True)
    description_eng = models.TextField(blank=True)
    logo = models.ImageField(upload_to='film/logo/', blank=True, max_length=250)
    url = models.URLField()
    type_3d = models.BooleanField()
    type_2d = models.BooleanField()
    type_imax = models.BooleanField()
    date_premiere = models.DateField()
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)





class Cinema(models.Model):
    name_uk = models.CharField(max_length=50, blank=True)
    description_uk = models.TextField(blank=True)
    name_eng = models.CharField(max_length=50, blank=True)
    description_eng = models.TextField(blank=True)
    term_uk = models.TextField()
    term_eng = models.TextField(blank=True)
    logo = models.ImageField(upload_to='cinema/logo/', blank=True)
    top_banner = models.ImageField(upload_to='cinema/top_banner/', blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)


class Hall(models.Model):
    hall_number = models.IntegerField()
    description_uk = models.TextField()
    description_eng = models.TextField(blank=True)
    scheme_hall = models.ImageField()
    top_banner = models.ImageField()
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)
    cinema = models.ForeignKey(Cinema, verbose_name="Кінотеатр", on_delete=models.CASCADE, blank=True, null=True)


class Session(models.Model):
    time_start = models.TimeField()
    day = models.DateField()
    hall = models.ForeignKey(Hall, verbose_name="Кінозал", on_delete=models.CASCADE, blank=True, null=True)
    film = models.ForeignKey(Film, verbose_name="Фільм", on_delete=models.CASCADE, blank=True, null=True)




class Ticket(models.Model):
    row = models.IntegerField()
    place = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=3 )
    session = models.ForeignKey(Session, verbose_name='Сеанс', on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey('user', verbose_name='Користувач', on_delete=models.CASCADE)


# Pages

class HomePage(models.Model):
    phone_number = models.IntegerField()
    date_create = models.DateField(auto_now=True)
    status = models.BooleanField()
    seo_text = models.TextField()
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)

class Page(models.Model):
    name_uk = models.CharField(max_length=50, blank=True)
    namepage = models.CharField(max_length=50, blank=True)
    description_uk = models.TextField(blank=True)
    name_eng = models.CharField(max_length=50, blank=True)
    description_eng = models.TextField(blank=True)
    status = models.BooleanField()
    date_create = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='PageImage/')
    url_video = models.URLField()
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, null=True, blank=True)
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, null=True, blank=True)


class Contact(models.Model):
    name_cinema = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    date_create = models.DateField(auto_now=True)
    coordinate = models.IntegerField()
    status = models.BooleanField()
    logo = models.ImageField(upload_to="ContactImage/")
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)


class NewsAndDiscount(models.Model):
    name_uk = models.CharField(max_length=50, blank=True)
    name_eng = models.CharField(max_length=50, blank=True)
    status = models.BooleanField()
    date_premiere = models.DateField(blank=True, null=True)
    date_created_updated = models.DateField(blank=True, null=True)
    description_uk = models.TextField(blank=True)
    description_eng = models.TextField(blank=True)
    logo = models.ImageField(upload_to='NewsAndDiscountLogo/')
    url_video = models.URLField()
    type = models.CharField(max_length=20, blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    seo_block = models.ForeignKey(SeoBlock, verbose_name='СЕО блок', on_delete=models.CASCADE, blank=True, null=True)


# Banners

SPEED_CHOICES = {
    (None, ''),
    (300, '3c'),
    (500, '5c'),
    (700, '7c'),
    (1000, '10c')
}

class SpeedCarousel(models.Model):
    speed_carousel = models.CharField(max_length=50, choices=SPEED_CHOICES, blank=True, null=True)
    status = models.BooleanField(default=True)

class TopHomeBanner(models.Model):
    image = models.ImageField(upload_to='Banner/TopBannerImage/', blank=True, null=True)
    url = models.URLField(blank=True)
    text = models.CharField(max_length=150, blank=True)

class BackgroundBanner(models.Model):
    image = models.ImageField(upload_to='Banner/BackgroundBanner/', blank=True, null=True)
    type = models.CharField(max_length=50)



class NewsAndDiscountBanner(models.Model):
    image = models.ImageField(upload_to='Banner/NewsAndDiscount/', blank=True, null=True)
    url = models.URLField()







