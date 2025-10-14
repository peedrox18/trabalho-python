from datetime import datetime  # Importa a biblioteca usada para validar datas

# CLASSE PESSOA (SUPERCLASSE)
# Esta classe é a base para Paciente e Médico. Ela guarda atributos comuns (nome, data de nascimento, CPF).
class Pessoa:
    def __init__(self, nome, data_nasc, cpf=None):
        # Atributos básicos de toda pessoa
        self.nome = nome
        self.data_nasc = data_nasc
        self._cpf = None  # CPF é privado, o que é indicado pelo underline
        if cpf:
            self.cpf = cpf  # Se um CPF for informado, ele é validado pelo setter

    # Getter do CPF, que permite acessar o CPF de forma controlada
    @property
    def cpf(self):
        return self._cpf

    # Setter do CPF que controla como o CPF é modificado e validado
    @cpf.setter
    def cpf(self, valor):
        if valor is None or valor == "":  # Caso o CPF seja vazio, define como None
            self._cpf = None
            return
        # verifica se foram inseridos 11 números 
        if isinstance(valor, str) and len(valor) == 11 and valor.isdigit(): 
            # isinstance verifica se o valor foi digitado como texto e isdigit se são números  
            self._cpf = valor
        else:
            # lança um erro caso não cumpra o requisito
            raise ValueError("CPF deve conter exatamente 11 números.")

# CLASSE PACIENTE (HERDA DE PESSOA)
# herda todos os atributos de Pessoa
class Paciente(Pessoa):
    def __init__(self, nome, data_nasc, cpf, gravidade):
        # usa super() para aproveitar a estrutura da classe Pessoa
        super().__init__(nome, data_nasc, cpf)
        self.gravidade = gravidade  # atributo pra pacientes 

    def __str__(self):
        # retorna uma string formatada com os dados do paciente
        return f"Nome: {self.nome} | Nasc.: {self.data_nasc} | CPF: {self.cpf} | Gravidade: {self.gravidade}"

# CLASSE MÉDICO (HERDA DE PESSOA)
# representa um médico que herda apenas alguns atributos específicos 
class Medico(Pessoa):
    def __init__(self, nome, data_nasc, crm, especialidade, cpf=None):
        super().__init__(nome, data_nasc, cpf)
        # Atributos específicos do médico
        self.crm = crm
        self.especialidade = especialidade

    def __str__(self):
        return f"Nome: {self.nome} | Nasc.: {self.data_nasc} | CRM: {self.crm} | Especialidade: {self.especialidade}"

# listas criadas para armazenar os cadastros 
pacientes = []
medicos = []
# tupla com os níveis de gravidade possíveis (fixos)
gravidades = ("Verde", "Amarelo", "Vermelho")

# FUNÇÕES DE VALIDAÇÃO
# Valida formato de data (usa datetime para checar se a data é real)
def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%d/%m/%Y")  # Tenta converter a data
        return True
    except ValueError:
        return False

# Valida formato do CRM (padrão médico)
def validar_crm(crm_texto):
    if not isinstance(crm_texto, str):
        return False
    crm = crm_texto.strip().upper() #strip remove espaços em branco e upper deixa todas as letras maiúsculas 
    if crm.startswith("CRM"): #verifica se começa com CRM
        crm = crm[3:].strip() #remove os 3 primeiros caracteres (CRM/SP 123456 vira /SP 123456)
    crm = crm.replace("-", " ").replace("/", " ").replace(".", " ") 
    parts = crm.split()
    # Aceita formatos como "123456" ou "CRM/SP 123456"
    if len(parts) == 1: #se for digitado apenas os números 
        if parts[0].isdigit() and 4 <= len(parts[0]) <= 7:
            return True
        return False
    elif len(parts) == 2: #se for em duas partes 
        a, b = parts #separa as partes em variáveis 
        if a.isalpha() and len(a) == 2 and b.isdigit() and 4 <= len(b) <= 7: #isalpha verifica se tem apenas letras 
            return True #primeira parte é estado (duas letras) e a segunda é número
        if b.isalpha() and len(b) == 2 and a.isdigit() and 4 <= len(a) <= 7:
            return True #primeira parte é número e a segunda é estado (duas letras)
        return False
    else:
        return False
        
# FUNÇÕES DE PACIENTE

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome: ")
    while any(char.isdigit() for char in nome):  # Impede números no nome
        print("Erro: o nome não pode conter números.")
        nome = input("Nome: ")
    # Validação da data
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    while not validar_data(data_nasc):
        print("Data inválida! Use o formato dd/mm/aaaa.")
        data_nasc = input("Data de nascimento: ")
    # Validação do CPF
    while True:
        cpf = input("CPF (11 números): ")
        if len(cpf) == 11 and cpf.isdigit():
            break
        else:
            print("CPF inválido! Digite exatamente 11 números.")
    # Escolha da gravidade
    print("Nível de gravidade:")
    for i, cor in enumerate(gravidades):
        print(f"{i + 1}. {cor}")
    while True:
        cor_gravidade = input("Escolha (1-3): ").strip()
        if cor_gravidade in ("1", "2", "3"):
            gravidade = gravidades[int(cor_gravidade) - 1] 
            break  # -1 é usado porque as listas em python começam na posição 0
        else:
            print("Erro: digite apenas 1, 2 ou 3.")
    # Cria o paciente e adiciona à lista
    paciente = Paciente(nome, data_nasc, cpf, gravidade)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for i, p in enumerate(pacientes):
        print(f"{i + 1}. {p}")

