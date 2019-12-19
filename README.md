# dish-challenge

## Project goals
Create a django-backed webpage emulating a given food delivery menu, and have the ability to take a "screenshot" of the page to send as an mms.

Built using Django, styled using CSS grid.

Deployed site: https://as-dishes-challenge.herokuapp.com/

## Dependencies
- Imgkit
- wkhtmltopdf (outside installation)
- dj-databse-url
- Django
- gunicorn
- pillow
- psycopg2-binary (for postgres database)
- whitenoise (for handling deployed static files)

### To run locally:
- `git clone` this repository
- run `pipenv install` to download dependencies
- run `pipenv shell` to access the virtual environment and use the dependencies
- to run start the server:

...run `python manage.py runserver`, then navigate to localhost:8000. You may also have to run `python manage.py makemigrations` and `python manage.py migrate`.

- to take an image of the deployed site:

...run `python food_imgkit.py`. This will output an image titled `dishmms.jpg` directly into the root of your local clone.

### A quick note about Imgkit, wkhtmltopdf, and the "screenshot"
You'll quickly notice that the output image has a different layout from the hosted site. This is because wkhtmltopdf does not support CSS grid or flexbox layouts. This is a known issue (source [here](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/3661)). To get around this, the layout would need to be rewritten using floats, which isn't feasible given the time constraints of this project. Other CSS elements have been preserved.

## Sources

- [Uploading images with Django](https://wsvincent.com/django-image-uploads/)
- [Deploying to Heroku with Django - MDN docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
- [Deploying to Heroku with Django - Youtube tutorial](https://www.youtube.com/watch?v=-OwUWBjSCFM)
- [Django Docs](https://docs.djangoproject.com/en/3.0/)
- [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

#### image attribution

Salmon: Photo by Shayda Torabi on Unsplash
Fries: Photo by Sarah Wardlaw on Unsplash
Almond salad: Photo by Gladys Aguayo on Unsplash
Chicken and rice bowl: Photo by khloe arledge on Unsplash
Chicken sandwich: Photo by Anthony Espinosa on Unsplash
Tacos: Photo by cyrus gomez on Unsplash
Doughnut: Photo by Allie Smith on Unsplash
Flatbread: Photo by Ashim D’Silva on Unsplash