# laLeveeDeCoude

### Create container :

docker-compose run web django-admin startproject lldc .

### When Models are created :

docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate

### Start project :

docker-compose up

### Stop project :

docker-compose down

### Create admin user :

docker-compose run web python manage.py createsuperuser

### Migrate data from API :

Go to the /migration page as admin and load the page 

## Styles

### Use

For each template, link the `main` style sheet of `css/base` and if necessary the style sheet of your template.

```
{% load compress %} {% compress css %}
<link
  type="text/x-scss"
  href="{% static 'css/base/main.scss' %}"
  rel="stylesheet"
  media="screen"
/>
<link
  type="text/x-scss"
  href="{% static 'css/custom/login.scss' %}"
  rel="stylesheet"
  media="screen"
/>
{% endcompress %}
```

### Organization

The project uses `scss` syntax for its style sheets. These are in the `static/css` folder at the root.

In this folder, you find all the style sheets concerning the theme and all the css classes that can be used in the project in the `base` folder. **A documentation of these classes is present in `READMECSS.md`**.

You will also find a `custom` folder in which to put your template-specific style sheets.

At the root, you will find a `shame.scss` file: this one is used in case you want to make a css class global to several templates but you don't know where to put this class in `base`. _This file should be emptied regularly._
