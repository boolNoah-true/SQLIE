import Import
import Export

def main():
    print("Choose a process:")
    print("1. Import Database")
    print("2. Export Database")
    print("3. Exit")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        dbname = input("Enter the name of the database to import: ")
        Import.run_mysql_import(dbname)
    elif choice == '2':
        dbname = input("Enter the name of the database to export: ")
        Export.run_mysqldump(dbname)
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

