from django.contrib import admin
from .models import Mailing, Film, Cinema, Session, Ticket, SeoBlock, Gallery, Image, Hall, HomePage, Page, Contact, NewsAndDiscount, NewsAndDiscountBanner, TopHomeBanner, BackgroundBanner, SpeedCarousel
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(Mailing)
admin.site.register(Film)
admin.site.register(Cinema)
admin.site.register(Session)
admin.site.register(Ticket)
admin.site.register(SeoBlock)
admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Hall)
admin.site.register(HomePage)
admin.site.register(Page)
admin.site.register(Contact)
admin.site.register(NewsAndDiscount)
admin.site.register(NewsAndDiscountBanner)
admin.site.register(TopHomeBanner)
admin.site.register(BackgroundBanner)
admin.site.register(SpeedCarousel)



