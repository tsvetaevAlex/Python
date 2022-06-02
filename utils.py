
class Utils:
    def __init__(self):

        self.datalist = []


def get_equipmentlist_fromfile(filename):
        #random.choice(city_list)
    with open(filename) as file:
        for datarow in file:
            datarow = datarow.rstrip()
            self.datalist.append(datarow)
    return self.datalist
