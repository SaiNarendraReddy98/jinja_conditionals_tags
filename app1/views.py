from django.shortcuts import render

# Create your views here.
def if_condition(request):
    d = {'a':100,}

    return render(request,'if_condition.html',d)

def if_else(request):
    d={'a':320,'b':54}

    return render(request,'if_else.html',d)

def if_elif(request):
    d={'a':130,'b':43,'c':120}

    return render(request,'if_elif.html',d)

def nested_if(request):
    d={'a':120,'b':150,'c':430,'d':210}

    return render(request,'nested_if.html',d)

