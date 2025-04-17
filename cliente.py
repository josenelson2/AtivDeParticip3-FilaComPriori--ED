from priorityQueue import priorityQueue

def menu():
    print("-----------------------------------------------------")
    print("1. Chegada de pessoa para atendimento")
    print("2. Atendimento de uma pessoa")
    print("3. Listar todas as pessoas da fila")
    print("4. Gerar informações sobre os atendimentos realizados e o tamanho atual da fila")
    print("5. SAIR")
    
fila = priorityQueue()
atendimentos_normais = 0
atendimentos_prioridade = 0

while True:

    menu()
    op = input("Selecione a opção desejada: ")

    if (op == '1'):
        print("-----------------------------------------------------")
        print("ATENDIMENTO:")
        print("1 - Prioridade")
        print("2 - Normal")

        modalidade = input("Selecione a modalidade do atendimento: ")

        if (modalidade == '1'):
            nome = input("Nome da pessoa: ")
            fila.enqueue(nome, True)
            print(f"Pronto. A pessoa '{nome}' foi adicionada na fila na modalidade PRIORIDADE")
            
        elif (modalidade == '2'):
            nome = input("Nome da pessoa: ")
            fila.enqueue(nome, False)
            print(f"Pronto. A pessoa '{nome}' foi adicionada na fila na modalidade NORMAL")
            
        else: 
            print("OPÇÃO INVÁLIDA! RETORNANDO AO MENU.")

    elif (op == '2'):
        print("-----------------------------------------------------")
        if fila.is_empty(): #verifica se a fila está vazia
            print("A fila está vazia!\n")
        else:
            atendidos = 0

        while atendidos < 3 and fila.sizeN  > 0:
            nome = fila.priority_dequeue(False)
            if nome:
                print(f"Atendendo: {nome} (normal)") 
                atendimentos_normais += 1 #incrementa um atendimento
                atendidos += 1
            else:
                break
        if fila.sizeP > 0:
            nome = fila.priority_dequeue(True)
            if nome:
                print(f"Atendendo: {nome} (prioridade)")
                atendimentos_prioridade += 1 #incrementa um atendimento

    elif (op == '3'):
        print("-----------------------------------------------------")
        if fila.is_empty():
            print("A fila está vazia!")
        else:
            print("--------FILA--------")
            fila.list()

    elif (op == '4'):
        print("-----------------------------------------------------")
        print("INFORMAÇÕES DOS ATENDIMENTOS:")
        print(f"ATENDIMENTOS NORMAIS: {atendimentos_normais}, ATENDIMENTOS PRIORITÁRIOS: {atendimentos_prioridade}")
        print(f"TAMANHO ATUAL DA FILA:\nNORMAIS: {fila.sizeN}, PRIORITÁRIOS: {fila.sizeP}")

    elif (op == '5'):
        print("-----------------------------------------------------")
        if fila.is_empty():
            total = atendimentos_normais + atendimentos_prioridade
            if total > 0:
                percentual_normal = (atendimentos_normais/total) * 100
                percentual_prioridade = (atendimentos_prioridade/total) * 100
            else:
                percentual_normal = 0
                percentual_prioridade = 0
            
            print("--------ESTATÍSTICAS--------")
            print("Total de atendimentos: {:.2f}".format(total))
            print("Percentual de atendimentos normais: {:.2f}%".format(percentual_normal))
            print("Percentual de atendimentos prioritários: {:.2f}%".format(percentual_prioridade))
            break
        else:
            print("Ainda há pessoas na fila!\n")

    else:
        print("-----------------------------------------------------")
        print("OPÇÃO INVÁLIDA. RETORNANDO AO MENU. TENTE NOVAMENTE.")