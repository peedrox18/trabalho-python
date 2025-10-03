ESPECIALIDADES = ("Ortopedia", "Pediatria", "Plantão")
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            print("Idade inválida, definindo como 0")
            self._idade = 0
        else:
            self._idade = valor

    def __str__(self):
        return f"Nome: {self._nome}, Idade: {self._idade}"

class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self._cpf = cpf

    def __str__(self):
        return f"Paciente - {super().__str__()}, CPF: {self._cpf}"

class Medico(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self._especialidade = especialidade

    def __str__(self):
        return f"Médico - {super().__str__()}, Especialidade: {self._especialidade}"

pacientes = []
medicos = []

def validar_nome(nome):
    return all(ch.isalpha() or ch.isspace() for ch in nome)
def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def cadastrar_paciente():
    try:
        nome = input("Nome do paciente: ").strip()
        if not validar_nome(nome):
            print("Nome inválido! Não pode conter números ou símbolos.")
            return

        idade = int(input("Idade: ").strip())
        cpf = input("CPF (11 números): ").strip()

        if not validar_cpf(cpf):
            print("CPF inválido! Deve conter exatamente 11 números.")
            return

        paciente = Paciente(nome, idade, cpf)
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar paciente:", e)

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for i, p in enumerate(pacientes):
            print(f"{i} - {p}")

def editar_paciente():
    listar_pacientes()
    try:
        idx = int(input("Digite o número do paciente para editar: "))
        if idx < 0 or idx >= len(pacientes):
            print("Paciente não encontrado.")
            return

        nome = input("Novo nome: ").strip()
        if not validar_nome(nome):
            print("Nome inválido!")
            return
        idade = int(input("Nova idade: ").strip())
        cpf = input("Novo CPF (11 números): ").strip()
        if not validar_cpf(cpf):
            print("CPF inválido!")
            return

        pacientes[idx] = Paciente(nome, idade, cpf)
        print("Paciente atualizado com sucesso!")
    except:
        print("Erro ao editar paciente.")

def remover_paciente():
    listar_pacientes()
    try:
        idx = int(input("Digite o número do paciente para remover: "))
        if idx < 0 or idx >= len(pacientes):
            print("Paciente não encontrado.")
            return
        pacientes.pop(idx)
        print("Paciente removido com sucesso!")
    except:
        print("Erro ao remover paciente.")

def cadastrar_medico():
    try:
        nome = input("Nome do médico: ").strip()
        if not validar_nome(nome):
            print("Nome inválido! Não pode conter números ou símbolos.")
            return

        idade = int(input("Idade: ").strip())
        print("Especialidades disponíveis:", ESPECIALIDADES)
        esp = input("Digite a especialidade: ").strip()
        if esp not in ESPECIALIDADES:
            print("Especialidade inválida!")
            return

        medico = Medico(nome, idade, esp)
        medicos.append(medico)
        print("Médico cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar médico:", e)

def listar_medicos():
    if not medicos:
        print("Nenhum médico cadastrado.")
    else:
        for i, m in enumerate(medicos):
            print(f"{i} - {m}")

def editar_medico():
    listar_medicos()
    try:
        idx = int(input("Digite o número do médico para editar: "))
        if idx < 0 or idx >= len(medicos):
            print("Médico não encontrado.")
            return

        nome = input("Novo nome: ").strip()
        if not validar_nome(nome):
            print("Nome inválido!")
            return
        idade = int(input("Nova idade: ").strip())
        print("Especialidades disponíveis:", ESPECIALIDADES)
        esp = input("Nova especialidade: ").strip()
        if esp not in ESPECIALIDADES:
            print("Especialidade inválida!")
            return

        medicos[idx] = Medico(nome, idade, esp)
        print("Médico atualizado com sucesso!")
    except:
        print("Erro ao editar médico.")

def remover_medico():
    listar_medicos()
    try:
        idx = int(input("Digite o número do médico para remover: "))
        if idx < 0 or idx >= len(medicos):
            print("Médico não encontrado.")
            return
        medicos.pop(idx)
        print("Médico removido com sucesso!")
    except:
        print("Erro ao remover médico.")

def menu():
    while True:
        print("\n--- MENU CLÍNICA ---")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Editar Paciente")
        print("4. Remover Paciente")
        print("5. Cadastrar Médico")
        print("6. Listar Médicos")
        print("7. Editar Médico")
        print("8. Remover Médico")
        print("9. Sair")

        opcao = input("Escolha: ").strip()

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
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
menu()
