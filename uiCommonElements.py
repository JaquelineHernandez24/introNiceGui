from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic', on_click=lambda: ui.notify('Hiciste clic'))
with ui.row():
    ui.checkbox('Controlar', on_change=show)
    ui.switch('Cambiar', on_change=show)
ui.radio(['Galletas', 'Chetos', 'Flan'], value='Galletas', on_change=show).props('inline')
with ui.row():
    ui.input('Texto', on_change=show)
    ui.select(['Uno', 'Dos'], value='Uno', on_change=show)
ui.link('Y mucho mas...', '/documentation').classes('mt-8')

ui.run()