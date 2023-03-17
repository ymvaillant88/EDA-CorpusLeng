class TU:
    def __init__(self, line=None):
        self.line= line
    
    def get_line(self):
        return self.line
    
    '''
    Método que divide la frase de una TU. 
    Lo que esté antes del primer tab lo guarda en "source" y todo los demás en "target"
    '''    
    def separate_tu(self):
        source, target = self.line.split("\t")
        return source,target
    
    '''
    Método que devuelve True si en la linea solo hay un tab 
    '''
    def validate_tab(self):        
        if self.line.count("\t") == 1:
            return True
        else:
            return False        
    
    '''
    Método que verifica si en una TU hay " o ' y lo remplaza por ""
    '''
    def validate_special_character(self):
        source, target = self.separate_tu()
        if (target[0] == '"' and  target.count('"') % 2 != 0):
            target = target[1:]
        else:
            target = target        
        return source, target

                     
                    
                    