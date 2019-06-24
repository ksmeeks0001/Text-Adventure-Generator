
import django
from django.conf import settings
from django.template import Template, Context
    
def setup_django():
    """Setup django settings and configurations"""
    
    TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates'}
    ]   
    settings.configure(TEMPLATES=TEMPLATES)
    django.setup()

def refresh_template(template, context=dict(), form=''):
    """
        Generate html from template.
        -template = url to html file
        -form = initialized form object
        -context = dictionary            """

    with open('templates\\' + template, 'r') as file:
        generate = Template(file.read())

    context['form'] = form
    generate_context = Context(context)

    with open('static\\' + template, 'w') as file:
        file.write(generate.render(generate_context))
