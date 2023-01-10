from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory, inlineformset_factory
from .forms import FilmForm, CinemaForm, TopHomeBannerForm, SeoBlockForm, GalleryForm, ImageForm, NewsForm, DiscountForm, SpeedCarouselForm, NewsAndDiscountBannerForm, MailingForm ,HallForm, HomePageForm, PageForm, ContactForm
from .models import Image, SeoBlock, Gallery, Film, NewsAndDiscount, TopHomeBanner, SpeedCarousel, NewsAndDiscountBanner, Cinema, Hall, HomePage, Page, Contact
from django.views.generic.base import View
from datetime import datetime, timedelta
from django.core.mail import send_mail
from user.models import User
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'adminlte/index.html')


def delete(request, delete_item, name):
    if name == 'Film':
        delit = Film.objects.get(pk=delete_item)
        delit.gallery.delete()
        for dele in Image.objects.filter(gallery=delit.gallery.id):
            dele.delete()
        delit.seo_block.delete()
        delit.delete()
        return redirect('films')
    if name == 'NewsAndDiscount':
        delit = NewsAndDiscount.objects.get(pk=delete_item)
        delit.gallery.delete()
        for dele in Image.objects.filter(gallery=delit.gallery.id):
            dele.delete()
        delit.seo_block.delete()
        delit.delete()
        return redirect('news')
    if name == 'Cinema':
        delit = Cinema.objects.get(pk=delete_item)
        delit.gallery.delete()
        for dele in Image.objects.filter(gallery=delit.gallery.id):
            dele.delete()
        delit.seo_block.delete()
        for dele in Hall.objects.filter(cinema=delit.id):
            dele.delete()
        delit.delete()
        return redirect('cinemas')
    if name == 'Hall':
        delit = Hall.objects.get(pk=delete_item)
        delit.gallery.delete()
        for dele in Image.objects.filter(gallery=delit.gallery.id):
            dele.delete()
        delit.seo_block.delete()
        delit.delete()
        return redirect('cinemadetail', pk=delit.cinema.id)

    return redirect('films')

def statistic(request):
    return render(request, 'adminlte/statistics.html')


#Для сторінки банерів
def banner(request):

    BannerFormset = modelformset_factory(TopHomeBanner, form=TopHomeBannerForm, extra=0, can_delete=True)
    formset = BannerFormset(request.POST or None, request.FILES or None, queryset=TopHomeBanner.objects.all())

    # NewsFormset = modelformset_factory(NewsAndDiscountBanner, form=NewsAndDiscountBannerForm, extra=0, can_delete=True)
    # formset_news = NewsFormset(request.POST or None, request.FILES or None, queryset=NewsAndDiscountBanner.objects.all())



    speedinstance = SpeedCarousel.objects.first()
    speed = SpeedCarouselForm(request.POST or None, instance=speedinstance)


    print(formset.errors)


    if formset.is_valid() and speed.is_valid():
        print(formset.errors)
        speed.save()
        for banner in formset:
            print(banner.instance.id)
            print(banner.errors)
            if banner.is_valid():
                print(banner.errors)
                banner.save()
        # for banner in formset_news:
        #     print(banner.errors)
        #     if banner.is_valid():
        #         print(banner.errors)
        #         print(formset.deleted_forms)
        #         banner.save()

    context = {'formset': formset, 'speed': speed }

    return render(request, 'adminlte/banners.html', context)




def cinema(request):
    return render(request, 'adminlte/cinemas.html')

def page(request):
    home = HomePage.objects.get(pk=1)
    aboutcinema = Page.objects.get(namepage='About Cinema')
    cafebar = Page.objects.get(namepage='Cafe-bar')
    viphall = Page.objects.get(namepage='VipHall')
    advert = Page.objects.get(namepage='Advert')
    child = Page.objects.get(namepage='Childroom')
    contact = Contact.objects.last()
    print(contact)
    context = {
        'home': home,
        'aboutcinema': aboutcinema,
        'cafebar': cafebar,
        'vip': viphall,
        'adv': advert,
        'child': child,
        'contact': contact
    }
    return render(request, 'adminlte/pages.html', context)

