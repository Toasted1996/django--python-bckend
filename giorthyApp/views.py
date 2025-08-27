from django.shortcuts import render

# Create your views here.

def inicio(request):
    indexImages = [
        {
            
        }
    ]
    return render(request,'index.html', {'inicio': inicio})


def bici_montana(request):
    bicicleta_montana = [
        {
            'marca':'Trek',
            'modelo':'marlin 7',
            'tipo':'montaña',
            'precio': 85000,
            'imagen':'/static/images/montana/marlin7.jpg'
        },
        {
            'marca':'Trek',
            'modelo':'marlin 8',
            'tipo':'montaña',
            'precio': 1150000,
            'imagen':'/static/images/montana/marlin8.jpg'
        },
        {
            'marca':'Trek',
            'modelo':'marlin 9',
            'tipo':'montaña',
            'precio': 3490000,
            'imagen':'/static/images/montana/marlin9.jpg'
        },
    ]
    return render(request,'bicis.html',{'bicicleta_montana':bicicleta_montana})


def bici_electrica(request):
    bicicleta_electrica =[
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000,
            'imagen':''
        },
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000,
            'imagen':''
        },
        {
            'marca':'Huang Queon',
            'modelo':'future200',
            'tipo':'electrica',
            'precio': 1500000,
            'imagen':''
        }
    ]
    return render(request, 'bicis.html', {'bicicleta_electrica': bicicleta_electrica})

def bici_bmx(request):
    bicicleta_bmx=[
        {
            'marca':'cult',
            'modelo':'Arcade candy ',
            'tipo':'bmx',
            'precio': 550000,
            'imagen':''
        },
        {
            'marca':'Subrosa',
            'modelo':'Sunday forecaster ',
            'tipo':'bmx',
            'precio': 995000,
            'imagen':''
        },
        {
            'marca':'vans',
            'modelo':'Box rail',
            'tipo':'bmx',
            'precio': 400000,
            'imagen':''
        }
    ]
    return render(request, 'bicis.html',{'bicicleta_bmx':bicicleta_bmx})