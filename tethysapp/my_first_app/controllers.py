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

    from tethys_sdk.gizmos import RangeSlider

    slider1 = RangeSlider(display_text='Runoff Coefficient, c',
                          name='runoff',
                          min=0,
                          max=1,
                          initial=0.4,
                          step=0.01)
    slider2 = RangeSlider(display_text='Rainfall Intensity, i [in/hr]',
                          name='intensity',
                          min=0,
                          max=20,
                          initial=4,
                          step=0.5,)
    slider3 = RangeSlider(display_text='Drainage Area, A [acre]',
                          name='area',
                          min=0,
                          max=1000,
                          initial=350,
                          step=1,)
    single_button = Button(display_text='Calculate Flow',
                           name='flow',
                           attributes='form=flow-form',
                           submit=True)

    text_input1 = TextInput(display_text='Runoff Coeficient, c',
                       name='runoff1',
                       initial='0.8',)

    text_input2 = TextInput(display_text='Rainfall Intentsiy, i [in/hr]',
                       name='intensity1',
                       initial='6',)

    text_input3 = TextInput(display_text='Drainage Area, A [acre]',
                       name='area1',
                       initial='160',)

    single_button1 = Button(display_text='Calculate Flow',
                           name='flow1',
                           attributes='form=flow1-form',
                           submit=True)

    context = {'slider1': slider1, 'slider2': slider2, 'slider3': slider3, 'single_button': single_button, 'text_input1': text_input1, 'text_input2': text_input2, 'text_input3': text_input3, 'single_button1': single_button1}

    return render(request, 'my_first_app/gizmo.html', context)

def flow(request):
    """
    Controller for the flow page.
    """
    print request.POST
    if request.POST:
        runoff = float(request.POST['runoff'])
        intensity = float(request.POST['intensity'])
        area = float(request.POST['area'])


    flow = runoff * intensity * area
    print flow

    context = {'runoff': runoff, 'intensity': intensity, 'area': area, 'flow': flow}

    return render(request, 'my_first_app/flow.html', context)

def flow1(request):
    """
    Controller for the flow1 page.
    """
    print request.POST
    if request.POST:
        runoff1 = float(request.POST['runoff1'])
        intensity1 = float(request.POST['intensity1'])
        area1 = float(request.POST['area1'])

    flow1 = runoff1 * intensity1 * area1
    print flow1

    context = {'runoff1': runoff1, 'intensity1': intensity1, 'area1': area1, 'flow1': flow1}

    return render(request, 'my_first_app/flow1.html', context)