def general_page(request):
    homepage = get_object_or_404(HomePage, pk=1)
    seo = get_object_or_404(SeoBlock, pk=homepage.seo_block.id)

    home = HomePageForm(request.POST or None, instance=homepage)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    if request.method == 'POST':
        if home.is_valid() and seoform.is_valid():
            homepage = home.save(commit=False)
            homepage.seo_block = seoform.save()
            homepage.save()
    return render(request, 'adminlte/generalpage.html', context={'home': home, 'seo': seoform})

def aboutcinema(request):
    aboutcinema = get_object_or_404(Page, namepage='About Cinema')
    seo = get_object_or_404(SeoBlock, pk=aboutcinema.seo_block.id)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=aboutcinema.gallery.id))

    aboutcinemaform = PageForm(request.POST or None, request.FILES or None, instance=aboutcinema)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    print(aboutcinemaform.errors, seoform.errors, formset.errors)

    if request.method == 'POST':
        if aboutcinemaform.is_valid() and seoform.is_valid() and formset.is_valid():
            print(aboutcinemaform.errors, formset.errors, seoform.errors)
            cinema = aboutcinemaform.save(commit=False)
            print(cinema)
            cinema.seo_block = seoform.save()
            print(cinema.seo_block)
            gallery = Gallery.objects.get(pk=aboutcinema.gallery.id)
            print(gallery)
            aboutcinema.gallery = get_object_or_404(Gallery, pk=gallery.id)
            print(aboutcinema.gallery)
            for img in formset:
                print(img)
                image = img.save(commit=False)
                print(image)
                image.gallery = aboutcinema.gallery
                print(image.gallery)
                image.save()
                print(image)
            formset.save()
            cinema.save()
        return redirect('pages')

    context = {'pagedetail': aboutcinemaform, 'seo': seoform, 'formset': formset}
    print('hello')
    return render(request, 'adminlte/pagedetail.html',  context)


def cafebar(request):
    cafebar = get_object_or_404(Page, namepage='Cafe-bar')
    seo = get_object_or_404(SeoBlock, pk=cafebar.seo_block.id)

    cafebarform = PageForm(request.POST or None, request.FILES or None, instance=cafebar)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=cafebar.gallery.id))

    if request.method == 'POST':
        if cafebarform.is_valid() and formset.is_valid() and seoform.is_valid():
            cafebar = cafebarform.save(commit=False)
            cafebar.seo_block = seoform.save()
            cafebar.gallery = get_object_or_404(Gallery, pk=cafebar.gallery.id)
            cafebar.gallery.text = cafebar.namepage
            for img in formset:
                image = img.save(commit=False)
                image.gallery = cafebar.gallery
                image.save()
            formset.save()
            cafebar.save()
        return redirect('pages')

    context = {'pagedetail': cafebarform, 'seo': seoform, 'formset': formset}
    return render(request, 'adminlte/pagedetail.html', context)


def viphalldetail(request):
    viphall = get_object_or_404(Page, namepage='VipHall')
    seo = get_object_or_404(SeoBlock, pk=viphall.seo_block.id)

    viphallform = PageForm(request.POST or None, request.FILES or None, instance=viphall)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=viphall.gallery.id))

    if request.method == 'POST':
        if viphallform.is_valid() and seoform.is_valid() and formset.is_valid():
            viphall = viphallform.save(commit=False)
            viphall.seo_block = seoform.save()
            viphall.gallery = get_object_or_404(Gallery, pk=viphall.gallery.id)
            for img in formset:
                image = img.save(commit=False)
                image.gallery = viphall.gallery
                image.save()
            formset.save()
            viphall.save()

        return redirect('pages')

    context = {'pagedetail': viphallform, 'seo': seoform, 'formset': formset}

    return render(request, 'adminlte/pagedetail.html', context)

