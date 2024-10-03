class Failure(Exception):
    pass

class NIL:
    pass

def occurs(variable, expression):
    """ Check if variable occurs in expression. """
    if isinstance(expression, str):  # Assuming constants are represented as strings
        return variable == expression
    elif isinstance(expression, list):  # If expression is a list (like a predicate)
        return any(occurs(variable, arg) for arg in expression)
    return False

def apply_substitution(substitution, expression):
    """ Apply substitution to an expression. """
    if isinstance(expression, str):  # If it's a constant
        return substitution.get(expression, expression)
    elif isinstance(expression, list):  # If it's a list (like a predicate)
        return [apply_substitution(substitution, arg) for arg in expression]
    return expression

def unify(S1, S2):
    """ Unify two expressions S1 and S2. """
    
    # Step 1: Handle variables and constants
    if isinstance(S1, str) or isinstance(S2, str):
        if S1 == S2:
            return NIL  # a)
        elif isinstance(S1, str):  # S1 is a variable
            if occurs(S1, S2):
                raise Failure  # b.i
            return {S1: S2}  # b.ii
        elif isinstance(S2, str):  # S2 is a variable
            if occurs(S2, S1):
                raise Failure  # c.i
            return {S2: S1}  # c.ii
        else:
            raise Failure  # d)
    
    # Step 2: Check predicate symbols
    if S1[0] != S2[0]:
        raise Failure  # Step 2

    # Step 3: Check number of arguments
    if len(S1) != len(S2):
        raise Failure  # Step 3

    # Step 4: Initialize substitution set
    substitution = {}

    # Step 5: Iterate over arguments
    for i in range(1, len(S1)):  # Start from 1 to skip the predicate symbol
        sub = unify(S1[i], S2[i])  # a)
        if sub is None:
            raise Failure  # b)
        if sub is not NIL:
            # Apply the substitution to the remainder
            S1 = apply_substitution(sub, S1)
            S2 = apply_substitution(sub, S2)
            substitution.update(sub)  # Append to SUBST

    return substitution  # Step 6

# Example usage
try:
    result = unify(['parent', 'X', 'Y'], ['parent', 'alice', 'Y'])
    print(result)
except Failure:
    print("FAILURE")
