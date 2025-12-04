# Интернет-магазин Skystore (Проект Django_HW1)

Проект интернет-магазина, выполненный на Django. В ходе курса проект будет дополняться новыми функциями. Домашнее задание охватывает базовую настройку проекта и создание простого интерфейса с двумя страницами: главной и контактной.

---

## Описание проекта

- Создан Django-проект с приложением `catalog`.
- В приложении реализованы контроллеры для отображения главной страницы и страницы контактов.
- Используются HTML-шаблоны с Bootstrap для стилизации.
- Статические файлы (CSS, JS) расположены в стандартной папке `catalog/static`.
- Настроена маршрутизация с применением `include` для подключения URL из приложения.
- Реализованы CRUD для продуктов.
- Реализованы формы создания, редактирования и удаления продуктов с валидацией на запрещённые слова и отрицательную цену. Проект использует Bootstrap для стилизации форм и страниц.

---

## Структура проекта

```
Django_HW1/
├── manage.py
├── blog/
│   ├── migrations/   
│   │    ├── __init__.py
│   │    └── 0001_initial.py
│   ├── templates/
│   │   └── blog/
│   │       ├── blog_confirm_delete.html
│   │       ├── blog_detail.html
│   │       ├── blog_form.html
│   │       └── blog_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── catalog/
│   ├── fixtures/   
│   │    ├── categories.json
│   │    └── products.json
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── load_test_data.py
│   ├── migrations/   
│   │    ├── __init__.py
│   │    └── 0001_initial.py
│   ├── templates/
│   │   └── catalog/
│   │       └── partials/
│   │       │   ├── footer.html
│   │       │   └── nav.html
│   │       ├── base.html
│   │       ├── contact.html
│   │       ├── home.html
│   │       └── product_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│        └── script.js
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .flake8
├── .gitignore
├── .isort.cfg
├── README.md
├── requirements.txt
└── ...
```

---
## Установка

### 1. Клонировать репозиторий
```
git clone <repository-url>
cd Django_HW1
```

### 2. Создать виртуальное окружение
```
python -m venv venv
```
### Windows:
```
venv\Scripts\activate
```
### Linux/Mac:
```
source venv/bin/activate
```

### 3. Установить зависимости
```
pip install -r requirements.txt
```

### 4. Настроить .env (скопировать .env.example)
cp .env.example .env
### Заполнить DB_NAME, DB_USER, DB_PASSWORD и SECRET_KEY

### 5. Миграции и тестовые данные
* python manage.py makemigrations
* python manage.py migrate
* python manage.py load_test_data

### 6. Запустить сервер
```
python manage.py runserver
```
Открыть в браузере: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


---

## Описание

- Главная страница по адресу `/` рендерится через `catalog.views.home`.
- Страница Контакты доступна по `/contacts/` через `catalog.views.contacts`.
- Шаблоны лежат в `catalog/templates/catalog/`.
- Статические файлы (CSS, JS) лежат в `catalog/static/` и подключаются через тег `{% static %}`.
- Настройки маршрутизации описаны в `config/urls.py` (главный маршрутизатор) и `catalog/urls.py` (маршруты приложения).

---

## Важные настройки

- В `settings.py` обязательно указан параметр:

```

STATIC_URL = '/static/'

```

- В шаблонах необходимо использовать:

```

{% load static %}

<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
<script src="{% static 'js/script.js' %}"></script>

```

---
### Новая функциональность

#### 1. Страница подробной информации о товаре

- Реализован контроллер `product_detail`, отображающий полную информацию о товаре.
- Создан шаблон `product_detail.html` с отображением всех данных: название, описание, категория, цена, изображение, даты создания и обновления.
- Добавлен маршрут с использованием первичного ключа товара для доступа к странице.

#### 2. Отображение списка товаров на главной странице

- Главная страница (`home.html`) теперь отображает список всех товаров из базы.
- В шаблоне использован цикл с обрезкой описания каждого товара до первых 100 символов для единообразного отображения.
- Добавлены ссылки на страницу подробностей каждого товара.

#### 3. Общие шаблоны и включаемые подшаблоны

- Создан базовый шаблон `base.html`, включающий общие элементы страницы: шапку, подвал, подключение стилей и скриптов.
- Для главного меню сделан отдельный подшаблон `menu.html`, который подключается в `base.html` и используется на всех страницах.

### Последнее задание: Рефакторинг на CBV + Блог

####  Рефакторинг catalog (FBV → CBV)
-  Все контроллеры переведены на Class-Based Views
-  `HomeView` (ListView) - список товаров
-  `ContactsView` (FormView) - форма контактов  
-  `ProductDetailView` (DetailView) - детальная страница товара

####  Новое приложение `blog`
-  Создано и зарегистрировано в `INSTALLED_APPS`
-  Модель `BlogPost` с полями: title, content, preview, created_at, is_published, views_count
-  Полный CRUD через CBV: ListView, DetailView, CreateView, UpdateView, DeleteView

####  Модификации блога
-  **Счетчик просмотров** - переопределен `get_object()` в DetailView
-  **Фильтрация** - только опубликованные статьи через `get_queryset()` в ListView
-  **Перенаправление** - после редактирования → страница статьи (`success_url`)

#### ️ Маршрутизация
```
blogs/          - список статей
blogs/create/   - создать статью
blogs/<pk>/     - просмотр статьи
blogs/<pk>/update/ - редактировать
blogs/<pk>/delete/ - удалить
```

####  Шаблоны блога
- Все шаблоны используют `catalog/base.html`
- Поддержка пагинации, изображений превью, счетчика просмотров

####  Быстрый старт блога
```
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000
```

**Админка:** `/admin/blog/blogpost/`  
**Блог:** `/blogs/`

---

### Функциональность по заданию ver.26.1

### Функционал

* CRUD операции с продуктами (создание, чтение, обновление, удаление)
* Формы с валидацией запрещённых слов в названии и описании продукта:
* запрещённые слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар
* Кастомная валидация для поля цены — отрицательная цена не допускается
* Валидация загрузки изображений — разрешены только JPG и PNG, размер не более 5 МБ
* Использование Django Class-Based Views: ListView, CreateView, UpdateView, DeleteView
* Стилизация форм и страниц с использованием Bootstrap 5

### Изменения в проекте

Добавлен файл `catalog/forms.py` с классом `ProductForm`, реализующим валидацию и стилизацию
В `catalog/views.py` добавлены классы для CRUD:
`
ProductListView
ProductCreateView
ProductUpdateView
ProductDeleteView
`

В `catalog/urls.py` добавлены маршруты для CRUD и зарегистрирован `app_name = 'catalog'`

### Шаблоны:

```
catalog/templates/catalog/product_form.html — форма создания и редактирования продукта
catalog/templates/catalog/product_confirm_delete.html — подтверждение удаления
catalog/templates/catalog/product_list.html — вывод списка продуктов с кнопками CRUD
```
Скорректированы ссылки в шаблонах с учётом `namespace 'catalog'`

В `config/settings.py` добавлены настройки `MEDIA_URL` и `MEDIA_ROOT` для загрузки изображений

Валидация изображений в ProductForm проверяет расширения и размер файла

---

## Авторы

Проект создан студентом SkyPro в учебных целях, для демонстрации полученных навыков работы с Django.

---

## Лицензия

Проект свободен для использования и модификации.

```