from WarehouseVisualizer import WarehouseVisualizer
from typing import List, Tuple

action_map = {
    0: ('store', 'white'),
    1: ('store', 'blue'),
    2: ('store', 'red'),
    3: ('restore', 'white'),
    4: ('restore', 'blue'),
    5: ('restore', 'red')
}

action_map_inverse = {v: k for k, v in action_map.items()}


class AIAlgo:
    def __init__(self, policy, statelist, amount_fields=4):
        self.wh = WarehouseVisualizer(amount_fields)
        if amount_fields == 4:
            #              field: 0  1  2  3
            self.distance_array = [1, 2, 2, 3]
        if amount_fields == 6:
            #              field: 0  1  2  3  4  5
            self.distance_array = [1, 2, 3, 2, 3, 4]
        self.distance_walked = 0
        self.str_to_ind_map = {'white': 1, 'blue': 2, 'red': 3}
        self.policy = policy
        self.statelist = statelist

    def get_state_index(self, fields: List[int], action: int) -> int:
        #print(f'tuple(fields + [action]):\t{tuple(fields + [action])}')
        for index, state in enumerate(self.statelist):
            if tuple(fields + [action]) == state:
                return index
        raise Exception(f'fields not found as state (\'{fields + [action]}\')')

    def run_next_action(self, action: Tuple[str]):
        #print(f'curr state:\t{self.wh.fields}')
        #print(f'run action:\t{action}')
        stateindex = self.get_state_index(self.wh.fields, action_map_inverse[action])
        position = self.policy[stateindex]
        #print(f'policy says:\t{position}')
        if action[0] == 'store':
            if self.wh.fields[position] != 0:
                raise Exception(f'can\'t store at position {position}, not empty (state: {self.wh.fields})')
            self.wh.fields[position] = self.str_to_ind_map[action[1]]
            self.distance_walked += self.distance_array[position]
        if action[0] == 'restore':
            if self.wh.fields[position] != self.str_to_ind_map[action[1]]:
                raise Exception(f'can\'t restore at position {position}, color not present')
            self.wh.fields[position] = 0
            self.distance_walked += self.distance_array[position]
        self.wh.prev_action = f'{action[0]} {action[1]}'
        #print(f'post state:\t{self.wh.fields}')

    def display(self):
        self.wh.display()