def advertisingdetail(request):
    adv = get_object_or_404(Page, namepage='Advert')
    seo = get_object_or_404(SeoBlock, pk=adv.seo_block.id)

    advform = PageForm(request.POST or None, request.FILES or None, instance=adv)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None,
                           queryset=Image.objects.filter(gallery=adv.gallery.id))

    if request.method == 'POST':
        if advform.is_valid() and formset.is_valid() and seoform.is_valid():
            adv = advform.save(commit=False)
            adv.seo_block = seoform.save()
            adv.gallery = get_object_or_404(Gallery, pk=adv.gallery.id)
            adv.gallery.text = adv.namepage
            for img in formset:
                image = img.save(commit=False)
                image.gallery = adv.gallery
                image.save()
            formset.save()
            adv.save()
        return redirect('pages')

    context = {'pagedetail': advform, 'seo': seoform, 'formset': formset}
    return render(request, 'adminlte/pagedetail.html', context)

def childroomdetail(request):
    child = get_object_or_404(Page, namepage='Childroom')
    seo = get_object_or_404(SeoBlock, pk=child.seo_block.id)

    childform = PageForm(request.POST or None, request.FILES or None, instance=child)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None,
                           queryset=Image.objects.filter(gallery=child.gallery.id))

    if request.method == 'POST':
        if childform.is_valid() and formset.is_valid() and seoform.is_valid():
            child = childform.save(commit=False)
            child.seo_block = seoform.save()
            child.gallery = get_object_or_404(Gallery, pk=child.gallery.id)
            child.gallery.text = child.namepage
            for img in formset:
                image = img.save(commit=False)
                image.gallery = child.gallery
                image.save()
            formset.save()
            child.save()
        return redirect('pages')

    context = {'pagedetail': childform, 'seo': seoform, 'formset': formset}
    return render(request, 'adminlte/pagedetail.html', context)

def contact(request):
    contact = get_object_or_404(Contact, pk=1)
    seo = get_object_or_404(SeoBlock, pk=contact.seo_block.id)
    print(seo)
    formseo = SeoBlockForm(request.POST or None, instance=seo)

    ContactFormset = modelformset_factory(Contact, form=ContactForm, extra=0, can_delete=True)
    formset = ContactFormset(request.POST or None, request.FILES or None, queryset=Contact.objects.all())

    if request.method == 'POST':
        if formset.is_valid() and formseo.is_valid():
            seo = formseo.save(commit=False)
            print(formseo.cleaned_data)
            for contact in formset:
                con = contact.save(commit=False)
                con.seo_block = seo
                con.save()
            formset.save()
            return redirect('pages')


    context = {'formset': formset,'formseo': formseo}
    return render(request, 'adminlte/contact.html', context)

def user(request):
    user = User.objects.all()
    return render(request, 'adminlte/users.html', {'user_list': user})

# add block
#Для створення нових фільмів
def addfilm(request):
    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.none())
    form = FilmForm(request.POST or None, request.FILES)
    formseo = SeoBlockForm(request.POST or None)

    if request.method == 'POST':
        print(form.errors, formseo.errors)
        if form.is_valid() and formseo.is_valid():
            # print(request.FILES)
            # print(form.cleaned_data)
            # print(formseo.cleaned_data)
            filmform = form.save(commit=False)
            filmform.seo_block = formseo.save()
            gallery = Gallery.objects.create(text=filmform.name_eng)
            filmform.gallery = get_object_or_404(Gallery, id=gallery.id)
            for img in formset:
                images = img.save(commit=False)
                images.gallery = filmform.gallery
                images.save()
            formset.save()
            filmform.save()
            print(filmform)

    context = {'form': form, 'formseo': formseo, 'formset': formset}

    return render(request, 'adminlte/addfilm.html', context=context)


