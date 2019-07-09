from WarehouseVisualizer import WarehouseVisualizer

action_map = {
    0: ('store', 'white'),
    1: ('store', 'blue'),
    2: ('store', 'red'),
    3: ('restore', 'white'),
    4: ('restore', 'blue'),
    5: ('restore', 'red')
}

action_map_inverse = {v: k for k, v in action_map.items()}

class GreedyAlgo:
    def __init__(self, amount_fields=4):
        self.wh = WarehouseVisualizer(amount_fields)
        if amount_fields == 4:
            #               field: 0  1  2  3
            self.distance_array = [1, 2, 2, 3]
        if amount_fields == 6:
            #               field: 0  1  2  3  4  5
            self.distance_array = [1, 2, 3, 2, 3, 4]
        self.distance_walked = 0
        self.str_to_ind_map = {'white': 1, 'blue': 2, 'red': 3}

    def run_next_action(self, action):
        if action[0] == 'store':
            index = -1
            for ind, field in enumerate(self.wh.fields):
                if field == 0:
                    index = ind
                    break
            self.wh.fields[index] = self.str_to_ind_map[action[1]]
            self.distance_walked += self.distance_array[index]
        if action[0] == 'restore':
            index = -1
            color_to_find = self.str_to_ind_map[action[1]]
            for ind, field in enumerate(self.wh.fields):
                if field == color_to_find:
                    index = ind
                    break
            self.wh.fields[index] = 0
            self.distance_walked += self.distance_array[index]
        self.wh.prev_action = f'{action[0]} {action[1]}'

    def display(self):
        self.wh.display()