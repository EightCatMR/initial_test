import re

def is_valid(string):
    valid= '[АВЕКМНОРСТУХ]'
    res = re.match(
        f'^{valid}\d{{3}}(?<!000){valid}{{2}}(([1-9]\d{{2}})|\d[1-9])$',
        string)
    return bool(res)


plates_set = ["А123АА11", "А222АА123", "А12АА123", "А123СС1234",
              "АА123А12", "А000АВ43", "Ц542ПД43", "З5421РО062",
              "Е043ВО59", "НО43ЗИ23", "54А542АГ54", "А539МР777"]

for plate in plates_set:
    if is_valid(plate):
        print(plate)
