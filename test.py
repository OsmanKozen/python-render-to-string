from django.template.loader import render_to_string
from django.conf import settings
import pathlib

# Python kodunuzun bulunduğu mevcut dizin
BASE_DIR = pathlib.Path(__file__).parent.absolute()

settings.configure(TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some other options here ...
        },
    },
])

if __name__ == '__main__':

    import django
    django.setup()

    context = {'deger_ad': 'Osman',
               'deger_soyad': 'Közen'}

    email_body = render_to_string("index.html", context)

    print(email_body)