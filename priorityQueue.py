from node import Node

class priorityQueue:
    def __init__(self):
        self.head = None #início da fila
        self.tail = None #final da fila
        self.sizeN = 0 #pessoas na fila normal
        self.sizeP = 0 #pessoas na fila prioritária

    def enqueue(self, name, priority):
        new_node = Node(name, priority)

        if priority: #caso a pessoa tenha prioridade
            if self.head is None or not self.head.priority: #verifica se a fila está vazia ou o primeiro da fila é normal 
                new_node.next = self.head #insere o novo nó como cabeça da fila
                self.head = new_node
                if self.tail is None: #final da fila recebe o novo nó se ela estiver totalmente vazia
                    self.tail = new_node
            else: #caso exista pessoas com prioridade na fila
                current = self.head
                while current.next and current.next.priority: #percorre a fila até encontrar o último elemento com prioridade 
                    current = current.next
                new_node.next = current.next #insere o novo nó depois da última prioridade
                current.next = new_node
            self.sizeP += 1 #incrementa uma pessoa na prioridade
        else: #atendimento normal
            if self.tail: #se tiver elementos na fila, adiciona após o último
                self.tail.next = new_node
                self.tail = new_node
            else: #se a fila estiver vazia, o novo nó é o primeiro e último
                self.head = self.tail = new_node
            self.sizeN += 1 #incrementa uma pessoa na fila normal
    
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
    
    def priority_dequeue(self, priority):
        if self.head is None: #verifica se a lista está vazia
            return None
        
        if self.head.priority == priority: #caso o primeiro caso da fila seja prioridade, remove normalmente 
            return self.dequeue()
        
        prev = self.head #ponteiro para o nó anterior
        current = self.head.next #ponteiro para o nó atual

        while current: #percorre a fila até encontrar o primeiro nó com prioridade
            if current.priority == priority:
                prev.next = current.next #remove o nó atual ao ajustar o ponteiro do anterior
                if current == self.tail: #se o removido for o último atualiza o ponteiro
                    self.tail = prev
                if priority: #atualiza o tamanho
                    self.sizeP -= 1
                else:
                    self.sizeN -= 1
                return current.name #retorna o nome da pessoa atendida
            prev = current #atualiza os ponteiros
            current = current.next
        return None #se não encontrar ninguém com prioridade retorna None

        

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

            