#Для створення нових новин
def addnews(request):
    ImageNewsFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageNewsFormset(request.POST or None, request.FILES or None, queryset=Image.objects.none())

    newsform = NewsForm(request.POST or None, request.FILES or None)
    formseo = SeoBlockForm(request.POST or None)

    print(formset.errors, newsform.errors, formseo.errors)
    if request.method == "POST":
        if newsform.is_valid() and formseo.is_valid() and formset.is_valid():
            news = newsform.save(commit=False)
            news.type = 'News'
            news.seo_block = formseo.save()
            gallery = Gallery.objects.create(text=news.name_eng)
            news.gallery = get_object_or_404(Gallery, id=gallery.id)
            for img in formset:
                images = img.save(commit=False)
                images.gallery = news.gallery
                images.save()
            formset.save()
            news.save()

    context = {'news': newsform, 'seo': formseo, 'formset': formset}

    return render(request, 'adminlte/addnews.html', context=context)


#Для створення нових акцій
def adddiscount(request):
    ImageDiscountFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageDiscountFormset(request.POST or None, request.FILES or None, queryset=Image.objects.none())

    discountform = DiscountForm(request.POST or None, request.FILES or None)
    formseo = SeoBlockForm(request.POST or None)


    print(formset.errors, discountform.errors, formseo.errors)
    if request.method == "POST":
        if discountform.is_valid() and formseo.is_valid() and formset.is_valid():
            discount = discountform.save(commit=False)
            discount.type = 'Discount'
            discount.seo_block = formseo.save()
            gallery = Gallery.objects.create(text=discount.name_eng)
            discount.gallery = get_object_or_404(Gallery, id=gallery.id)
            discount.date_created_updated = timezone.now()
            print(discount.date_created_updated)
            for img in formset:
                images = img.save(commit=False)
                images.gallery = discount.gallery
                images.save()
            formset.save()
            discount.save()

    context = {'discount': discountform, 'seo': formseo, 'formset': formset}

    return render(request, 'adminlte/adddiscount.html', context=context)


def addcinema(request):
    CinemaFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = CinemaFormset(request.POST or None, request.FILES or None, queryset=Image.objects.none())

    cinemaform = CinemaForm(request.POST or None, request.FILES or None)
    formseo = SeoBlockForm(request.POST or None)

    if request.method == 'POST':
        cinema = cinemaform.save(commit=False)
        cinema.seo_block = formseo.save()
        gallery = Gallery.objects.create(text=cinema.name_eng)
        cinema.gallery = get_object_or_404(Gallery, pk=gallery.id)
        for img in formset:
            images = img.save(commit=False)
            images.gallery = cinema.gallery
            images.save()
        formset.save()
        cinema.save()

    context = {
        'cinema': cinemaform,
        'seo': formseo,
        'formset': formset
    }

    return render(request, 'adminlte/addcinema.html', context)

def addhall(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    cinemaform = CinemaForm(request.POST or None, instance=cinema)
    hallform = HallForm(request.POST or None, request.FILES or None)
    formseo = SeoBlockForm(request.POST or None)
    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.none())

    if request.method == 'POST':

        if hallform.is_valid() and formseo.is_valid() and formset.is_valid():
            hall = hallform.save(commit=False)
            hall.seo_block = formseo.save()
            hall.cinema = cinemaform.instance
            gallery = Gallery.objects.create(text=hall.hall_number)
            hall.gallery = get_object_or_404(Gallery, pk=gallery.id)
            for img in formset:
                images = img.save(commit=False)
                images.gallery = hall.gallery
                images.save()
            formset.save()
            hall.save()

    context = {'hall': hallform, 'formset': formset, 'seo': formseo}

    return render(request, 'adminlte/addhall.html', context)

