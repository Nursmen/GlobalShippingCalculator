from django.shortcuts import render
from .models import History, TypeOfOrder

optoins = [
    110,120,130,140,150,160,170,180,190,200,250,300,350,400,600,800,1000
]
USDRUB = 103.74
CNYRUB = 14.41

coefs = {
    'base':[
        [0.20, 0.05],
        [0.18, 0.03],
        [0.18, 0.03],
        [0.18, 0.03],
        [0.18, 0.03],
        [0.18, 0.03],
        [0.17, 0.03],
        [0.17, 0.02],
        [0.17, 0.02],
        [0.17, 0.02],
        [0.17, 0.02],
        [0.15, 0.02],
        [0.13, 0.02],
        [0.11, 0.02],
        [0.10, 0.02],
        [0.06, 0.02],
        [0.05, 0.02],
        [0.04, 0.02],
        [0.02, 0.02],
    ], 
    'strong': [
        [0.25, 0.15],
        [0.23, 0.10],
        [0.23, 0.10],
        [0.23, 0.10],
        [0.23, 0.10],
        [0.23, 0.10],
        [0.21, 0.10],
        [0.21, 0.08],
        [0.21, 0.08],
        [0.21, 0.08],
        [0.21, 0.08],
        [0.19, 0.08],
        [0.16, 0.06],
        [0.14, 0.04],
        [0.13, 0.03],
        [0.08, 0.02],
        [0.06, 0.02],
        [0.05, 0.02],
        [0.03, 0.02],
    ]
}

def index(request):
    if request.method == 'POST':

        CostOfType = TypeOfOrder.objects.get(title=request.POST['type']).cost
        BoxType = request.POST['BoxType']
        Length = float(request.POST['length'])
        Width = float(request.POST['width'])
        Height = float(request.POST['height'])
        Number_of_pieces_per_box = float(request.POST['pieces in box'])
        Pieces = float(request.POST['pieces'])
        Weight = float(request.POST['weight'])
        Cost = float(request.POST['cost'])

        Volume = Length * Width * Height / 10**6
        Density = Weight / Volume

        coeficents = coefs[BoxType]

        if Density < 100:
            CostOfOrder = CostOfType*100 + adding
            coeficents = coeficents[0]
        else:
            adding = 420
            starting = 3.8
            for i, option in enumerate(optoins):
                if Density < option:
                    CostOfOrder = round(CostOfType + starting, 2)
                    coeficents = coeficents[i+1]
                    break
                starting -= 0.1
            if not CostOfOrder:
                CostOfOrder = round(CostOfType + starting, 2)
                coeficents = coeficents[-1]

        Logistics_naked = Volume if Density < 100 else Weight
        Logistics_naked = Logistics_naked*CostOfOrder*USDRUB/Number_of_pieces_per_box

        Logistics = Logistics_naked*(1+coeficents[1])
        Insurance = 0.015 * Cost  * CNYRUB
        Packing = 6 if BoxType == 'base' else 8
        Packing = Packing * USDRUB/Number_of_pieces_per_box * Volume/coeficents[0]
        Unloading_at_MSK = 250 if BoxType == 'base' else 300
        Unloading_at_MSK = Unloading_at_MSK/Number_of_pieces_per_box * Volume/coeficents[0]
        Total_cost_per_unit = Logistics + Insurance + Packing + Unloading_at_MSK

        Total_logistics_cost = Logistics * Pieces 
        Total_Insurance = Insurance * Pieces
        Total_Packaging = Packing * Pieces
        Total_Unloading = Unloading_at_MSK * Pieces
        Total_cost_of_the_lot = Total_cost_per_unit * Pieces

        history = History(Length=int(round(Length)), 
                          Width=int(round(Width)), 
                          Height=int(round(Height)), 
                          Number_of_pieces_per_box=int(round(Number_of_pieces_per_box)),
                          Total_quantity=int(round(Pieces)), 
                          Box_weight=int(round(Weight)), 
                          Cost_per_piece=int(round(Cost)), 
                          Density=int(round(Density)),
                          Logistics_naked=int(round(Logistics_naked)), 
                          Logistics=int(round(Logistics)), 
                          Insurance=int(round(Insurance)), 
                          Packaging=int(round(Packing)),
                          Unloading_at_MSK=int(round(Unloading_at_MSK)), 
                          Total_cost_per_unit=int(round(Total_cost_per_unit)),
                          Total_logistics_cost=int(round(Total_logistics_cost)), 
                          Total_Insurance=int(round(Total_Insurance)),
                          Total_Packaging=int(round(Total_Packaging)), 
                          Total_Unloading=int(round(Total_Unloading)),
                          Total_cost_of_the_lot=int(round(Total_cost_of_the_lot))
                          )
        history.save()
        

        return render(request, 'calcitself/results.html', {'history': history})
    
    types = TypeOfOrder.objects.all()

    return render(request, 'calcitself/index.html', {'types': types})