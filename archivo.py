import tu
import os

class File:
    def __init__(self, name=None):
        self.name = name
        
    

    
    '''
    Método que devuelve la ruta del file
    '''    
    def file_location(self):
        # ruta a la carpeta que contiene el file
        path_folder = "./Ficheros/"

        # Obtiene lista de los nombres de files en la carpeta
        files_in_folder = os.listdir(path_folder)

        # Verifica si el nombre file está en la lista de files de la carpeta
        if self.name in files_in_folder:
            location = f"{path_folder}{self.name}"
            return location
    
    '''
    Método que verifica las TU que se pueden leer y las copia en un fichero
    '''                 
    def read_file(self):
        file = self.file_location()
        target_file = self.get_translation_path()
        with open(file, "r") as source_file:
            with open(target_file, "w") as target_file:
                try:
                    for i,line in enumerate(source_file):
                        new_line=tu.TU(line)                
                        if new_line.validate_tab():
                            print(i,line) 
                            #source, target = new_line.separate_tu()
                            #source, target = new_line.validate_special_character()
                            #target_file.write(f"{source}\t{target}")
                except:
                    print("error")
                    
        
    '''
    Método que devuelve la ruta del fichero donde se va a guardar todas las TU
    '''
    def get_translation_path(self):        
        path_folder = "./Ficheros/traduction.tsv"
        return path_folder
    
    '''
    Método que borra todas las TU del fichero target
    '''    
    def clear_file(self):
        with open(self.get_translation_path(), "w") as file:
            file.write("")
    