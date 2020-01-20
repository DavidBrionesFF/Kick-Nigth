def preformat_note(note):
    print(" ==== Nota: " + str(note.title) + " - Fecha: " + str(note.create_at))
    
    if len(note.content) > 30:
        print(" ==== " + note.content[0:29] + "...")
    else:
        print(" ==== " + note.content)
    
    print(" ==== Note ID : " + str(note.no))
    print("")