def hallview(request, cinema_id,pk):

    hall = get_object_or_404(Hall, pk=pk)
    seo = get_object_or_404(SeoBlock, pk=hall.seo_block.id)

    hallform = HallForm(request.POST or None, request.FILES or None, instance=hall)
    seoform = SeoBlockForm(request.POST or None, instance=seo)

    ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=hall.gallery.id))
    context = {'hall': hallform, 'formset': formset, 'seo': seoform, 'image': hall}


    if request.method == 'POST':

        hall = get_object_or_404(Hall, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=hall.seo_block.id)

        hallform = HallForm(request.POST or None, request.FILES or None, instance=hall)
        seoform = SeoBlockForm(request.POST or None, instance=seo)

        ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = ImageFormset(request.POST or None, request.FILES or None,
                               queryset=Image.objects.filter(gallery=hall.gallery.id))
        if hallform.is_valid() and seoform.is_valid() and formset.is_valid():
            hall = hallform.save(commit=False)
            print(hall)
            hall.seo_block = seoform.save()
            print(hall.seo_block)
            gallery = Gallery.objects.get(pk=hall.gallery.id)
            print(gallery)
            gallery.text = hall.hall_number
            print(gallery.text)
            hall.gallery = get_object_or_404(Gallery, id=gallery.id)
            print(hall.gallery)
            print(hallform.errors, seoform.errors, formset.errors)
            for img in formset:
                print(img.errors)
                image = img.save(commit=False)
                image.gallery = hall.gallery
                image.save()

            formset.save()
            hall.save()

            context = {'hall': hallform, 'formset': formset, 'seo': seoform, 'image': hall}

            return redirect('hall_edit', pk=hall.id, cinema_id=hall.cinema.id)

    return render(request, 'adminlte/Hall_edit.html', context)

def test(request):
    if request.method == 'POST':
        print('Oki')
        form = CinemaForm(request.POST)
        if form.is_valid():
            print('Hiii')
            print(form.cleaned_data)

    else:
        form = CinemaForm()
    return render(request, 'adminlte/test.html', {'form': form})


def newtest(request):


    return render(request, 'adminlte/newtest.html')


class CinameView(View):
    def get(self, request):
        cinema = Cinema.objects.all()

        return render(request, 'adminlte/cinemas.html', {'cinema_list': cinema})


#Для відобреження існуючих фільмів
class FilmView(View):
    def get(self, request):
        startdate = datetime.today()
        enddate = startdate + timedelta(days=365 * 5)
        film_new = Film.objects.filter(date_premiere__range=[startdate, enddate])
        startolddate = startdate - timedelta(days=365 * 2)
        print(startolddate, startdate)
        film_old = Film.objects.filter(date_premiere__range=[startolddate, startdate])
        return render(request, 'adminlte/films.html', {'film_list_new': film_new, 'film_list_old': film_old})



#Для відобреження існуючих новин
class NewsView(View):
    def get(self, request):
        news = NewsAndDiscount.objects.filter(type='News')

        return render(request, 'adminlte/news.html', {'news_list': news})



#Для відобреження існуючих акцій
class DiscountView(View):
    def get(self, request):
        discount = NewsAndDiscount.objects.filter(type='Discount')

        return render(request, 'adminlte/discounts.html', {'discount_list': discount})



#Докладна інформація про фільм
class FilmDetailView(View):
    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=film.seo_block.id)

        filmsave = FilmForm(request.POST or None, request.FILES or None, instance=film)
        formseo = SeoBlockForm(request.POST or None, instance=seo)

        ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = ImageFormset(request.POST or None, request.FILES or None,
                               queryset=Image.objects.filter(gallery=film.gallery.id))
        print(formset.queryset)
        print(formset.errors)

        context = {'form': filmsave, 'formseo': formseo, 'formset': formset, 'film': film}

        return render(request, 'adminlte/Film_edit.html', context)


    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=film.seo_block.id)

        filmsave = FilmForm(request.POST or None, request.FILES or None, instance=film)
        formseo = SeoBlockForm(request.POST or None, instance=seo)


        ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = ImageFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=film.gallery.id))
        print(formset.errors, filmsave.errors)
        # print(formset)
        if request.method == 'POST':
            if filmsave.is_valid() and formseo.is_valid() and formset.is_valid():
                print('-------------')
                print(request.FILES)
                print(formset.errors, formset.cleaned_data)
                film = filmsave.save(commit=False)
                film.seo_block = formseo.save()
                gallery = Gallery.objects.get(pk=film.gallery.id)
                gallery.text = film.name_eng
                film.gallery = get_object_or_404(Gallery, id=gallery.id)
                for img in formset:
                    print('-------------')
                    images = img.save(commit=False)
                    images.gallery = film.gallery
                    images.save()


                print(formset.errors, filmsave.errors)

                formset.save()
                film.save()

            return redirect('films')


