from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=5).bind_value(demo, 'number')
    ui.toggle({1: 'POO', 2: 'Ing.Software', 3: 'IO', 4: 'Admin', 5: 'Estructura de Datos'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()