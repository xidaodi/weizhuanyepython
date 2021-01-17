from django.shortcuts import render, HttpResponse
from firstapp.models import People
from django.template import Context, Template

def firstpage(request):
    person = People.objects.all()

    html_str = '''
        <html>
            
            <body>
                
                {% for person in person.all %}
                    
                    <p>  Hello, {{person.name}}, your job is {{person.job}} </p>
                    
                {%  endfor %}
                    
                
               
            </body>
        </html>
    
    
    '''
    t= Template(html_str)
    c= Context({'person': person})

    webpage =t.render(c)

    return HttpResponse(webpage)

