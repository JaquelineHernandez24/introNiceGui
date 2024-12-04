from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=1000) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)
    model = scene.stl('/stl/utochka.stl').move(x=-0.5).scale(1.0)
    model.material(color='#edea91')  # Cambia el color al modelo

ui.run()
