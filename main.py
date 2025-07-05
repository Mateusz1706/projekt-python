def przywitanie():
    print("Witaj w moim projekcie! Wersja A nagłówka.")
    print("Witaj w moim projekcie! Wersja B nagłówka")
    print("Cześć, użytkowniku!")

def project_info():
    print("To jest prosty projekt demonstracyjny do nauki systemu kontroli wersji Git.") # poprawiona treść

def author_info():
    print("Autor: Mateusz Stasiak")

def show_menu():
    print("\n--- MENU ---")
    print("1. Powitanie")
    print("2. Informacje o projekcie")
    print("3. Zakończ")
    print("4. Informacje o autorze")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            przywitanie()
        elif choice == "2":
            project_info()
        elif choice == "3":
            print("Do zobaczenia!")
            break
	elif choice == "4":
    	    author_info()
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
