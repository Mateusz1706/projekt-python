def przywitanie():
    """Łączy oba powitalne komunikaty."""
    print("Witaj w moim projekcie!")
    print("Cześć, użytkowniku!")

def project_info():
    print("To jest prosty projekt demonstracyjny do nauki Gita.")

def show_menu():
    print("\n--- MENU ---")
    print("1. Powitanie")
    print("2. Informacje o projekcie")
    print("3. Zakończ")

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
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
