# Imports das classes dentro de 'funcoesInterface'

from funcoes.funcoesInterface.agendamentoInterface import AgendamentoInterface
from funcoes.funcoesInterface.categoriaInterface import CategoriaInterface
from funcoes.funcoesInterface.cidadeInterface import CidadeInterface 
from funcoes.funcoesInterface.coletorInterface import ColetorInterface 
from funcoes.funcoesInterface.depositoInterface import DepositoInterface 
from funcoes.funcoesInterface.entradaInterface import EntradaInterface
from funcoes.funcoesInterface.estadoInterface import EstadoInterface 
from funcoes.funcoesInterface.materialInterface import MaterialInterface
from funcoes.funcoesInterface.saidaInterface import SaidaInterface
from funcoes.funcoesInterface.tipo_usuarioInterface import TipoUsuarioInterface 
from funcoes.funcoesInterface.usuarioInterface import UsuarioInterface
from funcoes.funcoesInterface.rankingInterface import RankingInterface

# Conexao das classes de interface com banco passado pelo Menu

class ConexaoInterface:
    def __init__(self, banco):
        self.agendamento = AgendamentoInterface(banco)
        self.categoria = CategoriaInterface(banco)
        self.cidade = CidadeInterface(banco)
        self.coletor = ColetorInterface(banco)
        self.deposito = DepositoInterface(banco)
        self.entrada = EntradaInterface(banco)
        self.estado = EstadoInterface(banco)
        self.material = MaterialInterface(banco)
        self.saida = SaidaInterface(banco)
        self.tipo_usuario = TipoUsuarioInterface(banco)
        self.usuario = UsuarioInterface(banco)
        self.ranking = RankingInterface(banco)
