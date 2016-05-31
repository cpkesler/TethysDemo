from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)

def info(request):
    """
    Controller for the info page.
    """
    context = {}

    return render(request, 'my_first_app/info.html', context)

def map(request):
    """
    Controller for the map page.
    """
    context = {}

    return render(request, 'my_first_app/map.html', context)

def gizmo(request):
    """
    Controller for the gizmo page.
    """
    text_input1 = TextInput(display_text='Runoff Coeficient, c',
                       name='runoff',
                       initial='0.8',)

    text_input2 = TextInput(display_text='Rainfall Intentsiy, i [in/hr]',
                       name='intensity',
                       initial='6',)

    text_input3 = TextInput(display_text='Drainage Area, A [acre]',
                       name='area',
                       initial='160',)

    single_button = Button(display_text='Calculate Flow',
                           name='flow',
                           attributes='form=flow-form',
                           submit=True)

    context = {'text_input1': text_input1, 'text_input2': text_input2, 'text_input3': text_input3, 'single_button': single_button}

    return render(request, 'my_first_app/gizmo.html', context)

def flow(request):
    """
    Controller for the flow page.
    """
    if request.POST:
        runoff = float(request.POST['runoff'])
        intensity = float(request.POST['intensity'])
        area = float(request.POST['area'])

    flow = runoff * intensity * area

    context = {'runoff': runoff, 'intensity': intensity, 'area': area, 'flow': flow}

    return render(request, 'my_first_app/flow.html', context)