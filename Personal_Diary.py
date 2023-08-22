# Personal Diary Management System

diary_entries = []

def add_entry():
    title = input("Enter entry title: ")
    content = input("Enter entry content: ")
    entry = {"title": title, "content": content}
    diary_entries.append(entry)
    print("Entry added successfully!")

def view_entries():
    if not diary_entries:
        print("No entries available.")
    else:
        for idx, entry in enumerate(diary_entries, start=1):
            print(f"{idx}. {entry['title']} - {entry['content']}")

def search_entries():
    keyword = input("Enter keyword to search: ")
    search_results = [entry for entry in diary_entries if keyword in entry['content']]
    if search_results:
        print("Search results:")
        for idx, entry in enumerate(search_results, start=1):
            print(f"{idx}. {entry['title']} - {entry['content']}")
    else:
        print("No matching entries found.")

def main_menu():
    while True:
        print("\nPersonal Diary Management System")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entries")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            search_entries()
        elif choice == '4':
            print("Exiting the diary management system.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()
