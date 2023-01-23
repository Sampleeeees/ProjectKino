from django import forms
from django.forms import ModelForm
from KinoCMS import settings
from .models import Film, Cinema, TopHomeBanner, SeoBlock, Gallery, Image, NewsAndDiscount, SpeedCarousel, NewsAndDiscountBanner, BackgroundBanner, Hall, HomePage, Page, Contact, Mailing
from tempus_dominus.widgets import DatePicker
from time import sleep
from django.core.mail import send_mail
from adminlte.tasks import send_feedback_email_task


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['name_uk', 'name_eng', 'description_uk', 'description_eng', 'date_premiere', 'logo', 'url', 'type_imax', 'type_2d', 'type_3d']
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control ml-2'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control ml-2 w-50'}),
            'name_eng': forms.TextInput(attrs={'class': 'form-control ml-2'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control ml-2 w-50'}),
            'date_premiere': forms.DateInput(attrs={
                                                'class': 'form-control',
                                                'id': 'datepicker1',
                                                'type': 'text',
                                                'autocomplete': 'off'}),
            'logo': forms.FileInput(attrs={'class': 'form-control ml-2 d-none',
                                           'id': 'id_general_photo',
                                           'onchange': "addLogoImage(this, 'imgBanner')"}),
            'url': forms.URLInput(attrs={'class': 'form-control ml-2'})
        }



class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['text']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control ml-2 d-none',
                                            'id': 'id-__prefix__-image',
                                           'onchange': "addPhotoImage(this, 'img-__prefix__-Gallery')"}),
        }


class SeoBlockForm(ModelForm):
    class Meta:
        model = SeoBlock
        fields = ['url_seo', 'tittle_seo', 'keywords_seo', 'description_seo']
        widgets ={
            'url_seo': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'tittle_seo': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control mr-2 w-75'})
        }



class NewsForm(ModelForm):
    class Meta:
        model = NewsAndDiscount
        fields = ['name_uk', 'name_eng', 'status', 'description_uk', 'description_eng', 'logo', 'url_video', 'date_premiere']
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control mr-2 w-75'}),
            'name_eng': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control mr-2 w-75'}),
            'url_video': forms.URLInput(attrs={'class': 'form-control mr-2 w-75'}),
            'logo': forms.FileInput(attrs={'class': 'form-control ml-2 d-none',
                                           'id': 'id_general_photo',
                                           'onchange': "addLogoImage(this, 'imgBanner')"}),
            'date_premiere': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'datepicker1',
                'type': 'text',
                'autocomplete': 'off'}),

            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
                'id': 'id_news_status'
            })
        }

class DiscountForm(ModelForm):
    class Meta:
        model = NewsAndDiscount
        fields = ['name_uk', 'name_eng', 'status', 'description_uk', 'description_eng', 'logo', 'url_video', 'date_premiere']
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control mr-2 w-75'}),
            'name_eng': forms.TextInput(attrs={'class': 'form-control mr-2 w-75'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control mr-2 w-75'}),
            'url_video': forms.URLInput(attrs={'class': 'form-control mr-2 w-75'}),
            'logo': forms.FileInput(attrs={'class': 'form-control ml-2 d-none',
                                           'id': 'id_general_photo',
                                           'onchange': "addLogoImage(this, 'imgBanner')"}),
            'date_premiere': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'datepicker1',
                'autocomplete': 'off'}),

            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
                'id': 'id_discount_status'
            })
        }


#ModelForm

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = ['name_uk', 'name_eng', 'description_uk', 'description_eng', 'term_uk', 'term_eng', 'logo', 'top_banner']
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'name_eng': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'term_uk': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'term_eng': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'logo': forms.FileInput(attrs={'class': 'form-control mr-2 w-50 d-none', 'id': 'id_general_photo', 'onchange': 'addLogoImage(this, "imgBanner")'}),
            'top_banner': forms.FileInput(attrs={'class': 'form-control mr-2 w-50 d-none', 'id': 'id_topbanner_photo', 'onchange': 'addLogoImage(this, "imgTopBanner")'})
           }

