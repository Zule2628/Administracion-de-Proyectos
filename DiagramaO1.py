from graphviz import Digraph

# Crear un nuevo gráfico dirigido
dot = Digraph(comment='Diagrama de Flujo del BFOA Mejorado', format='png')

# Establecer estilos básicos
dot.attr('node', shape='rectangle', style='filled', color='lightblue', fontname="Arial", fontsize="12")

# Añadir nodos
dot.node('A', 'Inicio', shape='ellipse')
dot.node('B', 'Inicializar Población', shape='box')
dot.node('C', 'Movimiento Aleatorio', shape='box')
dot.node('D', 'Evaluar Fitness', shape='box')
dot.node('E', 'Quimiotaxis', shape='box')
dot.node('F', '¿Mejora en Fitness?', shape='diamond')
dot.node('G', 'Actualizar Posición y Reproducir', shape='box')
dot.node('H', 'Eliminar Bacteria', shape='box')
dot.node('I', 'Actualizar Global NFE', shape='box')
dot.node('J', '¿Número de Iteraciones Alcanzado?', shape='diamond')
dot.node('K', 'Imprimir Resultados', shape='box')
dot.node('L', 'Fin', shape='ellipse')

# Añadir aristas (conexiones)
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G', label='Sí')
dot.edge('F', 'H', label='No')
dot.edge('G', 'I')
dot.edge('H', 'I')
dot.edge('I', 'J')
dot.edge('J', 'C', label='No')
dot.edge('J', 'K', label='Sí')
dot.edge('K', 'L')

# Guardar y renderizar el archivo
dot.render('diagrama_bfoa', view=True)
