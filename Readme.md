# Setup básico de projetos em Python

Este repositório tem como objetivo auxiliar os desenvolvedores de novas 
tecnologias a construir um melhor código seguindo as boas práticas
baseadas na [PEP8]("https://peps.python.org/pep-0008/")

## Pré-requisitos
* Para o versionamento e reastreabiliade do código use o **[Git]("https://git-scm.com/")**
* Para melhor controle de versões de instalação do Python use o **[Pyenv]("https://github.com/pyenv/pyenv")**
* Para gerenciamento de pacotes de dependências use o **[Poetry](""https://python-poetry.org/docs/)**.

## Setup
Uma vez com os pré-requisitos atendidos, você pode clonar este repositório local em sua máquina.

* Clone repositório
```bash
git clone https://github.com/pcastr/pyproject-template
cd pyproject-template
```

* Uma vez no diretório, execute os comandos do `Poetry` para acessar a documentação 
com os detalhes da base do projeto

```bash
poetry config virtualenvs.in-project true   #Comando para criar os ambientes virtuais dentro do projeto
poetry config virtualenvs.prefer-active-python true #Comando para o poetry identificar a versão do python utilizada do projeto
```

```bash
poetry install --no-root    #instalar as dependencias base do projeto
```

```bash 
poetry run task docs    #iniciar a instancia da documentação
```

