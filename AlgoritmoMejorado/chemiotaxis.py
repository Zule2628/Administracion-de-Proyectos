import math
import random
import numpy as np  # Asegúrate de importar NumPy
from bacteria import bacteria

class chemiotaxis:
    def __init__(self):
        self.parcialNFE = 0  
        self.memory = set()  # Memoria de posiciones exploradas

    def adaptive_chemotaxis(self, bacteria, fitness_threshold, small_step, large_step):
        """ Ajusta el tamaño del paso basado en el fitness """
        step_size = small_step if bacteria.fitness > fitness_threshold else large_step
        return step_size

    def update_position(self, bacteria, new_position):
        """ Actualiza la posición de la bacteria si no ha sido explorada antes """
        # Convertir new_position a tupla para que sea hashable
        new_position_tuple = tuple(new_position.flatten())  # Asegúrate de que sea una tupla
        if new_position_tuple not in self.memory:
            self.memory.add(new_position_tuple)  # Añade como tupla
            bacteria.position = new_position

    def compute_cell_interaction(self, bacteria, poblacion, d, w):
        total = 0.0
        for other in poblacion:
            diff = (bacteria.blosumScore - other.blosumScore) ** 2.0
            total += d * math.exp(w * diff)
        return total

    def attract_repel(self, bacteria, poblacion, d_attr, w_attr, h_rep, w_rep):
        attract = self.compute_cell_interaction(bacteria, poblacion, -d_attr, -w_attr)
        repel = self.compute_cell_interaction(bacteria, poblacion, h_rep, -w_rep)
        return attract + repel   # Interaction

    def chemio(self, bacteria, poblacion, d_attr, w_attr, h_rep, w_rep):
        bacteria.interaction = self.attract_repel(bacteria, poblacion, d_attr, w_attr, h_rep, w_rep)
        bacteria.fitness = bacteria.blosumScore + bacteria.interaction

    def doChemioTaxis(self, poblacion, d_attr, w_attr, h_rep, w_rep):
        self.parcialNFE = 0
        for bacteria in poblacion:
            self.chemio(bacteria, poblacion, d_attr, w_attr, h_rep, w_rep)
            self.parcialNFE += bacteria.NFE
            bacteria.NFE = 0

    def eliminarClonar(self, path, poblacion):
        """ Elimina el 50% de las bacterias con menos fitness """
        poblacion.sort(key=lambda x: x.fitness)
        for i in range(int(len(poblacion) / 2)):
            del poblacion[0]
        
        clones = self.clonacion(path, poblacion)
        for clone in clones:
            poblacion.append(clone)

    def clonacion(self, path, poblacion):
        poblacionClones = []
        best = max(poblacion, key=lambda x: x.fitness)
        for bacteria in poblacion:
            newBacteria = bacteria.clonar(path)
            mutacion = int((best.fitness - bacteria.fitness) / 10)  # Mutación en función de la diferencia de fitness
            newBacteria.tumboNado(mutacion)
            newBacteria.autoEvalua()
            poblacionClones.append(newBacteria)
        return poblacionClones

    def randomBacteria(self, path):
        bact = bacteria(path)
        bact.tumboNado(random.randint(1, 10))
        return bact 
    
    def insertRamdomBacterias(self, path, num, poblacion):
        for _ in range(num):
            poblacion.append(self.randomBacteria(path))
            poblacion.sort(key=lambda x: x.fitness)
            del poblacion[0]
