# Create your views here.
from distutils.command.config import config

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def step1(request):
    return render(request, 'infoTemp.html')


def step2(request):
    return render(request, 'directT.html')


def step3(request):
    return render(request, 'reportT.html')


def step4(request):
    return render(request, 'indexTempOk.html')


def step5(request):
    return render(request, 'infoP.html')


def step6(request):
    return render(request, 'directP.html')


def step7(request):
    return render(request, 'reportP.html')


def step8(request):
    return render(request, 'indexPOK.html')


def step9(request):
    return render(request, 'infoWE.html')


def step10(request):
    return render(request, 'directWE.html')


def step11(request):
    return render(request, 'reportWE.html')


def step12(request):
    return render(request, 'indexWEOk.html')


def step13(request):
    return render(request, 'medicationCheck.html')


def step14(request):
    return render(request, 'direct.html')


def step15(request):
    return render(request, 'medicationAllOk.html')


def step16(request):
    return render(request, 'medSub2.html')


def step17(request):
    return render(request, 'medSub4.html')


def step18(request):
    return render(request, 'finalMed.html')


def step19(request):
    return render(request, 'reportMed.html')


def step20(request):
    return render(request, 'generalReport.html')


def step21(request):
    return render(request, 'success.html')


def step22(request):
    return render(request, 'patientInfo.html')


def reports(request):
    form = request.GET["myText"]

    context = {
        'form': form,
    }
    return render(request, 'reports.html', context)


def reportTextP(request):
    form = request.GET["myText"]

    context = {
        'form': form,
    }
    return render(request, 'reportTextP.html', context)


def reportTextWE(request):
    form = request.GET["myText"]

    context = {
        'form': form,
    }
    return render(request, 'reportTextWE.html', context)
