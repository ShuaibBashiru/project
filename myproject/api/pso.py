import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from django.http import JsonResponse, HttpResponse
from pyswarms.utils.search import RandomSearch
from scipy.optimize import minimize_scalar
import codecs, json
from pyswarms.utils.plotters.formatters import Mesher, Designer
from math import pi
import math, datetime
import numpy as np
from numpy import sin, cos, linspace
from sympy import symbols, solve, Eq
from django.db import connection
from .models import CreateReport

def f1_1(x, v_1, counter):
    if counter > 0:
        x=round(v_1, 4)
    else:
        x=x[:, 0]
    return x**2 + 3 * x + 2

def f1_2(x, v_2, counter):
    if counter > 0:
        x=round(v_2, 4)
    else:
        x = x[:, 0]
    return (x**2) + (3 * x) + 2

def func1(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = 0
            newx2 = 0

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options, bounds=bounds)
        gcost, gpos = generalPso.optimize(f1_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f1_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list=gpos_list[0].strip('[')
        cpos_list=cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter+=1
        fitness_value_pso = gpos_list ** 2 + 3 * gpos_list + 2
        fitness_value_cog = cpos_list ** 2 + 3 * cpos_list + 2
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f1'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other ='x^2 + (3 * x) + 2 = 0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f1' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f1' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)



def f2_1(x, v_1, counter):
    if counter > 0:
        x=round(v_1, 4)
    else:
        x = x[:, 0]
    return x**2 + 7 * x + 4

def f2_2(x, v_2, counter):
    if counter > 0:
        x=round(v_2, 4)
    else:
        x = x[:, 0]
    return x**2 + 7 * x + 4

def func2(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = 0
            newx2 = 0

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options, bounds=bounds)
        gcost, gpos = generalPso.optimize(f2_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f2_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list=gpos_list[0].strip('[')
        cpos_list=cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter+=1
        fitness_value_pso = gpos_list ** 2 + 7 * gpos_list + 4
        fitness_value_cog = cpos_list ** 2 + 7 * cpos_list + 4
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f2'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other ='x^2 + 7 * x + 4 = 0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f2' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f2' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)


def f3_1(x, v_1, counter):
    if counter > 0:
        x=round(v_1, 4)
    else:
        x = x[:, 0]
    return -(x**2) + 5 * x + 20

def f3_2(x, v_2, counter):
    if counter > 0:
        x=round(v_2, 4)
    else:
        x = x[:, 0]
    return -(x**2) + 5 * x + 20

def func3(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options, bounds=bounds)
        gcost, gpos = generalPso.optimize(f3_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f3_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list=gpos_list[0].strip('[')
        cpos_list=cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter+=1
        fitness_value_pso = -(gpos_list ** 2) + 5 * gpos_list + 20
        fitness_value_cog = -(cpos_list ** 2) + 5 * cpos_list + 20
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f3'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other ='-x^2 + 5 * x + 20 = 0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f3' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f3' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)

def f4_1(x, v_1, counter):
    if counter > 0:
        x=round(v_1, 4)
    else:
        x = x[:, 0]
    return x*3 + 4 * x**2 + 3 * x + 6

def f4_2(x, v_2, counter):
    if counter > 0:
        x=round(v_2, 4)
    else:
        x = x[:, 0]
    return x*3 + 4 * x**2 + 3 * x + 6

def func4(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options, bounds=bounds)
        gcost, gpos = generalPso.optimize(f4_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f4_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list=gpos_list[0].strip('[')
        cpos_list=cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter+=1

        fitness_value_pso = gpos_list*3 + 4 * gpos_list**2 + 3 * gpos_list + 6
        fitness_value_cog = cpos_list*3 + 4 * cpos_list**2 + 3 * cpos_list + 6
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f4'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other ='x*3 + 4 * x*2 + 3 * x +6 = 0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f4' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f4' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)



def f5_1(x, v_1, counter):
    if counter > 0:
        x=round(v_1, 4)
    else:
        x = x[:, 0]
    return x+1 * x-1 + 0.152

def f5_2(x, v_2, counter):
    if counter > 0:
        x=round(v_2, 4)
    else:
        x = x[:, 0]
    return x+1 * x-1 + 0.152

def func5(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options, bounds=bounds)
        gcost, gpos = generalPso.optimize(f5_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f5_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list=gpos_list[0].strip('[')
        cpos_list=cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter+=1

        fitness_value_pso = gpos_list + 1 * gpos_list - 1 + 0.152
        fitness_value_cog = cpos_list + 1 * cpos_list - 1 + 0.152
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f5'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other ='x+1 * x-1 + 0.152 = 0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f5' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f5' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)


def f6_1(x, v_1, counter):
    if counter > 0:
        x = round(v_1, 4)
    else:
        x = x[:, 0]
    return x*3 + x*2

def f6_2(x, v_2, counter):
    if counter > 0:
        x = round(v_2, 4)
    else:
        x = x[:, 0]
    return x*3 + x*2

