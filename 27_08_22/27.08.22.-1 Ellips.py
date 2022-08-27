class Ellipse:

    def __init__(self, x1 = None, y1 = None, x2 = None, y2 = None):
        if x1 !=None and y1 != None and x2 !=None and y2 !=None:
            self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            self.p = 1
        else:
            self.p = 0

    def __bool__(self):
        return True if self.p else False


    def get_coords(self):
        if not self.p:
            raise AttributeError('нет координат для извлечения')
        a = (self.x1, self.y1, self.x2, self.y2)
        print(a[-1])
        return a


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for elip in lst_geom:
    if bool(elip):
        elip.get_coords()
