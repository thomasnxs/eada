import csv

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaHeroes:
    def __init__(self):
        self.tamanho = 26
        self.tabela = [[] for _ in range(self.tamanho)]

   
        self.importar_contatos('agenda.csv')  

    def calcular_indice(self, nome):
        primeira_letra = nome[0].upper()
        indice = ord(primeira_letra) - ord('A')
        return indice

    def adicionar_contato(self, nome, telefone):
        indice = self.calcular_indice(nome)
        novo_contato = Contato(nome, telefone)
        for contato in self.tabela[indice]:
            if contato.nome == nome:
                print("\nO Super-Herói {nome} já existe na agenda.")
                return
        self.tabela[indice].append(novo_contato)
        print(f"\nSuper-Herói {nome} adicionado com sucesso!")

    def buscar_contato_por_nome(self, nome):
        indice = self.calcular_indice(nome)
        for contato in self.tabela[indice]:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos_por_letra(self, letra):
        indice = ord(letra.upper()) - ord('A')
        contatos_letra = []
        for contato in self.tabela[indice]:
            contatos_letra.append(contato)
        return contatos_letra

    def remover_contato(self, nome):
        indice = self.calcular_indice(nome)
        for contato in self.tabela[indice]:
            if contato.nome == nome:
                self.tabela[indice].remove(contato)
                print(f"\nSuper-Herói {nome} removido com sucesso!")
                return
        print("\nSuper-Herói não encontrado na agenda.")

    def buscar_contatos_por_primeira_letra(self, letra):
        indice = ord(letra.upper()) - ord('A')
        contatos_letra = []
        for contato in self.tabela[indice]:
            contatos_letra.append(contato)
        return contatos_letra

    def importar_contatos(self, arquivo_csv):
        with open(arquivo_csv, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 2:
                    nome, telefone = row
                    self.adicionar_contato(nome, telefone)

    def menu_interativo(self):
        while True:
            print("\nBem-vindo ao Sistema da Agenda do Clube Secreto de Super-Heróis!")
            print("\nMenu:")
            print("1. Adicionar Super-Herói")
            print("2. Buscar Super-Heróis")
            print("3. Mostrar todos os Super-Heróis pela letra:")
            print("4. Remover Super-Herói")
            print("5. Sair")
            
            escolha = input("\nEscolha uma opção: ")

            if escolha == "1":
                nome = input("\nDigite o nome do Super-Herói: ")
                telefone = input("\nDigite o telefone do Super-Herói: ")
                self.adicionar_contato(nome, telefone)
            elif escolha == "2":
                nome = input("\nDigite o nome do Super-Herói a ser buscado: ")
                contato = self.buscar_contato_por_nome(nome)
                if contato:
                    print(f"\nSuper-Herói encontrado: {contato.nome}, {contato.telefone}")
                else:
                    print("\nSuper-Herói não encontrado na agenda.")
            elif escolha == "3":
                letra = input("\nDigite a letra para listar os Super-Heróis: ")
                contatos_letra = self.listar_contatos_por_letra(letra)
                if contatos_letra:
                    print(f"\nSuper-Heróis com a letra {letra}:")
                    for contato in contatos_letra:
                        print(f"{contato.nome}, {contato.telefone}")
                else:
                    print(f"\nNenhum Super-Herói encontrado com a letra {letra}.")
            elif escolha == "4":
                nome = input("\nDigite o nome do Super-Herói a ser removido: ")
                self.remover_contato(nome)
            elif escolha == "5":
                print("\nSaindo da agenda.")
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    agenda = AgendaHeroes()
    agenda.menu_interativo()
