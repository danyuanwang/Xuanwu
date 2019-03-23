class Rectangle:
    def __init__(self, upper_left_x, upper_left_y, width, length):
        self. upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.length = length
        self.width = width

    def get_center_point(self):
        center_x = self.upper_left_x + (self.width / 2)
        center_y = self.upper_left_y + (self.length / 2)
        return center_x, center_y
