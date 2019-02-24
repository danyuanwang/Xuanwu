import constants
#rgb
bg_color = constants.Color.WHITE

#caption for window
screen_name = "xuanwu game"

#x, y
screen_size = (1200, 830)

#width, height , x_margin, y_margin
cell_size = {
    'cell_width': 50,
    'cell_height': 50,
    'x_margin': 1,
    'y_margin': 1,
}#(50, 50, 1, 1)

#i, j , i_margin, j_margin
board_dimension = {
                'width': 20,
                'height': 16,
                'x_offset': 10,
                'y_offset': 10,
                }
#mine numbers,
#stone
stone_mine_number = {
                'low_value': 2,
                'high_value': 5,
                }
#iron
iron_mine_number = {
                'low_value': 2,
                'high_value': 4,
                }
#diamond
diamond_mine_number = {
                'low_value': 1,
                'high_value': 2,
                }
