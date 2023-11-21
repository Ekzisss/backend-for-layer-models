from django.http import JsonResponse

from backend.models_genearateor.main import layer_models

def main(request):
    models = layer_models(N=10, NX=15, NY=300, layerCount=4, scatterPeriod=1, sole = [[50, 74], [90, 99], [110, 114], [1000, 1000]], shiftForce=[5,15], side=0, shiftType=0)

    result = models.save_to_param(skipLast = True, step=1)

    print(request)

    if request.method == "GET":
        models = layer_models(N=10, NX=15, NY=300, layerCount=4, scatterPeriod=1, sole = [[50, 74], [90, 99], [110, 114], [1000, 1000]], shiftForce=[15,30], side=0, shiftType=0)
        result = models.save_to_param(skipLast = True, step=1)

        response_data = {}
        response_data['result'] = result

    elif request.method == "POST":
        print(request.body)
        pass


    # print(models.models)
    # data = models.models
    # for i in range(len(data)):
    #     data[i] = data[i].tolist()
    # print(type(data[0]).__module__)
    # dataNew = data.tolist()
    # print(type(dataNew))

    response_data = {}
    response_data['result'] = result

    response = JsonResponse(response_data)

    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response