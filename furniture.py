class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具 %s 占地 %.2f" % (self.name, self.area)
        # return ({
        #     "name": self.name,
        #     "area": self.area
        # })


bed = Furniture("席梦思", 40)
chest = Furniture("衣柜", 30)
table = Furniture("桌子", 2)
print(bed)
print(chest)
print(table)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "类型 %s 面积 %.2f 可用面积 %.2f 家具有 %s" % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print("添加%s" % item.name)
        if item.area > self.free_area:
            print("%s 家具太大" % item.name)
            return
        else:
            self.free_area = self.area - item.area
            self.item_list.append(item.name)


house = House("公寓", 50)
house.add_item(bed)
house.add_item(chest)
print(house)