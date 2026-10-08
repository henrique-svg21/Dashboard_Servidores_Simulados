# Monitoramento de Servidores em Tempo Real

> Projeto acadêmico de simulação, processamento e visualização de dados em tempo real aplicado ao contexto industrial.

---

## Sobre o projeto

Este projeto simula a **visualização e o monitoramento em tempo real de dados de servidores**, utilizando três servidores distintos como fonte de dados.

O sistema apresenta, de forma dinâmica, informações como:

- Temperatura da CPU;
- Uso da CPU;
- Uso da memória RAM;
- Latência do servidor;
- Histórico das leituras;
- Gráficos de acompanhamento ao longo do tempo.

Os dados são gerados continuamente pelo arquivo `simulator.py`, armazenados em um banco de dados SQLite e posteriormente consultados e apresentados pelo dashboard desenvolvido em `app.py`.

O projeto foi desenvolvido com **cunho pedagógico e avaliativo** para a disciplina **Desenvolvimento de Interfaces para Visualização de Dados**, lecionada pelo docente **Fabiano da Silva Luiz**, no curso de **Cibersistemas para Automação**, turma **MA77**, no **CentroWEG**, em Jaraguá do Sul – SC.

---

## Objetivo

O objetivo principal é demonstrar, de maneira prática, o funcionamento de uma aplicação capaz de:

1. Gerar dados simulados de equipamentos;
2. Armazenar as informações em um banco de dados;
3. Consultar os dados de forma contínua;
4. Processar e organizar as informações;
5. Apresentar indicadores e gráficos em uma interface visual;
6. Atualizar o dashboard automaticamente, simulando um cenário de monitoramento em tempo real.

---

## Funcionamento do sistema

O projeto é dividido principalmente em duas partes:

### `simulator.py`

Responsável pela **simulação dos servidores**.

O arquivo cria três servidores:

- `Servidor_A`
- `Servidor_B`
- `Servidor_C`

Para cada servidor são gerados valores de:

| Indicador | Descrição |
|---|---|
| Temperatura da CPU | Temperatura atual simulada do processador |
| Uso de CPU | Percentual de utilização do processador |
| Uso de RAM | Percentual de utilização da memória |
| Latência | Tempo de resposta simulado do servidor |

Os valores sofrem pequenas variações a cada ciclo, criando uma sequência de dados que representa um monitoramento contínuo.

As leituras são armazenadas no banco de dados `telemetria.db`.

### `app.py`

Responsável pela **interface de visualização**.

O aplicativo utiliza o Streamlit para construir o dashboard e consulta continuamente o banco de dados, apresentando:

- Indicadores individuais para cada servidor;
- Filtro por servidor;
- Controle da frequência de atualização;
- Controle da quantidade de registros históricos;
- Gráfico de temperatura da CPU;
- Gráfico de uso de RAM;
- Tabela com os registros coletados.

O dashboard é atualizado automaticamente enquanto o simulador estiver em execução.

---

## Fluxo do projeto

```text
┌──────────────────┐
│  simulator.py    │
│                  │
│ Gera os dados    │
│ dos servidores   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  telemetria.db   │
│                  │
│ Banco SQLite     │
│ com as leituras  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     app.py       │
│                  │
│ Consulta e       │
│ processa dados   │
└────────┬─────────┘
         │
         ▼
┌────────────────────────────┐
│        Dashboard            │
│                            │
│ Indicadores + Gráficos +   │
│ Filtros + Tabela           │
└────────────────────────────┘
```

---

## Tecnologias utilizadas

| Tecnologia | Função |
|---|---|
| **Python** | Linguagem principal do projeto |
| **SQLite** | Armazenamento das leituras |
| **Pandas** | Manipulação e organização dos dados |
| **Plotly** | Criação dos gráficos |
| **Streamlit** | Desenvolvimento do dashboard |
| **HTML/CSS** | Personalização visual da interface |

### Bibliotecas Python

As principais bibliotecas utilizadas são:

```text
pandas
plotly
streamlit
```

> **Observação:** `sqlite3` faz parte da biblioteca padrão do Python e, portanto, não precisa ser instalado separadamente com `pip`.

---

## Estrutura do projeto

A estrutura esperada é:

```text
Atividade/
│
├── app.py
├── simulator.py
├── telemetria.db
├── weg.png
├── senai.png
│
└── .streamlit/
    └── config.toml
```

### Descrição dos arquivos

| Arquivo | Função |
|---|---|
| `app.py` | Aplicação responsável pelo dashboard |
| `simulator.py` | Geração contínua dos dados simulados |
| `telemetria.db` | Banco de dados SQLite utilizado pelo sistema |
| `weg.png` | Logo utilizada no cabeçalho |
| `senai.png` | Logo utilizada no cabeçalho |
| `.streamlit/config.toml` | Configuração visual do Streamlit |

