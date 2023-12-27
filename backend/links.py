from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

from backend.models_genearateor.main import layer_models

import json

@csrf_exempt 
def main(request):
    result = []
    print(request.method)
    if request.method == "GET":
        models = layer_models(N=1, NX=15, NY=150, layerCount=4, scatterPeriod=1, sole = [[50, 74], [90, 99], [110, 114], [1000, 1000]], shiftForce=[15,30], side=0, shiftType=0)
        result = models.save_to_param(skipLast = True, step=1)

        response_data = {}
        response_data['result'] = result

    elif request.method == "POST":
        data = json.loads(request.body)
        print(f'gentype - {data["generationType"]}')


        skiplast = False
        match data['generationType']:
            case 0:
                del data['scatterAmount']
                del data['sole']
            case 1:
                del data['scatterMaxValue']
                del data['scatterPeriod']
                del data['sole']
                data['smoothness'] = True
            case 2:
                del data['layerThickness']
                del data['scatterMaxValue']
                del data['scatterPeriod']
                del data['scatterAmount']
                skiplast = True
        del data['generationType']

        models = layer_models(**data)

        result = models.save_to_param(skipLast=skiplast, step=1)

    response_data = {}
    response_data['result'] = result

    response = JsonResponse(response_data)

    try:
        Host = os.environ['FRONT_IP']
    except:
        Host = 'http://localhost:3000'

    response["Access-Control-Allow-Origin"] = Host
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response