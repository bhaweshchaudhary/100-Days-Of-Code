from django.shortcuts import render, HttpResponse

# Create your views here.
def app(request):
    head = "App Land"
    main_text = "Promote Your App with App Land"
    desc = "We can promote your App better than anyone."
    return render(request, 'index.html', {"logo": head, "main_text": main_text, "desc": desc,})
