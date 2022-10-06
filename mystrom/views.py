from django.shortcuts import render, get_object_or_404

from mystrom_rest.models import MystromDevice
from shelly3em_rest.models import Shelly3EMDevice
from .forms import MystromDeviceForm

def index(request):
    form = MystromDeviceForm()

    return render(request, 'index.html', {
        'devices' : MystromDevice.objects.all(),
        'form': form
    })

def results(request):
    return render(request, 'results.html', {
        'devices' : MystromDevice.objects.all(),
        'shelly_devices' : Shelly3EMDevice.objects.all()
    })

def mystrom_results(request, id):
    device = get_object_or_404(MystromDevice, id=id)
    return render(request, 'mystrom_result.html', {
        'device' : device,
    })

def shelly_results(request, id):
    device = get_object_or_404(Shelly3EMDevice, id=id)
    return render(request, 'shelly_result.html', {
        'device' : device,
    })

def devices(request):
    if request.method == "POST":
        form = MystromDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'device_table_entries.html', {
                'devices' : MystromDevice.objects.all(),
            })
        else:
            return render(request, 'device_form_rows.html', {
                'form' : form,
            })
    elif request.method == "DELETE":
        MystromDevice.objects.all().delete()
        return render(request, 'device_table_entries.html', {
            'devices' : []
        })
    else:
        form = MystromDeviceForm()
    return render(request, 'device_form.html', {
        'form': form
    })

def device_info(request, id):
    device = get_object_or_404(MystromDevice, id=id)
    if request.method == "POST":
        form = MystromDeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return render(request, 'device_table_entries.html', {
                'devices' : MystromDevice.objects.all(),
            })
        else:
             return render(request, 'device_form_rows.html', {
                'form' : form,
            })
    elif request.method == "DELETE":
        MystromDevice.objects.filter(id=device.id).delete()
        return render(request, 'device_table_entries.html', {
            'devices' : MystromDevice.objects.all(),
        })
    else:
        form = MystromDeviceForm(instance=device)
    return render(request, 'device_form.html', {
        'form': form,
        'device': device,
    })