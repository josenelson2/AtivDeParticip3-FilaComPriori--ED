from node import Node

class priorityQueue:
    def __init__(self):
        self.head = None #início da fila
        self.tail = None #final da fila
        self.sizeN = 0 #pessoas na fila normal
        self.sizeP = 0 #pessoas na fila prioritária

    def enqueue(self, name, priority):
        new_node = Node(name, priority)

        if (self.tail != None): #se o "rabo" da fila tem alguem, o proximo dele passa a ser o novo no
            self.tail.next = new_node
        self.tail = new_node  

        if (self.head == None):
            self.head = new_node

        if (priority == True):
            self.sizeP += 1

        else:
            self.sizeN += 1
    
    def dequeue(self):
        if (self.head == None):
            return None
        
        node_remove = self.head
        self.head = self.head.next

        if (self.head == None):
            self.tail = None

        if (node_remove.priority == True):
            self.sizeP -= 1
        else:
            self.sizeN -= 1

        return node_remove.name

    def size(self):
        return self.sizeP + self.sizeN


    def list(self): #listar todas as pessoas da fila
        current = self.head #current recebe o nó do início
        while current: #enquanto  houver nós na fila
            if current.priority:
                tipo = "Prioridade"
            else:
                tipo = "Normal"
            print(current.name + " - " + tipo) 
            current = current.next

    def is_empty(self):
        return self.head is None

            