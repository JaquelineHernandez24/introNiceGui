from nicegui import ui

ui.icon('thumb_up', color='Red').classes('text-7xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Jaqueline ').style('color: #eaacf2; font-weight: bold; font-family: Georgia, serif;  font-size: 24px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()