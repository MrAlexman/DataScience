def person(documents, doc_number):
    """
    Returns name of document owner
    :param documents: list[dict]
    :param number: str
    :return: str
    """
    for document in documents:
        if document["number"] == doc_number:
            return document['name']
    return False


def shelf(directories, doc_number):
    """
    Returns number of shield
    :param directories: dict{str:list}
    :param doc_number: str
    :return: str
    """
    for key in directories.keys():
        for i in directories[key]:
            if i == doc_number:
                return key
    return False


def info(documents, directories):
    """
    Returns complemented box of documents. Depends on function 'shelf'
    :param documents: list[dict]
    :param directories: dict{str:list}
    :return list[dict]
    """
    for i in documents:
        i['shelf'] = shelf(directories, i['number'])
        print(f"| №: {i['number']:15}| type: {i['type']:15}|"
              f" owner: {i['name']:20}| shelf: {i['shelf']}")
    for key in directories.keys():
        if len(directories[key]) == 0:
            print(f"| №: {'':15}| type: {'':15}|"
                  f" owner: {'':20}| shelf: {key}")


def ads(directories, shelf_number):
    """
    Adds new dictionary element, returns result in boolean
    :param directories: dict{str:list}
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
    :param directories: dict{str:list}
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


def ad(documents, directories, doc_number, doc_type, doc_person, doc_shelf):
    """
    Adds new document, returns result
    :param documents: list[dict]
    :param directories: dict{str:list}
    :param doc_number: str
    :param doc_type: str
    :param doc_person: str
    :param doc_shelf: str
    :return: int
    """
    if finder(documents, doc_number):
        print("This document have already added. Current data:")
        info(documents, directories)
        return False
    if doc_shelf not in list(directories.keys()):
        print("There`s no this number shelf. Please, create it wits command 'ads'. "
              "Current data:")
        info(documents, directories)
        return False
    documents.append({"type": f"{doc_type}", "number": f"{doc_number}", "name": f"{doc_person}"})
    directories[doc_shelf].append(doc_number)
    print("New document added successfully. Current data:")
    info(documents, directories)
    return True


def d(documents, directories, doc_number):
    """
    Deletes document. Returns result.
    :param documents: list[dict]
    :param directories: dict{str:list}
    :param doc_number: boolean
    :return:
    """

    for index1, item1 in enumerate(documents):
        if item1['number'] == doc_number:
            del documents[index1]
            for key in directories.keys():
                for index2, item2 in enumerate(directories[key]):
                    if item2 == doc_number:
                        del directories[key][index2]
                        break
            print("Document was deleted. Current data:")
            info(documents, directories)
            return True
    print("There`s no such document. Current data:")
    info(documents, directories)
    return False


def finder(documents, doc_number):
    """
    Checks if the current document exist
    :param documents: list[dict]
    :param doc_number: str
    :return: boolean
    """
    for i in documents:
        if i['number'] == doc_number:
            return True
    return False


def mover(directories, doc_shelf, doc_number):
    """
    Moves document from one self to another
    :param directories:
    :param doc_shelf:
    :param doc_number:
    :return:
    """
    if finder(documents, doc_number):
        if doc_shelf in directories.keys():
            for keys in directories.keys():
                for index, value in enumerate(directories[keys]):
                    if value == doc_number:
                        del directories[keys][index]
            directories[doc_shelf].append(doc_number)
            print("Document moved. Current data:")
            info(documents, directories)
            return True
        else:
            print("There`s no this number shelf. Please, create it wits command 'ads'. "
                  "Current data:")
            info(documents, directories)
            return False

    else:
        print("There`s no such document. Current data:")
        info(documents, directories)
        return False


if __name__ == "__main__":
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
    first = 0
    while True:
        if first != 0:
            input()
        first = 1
        print('\n' * 100)
        print("You`re in workspace:\n"
              "Please Enter one of command (Num/Name):\n"
              "0) 'q'   - Quit execution.\n"
              "1) 'p'   - Name of document owner.\n"
              "2) 's'   - Number of document shelf.\n"
              "3) 'l'   - Full data.\n"
              "4) 'ads' - Adds new shelf.\n"
              "5) 'ds'  - Deletes chosen shelf, if it`s empty.\n"
              "6) 'ad'  - Adds new document.\n"
              "7) 'd'   - Deletes chosen document.\n"
              "8) 'm'   - Moves document from its shelf to another")

        commandline = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                       'q', 'p', 's', 'l', 'ads', 'ds', 'ad', 'd', 'm']
        while True:
            command = input()
            if command in commandline:
                break
            else:
                print("Incorrect input.")
        if command in ['p', '1', 's', '2', 'd', '7', 'm', '8']:
            doc_number = input("Enter document number: ")
            if command in ['s', '2']:
                result = shelf(directories, doc_number)
                if result:
                    print(f"The document is stored on the shelf: {result}")
                    continue
            elif command in ['d', '7']:
                d(documents, directories, doc_number)
                continue
            elif command in ['m', '8']:
                doc_shelf = input("Enter new sheld: ")
                mover(directories, doc_shelf, doc_number)
                continue
            else:
                result = person(documents, doc_number)
                if result:
                    print(f"Document owner: {result}")
                    continue
            print("Document wasn`t found in base")

        elif command in ['l', '3']:
            info(documents, directories)
            continue

        elif command in ['ads', '4', 'ds', '5', 'm', '8']:
            shelf_number = input("Enter shelf number: ")
            if command in ['ds', '5']:
                ds(directories, shelf_number)
                continue
            else:
                ads(directories, shelf_number)
                continue
        elif command in ['ad', '6']:
            doc_number = input("Enter document number: ")
            doc_type = input("Enter document type: ")
            doc_person = input("Enter document owner: ")
            doc_shelf = input("Enter document sheld: ")

            result = ad(documents, directories, doc_number, doc_type, doc_person, doc_shelf)
            print(1)
            continue
        elif command in ['0', 'q']:
            print("Good luck!")
            break
