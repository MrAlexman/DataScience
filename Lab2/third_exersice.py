""" Data Base with funcs """


def person(docs, doc_n):
    """
    Returns name of doc owner
    :param doc_n: str
    :param docs: list[dict]
    :return: str
    """
    for doc in docs:
        if doc["number"] == doc_n:
            return doc['name']
    return False


def shelf(dirs, doc_n):
    """
    Returns number of shield
    :param dirs: dict{str:list}
    :param doc_n: str
    :return: str
    """
    for key in dirs.keys():
        for i in dirs[key]:
            if i == doc_n:
                return key
    return False


def info(docs, dirs):
    """
    Returns complemented box of docs. Depends on function 'shelf'
    :param docs: list[dict]
    :param dirs: dict{str:list}
    :return None
    """
    for i in docs:
        i['shelf'] = shelf(dirs, i['number'])
        print(f"| №: {i['number']:15}| type: {i['type']:15}|"
              f" owner: {i['name']:20}| shelf: {i['shelf']}")
    for key in dirs.keys():
        if len(dirs[key]) == 0:
            print(f"| №: {'':15}| type: {'':15}|"
                  f" owner: {'':20}| shelf: {key}")
    if docs == [] and dirs == {}:
        print("Empty")


def ads(dirs, self_n):
    """
    Adds new dictionary element
    :param dirs: dict{str:list}
    :param self_n: str
    :return: None
    """
    if self_n not in list(dirs.keys()):
        dirs[self_n] = []
        print(f"A shelf has been added. The current list of shelves: "
              f"{', '.join(dirs.keys())}")
    else:
        print(f"A shelf with this number already exists. "
              f"The current list of shelves: {', '.join(dirs.keys())}")
        if not dirs:
            print('Empty')


def del_s(dirs, self_n):
    """
    Deletes chosen shelf
    :param dirs: dict{str:list}
    :param self_n: str
    :return: None
    """
    if self_n in dirs.keys():
        if len(dirs[self_n]) == 0:
            dirs.pop(self_n)
            print(f"shelf was deleted. Current list of shelfs: {', '.join(dirs.keys())}")
            if not dirs:
                print("Empty")
        else:
            print(f"There`s docs on shelf. Please delete them at first. "
                  f"Current list of shelfs:  {', '.join(dirs.keys())}")
    else:
        print(f"Shelf wasn`t found in base. Current list of shelfs: "
              f"{', '.join(dirs.keys())}")
        if not dirs:
            print("Empty")


def add_doc(docs, dirs, doc_pars):
    """
    Adds new doc
    :param doc_pars: list[str]
    :param docs: list[dict]
    :param dirs: dict{str:list}
    """
    if finder(docs, doc_pars[0]):
        print("This document have already added. Current data:")
        info(docs, dirs)
    if doc_pars[3] not in list(dirs.keys()):
        print("There`s no this number shelf. Please, create it wits command 'ads'. "
              "Current data:")
        info(docs, dirs)
    else:
        docs.append({"type": f"{doc_pars[1]}", "number": f"{doc_pars[0]}",
                     "name": f"{doc_pars[2]}"})
        dirs[doc_pars[3]].append(doc_pars[0])
        print("New doc added successfully. Current data:")
        info(docs, dirs)


def del_doc(docs, dirs, doc_n):
    """
    Deletes doc
    :param docs: list[dict]
    :param dirs: dict{str:list}
    :param doc_n: boolean
    :return: None
    """
    flag = 0
    for index1, item1 in enumerate(docs):
        if item1['number'] == doc_n:
            del docs[index1]
            for key in dirs.keys():
                for index2, item2 in enumerate(dirs[key]):
                    if item2 == doc_n:
                        del dirs[key][index2]
            print("Document was deleted.")
            flag = 1
    if flag != 1:
        print("There`s no such doc.")
    print("Current data:")
    info(docs, dirs)


def finder(docs, doc_n):
    """
    Checks if the current doc exist
    :param docs: list[dict]
    :param doc_n: str
    :return: boolean
    """
    for i in docs:
        if i['number'] == doc_n:
            return True
    return False


def mover(docs, dirs, doc_s, doc_n):
    """
    Moves doc from one self to another
    :param docs: list[dict]
    :param dirs: dict{str:list}
    :param doc_s: str
    :param doc_n: str
    :return: None
    """
    if finder(docs, doc_n):
        if doc_s in dirs.keys():
            for keys in dirs.keys():
                for index3, value3 in enumerate(dirs[keys]):
                    if value3 == doc_n:
                        del dirs[keys][index3]
            dirs[doc_s].append(doc_n)
            print("doc moved. Current data:")
            info(docs, dirs)
        else:
            print("There`s no this number shelf. Please, create it wits command 'ads'. "
                  "Current data:")
            info(docs, dirs)

    else:
        print("There`s no such doc. Current data:")
        info(docs, dirs)


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
    F = 0
    C = None
    while C != 'q':
        if F != 0:
            input()
        F = 1
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
        C = input()
        while C not in commandline:
            print("Incorrect input.")
            C = input()
        if C in ['p', '1', 's', '2', 'd', '7', 'm', '8']:
            doc_number = input("Enter document number: ")
            if C in ['s', '2']:
                result = shelf(directories, doc_number)
                if result:
                    print(f"The document is stored on the shelf: {result}")
            elif C in ['d', '7']:
                del_doc(documents, directories, doc_number)
            elif C in ['m', '8']:
                doc_shelf = input("Enter new shelf: ")
                mover(documents, directories, doc_shelf, doc_number)
            elif C in ['p', '1']:
                result = person(documents, doc_number)
                if result:
                    print(f"Document owner: {result}")
                else:
                    print("There`s no such document")
            else:
                print("Document wasn`t found in base")
        elif C in ['l', '3']:
            info(documents, directories)
        elif C in ['ads', '4', 'ds', '5']:
            shelf_number = input("Enter shelf number: ")
            if C in ['ds', '5']:
                del_s(directories, shelf_number)
            elif C in ['ads', '4']:
                ads(directories, shelf_number)
        elif C in ['ad', '6']:
            doc_parameters = ['number', 'type', 'owner', 'shelf']
            for ind, val in enumerate(doc_parameters):
                doc_parameters[ind] = input(f"Enter document {val}: ")
            add_doc(documents, directories, doc_parameters)
print("Good bye!")