class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = ['hall_number', 'description_uk', 'description_eng', 'scheme_hall', 'top_banner']
        widgets = {
            'hall_number': forms.NumberInput(attrs={'class': 'form-control w-50'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control w-50'}),
            'scheme_hall': forms.FileInput(attrs={'class': 'form-control mr-2 d-none', 'id': 'id_scheme_hall', 'onchange': 'addLogoImage(this, "SchemeHall")'}),
            'top_banner': forms.FileInput(attrs={'class': 'form-control mr-2 d-none', 'id': 'id_topbanner_hall', 'onchange': 'addLogoImage(this, "TopBannerHall")'})
        }

class TopHomeBannerForm(ModelForm):
    class Meta:
        model = TopHomeBanner
        fields = ['image', 'url', 'text']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control w-100 mt-2 mb-2', 'id': 'id_form-__prefix__-url', 'placeholder': 'URL'}),
            'text': forms.TextInput(attrs={'class': 'form-control w-100 mt-2 mb-2', 'id': 'id_form-__prefix__-text', 'placeholder': 'Text'}),
            'image': forms.FileInput(attrs={'class': 'form-control w-100 d-none',
                                            'id': 'img-__prefix__-Banner',
                                            'onchange': "addPhotoImage(this, 'img-__prefix__-Gallery')"})
        }
class SpeedCarouselForm(ModelForm):
    class Meta:
        model = SpeedCarousel
        fields = ['speed_carousel', 'status']
        widgets = {
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'speed_carousel': forms.Select(attrs={
                'class': 'speed_check form-select rounded',
            })
        }

class NewsAndDiscountBannerForm(ModelForm):
    class Meta:
        model = NewsAndDiscountBanner
        fields = ['image', 'url']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control w-100', 'id': 'id_form-__prefix__-url-news', 'placeholder': 'URL'}),
            'image': forms.FileInput(attrs={'class': 'form-control w-100 d-none',
                                            'id': 'img-__prefix__-BannerNews',
                                            'onchange': "addPhotoImage(this, 'img-__prefix__-News')"})
        }

class BackgroundForm(ModelForm):
    class Meta:
        model = BackgroundBanner
        choices_type = (('10', 'Фон-картинка'), ('1000', 'Звичаний фон'))
        fields = ['type', 'image']
        widgets = {
            'type': forms.RadioSelect(choices=choices_type, attrs={'class': 'form-check-inline'}),
            'image': forms.FileInput(attrs={'class': 'd-none',
                                            'id': 'img_back_banner',
                                            'onchange': "addPhotoImage(this, 'img-BackBanner')"})
        }


class HomePageForm(ModelForm):
    class Meta:
        model = HomePage
        fields = ['phone_number',  'status', 'seo_text']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class': 'form-control w-25'}),
            'seo_text': forms.Textarea(attrs={'class': 'form-control w-25'}),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            }),
        }

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name_uk', 'name_eng', 'description_uk', 'description_eng', 'url_video',  'status', 'logo']
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control w-50 ml-2'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control w-50 ml-2'}),
            'name_eng': forms.TextInput(attrs={'class': 'form-control w-50 ml-2'}),
            'description_eng': forms.Textarea(attrs={'class': 'form-control w-50 ml-2'}),
            'url_video': forms.URLInput(attrs={'class': 'form-control w-50 ml-2'}),
            'logo': forms.FileInput(attrs={'class': 'ml-2 d-none', 'id': 'id_aboutcinema_logo', 'onchange': 'addPhotoImage(this, "ImgAboutCinemaLogo")'}),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            }),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name_cinema', 'address', 'coordinate', 'status', 'logo']
        widgets = {
            'name_cinema': forms.TextInput(attrs={'class': 'form-control w-100 ml-auto mr-auto'}),
            'address': forms.Textarea(attrs={'class': 'form-control w-100 ml-auto mr-auto '}),
            'coordinate': forms.TextInput(attrs={'class': 'form-control w-100 ml-auto mr-auto'}),
            'logo': forms.FileInput(attrs={'class': 'd-none', 'id': 'id-__prefix__-contact-logo', 'onchange': 'addPhotoImage(this, "id-__prefix__-contact")'}),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            })
        }

class MailingForm(ModelForm):
    all_user = forms.ChoiceField(widget=(forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'radio', 'checked': '', 'onclick': 'switchList(this)'})))
    select_user = forms.ChoiceField(widget=(forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'radio', 'onclick': 'switchList(this)'})))
    class Meta:
        model = Mailing
        fields = ['template']
        widgets = {
            'template': forms.FileInput(attrs={'class': 'd-none'})
        }
    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )

