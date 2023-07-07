import pygame_menu
menu = pygame_menu.Menu(...)

def change_background_color(selected_value, color, **kwargs):
    value_tuple, index = selected_value
    print('Change widget color to', value_tuple[0])  # selected_value ('Color', surface, color)
    if color == (-1, -1, -1):  # Generate a random color
        color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    widget: 'pygame_menu.widgets.Selector' = kwargs.get('widget')
    widget.update_font({'selected_color': color})
    widget.get_selection_effect().color = color

items = [('Default', (255, 255, 255)),
         ('Black', (0, 0, 0)),
         ('Blue', (0, 0, 255)),
         ('Random', (-1, -1, -1))]
selector = menu.add.selector(
    title='Current color:\t',
    items=items,
    onreturn=change_background_color,  # User press "Return" button
    onchange=change_background_color  # User changes value with left/right keys
)
selector.add_self_to_kwargs()  # Callbacks will receive widget as parameter
selector2 = menu.add.selector(
    title='New color:',
    items=items,
    style=pygame_menu.widgets.SELECTOR_STYLE_FANCY
)