def func6(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options,
                                            bounds=bounds)
        gcost, gpos = generalPso.optimize(f5_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f5_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list = gpos_list[0].strip('[')
        cpos_list = cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter += 1

        fitness_value_pso = gpos_list * 3 + gpos_list * 2
        fitness_value_cog = cpos_list * 3 + cpos_list * 2
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f6'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other = 'x*3 + x*2=0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f6' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f6' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)


def f7_1(x, v_1, counter):
    if counter > 0:
        x = round(v_1, 4)
    else:
        x = x[:, 0]
    return x*3 - 0.165 * x*2 + 0.0003993 * x


def f7_2(x, v_2, counter):
    if counter > 0:
        x = round(v_2, 4)
    else:
        x = x[:, 0]
    return  x*3 - 0.165 * x*2 + 0.0003993 * x


def func7(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options,
                                            bounds=bounds)
        gcost, gpos = generalPso.optimize(f5_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f5_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list = gpos_list[0].strip('[')
        cpos_list = cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter += 1

        fitness_value_pso = gpos_list * 3 - 0.165 * gpos_list * 2 + 0.0003993 * gpos_list
        fitness_value_cog = cpos_list * 3 - 0.165 * cpos_list * 2 + 0.0003993 * cpos_list
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f7'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other = 'x*3 - 0.165 * x*2 + 0.0003993 * x=0'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f7' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f7' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)


def f8_1(x, v_1, counter):
    if counter > 0:
        x = round(v_1, 4)
    else:
        x = x[:, 0]
    return x**2 * sin(20 * x) + cos(x - 3.14)**3 + 1


def f8_2(x, v_2, counter):
    if counter > 0:
        x = round(v_2, 4)
    else:
        x = x[:, 0]
    return  x**2 * sin(20 * x) + cos(x - 3.14)**3 + 1

# SELECT other, generalPso, cognitivePso, generalfitness, cognitivefitness, particle, iteration runtime from report_tbl where functions = 'f3' limit 10

def func8(request):
    no_iterations = int(request.GET['iteration'])
    no_particles = int(request.GET['particle'])
    runtime = int(request.GET['runtime'])
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    cog_options = {'c1': 0.5, 'c2': 0.0, 'w': 0.9}
    counter = 0
    for counter in range(runtime):
        if counter == 0:
            newx1 = int(0)
            newx2 = int(0)

        kwargsPso = {'v_1': newx1, 'counter': counter}
        kwargsCog = {'v_2': newx2, 'counter': counter}
        generalPso = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=options, bounds=bounds)
        cognitive = ps.single.GlobalBestPSO(n_particles=no_particles, dimensions=2, options=cog_options,
                                            bounds=bounds)
        gcost, gpos = generalPso.optimize(f5_1, iters=no_iterations, **kwargsPso)
        ccost, cpos = cognitive.optimize(f5_2, iters=no_iterations, **kwargsCog)
        lists = gpos.tolist()
        lists2 = cpos.tolist()
        gpos_list = json.dumps(lists)
        gpos_list = gpos_list.split(',')
        cpos_list = json.dumps(lists2)
        cpos_list = cpos_list.split(',')
        gpos_list = gpos_list[0].strip('[')
        cpos_list = cpos_list[0].strip('[')
        gpos_list = float(gpos_list)
        cpos_list = float(cpos_list)
        counter += 1

        fitness_value_pso = gpos_list**2 * sin(20 * gpos_list)+cos(gpos_list-3.14) ** 3 + 1
        fitness_value_cog = cpos_list**2 * sin(20 * cpos_list)+cos(cpos_list-3.14) ** 3 + 1
        newx1 = gpos_list
        newx2 = cpos_list
        save_record = CreateReport()
        save_record.functions = 'f8'
        save_record.generalPso = round(gpos_list, 4)
        save_record.cognitivePso = round(cpos_list, 4)
        save_record.generalfitness = round(fitness_value_pso, 4)
        save_record.cognitivefitness = round(fitness_value_cog, 4)
        save_record.particle = no_particles
        save_record.iteration = no_iterations
        save_record.runtime = counter
        save_record.other = 'x^2 * sin(20x)+cos(x−π)^3+1'
        save_record.date_created = datetime.datetime.now()
        save_record.save()

    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM report_tbl WHERE functions = 'f8' AND "
                                 "(select min(generalPso) from report_tbl WHERE functions = 'f8' )  LIMIT 1 ")
        row = cursor.fetchone()
        if counter > 0:
            feedback = {
                'status': 'success',
                'msg': "Optimization is successful",
                'function': row[9],
                'iteration': row[7],
                'particle': row[6],
                'classname': 'alert alert-primary p-1 text-center',
                'gpos': row[2],
                'cpos': row[3],
                'fgpos': row[4],
                'fcpos': row[5],
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data found yet',
                'row': 'No record',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)


# select other as functions, generalPso, generalfitness, cognitivePso, cognitivefitness, runtime FROM report_tbl ORDER by functions, runtime