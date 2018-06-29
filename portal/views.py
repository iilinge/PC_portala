from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.template  import loader
from django.conf.urls.static import static
# from .models import Female, Male, Movie
from portal.forms import ContactForm
from .models import Question
from .graphmodel import Country, Person
from .forms import ContactForm


#def index(request):
#    latest_question_list = Question.objects.order_by('-pubdate')[:5]
#    template = loader.get_template('portal/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#        #        'Узлы': Male.nodes.all(),
#    }
#    return HttpResponse(template.render(context, request))
#
#    # def get_books(request):
#    #       return render('portal/books.html', request, {'Узлы': Male.nodes.all()})
#    return render_to_response('portal/index.html', {'error': True})


def index(request):
    dict_f_search = "Введите термин ..."
    return render_to_response('index.html', {'f_search': dict_f_search})

def searchres(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос.')
        elif len(q) > 5:
            errors.append('Длина термина должна быть больше 5 символов.')
        else:
           resq = Question.objects.filter(questiontext__icontains=q)
           return render_to_response('search_results.html',{'questions': resq, 'query': q})
    return render_to_response('index.html',{'errors': errors})

def contact(request):
    if request.method == 'POST':
       yform = ContactForm(request.POST)
       if yform.is_valid():
          cd = yform.cleaned_data
          send_mail(
              cd['subject'],
              cd['message'],
              cd.get('email', 'noreply@example.com'),['iil@ibrae.ac.ru'],
          )
          return HttpResponseRedirect('/contact/thanks/')
    else:
        yform = ContactForm()
    return render_to_response('contact_form.html', {'form': yform})

def terr(request):
    te = get_template('blockone.html')
    html = te.render()
    return HttpResponse(html)