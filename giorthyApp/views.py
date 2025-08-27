from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'index.html', {'inicio': inicio})


def bici_montana(request):
    bicicleta_montana = [
        {
            'marca':'Trek',
            'modelo':'marlin 7',
            'tipo':'montaña',
            'precio': 55000
        },
        {
            'marca':'Trek',
            'modelo':'marlin 7',
            'tipo':'montaña',
            'precio': 55000
        },
        {
            'marca':'Trek',
            'modelo':'marlin 7',
            'tipo':'montaña',
            'precio': 55000
        },
    ]
    return render(request,'bicis.html',{'bicicleta_montana':bicicleta_montana})


def bici_electrica(request):
    bicicleta_electrica =[
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000
        },
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000
        },
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000
        }
    ]
    return render(request, 'bicis.html', {'bicicleta_electrica': bicicleta_electrica})

def bici_bmx(request):
    bicicleta_bmx=[
        {
            'marca':'cult',
            'modelo':'Arcade candy ',
            'tipo':'bmx',
            'precio': 550000
        },
        {
            'marca':'Subrosa',
            'modelo':'Sunday forecaster ',
            'tipo':'bmx',
            'precio': 995000
        },
        {
            'marca':'vans',
            'modelo':'Box rail',
            'tipo':'bmx',
            'precio': 400000
        }
    ]
    return render(request, 'bicis.html',{'bicicleta_bmx':bicicleta_bmx})