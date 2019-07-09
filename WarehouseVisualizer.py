import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as PathEffects


template_str_repr = '''Warehouse object with {amount_fields} fields.
layout:
{layout_str}'''

layout_str_4_2x2 = '''0 1
2 3'''

layout_str_6_3x2 = '''0 1 2
3 4 5'''

class WarehouseVisualizer:
    def __init__(self, amount_fields: int):
        self.amount_fields = amount_fields
        self.fields = [0] * self.amount_fields
        if not (amount_fields == 4 or amount_fields == 6):
            raise Exception(f'amount_fields={amount_fields}: only 4 or 6 supported.')
        if amount_fields == 4:
            self.field_coord_map = {
                0: (0,0),
                1: (1,0),
                2: (0,1),
                3: (1,1)
            }
        if amount_fields == 6:
            self.field_coord_map = {
                0: (0,0),
                1: (1,0),
                2: (2,0),
                3: (0,1),
                4: (1,1),
                5: (2,1),
            }
        self.prev_action = 'init'
        self.item_rgb_map = {
            0: np.array([0, 0, 0]),       # black
            1: np.array([255, 255, 255]), # white
            2: np.array([0, 0, 255]),     # blue
            3: np.array([255, 0, 0]),     # red
        }

    def __str__(self):
        if self.amount_fields == 4:
            layout_str = layout_str_4_2x2
        if self.amount_fields == 6:
            layout_str = layout_str_6_3x2
        return template_str_repr.format(amount_fields=self.amount_fields, layout_str=layout_str)

    def __repr__(self):
        return self.__str__()

    def display(self):
        if self.amount_fields == 4:
            plt.title(f'2x2: after "{self.prev_action}"')
            # layout: 0 1
            #         2 3
            layout = np.array(
                        [[self.item_rgb_map[field] for field in self.fields[:2]],
                        [self.item_rgb_map[field] for field in self.fields[2:]]])

        if self.amount_fields == 6:
            plt.title(f'3x2: after "{self.prev_action}"')
            # layout: 0 1 2
            #         3 4 5
            layout = np.array(
                        [[self.item_rgb_map[field] for field in self.fields[:3]],
                        [self.item_rgb_map[field] for field in self.fields[3:]]])
        # add labels
        for num in range(self.amount_fields):
            p = plt.annotate(str(num), xy=self.field_coord_map[num], fontsize=30, ha='center', va='center')
            p.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])
        plt.axis('off')
        plt.imshow(layout)