class CinemaDetailView(View):
    def get(self, request, pk):
        cinema = get_object_or_404(Cinema, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=cinema.seo_block.id)
        hall = Hall.objects.filter(cinema=cinema.id)

        formcinema = CinemaForm(request.POST or None, request.FILES or None, instance=cinema)
        formseo = SeoBlockForm(request.POST or None, request.FILES or None, instance=seo)

        CinemaFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = CinemaFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=cinema.gallery.id))

        print(formcinema.errors, formcinema.instance.top_banner.url)

        context = {'cinema': formcinema, 'seo': formseo, 'formset': formset, 'image': cinema, 'hall_list': hall}

        return render(request, 'adminlte/Cinema_edit.html', context=context)

    def post(self, request, pk):
        cinema = get_object_or_404(Cinema, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=cinema.seo_block.id)

        formcinema = CinemaForm(request.POST or None, request.FILES or None, instance=cinema)
        formseo = SeoBlockForm(request.POST or None, instance=seo)

        CinemaFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = CinemaFormset(request.POST or None, request.FILES or None, queryset=Image.objects.filter(gallery=cinema.gallery.id))

        if request.method == 'POST':
            print(formset.errors, formseo.errors, formcinema.errors)
            if formset.is_valid() and formseo.is_valid() and formcinema.is_valid():
                print(formset.errors, formseo.errors, formcinema.errors)
                cinema = formcinema.save(commit=False)
                cinema.seo_block = formseo.save()
                gallery = Gallery.objects.get(pk=cinema.gallery.id)
                gallery.text = cinema.name_eng
                cinema.gallery = get_object_or_404(Gallery, id=gallery.id)
                for img in formset:
                    image = img.save(commit=False)
                    image.gallery = cinema.gallery
                    image.save()
                formset.save()
                cinema.save()

        return redirect('cinemas')





#Докладна інформація про новину
class NewsDetailView(View):
    def get(self, request, pk):
        news = get_object_or_404(NewsAndDiscount, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=news.seo_block.id)

        newssave = NewsForm(request.POST or None, request.FILES or None, instance=news)
        formseo = SeoBlockForm(request.POST or None, instance=seo)

        ImageNewsFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = ImageNewsFormset(request.POST or None, request.FILES or None,
                               queryset=Image.objects.filter(gallery=news.gallery.id))
        print(formset.queryset)
        print(formset.errors)

        context = {'news': newssave, 'seo': formseo, 'formset': formset, 'image': news}

        return render(request, 'adminlte/News_edit.html', context)

    def post(self, request, pk):
        news = get_object_or_404(NewsAndDiscount, pk=pk)
        seo = get_object_or_404(SeoBlock, pk=news.seo_block.id)

        newssave = NewsForm(request.POST or None, request.FILES or None, instance=news)
        formseo = SeoBlockForm(request.POST or None, instance=seo)

        ImageNewsFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        formset = ImageNewsFormset(request.POST or None, request.FILES or None,
                               queryset=Image.objects.filter(gallery=news.gallery.id))
        print(formset.errors, newssave.errors)
        # print(formset)
        if request.method == 'POST':
            if newssave.is_valid() and formseo.is_valid() and formset.is_valid():
                print('-------------')
                print(request.FILES)
                print(formset.errors, formset.cleaned_data)
                news = newssave.save(commit=False)
                news.seo_block = formseo.save()
                gallery = Gallery.objects.get(pk=news.gallery.id)
                gallery.text = news.name_eng
                news.gallery = get_object_or_404(Gallery, id=gallery.id)
                for img in formset:
                    print('-------------')
                    images = img.save(commit=False)
                    images.gallery = news.gallery
                    images.save()

                print(formset.errors, newssave.errors)
                formset.save()
                news.save()

            return redirect('news')


