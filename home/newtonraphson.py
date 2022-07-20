from django.shortcuts import render, HttpResponse
from . import forms

def NewtonRaphson(request):
    tol = ''
    val1 = ''
    val2 = ''
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

                            # Defining Function
            def f(x):
                return x**3 - 5*x - 9

            # Defining derivative of function
            def g(x):
                return 3*x**2 - 5

            # Implementing Newton Raphson Method

            def newtonRaphson(x0,e,N):
                # print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
                step = 1
                flag = 1
                condition = True
                while condition:
                    if g(x0) == 0.0:
                        print('Divide by zero error!')
                        break
                    
                    x1 = x0 - f(x0)/g(x0)
                    # print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))

                    

                    x0 = x1
                    step = step + 1

                    a.append('%.3f' % x1 )
                    b.append('%.3f' % f(x1) )
                    
                    if step > N:
                        flag = 0
                        break
                    
                    condition = abs(f(x1)) > e
                
                if flag==1:
                    print('\nRequired root is: %0.8f' % x1)
                else:
                    print('\nNot Convergent.')


            # Input Section
            x0= val1
            e = tol
            N = val2

            # Converting x0 and e to float
            x0 = float(x0)
            e = float(e)

            # Converting N to integer
            N = int(N)

            # Starting Newton Raphson Method
            newtonRaphson(x0,e,N)

            k = b.copy()
            last = k.pop()

    return render(request,'NewtonRaphson.html',{'form':form, 'a':a ,'b':b, 'last':last }) 