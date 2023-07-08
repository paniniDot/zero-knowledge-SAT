from pysat.solvers import Solver
from pysat.formula import CNF
import sat_factory as sf

cnf_formula = CNF(from_clauses=sf.SATGenerator(num_variables=3).generate_problem(num_clauses=3)) # 3-CNF formula 

# create a SAT solver for this formula:
with Solver(bootstrap_with=cnf_formula) as solver:
    # 1.1 call the solver for this formula:
    print('formula', cnf_formula.clauses, 'is', f'{"s" if solver.solve() else "uns"}atisfiable')

    # 1.2 the formula is satisfiable and so has a model:
    print('and the model is:', solver.get_model())

    # 2.1 apply the MiniSat-like assumption interface:
    print('formula is',
        f'{"s" if solver.solve(assumptions=[1, 2, -3]) else "uns"}atisfiable',
        'assuming x1 and x2 and not x3')

    # 2.2 the formula is unsatisfiable,
    # i.e. an unsatisfiable core can be extracted:
    print('and the unsatisfiable core is:', solver.get_core())