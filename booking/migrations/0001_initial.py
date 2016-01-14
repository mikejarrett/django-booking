# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('gender', models.CharField(choices=[('mrs', 'Mrs'), ('mr', 'Mr')], blank=True, verbose_name='Gender', max_length=10)),
                ('title', models.CharField(choices=[('dr', 'Dr.'), ('prof', 'Prof.')], blank=True, verbose_name='Title', max_length=10)),
                ('forename', models.CharField(blank=True, verbose_name='First name', max_length=20)),
                ('surname', models.CharField(blank=True, verbose_name='Last name', max_length=20)),
                ('nationality', models.CharField(choices=[('AO', 'Angola'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BW', 'Botswana'), ('CD', 'Congo'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CI', "Cote d'Ivoire"), ('CM', 'Cameroon'), ('CV', 'Cape Verde'), ('DJ', 'Djibouti'), ('DZ', 'Algeria'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ET', 'Ethiopia'), ('GA', 'Gabon'), ('GH', 'Ghana'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GQ', 'Equatorial Guinea'), ('GW', 'Guinea-Bissau'), ('KE', 'Kenya'), ('KM', 'Comoros'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LY', 'Libyan Arab Jamahiriya'), ('MA', 'Morocco'), ('MG', 'Madagascar'), ('ML', 'Mali'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('RE', 'Reunion'), ('RW', 'Rwanda'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SH', 'Saint Helena'), ('SL', 'Sierra Leone'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SZ', 'Swaziland'), ('TD', 'Chad'), ('TG', 'Togo'), ('TN', 'Tunisia'), ('TZ', 'Tanzania'), ('UG', 'Uganda'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'), ('AQ', 'Antarctica'), ('BV', 'Bouvet Island'), ('GS', 'South Georgia and the South Sandwich Islands'), ('HM', 'Heard Island and McDonald Islands'), ('TF', 'French Southern Territories'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AM', 'Armenia'), ('AZ', 'Azerbaijan'), ('BD', 'Bangladesh'), ('BH', 'Bahrain'), ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('CC', 'Cocos'), ('CN', 'China'), ('CX', 'Christmas Island'), ('GE', 'Georgia'), ('HK', 'Hong Kong'), ('ID', 'Indonesia'), ('IL', 'Israel'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KG', 'Kyrgyz Republic'), ('KH', 'Cambodia'), ('KP', 'Korea'), ('KR', 'Korea'), ('KW', 'Kuwait'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LK', 'Sri Lanka'), ('MM', 'Myanmar'), ('MN', 'Mongolia'), ('MO', 'Macao'), ('MV', 'Maldives'), ('MY', 'Malaysia'), ('NP', 'Nepal'), ('OM', 'Oman'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PS', 'Palestinian Territory'), ('QA', 'Qatar'), ('SA', 'Saudi Arabia'), ('SG', 'Singapore'), ('SY', 'Syrian Arab Republic'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TW', 'Taiwan'), ('UZ', 'Uzbekistan'), ('VN', 'Vietnam'), ('XD', 'United Nations Neutral Zone'), ('XE', 'Iraq-Saudi Arabia Neutral Zone'), ('XS', 'Spratly Islands'), ('XS', 'Spratly Islands'), ('YE', 'Yemen'), ('AD', 'Andorra'), ('AL', 'Albania'), ('AT', 'Austria'), ('AX', 'Åland Islands'), ('BA', 'Bosnia and Herzegovina'), ('BE', 'Belgium'), ('BG', 'Bulgaria'), ('BY', 'Belarus'), ('CH', 'Switzerland'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DK', 'Denmark'), ('EE', 'Estonia'), ('ES', 'Spain'), ('FI', 'Finland'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GB', 'United Kingdom'), ('GG', 'Guernsey'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('HR', 'Croatia'), ('HU', 'Hungary'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MC', 'Monaco'), ('MD', 'Moldova'), ('ME', 'Montenegro'), ('MK', 'Macedonia'), ('MT', 'Malta'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russian Federation'), ('SE', 'Sweden'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen Islands'), ('SK', 'Slovakia'), ('SM', 'San Marino'), ('TR', 'Turkey'), ('UA', 'Ukraine'), ('VA', 'Holy See'), ('AG', 'Antigua and Barbuda'), ('AI', 'Anguilla'), ('AN', 'Netherlands Antilles'), ('AW', 'Aruba'), ('BB', 'Barbados'), ('BL', 'Saint Barthelemy'), ('BM', 'Bermuda'), ('BQ', 'Bonaire'), ('BS', 'Bahamas'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GP', 'Guadeloupe'), ('GT', 'Guatemala'), ('HN', 'Honduras'), ('HT', 'Haiti'), ('JM', 'Jamaica'), ('KN', 'Saint Kitts and Nevis'), ('KY', 'Cayman Islands'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin'), ('MQ', 'Martinique'), ('MS', 'Montserrat'), ('MX', 'Mexico'), ('NI', 'Nicaragua'), ('PA', 'Panama'), ('PM', 'Saint Pierre and Miquelon'), ('PR', 'Puerto Rico'), ('SV', 'El Salvador'), ('SX', 'Sint Maarten'), ('TC', 'Turks and Caicos Islands'), ('TT', 'Trinidad and Tobago'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States'), ('VC', 'Saint Vincent and the Grenadines'), ('VG', 'British Virgin Islands'), ('VI', 'United States Virgin Islands'), ('AS', 'American Samoa'), ('AU', 'Australia'), ('CK', 'Cook Islands'), ('FJ', 'Fiji'), ('FM', 'Micronesia'), ('GU', 'Guam'), ('KI', 'Kiribati'), ('MH', 'Marshall Islands'), ('MP', 'Northern Mariana Islands'), ('NC', 'New Caledonia'), ('NF', 'Norfolk Island'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PN', 'Pitcairn Islands'), ('PW', 'Palau'), ('SB', 'Solomon Islands'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TV', 'Tuvalu'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('XX', 'Disputed Territory'), ('AR', 'Argentina'), ('BO', 'Bolivia'), ('BR', 'Brazil'), ('CL', 'Chile'), ('CO', 'Colombia'), ('EC', 'Ecuador'), ('FK', 'Falkland Islands'), ('GF', 'French Guiana'), ('GY', 'Guyana'), ('PE', 'Peru'), ('PY', 'Paraguay'), ('SR', 'Suriname'), ('UY', 'Uruguay'), ('VE', 'Venezuela')], blank=True, verbose_name='Nationality', max_length=2)),
                ('street1', models.CharField(blank=True, verbose_name='Street 1', max_length=256)),
                ('street2', models.CharField(blank=True, verbose_name='Street 2', max_length=256)),
                ('city', models.CharField(blank=True, verbose_name='City', max_length=256)),
                ('zip_code', models.CharField(blank=True, verbose_name='ZIP/Postal code', max_length=256)),
                ('country', models.CharField(choices=[('AO', 'Angola'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BW', 'Botswana'), ('CD', 'Congo'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CI', "Cote d'Ivoire"), ('CM', 'Cameroon'), ('CV', 'Cape Verde'), ('DJ', 'Djibouti'), ('DZ', 'Algeria'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ET', 'Ethiopia'), ('GA', 'Gabon'), ('GH', 'Ghana'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GQ', 'Equatorial Guinea'), ('GW', 'Guinea-Bissau'), ('KE', 'Kenya'), ('KM', 'Comoros'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LY', 'Libyan Arab Jamahiriya'), ('MA', 'Morocco'), ('MG', 'Madagascar'), ('ML', 'Mali'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('RE', 'Reunion'), ('RW', 'Rwanda'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SH', 'Saint Helena'), ('SL', 'Sierra Leone'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SZ', 'Swaziland'), ('TD', 'Chad'), ('TG', 'Togo'), ('TN', 'Tunisia'), ('TZ', 'Tanzania'), ('UG', 'Uganda'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'), ('AQ', 'Antarctica'), ('BV', 'Bouvet Island'), ('GS', 'South Georgia and the South Sandwich Islands'), ('HM', 'Heard Island and McDonald Islands'), ('TF', 'French Southern Territories'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AM', 'Armenia'), ('AZ', 'Azerbaijan'), ('BD', 'Bangladesh'), ('BH', 'Bahrain'), ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('CC', 'Cocos'), ('CN', 'China'), ('CX', 'Christmas Island'), ('GE', 'Georgia'), ('HK', 'Hong Kong'), ('ID', 'Indonesia'), ('IL', 'Israel'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KG', 'Kyrgyz Republic'), ('KH', 'Cambodia'), ('KP', 'Korea'), ('KR', 'Korea'), ('KW', 'Kuwait'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LK', 'Sri Lanka'), ('MM', 'Myanmar'), ('MN', 'Mongolia'), ('MO', 'Macao'), ('MV', 'Maldives'), ('MY', 'Malaysia'), ('NP', 'Nepal'), ('OM', 'Oman'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PS', 'Palestinian Territory'), ('QA', 'Qatar'), ('SA', 'Saudi Arabia'), ('SG', 'Singapore'), ('SY', 'Syrian Arab Republic'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TL', 'Timor-Leste'), ('TM', 'Turkmenistan'), ('TW', 'Taiwan'), ('UZ', 'Uzbekistan'), ('VN', 'Vietnam'), ('XD', 'United Nations Neutral Zone'), ('XE', 'Iraq-Saudi Arabia Neutral Zone'), ('XS', 'Spratly Islands'), ('XS', 'Spratly Islands'), ('YE', 'Yemen'), ('AD', 'Andorra'), ('AL', 'Albania'), ('AT', 'Austria'), ('AX', 'Åland Islands'), ('BA', 'Bosnia and Herzegovina'), ('BE', 'Belgium'), ('BG', 'Bulgaria'), ('BY', 'Belarus'), ('CH', 'Switzerland'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DK', 'Denmark'), ('EE', 'Estonia'), ('ES', 'Spain'), ('FI', 'Finland'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GB', 'United Kingdom'), ('GG', 'Guernsey'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('HR', 'Croatia'), ('HU', 'Hungary'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MC', 'Monaco'), ('MD', 'Moldova'), ('ME', 'Montenegro'), ('MK', 'Macedonia'), ('MT', 'Malta'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russian Federation'), ('SE', 'Sweden'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen Islands'), ('SK', 'Slovakia'), ('SM', 'San Marino'), ('TR', 'Turkey'), ('UA', 'Ukraine'), ('VA', 'Holy See'), ('AG', 'Antigua and Barbuda'), ('AI', 'Anguilla'), ('AN', 'Netherlands Antilles'), ('AW', 'Aruba'), ('BB', 'Barbados'), ('BL', 'Saint Barthelemy'), ('BM', 'Bermuda'), ('BQ', 'Bonaire'), ('BS', 'Bahamas'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GP', 'Guadeloupe'), ('GT', 'Guatemala'), ('HN', 'Honduras'), ('HT', 'Haiti'), ('JM', 'Jamaica'), ('KN', 'Saint Kitts and Nevis'), ('KY', 'Cayman Islands'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin'), ('MQ', 'Martinique'), ('MS', 'Montserrat'), ('MX', 'Mexico'), ('NI', 'Nicaragua'), ('PA', 'Panama'), ('PM', 'Saint Pierre and Miquelon'), ('PR', 'Puerto Rico'), ('SV', 'El Salvador'), ('SX', 'Sint Maarten'), ('TC', 'Turks and Caicos Islands'), ('TT', 'Trinidad and Tobago'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States'), ('VC', 'Saint Vincent and the Grenadines'), ('VG', 'British Virgin Islands'), ('VI', 'United States Virgin Islands'), ('AS', 'American Samoa'), ('AU', 'Australia'), ('CK', 'Cook Islands'), ('FJ', 'Fiji'), ('FM', 'Micronesia'), ('GU', 'Guam'), ('KI', 'Kiribati'), ('MH', 'Marshall Islands'), ('MP', 'Northern Mariana Islands'), ('NC', 'New Caledonia'), ('NF', 'Norfolk Island'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PN', 'Pitcairn Islands'), ('PW', 'Palau'), ('SB', 'Solomon Islands'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TV', 'Tuvalu'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('XX', 'Disputed Territory'), ('AR', 'Argentina'), ('BO', 'Bolivia'), ('BR', 'Brazil'), ('CL', 'Chile'), ('CO', 'Colombia'), ('EC', 'Ecuador'), ('FK', 'Falkland Islands'), ('GF', 'French Guiana'), ('GY', 'Guyana'), ('PE', 'Peru'), ('PY', 'Paraguay'), ('SR', 'Suriname'), ('UY', 'Uruguay'), ('VE', 'Venezuela')], blank=True, verbose_name='Country', max_length=2)),
                ('email', models.EmailField(blank=True, verbose_name='Email', max_length=75)),
                ('phone', models.CharField(blank=True, verbose_name='Phone', max_length=256)),
                ('special_request', models.TextField(blank=True, verbose_name='Special request', max_length=1024)),
                ('date_from', models.DateTimeField(blank=True, null=True, verbose_name='From')),
                ('date_until', models.DateTimeField(blank=True, null=True, verbose_name='Until')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('booking_id', models.CharField(blank=True, verbose_name='Booking ID', max_length=100)),
                ('notes', models.TextField(blank=True, verbose_name='Notes', max_length=1024)),
                ('time_period', models.PositiveIntegerField(blank=True, null=True, verbose_name='Time period')),
                ('time_unit', models.CharField(blank=True, max_length=64, verbose_name='Time unit', default='')),
                ('total', models.DecimalField(blank=True, null=True, max_digits=36, verbose_name='Total', decimal_places=2)),
                ('currency', models.CharField(blank=True, verbose_name='Currency', max_length=128)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingError',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('message', models.CharField(blank=True, verbose_name='Message', max_length=1000)),
                ('details', models.TextField(blank=True, verbose_name='Details', max_length=4000)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('booking', models.ForeignKey(to='booking.Booking', verbose_name='Booking')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity', default=1)),
                ('persons', models.PositiveIntegerField(blank=True, null=True, verbose_name='Persons')),
                ('subtotal', models.DecimalField(blank=True, null=True, max_digits=36, verbose_name='Subtotal', decimal_places=2)),
                ('object_id', models.PositiveIntegerField()),
                ('booking', models.ForeignKey(to='booking.Booking', verbose_name='Booking')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-booking__creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingStatusTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=128)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(related_name='translations', null=True, to='booking.BookingStatus', editable=False)),
            ],
            options={
                'default_permissions': (),
                'managed': True,
                'db_table': 'booking_bookingstatus_translation',
                'abstract': False,
                'db_tablespace': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraPersonInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('forename', models.CharField(verbose_name='First name', max_length=20)),
                ('surname', models.CharField(verbose_name='Last name', max_length=20)),
                ('arrival', models.DateTimeField(blank=True, null=True, verbose_name='Arrival')),
                ('message', models.TextField(blank=True, verbose_name='Message', max_length=1024)),
                ('booking', models.ForeignKey(to='booking.Booking', verbose_name='Booking')),
            ],
            options={
                'ordering': ['-booking__creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='bookingstatustranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.ForeignKey(null=True, verbose_name='Booking status', blank=True, to='booking.BookingStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='session',
            field=models.ForeignKey(null=True, verbose_name='Session', blank=True, to='sessions.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(related_name='bookings', null=True, verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
