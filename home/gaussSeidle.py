from django.shortcuts import render, HttpResponse

def GaussSeidle(request):
    x1 = ''
    y1 =''
    z1= ''
    tol = ''
    a=[]
    if request.method == 'POST':
            tol = eval(request.POST.get('tol'))
            
            f1 = lambda x, y, z: (17 - y + 2 * z) / 20
            f2 = lambda x, y, z: (-18 - 3 * x + z) / 20
            f3 = lambda x, y, z: (25 - 2 * x + 3 * y) / 20

# Initial setup
            x0 = 0
            y0 = 0
            z0 = 0
            count = 1

# Reading tolerable error
            e = tol

# Implementation of Gauss Seidel Iteration
            
            condition = True

            while condition:
                    x1 = f1(x0, y0, z0)
                    y1 = f2(x1, y0, z0)
                    z1 = f3(x1, y1, z0)
                 
                    e1 = abs(x0 - x1)
                    e2 = abs(y0 - y1)
                    e3 = abs(z0 - z1)
                    count += 1
                    x0 = x1
                    y0 = y1
                    z0 = z1

                    condition = e1 > e and e2 > e and e3 > e
                    a.append('%.3f' % x1 )
                    a.append('%.3f' % y1)
                    a.append('%.3f' % z1)
                    
    return render(request, 'GaussSeidle.html', {'a': a})