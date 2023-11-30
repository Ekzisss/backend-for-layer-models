from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.models_genearateor.main import layer_models

import json

@csrf_exempt 
def main(request):
    result = []
    print(request.method)
    if request.method == "GET":
        models = layer_models(N=1, NX=15, NY=150, layerCount=4, scatterPeriod=1, sole = [[50, 74], [90, 99], [110, 114], [1000, 1000]], shiftForce=[15,30], side=0, shiftType=0)
        result = models.save_to_param(skipLast = True, step=1)

        # models.show(limit=2)

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

        print(data)

        models = layer_models(**data)

        # models = layer_models(N=1, NX=100, NY=100, smoothness=False, layerCount=5, scatterPeriod=1, shiftForce=30, side=0, shiftType=0)

        # models = layer_models(N=1, NX=15, NY=150, layerCount=4, scatterPeriod=1, sole = [[50, 74], [90, 99], [110, 114], [1000, 1000]], shiftForce=[15,30], side=0, shiftType=0)
        models.show(limit=1)
        result = models.save_to_param(skipLast=skiplast, step=1)

    elif request.method == "OPTIONS":
        print(request.body)
        result = 'lllllll'

    response_data = {}
    response_data['result'] = result

    response = JsonResponse(response_data)

    Host = 'https://layer-models.vercel.app/'
    # Host = 'http://localhost:3000'

    response["Access-Control-Allow-Origin"] = '*'
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response