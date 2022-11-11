def person(documents, search_number):
    """
    Returns name of document owner
    :param documents: list[dict]
    :param number: str
    :return: str
    """
    for document in documents:
        if document["number"] == search_number:
            return document['name']
    return False


def shelf(directories, search_number):
    """
    Returns number of shield
    :param directories: dict
    :param search_number: str
    :return: str
    """
    for key in directories.keys():
        for i in directories[key]:
            if i == search_number:
                return key
    return False


def info(documents, directories):
    """
    Returns complemented box of documents. Depends on function 'shelf'
    :param documents: list[dict]
    :param directories: dict
    :return list[dict]
    """
    for i in documents:
        i['shelf'] = shelf(directories, i['number'])
    return documents


def add(directories, shelf_number):
    """
    Adds new dictionary element, returns result in boolean
    :param directories: dict
    :param shelf_number: str
    :return: boolean
    """
    if shelf_number not in list(directories.keys()):
        directories[shelf_number] = []
        print(f"A shelf has been added. The current list of shelves: {', '.join(directories.keys())}")
        return True
    else:
        print(f"A shelf with this number already exists. The current list of shelves: {', '.join(directories.keys())}")
        return False


def ds(directories, shelf_number):
    """
    Deletes chosen shelf. Returns result in boolean
    :param directories: dict
    :param shelf_number: str
    :return: boolean
    """
    if shelf_number in directories.keys():
        if len(directories[shelf_number]) == 0:
            directories.pop(shelf_number)
            print(f"shelf was deleted. Current list of shelfs: {', '.join(directories.keys())}")
            return True
        else:
            print(f"There`s documents on shelf. Please delete them at first. "
                  f"Current list of shelfs:  {', '.join(directories.keys())}")
            return False
    else:
        print(f"shelf wasn`t found in base. Current list of shelfs: {', '.join(directories.keys())}")
        return None


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    "1": ["2207 876234", "11-2"],
    "2": ["10006"],
    "3": []
}



if __name__ == "__main__":
    while True:
        print('\n' * 100)
        print("You`re in workspace:\n"
              "Please Enter one of command (Num/Name):\n"
              "0) 'q'   - Quit execution.\n"
              "1) 'p'   - Name of document owner.\n"
              "2) 's'   - Number of document shelf.\n"
              "3) 'l'   - Full data.\n"
              "4) 'ads' - Adds new shelf.\n"
              "5) 'ds'  - Deletes chosen shelf, if it`s empty.")

        commandline = ['0', '1', '2', '3', '4', '5', 'q', 'p', 's', 'l', 'ads', 'ds']
        command = None
        while True:
            command = input()
            if command in commandline:
                break
            else:
                print("Incorrect input.")
        print('\n' * 100)
        if command in ['p', '1', 's', '2']:
            search_number = input("Enter document number: ")

            if command in ['s', '2']:
                result = shelf(directories, search_number)
                if result:
                    print(f"The document is stored on the shelf: {result}")
                else:
                    print("Document wasn`t found in base")
            else:
                result = person(documents, search_number)
                if result:
                    print(f"Document owner: {result}")
                else:
                    print("Document wasn`t found in base")

        elif command in ['l', '3']:
            result = info(documents, directories)
            for i in result:
                print(f"| №: {i['number']:15}| type: {i['type']:15}|"
                      f" owner: {i['name']:20}| shelf: {i['shelf']}")

        elif command in ['ads', '4', 'ds', '5']:
            shelf_number = input("Enter shelf number: ")
            if command in ['ds', '5']:
                ds(directories, shelf_number)
            else:
                add(directories, shelf_number)
        elif command in ['0', 'q']:
            print("Good luck!")
            break
        input()
