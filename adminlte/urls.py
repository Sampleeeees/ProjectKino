from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin'),
    path('statistics/', views.statistic, name='statistic'),
    path('banners/', views.banner, name='banners'),
    path('cinemas/', views.CinameView.as_view(), name='cinemas'),
    path('films/', views.FilmView.as_view(), name='films'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('discounts/', views.DiscountView.as_view(), name='discounts'),
    path('pages/', views.page, name='pages'),
    path('users/', views.user, name='users'),
    path('users/edit<user_id>', views.useredit, name='useredit'),
    path('mailings/', views.mailing, name='mailings'),
    # add block
    # films
    path('films/createfilm/', views.addfilm, name='addfilm'),
    path('films/edit/<int:pk>', views.FilmDetailView.as_view(), name='filmdetailadmin'),
    # news
    path('news/createnews/', views.addnews, name='addnews'),
    path('news/edit/<int:pk>', views.NewsDetailView.as_view(), name='newsdetail'),
    # discount
    path('discounts/creatediscount/', views.adddiscount, name='adddiscount'),
    path('discounts/edit/<int:pk>', views.DiscountDetailView.as_view(), name='discountdetail'),
    # cinema
    path('cinemas/createcinema/', views.addcinema, name='addcinema'),
    path('cinemas/edit/<int:pk>/', views.CinemaDetailView.as_view(), name='cinemadetail'),
    # hall
    path('cinemas/edit/createhall/<int:pk>', views.addhall, name='addhall'),
    path('cinemas/edit/<cinema_id>/hall/<int:pk>', views.hallview, name='hall_edit'),
    path('test/', views.test, name='test'),
    path('newtest/', views.newtest, name='newtest'),
    #
    path('<name>/delete/<delete_item>', views.delete, name='delete-any'),
    path('pages/homepage', views.general_page, name='homepage'),
    path('pages/aboutcinema', views.aboutcinema, name='aboutcinema'),
    path('pages/cafebar', views.cafebar, name='cafebardetail'),
    path('pages/viphall', views.viphalldetail, name='viphalldetail'),
    path('pages/adverising', views.advertisingdetail, name='advertisingdetail'),
    path('pages/childroom', views.childroomdetail, name='childroomdetail'),
    path('pages/contacts', views.contact, name='contactdetail'),
    path('pages/newpage', views.newpage, name='createnewpage'),
    path('pages/newpageedit/<page_id>', views.newpageedit, name='newpageedit'),
]


