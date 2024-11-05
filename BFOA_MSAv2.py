from bacteria import bacteria as Bacteria  # Renombramos la clase
from chemiotaxis import chemiotaxis
import numpy as np
import pandas as pd

# Configuración inicial
path = "C:/Users/sauce/Documents/secuenciasBFOA/multifasta.fasta"
numeroDeBacterias = 5
numRandomBacteria = 1
iteraciones = 30
tumbo = 1  # número de gaps a insertar

# Inicialización
poblacion = [Bacteria(path) for _ in range(numeroDeBacterias)]
chemio = chemiotaxis()
veryBest = Bacteria(path)  # mejor bacteria
globalNFE = 0  # número de evaluaciones de la función objetivo

# Para almacenar resultados
resultados = []

# Parámetros para la quimiotaxis
dAttr = 0.1
wAttr = 0.2
hRep = dAttr
wRep = 10

def clonaBest(veryBest, best):
    veryBest.matrix.seqs = np.array(best.matrix.seqs)
    veryBest.blosumScore = best.blosumScore
    veryBest.fitness = best.fitness
    veryBest.interaction = best.interaction

def validaSecuencias(path, veryBest):
    tempBacteria = Bacteria(path)  # Usar el nuevo nombre
    tempBacteria.matrix.seqs = np.array(veryBest.matrix.seqs)
    for i in range(len(tempBacteria.matrix.seqs)):
        tempBacteria.matrix.seqs[i] = tempBacteria.matrix.seqs[i].replace("-", "")
    for i in range(len(tempBacteria.matrix.seqs)):
        if tempBacteria.matrix.seqs[i] != original_bacteria.matrix.seqs[i]:
            print("*****************Secuencias no coinciden********************")
            return

# Guardar la bacteria original en otra variable
original_bacteria = Bacteria(path)  # bacteria original sin gaps

# Ejecución del algoritmo
for _ in range(iteraciones):  # número de iteraciones
    for bacterium in poblacion:  # Cambié 'bacteria' por 'bacterium'
        bacterium.tumboNado(tumbo)
        bacterium.autoEvalua()
    
    chemio.doChemioTaxis(poblacion, dAttr, wAttr, hRep, wRep)
    globalNFE += chemio.parcialNFE
    best = max(poblacion, key=lambda x: x.fitness)
    
    if (veryBest is None) or (best.fitness > veryBest.fitness):
        clonaBest(veryBest, best)

    # Guardar resultados
    resultados.append({
        "Iteración": len(resultados) + 1,
        "Interacción": veryBest.interaction,
        "Fitness": veryBest.fitness,
        "NFE": globalNFE,
        "Población": len(poblacion)
    })

    chemio.eliminarClonar(path, poblacion)
    chemio.insertRamdomBacterias(path, numRandomBacteria, poblacion)

# Validación de secuencias
validaSecuencias(path, veryBest)

# Crear DataFrame y guardar resultados
df_resultados = pd.DataFrame(resultados)
print(df_resultados)
df_resultados.to_csv("resultados_bfoa.csv", index=False)

# Mostrar la mejor bacteria
veryBest.showGenome()
