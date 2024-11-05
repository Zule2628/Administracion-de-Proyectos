from graphviz import Digraph

# Crear un objeto Digraph para el diagrama de flujo mejorado
dot = Digraph(comment='BFOA Mejorado', format='png')

# Establecer estilos básicos
dot.attr('node', shape='rectangle', style='filled', color='lightblue', fontname="Arial", fontsize="12")

# Nodos principales del flujo mejorado
dot.node('A', 'Inicio: Inicializar población y parámetros')
dot.node('B', 'Movimiento Aleatorio Adaptativo\n(Ajuste de paso según quimiotaxis adaptativa)', color='lightgreen')  # Nodo mejorado en verde
dot.node('C', 'Evaluación de Fitness')
dot.node('D', 'Actualización de Memoria', color='lightgreen')  # Nodo mejorado en verde
dot.node('E', '¿Mejora en Fitness?')
dot.node('F', 'Actualizar Posición y Reproducir')
dot.node('G', 'Eliminar y Dispersar Bacterias')
dot.node('H', 'Actualizar Global NFE')
dot.node('I', '¿Número de Iteraciones Alcanzado?')
dot.node('J', 'Imprimir Resultados')
dot.node('K', 'Fin')

# Conectar los nodos en el orden de ejecución
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F', label="Sí",)
dot.edge('E', 'G', label="No")
dot.edge('F', 'H')
dot.edge('G', 'H')
dot.edge('H', 'I')
dot.edge('I', 'B', label="No")  # Bucle hacia el movimiento aleatorio si no se cumple el criterio de parada
dot.edge('I', 'J', label="Sí")
dot.edge('J', 'K')

# Guardar y visualizar el diagrama
dot.render('/mnt/data/diagrama_flujo_bfoa_mejorado', view=True)
