import random

class SATGenerator:
    def __init__(self, num_variables):
        self.num_variables = num_variables
    
    def generate_problem(self, num_clauses):
        variables = list(range(1, self.num_variables + 1))
        clauses = []
        
        for _ in range(num_clauses):
            # Seleziona casualmente tre variabili
            clause = random.sample(variables, 3)
            
            # Assegna casualmente il segno positivo o negativo a ciascuna variabile
            clause = [var if random.choice([True, False]) else -var for var in clause]
            
            clauses.append(clause)
        
        return clauses
