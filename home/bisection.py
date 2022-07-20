from django.shortcuts import render, HttpResponse
from . import forms

def BiSection(request):
    tol = ''
    val1 = ''
    val2 = ''
    a = []
    b = []
    s =[]
    last = ''
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            tol = eval(request.POST.get('tol'))
            val2 = eval(request.POST.get('val2'))
            val1 = eval(request.POST.get('val1'))

            
            # Defining Function
            def f(x):
                return x**3-5*x-9

            # Implementing Bisection Method
            def bisection(x0,x1,e):
                step = 1
                # print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
                condition = True
                while condition:
                    x2 = (x0 + x1)/2
                    # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
                    s.append(step)
                    a.append('%.3f' % x2 )
                    b.append('%.3f' % f(x2) )
                    
                    if f(x0) * f(x2) < 0:
                        x1 = x2
                    else:
                        x0 = x2

                    step = step + 1
                    condition = abs(f(x2)) > e


            # Input Section
            x0= val1
            x1 = val2
            e = tol

            # Converting input to float
            x0 = float(x0)
            x1 = float(x1)
            e = float(e)


            # Checking Correctness of initial guess values and bisecting
            if f(x0) * f(x1) > 0.0:
                print('Given guess values do not bracket the root.')
                print('Try Again with different guess values.')
            else:
                bisection(x0,x1,e)

            k = b.copy()
            last = k.pop()

    return render(request,'BiSection.html',{'form':form, 'a':a ,'b':b,'s': s, 'last':last }) 
