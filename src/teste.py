from typing import Optional

from pydantic import BaseModel


class Endereco(BaseModel):
    """
    Representa o endereço da empresa dona do empreendimento.

    Attributes:
        cep (str): Código postal.
        pais (str): País.
        estado (str): Estado.
        municipio (str): Município.
        bairro (str): Bairro.
        tipoLogradouro (str): Tipo de logradouro.
        numero (str): Número do endereço.
        complemento (str): Informações adicionais do endereço.
        referencia (str): Ponto de referência do endereço.
    """

    cep: Optional[str]
    pais: Optional[str]
    estado: Optional[str]
    municipio: Optional[str]
    bairro: Optional[str]
    tipoLogradouro: Optional[str]
    numero: Optional[str]
    complemento: Optional[str]
    referencia: Optional[str]


class CentroCusto(BaseModel):
    """
    Representa o centro de custo do empreendimento.

    Attributes:
        id (str): Identificador único do centro de custo.
        padrao (int): Indica se é um centro de custo padrão.
        identificador (str): Identificador do centro de custo.
        reduzido (int): Código reduzido do centro de custo.
        extenso (str): Descrição extensa do centro de custo.
        descricao (str): Descrição do centro de custo.
        global (str): Indica se é global.
        usuarios (dict): Informações sobre os usuários do centro de custo.
    """

    id: Optional[str]
    padrao: Optional[int]
    identificador: Optional[str]
    reduzido: Optional[int]
    extenso: Optional[str]
    descricao: Optional[str]
    global_is: Optional[str]
    usuarios: Optional[dict]


class Projeto(BaseModel):
    """
    Representa o projeto do empreendimento.

    Attributes::
        id (str): Identificador único do projeto.
        padrao (int): Indica se é um projeto padrão.
        identificador (str): Identificador do projeto.
        reduzido (int): Código reduzido do projeto.
        extenso (str): Descrição extensa do projeto.
        descricao (str): Descrição do projeto.
        global (str): Indica se é global.
        usuarios (dict): Informações sobre os usuários do projeto.
        tabOrganizacao (float): Valor numérico relacionado à organização da tabela.
        padraoOrganizacao (float): Valor numérico relacionado ao padrão de organização.
        expand (str): Indica se deve expandir.
    """

    id: Optional[str]
    padrao: int
    identificador: Optional[str]
    reduzido: int
    extenso: Optional[str]
    descricao: Optional[str]
    global_is: str
    usuarios: Optional[dict]
    tabOrganizacao: Optional[float]
    padraoOrganizacao: Optional[float]
    expand: Optional[str]


class Empreendimentos(BaseModel):
    """
    Representa um empreendimento.

    Attributes:
        id (str): Código ID base64 interno do empreendimento.
        codigo (float): Código do empreendimento.
        codigoOrganizacao (float): Código da organização do empreendimento.
        codigoFilial (float): Código da filial do empreendimento.
        nomeFilial (str): Nome da empresa dona do empreendimento.
        fantasiaFilial (str): Nome fantasia da empresa dona do empreendimento.
        cnpjFilial (str): CNPJ da empresa dona do empreendimento.
        codigo_externo (str): Código externo do empreendimento.
        nome (str): Nome do empreendimento.
        nomeReal (str): Nome real do empreendimento.
        tipoImovel (str): Tipo de imóvel do empreendimento.
        disponivelPortalCliente (str): Disponibilidade no portal do cliente.
        disponivelHomepay (str): Disponibilidade no Homepay.
        inicioObra (str): Data de início da obra.
        fimObra (str): Data de conclusão da obra.
        habite (str): Data de habite-se.
        previsaoHabite (str): Previsão de habite-se.
        averbacao (str): Averbação.
        instalacaoCondominio (str): Instalação no condomínio.
        cadastro (str): Cadastro.
        lancamento (str): Lançamento.
        vencimentoDivida (str): Vencimento da dívida.
        conclusaoPastaMae (str): Conclusão da pasta mãe.
        entregaAreaComum (str): Entrega da área comum.
        areaTerreno (float): Área do terreno do empreendimento.
        areaEquivalente (float): Área equivalente do empreendimento.
        areaPrivada (float): Área privada do empreendimento.
        areaTotal (float): Área total do empreendimento.
        areaConstrucaoPrefeitura (float): Área de construção pela prefeitura.
        areaConstrucaoEquivalente (float): Área de construção equivalente.
        areaConstrucaoTotal (float): Área de construção total.
        codigoCentroCustoComercial (float): Código do centro de custo comercial.
        codigoCentroCustoCliente (float): Código do centro de custo do cliente.
        dataCriacao (str): Data de criação.
        dataAlteracao (str): Data de alteração.
        endereco (Endereco): Endereço referente à empresa dona do empreendimento.
        centroCusto (CentroCusto): Centro de custo do empreendimento.
        projeto (Projeto): Projeto do empreendimento.
    """

    id: Optional[str]
    codigo: Optional[float]
    codigoOrganizacao: Optional[float]
    codigoFilial: Optional[float]
    nomeFilial: Optional[str]
    fantasiaFilial: Optional[str]
    cnpjFilial: Optional[str]
    codigo_externo: Optional[str]
    nome: Optional[str]
    nomeReal: Optional[str]
    tipoImovel: Optional[str]
    disponivelPortalCliente: Optional[str]
    disponivelHomepay: Optional[str]
    inicioObra: Optional[str]
    fimObra: Optional[str]
    habite: Optional[str]
    previsaoHabite: Optional[str]
    averbacao: Optional[str]
    instalacaoCondominio: Optional[str]
    cadastro: Optional[str]
    lancamento: Optional[str]
    vencimentoDivida: Optional[str]
    conclusaoPastaMae: Optional[str]
    entregaAreaComum: Optional[str]
    areaTerreno: Optional[float]
    areaEquivalente: Optional[float]
    areaPrivada: Optional[float]
    areaTotal: Optional[float]
    areaConstrucaoPrefeitura: Optional[float]
    areaConstrucaoEquivalente: Optional[float]
    areaConstrucaoTotal: Optional[float]
    codigoCentroCustoComercial: Optional[float]
    codigoCentroCustoCliente: Optional[float]
    dataCriacao: Optional[str]
    dataAlteracao: Optional[str]
    endereco: Optional[Endereco]
    centroCusto: Optional[CentroCusto]
    projeto: Optional[Projeto]
