def dpll(clauses, assignment):
    """
    DPLL algorithm to solve SAT problem.
    
    :param clauses: List of clauses, each clause is a list of literals.
    :param assignment: Current variable assignment.
    :return: A satisfying assignment or None if unsatisfiable.
    """
    # If all clauses are satisfied
    if not clauses:
        return assignment

    # If any clause is empty, the formula is unsatisfiable
    if any([clause == [] for clause in clauses]):
        return None

    # Unit propagation
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    if unit_clauses:
        literal = unit_clauses[0][0]
        return dpll(propagate(clauses, literal), assignment + [literal])

    # Choose a variable to assign
    literal = clauses[0][0]
    result = dpll(propagate(clauses, literal), assignment + [literal])
    if result is not None:
        return result
    return dpll(propagate(clauses, -literal), assignment + [-literal])

def propagate(clauses, literal):
    """
    Propagate a literal and simplify the clauses.
    
    :param clauses: List of clauses.
    :param literal: Literal to propagate.
    :return: Simplified list of clauses.
    """
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue
        new_clause = [lit for lit in clause if lit != -literal]
        new_clauses.append(new_clause)
    return new_clauses

def encrypt_circuit(inputs, key):
    return [inp ^ k for inp, k in zip(inputs, key)]

def sat_attack(encrypted_output, num_inputs, num_keys):
    input_vars = list(range(1, num_inputs + 1))
    key_vars = list(range(num_inputs + 1, num_inputs + num_keys + 1))
    output_vars = list(range(num_inputs + num_keys + 1, num_inputs + num_keys + num_inputs + 1))

    clauses = []

    # Add XOR constraints for each bit
    for i in range(num_inputs):
        clauses.append([-input_vars[i], -key_vars[i], -output_vars[i]])
        clauses.append([-input_vars[i], key_vars[i], output_vars[i]])
        clauses.append([input_vars[i], -key_vars[i], output_vars[i]])
        clauses.append([input_vars[i], key_vars[i], -output_vars[i]])

    # Add known encrypted output as assumptions
    assumptions = [output_vars[i] if encrypted_output[i] == 1 else -output_vars[i] for i in range(num_inputs)]
    
    # Solve with assumptions
    solution = dpll(clauses, assumptions)

    if solution is not None:
        recovered_key = []
        for var in key_vars:
            if var in solution:
                recovered_key.append(1)
            elif -var in solution:
                recovered_key.append(0)
            else:
                recovered_key.append(None)  # In case of an incomplete solution (shouldn't happen here)
        return recovered_key

    return None

# Example usage
num_inputs = 4
num_keys = 4

# Original circuit inputs
original_inputs = [1, 0, 1, 0]

# Key used for encryption
key = [1, 1, 0, 0]

# Encrypt the circuit
encrypted_output = encrypt_circuit(original_inputs, key)

print(f"Encrypted Output: {encrypted_output}")

# Perform SAT attack to recover the key
recovered_key = sat_attack(encrypted_output, num_inputs, num_keys)

print(f"Original Key: {key}")
print(f"Recovered Key: {recovered_key}")
