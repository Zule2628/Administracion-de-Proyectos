from bacteria import bacteria as Bacteria
from chemiotaxis import chemiotaxis
import numpy as np
import pandas as pd

# Configuración inicial
path = "C:/Users/sauce/Documents/secuenciasBFOA/multifasta.fasta"
numeroDeBacterias = 5
numRandomBacteria = 1
iteraciones = 30

# Inicialización
poblacion = [Bacteria(path) for _ in range(numeroDeBacterias)]
chemio = chemiotaxis()
veryBest = Bacteria(path)
globalNFE = 0

# Para almacenar resultados
resultados = []

# Parámetros de quimiotaxis
dAttr = 0.1
wAttr = 0.2
hRep = dAttr
wRep = 10

def clonaBest(veryBest, best):
    veryBest.matrix.seqs = np.array(best.matrix.seqs)
    veryBest.blosumScore = best.blosumScore
    veryBest.fitness = best.fitness
    veryBest.interaction = best.interaction

# Guardar la bacteria original en otra variable
original_bacteria = Bacteria(path)

# Ejecución del algoritmo
for _ in range(iteraciones):
    for bacterium in poblacion:
        # Movimiento adaptativo
        step_size = chemio.adaptive_chemotaxis(bacterium, fitness_threshold=10, small_step=1, large_step=5)
        bacterium.tumboNado(step_size)
        bacterium.autoEvalua()
        
        # Actualiza la posición solo si es nueva
        chemio.update_position(bacterium, bacterium.matrix.seqs)
    
    # Aplicar quimiotaxis y evaluar interacción
    chemio.doChemioTaxis(poblacion, dAttr, wAttr, hRep, wRep)
    globalNFE += chemio.parcialNFE
    best = max(poblacion, key=lambda x: x.fitness)
    
    if best.fitness > veryBest.fitness:
        clonaBest(veryBest, best)

    # Guardar resultados
    resultados.append({
        "Iteración": len(resultados) + 1,
        "Interacción": veryBest.interaction,
        "Fitness": veryBest.fitness,
        "NFE": globalNFE,
        "Población": len(poblacion)
    })

    # Eliminar y clonar bacterias
    chemio.eliminarClonar(path, poblacion)
    chemio.insertRamdomBacterias(path, numRandomBacteria, poblacion)

# Crear DataFrame y guardar resultados
df_resultados = pd.DataFrame(resultados)
print(df_resultados)
df_resultados.to_csv("resultados_bfoa.csv", index=False)

# Mostrar la mejor bacteria
veryBest.showGenome()
