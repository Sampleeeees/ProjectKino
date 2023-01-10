# Generated by Django 3.2.15 on 2023-01-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Banner/BackgroundBanner/')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uk', models.CharField(blank=True, max_length=50)),
                ('description_uk', models.TextField(blank=True)),
                ('name_eng', models.CharField(blank=True, max_length=50)),
                ('description_eng', models.TextField(blank=True)),
                ('term_uk', models.TextField()),
                ('term_eng', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='cinema/logo/')),
                ('top_banner', models.ImageField(blank=True, upload_to='cinema/top_banner/')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uk', models.CharField(blank=True, max_length=50)),
                ('description_uk', models.TextField(blank=True)),
                ('name_eng', models.CharField(blank=True, max_length=50)),
                ('description_eng', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, max_length=250, upload_to='film/logo/')),
                ('url', models.URLField()),
                ('type_3d', models.BooleanField()),
                ('type_2d', models.BooleanField()),
                ('type_imax', models.BooleanField()),
                ('date_premiere', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_number', models.IntegerField()),
                ('description', models.TextField()),
                ('scheme_hall', models.ImageField(upload_to='')),
                ('top_banner', models.ImageField(upload_to='')),
                ('cinema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.cinema', verbose_name='Кінотеатр')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея')),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewsAndDiscountBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Banner/NewsAndDiscount/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SeoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_seo', models.URLField()),
                ('tittle_seo', models.CharField(max_length=150)),
                ('keywords_seo', models.CharField(max_length=50)),
                ('description_seo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('day', models.DateField()),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.film', verbose_name='Фільм')),
                ('hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.hall', verbose_name='Кінозал')),
            ],
        ),
        migrations.CreateModel(
            name='SpeedCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed_carousel', models.CharField(blank=True, choices=[('6', '10c'), ('2', '6c'), ('5', '9c'), ('1', '5c'), ('4', '8c'), ('3', '7c')], max_length=50, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopHomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Banner/TopBannerImage/')),
                ('url', models.URLField(blank=True)),
                ('text', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('place', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.session', verbose_name='Сеанс')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uk', models.CharField(blank=True, max_length=50)),
                ('namepage', models.CharField(blank=True, max_length=50)),
                ('description_uk', models.TextField(blank=True)),
                ('name_eng', models.CharField(blank=True, max_length=50)),
                ('description_eng', models.TextField(blank=True)),
                ('status', models.BooleanField()),
                ('date_create', models.DateField(auto_now=True)),
                ('logo', models.ImageField(upload_to='PageImage/')),
                ('url_video', models.URLField()),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея')),
                ('seo_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок')),
            ],
        ),
        migrations.CreateModel(
            name='NewsAndDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uk', models.CharField(blank=True, max_length=50)),
                ('name_eng', models.CharField(blank=True, max_length=50)),
                ('status', models.BooleanField()),
                ('description_uk', models.TextField(blank=True)),
                ('description_eng', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='NewsAndDiscountLogo/')),
                ('url_video', models.URLField()),
                ('type', models.CharField(blank=True, max_length=20)),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея')),
                ('seo_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/gallery_image/')),
                ('gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея')),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('date_create', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('seo_text', models.TextField()),
                ('seo_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок')),
            ],
        ),
        migrations.AddField(
            model_name='hall',
            name='seo_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок'),
        ),
        migrations.AddField(
            model_name='film',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея'),
        ),
        migrations.AddField(
            model_name='film',
            name='seo_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cinema', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('date_create', models.DateField(auto_now=True)),
                ('coordinate', models.IntegerField()),
                ('status', models.BooleanField()),
                ('logo', models.ImageField(upload_to='ContactImage/')),
                ('seo_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.gallery', verbose_name='Галерея'),
        ),
        migrations.AddField(
            model_name='cinema',
            name='seo_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminlte.seoblock', verbose_name='СЕО блок'),
        ),
    ]
