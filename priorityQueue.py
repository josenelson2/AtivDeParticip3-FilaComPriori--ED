from node import Node

class priorityQueue:
    def __init__(self):
        self.head = None #início da fila
        self.tail = None #final da fila
        self.sizeN = 0 #pessoas na fila normal
        self.sizeP = 0 #pessoas na fila prioritária
    


    def list(self): #listar todas as pessoas da fila
        current = self.head #current recebe o nó do início
        while current: #enquanto  houver nós na fila
            if current.priority:
                tipo = "Prioridade"
            else:
                tipo = "Normal"
            print(current.name + " - " + tipo) 
            current = current.next

    

            

