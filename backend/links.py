from django.http import JsonResponse

from backend.models_genearateor.main import layer_models

def main(request):
    models = layer_models(N=1, NX=15, NY=300, layerCount=4, scatterPeriod=1, sole = [[35, 89], [75, 114], [95, 129], [1000, 1000]], withoutShift=True)

    print(models.models)

    data = models.models

    for i in range(len(data)):
        data[i] = data[i].tolist()

    print(type(data[0]).__module__)

    # dataNew = data.tolist()

    # print(type(dataNew))

    response_data = {}
    response_data['result'] = data
    response_data['message'] = '1231312312321'
    return JsonResponse(response_data)