import os
import sys
from enviroment import init_directories
import datetime
from model.note import Note
from util import preformat_note

# print(sys.argv)

def view_message_welcome():
    print(" Kick Nigth ".center(100, "="))

def view_menu_select():
    print("Seleccione una opcion")
    print("1. Todas las notas")
    print("2. Crear Nota")
    print("3. Editar Nota")
    print("4. Eliminar Nota")
    print("5. Salir")

    try:
        option = int(input())
        if option < 6 and option > 0:
            return option
        else:
            return view_menu_select()
    except:
        return view_menu_select()

def create_note():
    titulo = str(input("Ingrese el titulo: "))
    mensaje = str(input("Ingrese el cuerpo de la nota: "))

    note  = {
        "title": titulo,
        "content": mensaje,
        "create_at": str(datetime.datetime.now()),
        "no": Note.generate_no()
    }

    note_created = Note.create(note)


def update_note():
    no = input("Ingrese el ID de nota: ")
    note = Note.find_by_id(no)

    title = input("Ingrese el nuevo titulo  (Titulo antiguo, vacio para conservarlo: " + note.title + ")")
    content = input("Ingrese el nuevo contenido  (Contenido antiguo, vacio para conservarlo: " + note.content + ")")

    if len(title) > 1:
        note.title = title
    
    if len(content) > 1:
        note.content = content
    
    note.update()


def delete_note():
    no = input("Ingrese el ID de la nota: ")
    opt = input("Desea elimnar la nota (y/n)")
    
    if opt == "y":
        Note.delete(no)

def find_all_note():
    for note in Note.find_all():
        preformat_note(note)

def navigate():
    option = view_menu_select()

    if option == 1:
        find_all_note()
    elif option == 2:
        create_note()
    elif option == 3:
        update_note()
    elif option == 4:
        delete_note()
    elif option == 5:
        return
    
    navigate()

def main():
    init_directories()
    view_message_welcome()
    navigate()
    

if __name__ == '__main__':
    main()