from django.shortcuts import render, redirect, get_object_or_404
from .models import Test
from .form import TestForm



def tests(request):
    tests = Test.objects.all()
    return render(request, 'tests.html', context={'tests': tests})


def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test_detail.html', context={'test': test})


def test_create(request):
    testform = TestForm()
    if request.method == 'POST':
        testform = TestForm(request.POST)
        if testform.is_valid():
            testform.save()
            return redirect('tests')
    return render(request, 'test_create.html', context={'form': testform})


def test_update(request, pk):
    test = get_object_or_404(Test, pk=pk)

    testform = TestForm(instance=test)
    if request.method == 'POST':
        testform = TestForm(request.POST, instance=test)
        if testform.is_valid():
            testform.save()
            return redirect('tests') 
    return render(request, 'test_update.html', context={'form': testform})



def test_delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('tests')