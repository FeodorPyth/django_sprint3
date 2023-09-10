from django.shortcuts import render


def about(request):
    temlate_name = 'pages/about.html'
    return render(request, temlate_name)


def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)
