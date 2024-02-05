def fibo_terms(n_terms):
    fibo_terms_list = []
    x1 = 1
    x2 = 1
    while n_terms > 0:
        fibo_terms_list.append(x1)
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        n_terms -= 1
    return fibo_terms_list
def addition_terms(numeric_serie):
    addition = 0
    for term in numeric_serie:
        addition += term
    return addition

def prints_and_get_addition(n_terms):
    print("First" , n_terms , "terms of fibonacci series:")
    fibonacci_terms = fibo_terms(n_terms)
    for terms in fibonacci_terms:
        print(terms, end=",")
    print("\nTheir sum is" , addition_terms(fibonacci_terms))


# -- The main program starts here
print("---------------------------------")
prints_and_get_addition(5)
print("---------------------------------")
prints_and_get_addition(10)