#Докладна інформація про акцію
class DiscountDetailView(View):
        def get(self, request, pk):
            discount = get_object_or_404(NewsAndDiscount, pk=pk)
            seo = get_object_or_404(SeoBlock, pk=discount.seo_block.id)

            discountsave = DiscountForm(request.POST or None, request.FILES or None, instance=discount)
            formseo = SeoBlockForm(request.POST or None, instance=seo)

            ImageDiscountFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
            formset = ImageDiscountFormset(request.POST or None, request.FILES or None,
                                       queryset=Image.objects.filter(gallery=discount.gallery.id))
            print(formset.queryset)
            print(formset.errors)

            context = {'news': discountsave, 'seo': formseo, 'formset': formset, 'image': discount}

            return render(request, 'adminlte/News_edit.html', context)

        def post(self, request, pk):
            discount = get_object_or_404(NewsAndDiscount, pk=pk)
            seo = get_object_or_404(SeoBlock, pk=discount.seo_block.id)

            discount.type = 'Discount'

            discountsave = DiscountForm(request.POST or None, request.FILES or None, instance=discount)
            formseo = SeoBlockForm(request.POST or None, instance=seo)

            ImageDiscountFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
            formset = ImageDiscountFormset(request.POST or None, request.FILES or None,
                                       queryset=Image.objects.filter(gallery=discount.gallery.id))
            print(formset.errors, discountsave.errors)
            # print(formset)
            if request.method == 'POST':
                if discountsave.is_valid() and formseo.is_valid() and formset.is_valid():
                    print('-------------')
                    print(request.FILES)
                    print(formset.errors, formset.cleaned_data)
                    discount = discountsave.save(commit=False)
                    discount.seo_block = formseo.save()
                    gallery = Gallery.objects.get(pk=discount.gallery.id)
                    gallery.text = discount.name_eng
                    discount.gallery = get_object_or_404(Gallery, id=gallery.id)
                    for img in formset:
                        print('-------------')
                        images = img.save(commit=False)
                        images.gallery = discount.gallery
                        images.save()

                    print(formset.errors, discountsave.errors)

                    formset.save()
                    discount.save()

                return redirect('discounts')


class BannerView(View):
    def get(self, request, pk):
        banner = get_object_or_404(TopHomeBanner, pk=pk)

        return render(request, 'adminlte/banners.html', {'banner_list': banner})

    def post(self, request, pk):
        banner = get_object_or_404(TopHomeBannerForm, pk=pk)
        speeds = get_object_or_404(SpeedCarouselForm, pk=banner.speed_carousel.id)

        BannerFormset = modelformset_factory(TopHomeBanner, form=TopHomeBannerForm, extra=0, can_delete=True)
        formset = BannerFormset(request.POST or None, request.FILES or None, queryset=TopHomeBanner.objects.none())

        speed = SpeedCarouselForm(request.POST or None, instance=speeds)

        print(formset.errors, speed.errors)

        if formset.is_valid() and speed.is_valid():
            speed.save()
            for banner in formset:
                if banner.is_valid():
                    print(speed.cleaned_data, speed.instance.speed_carousel)
                    print(speed.errors, banner.errors)
                    banner.save(commit=False)
                    banner.instance.speed_carousel = speed.instance
                    banner.instance.status = speed.instance.status
                    banner.save()
                    print(banner, banner.errors)




        context = {'formset': formset, 'speed': speed}

        return render(request, 'adminlte/banners.html', context)

def send(user_email):
    send_mail('Ви підписалися на розсилку ',
        [user_email],
        fail_silently=False)

def mailing(request):
    mail = MailingForm(request.POST or None, request.FILES or None)
    return render(request, 'adminlte/mailings.html', {'mailing': mail})



