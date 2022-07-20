from django.shortcuts import render, HttpResponse
from . import forms

def Secant(request):
    tol = ''
    val1 = ''
    val2 = ''
    stp = ''
    a = []
    b = []
    last = ''
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            tol = eval(request.POST.get('tol'))
            val2 = eval(request.POST.get('val2'))
            val1 = eval(request.POST.get('val1'))
            stp = eval(request.POST.get('stp'))

                        
            # Defining Function
            def f(x):
                return x**3 - 5*x - 9

            # Implementing Secant Method

            def secant(x0,x1,e,N):
                print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
                step = 1
                condition = True
                while condition:
                    if f(x0) == f(x1):
                        print('Divide by zero error!')
                        break
                    
                    x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
                    # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
                    x0 = x1
                    x1 = x2
                    step = step + 1
                    a.append('%.3f' % x2 )
                    b.append('%.3f' % f(x2) )
                    if step > N:
                        print('Not Convergent!')
                        break
                    
                    condition = abs(f(x2)) > e

            # Input Section
            x0= val1
            x1 = val2
            e = tol
            N = stp

            # Converting x0 and e to float
            x0 = float(x0)
            x1 = float(x1)
            e = float(e)

            # Converting N to integer
            N = int(N)

            # Starting Secant Method
            secant(x0,x1,e,N)
            k = b.copy()
            last = k.pop()

    return render(request,'Secant.html',{'form':form, 'a':a ,'b':b, 'last':last  })    
 