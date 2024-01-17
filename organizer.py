import os
import shutil

def organize_files():
    # Norādiet direktoriju, kurā jūs vēlaties organizēt failus
    source_directory = "/celš/uz/jūsu/failu/direktoriju"
    
    # Izveidojiet direktorijas, ja tās vēl neeksistē
    create_directories(source_directory)
    
    files = os.listdir(source_directory)

    for file_name in files:
        # Izveidojiet pilnu ceļu līdz failam
        file_path = os.path.join(source_directory, file_name)

        if os.path.isfile(file_path):
            # Iegūstiet faila paplašinājumu (piemēram, .txt, .jpg)
            file_extension = os.path.splitext(file_name)[1].lower()

            # Noteikiet, kurā direktorijā jāsaglabā faili
            destination_directory = determine_destination_directory(file_extension)

            # Ja direktorija neeksistē, izveidojiet to
            create_directory(destination_directory)

            shutil.move(file_path, os.path.join(destination_directory, file_name))

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_directories(source_directory):
    extensions = set([os.path.splitext(file)[1].lower() for file in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, file))])

    for extension in extensions:
        directory = determine_destination_directory(extension)
        create_directory(directory)

def determine_destination_directory(file_extension):
    # Norādiet, kā jūs vēlaties organizēt failus atkarībā no paplašinājuma
    # Piemēram, ja vēlaties saglabāt .txt failus "TekstaFaili" mapē:
    if file_extension == ".txt":
        return "/celš/uz/jūsu/failu/direktoriju/TekstaFaili"
    # Papildiniet ar citiem nosacījumiem, ja nepieciešams

    # Ja nekas neatbilst, atgriezt noklusējuma direktoriju
    return "/celš/uz/jūsu/failu/direktoriju/NepieciesamaisDirektorijasNosaukums"
