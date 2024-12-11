import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# UPDATE secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalog",
    "blog",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_ADMIN = EMAIL_HOST_USER

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "catalog:product_list"
LOGOUT_REDIRECT_URL = "catalog:product_list"
LOGIN_URL = "users:login"

BANNED_WORDS = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")
ALLOWED_EXTENSIONS = ("jpeg", "png")
MAX_UPLOAD_SIZE = 5242880

COUNTRIES = (
    ("AUS", "Австралия"),
    ("AUT", "Австрия"),
    ("AZE", "Азербайджан"),
    ("ALA", "Аландские острова"),
    ("ALB", "Албания"),
    ("DZA", "Алжир"),
    ("VIR", "Виргинские Острова (США)"),
    ("ASM", "Американское Самоа"),
    ("AIA", "Ангилья"),
    ("AGO", "Ангола"),
    ("AND", "Андорра"),
    ("ATA", "Антарктика"),
    ("ATG", "Антигуа и Барбуда"),
    ("ARG", "Аргентина"),
    ("ARM", "Армения"),
    ("ABW", "Аруба"),
    ("AFG", "Афганистан"),
    ("BHS", "Багамские Острова"),
    ("BGD", "Бангладеш"),
    ("BB", "Барбадос"),
    ("BHR", "Бахрейн"),
    ("BLR", "Беларусь"),
    ("BLZ", "Белиз"),
    ("BEL", "Бельгия"),
    ("BEN", "Бенин"),
    ("BMU", "Бермуды"),
    ("BGR", "Болгария"),
    ("BOL", "Боливия"),
    ("BES", "Бонайре, Синт-Эстатиус и Саба"),
    ("BIH", "Босния и Герцеговина"),
    ("BWA", "Ботсвана"),
    ("BRA", "Бразилия"),
    ("IOT", "Британская Территория в Индийском Океане"),
    ("VGB", "Виргинские Острова (Великобритания)"),
    ("BRN", "Бруней"),
    ("BFA", "Буркина-Фасо"),
    ("BDI", "Бурунди"),
    ("BTN", "Бутан"),
    ("VUT", "Вануату"),
    ("VAT", "Ватикан"),
    ("GBR", "Великобритания"),
    ("HUN", "Венгрия"),
    ("VEN", "Венесуэла"),
    ("UMI", "Внешние малые острова США"),
    ("TLS", "Восточный Тимор"),
    ("VNM", "Вьетнам"),
    ("GAB", "Габон"),
    ("HTI", "Гаити"),
    ("GUY", "Гайана"),
    ("GMB", "Гамбия"),
    ("GHA", "Гана"),
    ("GLP", "Гваделупа"),
    ("GTM", "Гватемала"),
    ("GUF", "Гвиана"),
    ("GIN", "Гвинея"),
    ("GNB", "Гвинея-Бисау"),
    ("DEU", "Германия"),
    ("GGY", "Гернси"),
    ("GIB", "Гибралтар"),
    ("HND", "Гондурас"),
    ("HKG", "Гонконг"),
    ("GRD", "Гренада"),
    ("GRL", "Гренландия"),
    ("GRC", "Греция"),
    ("GEO", "Грузия"),
    ("GUM", "Гуам"),
    ("DNK", "Дания"),
    ("JEY", "Джерси"),
    ("DJI", "Джибути"),
    ("DMA", "Доминика"),
    ("DOM", "Доминиканская Республика"),
    ("COD", "ДР Конго"),
    ("EGY", "Египет"),
    ("ZMB", "Замбия"),
    ("ESH", "Западная Сахара"),
    ("ZWE", "Зимбабве"),
    ("ISR", "Израиль"),
    ("IND", "Индия"),
    ("IDN", "Индонезия"),
    ("JOR", "Иордания"),
    ("IRQ", "Ирак"),
    ("IRN", "Иран"),
    ("IRL", "Ирландия"),
    ("ISL", "Исландия"),
    ("ESP", "Испания"),
    ("ITA", "Италия"),
    ("YEM", "Йемен"),
    ("CPV", "Кабо-Верде"),
    ("KAZ", "Казахстан"),
    ("CYM", "Острова Кайман"),
    ("KHM", "Камбоджа"),
    ("CMR", "Камерун"),
    ("CAN", "Канада"),
    ("QAT", "Катар"),
    ("KEN", "Кения"),
    ("CYP", "Кипр"),
    ("KGZ", "Кыргызстан"),
    ("KIR", "Кирибати"),
    ("TWN", "Китайская Республика"),
    ("PRK", "КНДР"),
    ("CHN", "Китай"),
    ("CCK", "Кокосовые острова"),
    ("COL", "Колумбия"),
    ("COM", "Коморские острова"),
    ("CRI", "Коста-Рика"),
    ("CIV", "Кот-д'Ивуар"),
    ("CUB", "Куба"),
    ("KWT", "Кувейт"),
    ("CUW", "Кюрасао"),
    ("LAO", "Лаос"),
    ("LVA", "Латвия"),
    ("LSO", "Лесото"),
    ("LBR", "Либерия"),
    ("LBN", "Ливан"),
    ("LBY", "Ливия"),
    ("LTU", "Литва"),
    ("LIE", "Лихтенштейн"),
    ("LUX", "Люксембург"),
    ("MUS", "Маврикий"),
    ("MRT", "Мавритания"),
    ("MDG", "Мадагаскар"),
    ("MDG", "Мадагаскар"),
    ("MYT", "Майотта"),
    ("MAC", "Макао"),
    ("MKD", "Северная Македония"),
    ("MWI", "Малави"),
    ("MYS", "Малайзия"),
    ("MLI", "Мали"),
    ("MDV", "Мальдивы"),
    ("MLT", "Мальта"),
    ("MAR", "Марокко"),
    ("MTQ", "Мартиника"),
    ("MHL", "Маршалловы острова"),
    ("MEX", "Мексика"),
    ("FSM", "Микронезия"),
    ("MOZ", "Мозамбик"),
    ("MDA", "Молдова"),
    ("MCO", "Монако"),
    ("MNG", "Монголия"),
    ("MSR", "Монтсеррат"),
    ("MMR", "Мьянма"),
    ("NAM", "Намибия"),
    ("NRU", "Науру"),
    ("NPL", "Непал"),
    ("NER", "Нигер"),
    ("NGA", "Нигерия"),
    ("NLD", "Нидерланды"),
    ("NIC", "Никарагуа"),
    ("NIU", "Ниуэ"),
    ("NZL", "Новая Зеландия"),
    ("NCL", "Новая Каледония"),
    ("NOR", "Норвегия"),
    ("ARE", "ОАЭ"),
    ("OMN", "Оман"),
    ("BVT", "Остров Буве"),
    ("IMN", "Остров Мэн"),
    ("COK", "Острова Кука"),
    ("NFK", "Остров Норфолк"),
    ("CXR", "Остров Рождества"),
    ("PCN", "Острова Питкэрн"),
    ("SHN", "Остров Святой Елены"),
    ("PAK", "Пакистан"),
    ("PLW", "Палау"),
    ("PSE", "Государство Палестина"),
    ("PAN", "Панама"),
    ("PNG", "Папуа-Новая Гвинея"),
    ("PRY", "Парагвай"),
    ("PER", "Перу"),
    ("POL", "Польша"),
    ("PRT", "Португалия"),
    ("PRI", "Пуэрто-Рико"),
    ("COG", "Республика Конго"),
    ("KOR", "Республика Корея"),
    ("REU", "Реюньон"),
    ("RUS", "Россия"),
    ("RWA", "Руанда"),
    ("ROU", "Румыния"),
    ("SLV", "Сальвадор"),
    ("WSM", "Самоа"),
    ("SMR", "Сан-Марино"),
    ("STP", "Сан-Томе и Принсипи"),
    ("SAU", "Саудовская Аравия"),
    ("MNP", "Северные Марианские острова"),
    ("SYC", "Сейшельские Острова"),
    ("BLM", "Сен-Бартелеми"),
    ("MAF", "Сен-Мартен"),
    ("SPM", "Сен-Пьер и Микелон"),
    ("SEN", "Сенегал"),
    ("VCT", "Сен-Винсент и Гренадины"),
    ("KNA", "Сент-Китс и Невис"),
    ("LCA", "Сент-Люсия"),
    ("SRB", "Сербия"),
    ("SGP", "Сингапур"),
    ("SXM", "Синт-Мартен"),
    ("SYR", "Сирия"),
    ("SVK", "Словакия"),
    ("SVN", "Словения"),
    ("SLB", "Соломоновы острова"),
    ("SOM", "Сомали"),
    ("SDN", "Судан"),
    ("SUR", "Суринам"),
    ("USA", "США"),
    ("SLE", "Сьерра-Леоне"),
    ("TJK", "Таджикистан"),
    ("THA", "Таиланд"),
    ("TZA", "Танзания"),
    ("TCA", "Теркс и Кайкос"),
    ("TGO", "Того"),
    ("TKL", "Токелау"),
    ("TON", "Тонга"),
    ("TTO", "Тринидад и Тобаго"),
    ("TUV", "Тувалу"),
    ("TUN", "Тунис"),
    ("TKM", "Туркменистан"),
    ("TUR", "Турция"),
    ("UGA", "Уганда"),
    ("UZB", "Узбекистан"),
    ("UKR", "Украина"),
    ("WLF", "Уоллис и Футуна"),
    ("URY", "Уругвай"),
    ("FRO", "Фарерские острова"),
    ("FJI", "Фиджи"),
    ("PHL", "Филиппины"),
    ("FIN", "Финляндия"),
    ("FLK", "Фолклендские острова"),
    ("FRA", "Франция"),
    ("PYF", "Французская Полинезия"),
    ("ATF", "Французские Южные и Антарктические территории"),
    ("HMD", "Херд и Макдональд"),
    ("HRV", "Хорватия"),
    ("CAF", "ЦАР"),
    ("TCD", "Чад"),
    ("MNE", "Черногория"),
    ("CZE", "Чехия"),
    ("CHL", "Чили"),
    ("CHE", "Швейцария"),
    ("SWE", "Швеция"),
    ("SJM", "Шпицберген и Ян-Майен"),
    ("LKA", "Шри-Ланка"),
    ("ECU", "Эквадор"),
    ("GNQ", "Экваториальная Гвинея"),
    ("ERI", "Эритрея"),
    ("SWZ", "Эсватини"),
    ("EST", "Эстония"),
    ("ETH", "Эфиопия"),
    ("ZAF", "ЮАР"),
    ("SGS", "Южная Георгия и Южные Сандвичевы о‐ва"),
    ("SSD", "Южный Судан"),
    ("JAM", "Ямайка"),
    ("JPN", "Япония"),
)