def editar_paciente():
    listar_pacientes()
    try:
        indice = int(input("Informe o número do paciente para editar: ")) - 1
        if indice < 0 or indice >= len(pacientes):
            raise IndexError
        p = pacientes[indice]
        # Permite editar cada campo opcionalmente
        print(f"Editando: {p.nome}")
        novo_nome = input("Novo nome (vazio p/ manter): ")
        if novo_nome != "":
            while any(char.isdigit() for char in novo_nome):
                print("Erro: o nome não pode conter números.")
                novo_nome = input("Novo nome: ")
            p.nome = novo_nome
        nova_data = input("Nova data de nascimento (dd/mm/aaaa ou vazio p/ manter): ")
        if nova_data != "":
            while not validar_data(nova_data):
                print("Data inválida! Use o formato dd/mm/aaaa.")
                nova_data = input("Nova data de nascimento: ")
            p.data_nasc = nova_data
        novo_cpf = input("Novo CPF (11 números ou vazio p/ manter): ")
        if novo_cpf != "":
            try:
                p.cpf = novo_cpf
            except ValueError as e:
                print(e)
        print("Níveis de gravidade: 1-Verde, 2-Amarelo, 3-Vermelho")
        while True:
            nova_gravidade = input("Nova gravidade (1-3 ou vazio p/ manter): ").strip()
            if nova_gravidade == "":
                break
            if nova_gravidade in ("1", "2", "3"):
                p.gravidade = gravidades[int(nova_gravidade) - 1]
                break  
            else:
                print("Erro: digite apenas 1, 2 ou 3 ou deixe vazio para manter.")
        print("Paciente editado com sucesso!")
    except (ValueError, IndexError):
        print("Erro: paciente não encontrado.")

def remover_paciente():
    listar_pacientes()
    try:
        indice = int(input("Informe o número do paciente para remover: ")) - 1
        if indice < 0 or indice >= len(pacientes): #veridfica se o número está na lista 
            raise IndexError
        removido = pacientes.pop(indice) #.pop tira da lista e retorna na variável removido
        print(f"Paciente '{removido.nome}' removido com sucesso!")
    except (ValueError, IndexError):
        print("Erro: paciente não encontrado.")

# FUNÇÕES DE MÉDICO

def cadastrar_medico():
    print("\n--- Cadastro de Médico ---")
    nome = input("Nome: ")
    while any(char.isdigit() for char in nome):
        print("Erro: o nome não pode conter números.")
        nome = input("Nome: ")
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    while not validar_data(data_nasc):
        print("Data inválida! Use o formato dd/mm/aaaa.")
        data_nasc = input("Data de nascimento: ")
    crm = input("CRM (ex: 'CRM/SP 123456' ou '123456'): ")
    while not validar_crm(crm):
        print("CRM inválido! Use um formato como '123456' ou 'CRM/SP 123456'.")
        crm = input("CRM: ")
    especialidade = input("Especialidade: ")
    medico = Medico(nome, data_nasc, crm, especialidade)
    medicos.append(medico)
    print("Médico cadastrado com sucesso!")

def listar_medicos():
    print("\n--- Lista de Médicos ---")
    if not medicos:
        print("Nenhum médico cadastrado.")
        return
    for i, m in enumerate(medicos):
        print(f"{i + 1}. {m}")

def editar_medico():
    listar_medicos()
    try:
        indice = int(input("Informe o número do médico para editar: ")) - 1
        if indice < 0 or indice >= len(medicos):
            raise IndexError
        m = medicos[indice]
        print(f"Editando: {m.nome}")
        novo_nome = input("Novo nome (vazio p/ manter): ")
        if novo_nome != "":
            while any(char.isdigit() for char in novo_nome):
                print("Erro: o nome não pode conter números.")
                novo_nome = input("Novo nome: ")
            m.nome = novo_nome
        nova_data = input("Nova data de nascimento (dd/mm/aaaa ou vazio p/ manter): ")
        if nova_data != "":
            while not validar_data(nova_data):
                print("Data inválida! Use o formato dd/mm/aaaa.")
                nova_data = input("Nova data de nascimento: ")
            m.data_nasc = nova_data
        novo_crm = input("Novo CRM (vazio p/ manter): ")
        if novo_crm != "":
            while not validar_crm(novo_crm):
                print("CRM inválido! Use um formato como '123456' ou 'CRM/SP 123456'.")
                novo_crm = input("Novo CRM: ")
            m.crm = novo_crm
        nova_esp = input("Nova especialidade (vazio p/ manter): ")
        if nova_esp != "":
            m.especialidade = nova_esp
        print("Médico editado com sucesso!")
    except (ValueError, IndexError):
        print("Erro: médico não encontrado.")

def remover_medico():
    listar_medicos()
    try:
        indice = int(input("Informe o número do médico para remover: ")) - 1
        if indice < 0 or indice >= len(medicos):
            raise IndexError
        removido = medicos.pop(indice)
        print(f"Médico '{removido.nome}' removido com sucesso!")
    except (ValueError, IndexError):
        print("Erro: médico não encontrado.")

# MENU PRINCIPAL DO SISTEMA
# Mantém o programa rodando até o usuário decidir sair.
while True:
    print("\n===== CLÍNICA MÉDICA =====")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Editar paciente")
    print("4 - Remover paciente")
    print("5 - Cadastrar médico")
    print("6 - Listar médicos")
    print("7 - Editar médico")
    print("8 - Remover médico")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        listar_pacientes()
    elif opcao == "3":
        editar_paciente()
    elif opcao == "4":
        remover_paciente()
    elif opcao == "5":
        cadastrar_medico()
    elif opcao == "6":
        listar_medicos()
    elif opcao == "7":
        editar_medico()
    elif opcao == "8":
        remover_medico()
    elif opcao == "9":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

