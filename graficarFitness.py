import plotly.graph_objects as go

# Función para leer resultados de un archivo
def read_results(file_path):
    interacciones = []
    fitness = []
    
    with open(file_path, 'r') as f:
        next(f)  # Saltar la primera línea (encabezados)
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                gen = float(parts[0])  # Convertir a float
                score = float(parts[1])  # Convertir a float
                interacciones.append(gen)
                fitness.append(score)
                
    return interacciones, fitness

# Leer múltiples archivos de resultados
file_paths = ['resultados_bacteria1.txt', 'resultados_bacteria2.txt']
all_interacciones = []
all_fitness = []

for file_path in file_paths:
    interacciones, fitness = read_results(file_path)
    all_interacciones.append(interacciones)
    all_fitness.append(fitness)

# Crear la figura de Plotly
fig = go.Figure()

# Colores y estilos para las diferentes ejecuciones
colors = ['blue', 'green', 'orange', 'red', 'purple']
line_styles = ['solid', 'dash', 'dot', 'longdash', 'dashdot']

for i, (interacciones, fitness) in enumerate(zip(all_interacciones, all_fitness)):
    fig.add_trace(go.Scatter(
        x=interacciones,
        y=fitness,
        mode='lines+markers',
        name=f'Ejecución {i + 1}',
        line=dict(color=colors[i % len(colors)], dash=line_styles[i % len(line_styles)]),
        marker=dict(size=6),
        text=[f'{score:.0f}' for score in fitness],
        textposition='top center'
    ))

# Configurar el diseño del gráfico
fig.update_layout(
    title='Progreso del Fitness a lo Largo de las Generaciones',
    xaxis_title='Generación',
    yaxis_title='Fitness',
    xaxis=dict(tickmode='linear'),
    yaxis=dict(range=[min(min(f) for f in all_fitness) - 100, max(max(f) for f in all_fitness) + 100]),
    legend=dict(x=0.01, y=0.99),
    template='plotly_white',
    margin=dict(l=40, r=40, t=40, b=40),
    hovermode='closest'
)

# Mostrar el gráfico
fig.show()
