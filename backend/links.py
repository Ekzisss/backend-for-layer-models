from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os

from backend.models_genearateor.main import layer_models

import json

load_dotenv()

@csrf_exempt 
def main(request):
    result = []
    print(os.environ['FRONT_IP'])
    if request.method == "POST":
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
                data['scatterAmount'].pop(0)
                for i in range(len(data['scatterAmount'])):
                    data['scatterAmount'][i] = -data['scatterAmount'][i]
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

    Host = os.environ['FRONT_IP']

    response["Access-Control-Allow-Origin"] = Host
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response