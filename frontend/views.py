from django.shortcuts import render

# Create your views here.

def dashboard(request):
    markers = [
        {
            'location': [12.985531, 7.617144],
            'popup': 'Katsina'
        },
        {
            'location': [13.0330, 8.3235],
            'popup': 'Daura'
        },
        {
            'location': [11.717, 7.033],
            'popup': 'Faskari'
        },
        {
            'location': [11.518482, 7.312930],
            'popup': 'Funtua'
        },
        {
            'location': [11.6738, 7.6897],
            'popup': 'Kafur'
        },
        {
            'location': [12.4539, 7.4972],
            'popup': 'Dutsin-ma'
        },
        {
            'location': [12.675, 7.7275],
            'popup': 'Charanchi'
        },
        {
            'location': [12.462174, 7.828637],
            'popup': 'Kankia'
        },
    ]
    
    return render(request, 'dashboard.html', {'markers': markers})