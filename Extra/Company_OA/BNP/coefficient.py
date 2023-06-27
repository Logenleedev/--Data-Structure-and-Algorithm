def Coefficients(arr):
    # Remove whitespace and ensure proper formatting
    arr = arr.replace(' ', '')
    arr = arr.replace('^', '**')
    
    # Separate the terms by "+" or "-"
    terms = []
    term = ""
    for i in range(len(arr)):
        if arr[i] == '+' or arr[i] == '-':
            terms.append(term)
            term = arr[i]
        else:
            term += arr[i]
    terms.append(term)  # Add the last term
  
    # Extract the coefficients from the terms
    coefficients = []
    for term in terms:
        # Remove "+" or "-" at the beginning
        if term != "":
            if term[0] == '+' or term[0] == '-':
                term = term[1:]
        
            # Split the term into coefficient and exponent
            if 'x' in term:
                # correspond to 3x**2 -> coefficient = 3
                coefficient, exponent = term.split('x')
            else:
                # correspond to 3 -> coefficient = 3
                coefficient = term
                exponent = '0'
            
            # Append the coefficient to the list
            coefficients.append(float(coefficient))
    
    # Return the coefficients as strings with 5 decimal places
    coefficient_strings = [format(coefficient, '.5f') for coefficient in coefficients]
    return coefficient_strings

polynomial = "-2x^3 + 5.5x^2 - 0.3x + 1"
coefficients = Coefficients(polynomial)
print(coefficients)