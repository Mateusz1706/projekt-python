def nowafunkcja(a, b):
    if a == "" or b == "":
        raise ValueError("Puste dane wejściowe niedozwolone")
    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        raise ValueError("Argumenty muszą być liczbami lub tekstem reprezentującym liczbę")
    return a_int + b_int