O arquivo `telemetria.db` é utilizado para armazenar as leituras geradas pelo simulador.

---

# Instalação

## 1. Pré-requisito

É necessário possuir o **Python** instalado no computador.

Recomenda-se utilizar uma versão recente do Python 3.

Para verificar se o Python está instalado:

```bash
python --version
```

---

## 2. Instalar as dependências

Abra um terminal dentro da pasta do projeto e execute:

```bash
pip install pandas plotly streamlit
```

As bibliotecas necessárias para o funcionamento do dashboard serão instaladas.

---

# Como executar

O sistema precisa que o **simulador** e o **dashboard** estejam funcionando simultaneamente.

## 1. Iniciar o simulador

Abra um terminal na pasta do projeto e execute:

```bash
python simulator.py
```

O terminal deverá indicar que o simulador está em execução.

O programa passará a gerar novas leituras continuamente e armazená-las no banco de dados.

---

## 2. Iniciar o dashboard

Abra **outro terminal**, também dentro da pasta do projeto, e execute:

```bash
python -m streamlit run app.py
```

O Streamlit deverá abrir o dashboard automaticamente no navegador.

Caso isso não aconteça, acesse manualmente:

```text
http://localhost:8501
```

---

## 3. Utilizar o dashboard

Com os dois programas em execução, o dashboard começará a apresentar os dados gerados pelo simulador.

Na barra lateral é possível controlar:

### Frequência de atualização

Define o intervalo, em segundos, entre as atualizações do dashboard.

### Histórico de leituras

Define a quantidade de registros considerados para a visualização.

### Filtro por servidor

Permite visualizar os dados de:

- Todos os servidores;
- `Servidor_A`;
- `Servidor_B`;
- `Servidor_C`.

Abaixo dos indicadores são apresentados os gráficos e, posteriormente, a tabela com os registros coletados.

---

# Identidade visual

A interface foi personalizada com uma paleta inspirada na identidade visual da **WEG**, utilizando diferentes tons de azul e ciano.

A identidade visual está presente em elementos como:

- Cabeçalho;
- Logos;
- Títulos;
- Indicadores;
- Bordas;
- Gráficos;
- Controles da barra lateral;
- Elementos de destaque.

As logos da **WEG** e do **SENAI** são apresentadas no cabeçalho do dashboard.

A configuração de cores dos componentes nativos do Streamlit é definida no arquivo:

```text
.streamlit/config.toml
```

---

# Banco de dados

O sistema utiliza o **SQLite** para armazenar as leituras dos servidores.

A tabela principal utilizada é:

```text
leituras_servidores
```

Ela contém informações como:

```text
id
timestamp
server_id
temp_CPU
uso_CPU
uso_RAM
latencia
```

O simulador insere novas leituras periodicamente, enquanto o dashboard consulta esses registros para atualizar sua visualização.

---

# Observações

- O `simulator.py` deve permanecer em execução para que novas leituras continuem sendo geradas.
- O `app.py` pode ser executado em um segundo terminal.
- O dashboard depende do banco `telemetria.db` para apresentar os dados.
- As imagens `weg.png` e `senai.png` devem permanecer na pasta principal do projeto.
- O arquivo `.streamlit/config.toml` deve permanecer dentro da pasta `.streamlit`.
- Caso o simulador seja encerrado, o dashboard continuará podendo exibir os dados já armazenados, mas novas leituras deixarão de ser inseridas.

---

# Finalidade acadêmica

Este projeto foi desenvolvido exclusivamente para fins **pedagógicos e avaliativos**, tendo como finalidade aplicar conceitos relacionados à:

- Programação em Python;
- Banco de dados;
- Manipulação de dados;
- Visualização de informações;
- Desenvolvimento de interfaces;
- Monitoramento de dados em tempo real;
- Aplicações voltadas ao contexto de automação e indústria.

---

## Disclaimer

O **frontend e a personalização visual do arquivo `app.py`** foram desenvolvidos e aprimorados com auxílio de **Inteligência Artificial, especificamente o ChatGPT**.

A utilização da IA esteve concentrada principalmente na estruturação e personalização da interface, mantendo o projeto como uma atividade de caráter acadêmico e avaliativo.

---

## Execução rápida

Para facilitar, depois de instalar as dependências, basta utilizar **dois terminais**:

**Terminal 1 — simulador**

```bash
python simulator.py
```

**Terminal 2 — dashboard**

```bash
python -m streamlit run app.py
```

Depois, acesse:

```text
http://localhost:8501
```

---

<p align="center">
  <strong>Projeto acadêmico — CentroWEG | Cibersistemas para Automação | MA77</strong>
</p>
