# Rozwiązywanie konfliktu merge

Podczas łączenia gałęzi `feature/header-design-b` z `main` wystąpił konflikt w pliku `main.py` w funkcji `przywitanie`.

Konflikt polegał na dwóch różnych wersjach nagłówka. 

Rozwiązaliśmy konflikt ręcznie poprzez połączenie obu wersji komunikatu w funkcji:

```python
def przywitanie():
    print("Witaj w moim projekcie! Wersja A nagłówka.")
    print("Witaj w moim projekcie! Wersja B nagłówka")
    print("Cześć, użytkowniku!")

