Esse projeto é uma simulação da visualização e monitoramento em tempo real de dados na indústria. Mais especificadamente, ele mostra dados simulados de 3 servidores distintos, mostrando dados como temperatura da CPU, uso da CPU, uso da memória RAM e latência do servidor.

Feito com cunho pedagógico e avaliativo na matéria de "Desenvolvimento de Interfaces para Visualização de Dados", matéria lecionada pelo docente Fabiano da Silva Luiz, para o curso de Cibersistemas para Automação, turma MA77, no CentroWEG, em Jaraguá do Sul, SC.

Como executar

Baixe a pasta 'Atividade' do projeto
Rode o arquivo simulator.py utilizando o comando 'python simulator.py'
Abra outro terminal e rode o arquivo app.py com 'python -m streamlit run app.py'
O mesmo abrirá diretamente no navegador. Se não abrir, abra manualmente e digite: "localhost:8501"
Ao adentrar, você verá o dashboard atualizando em tempo real com os dados simulados pelo arquivo 'simulator.py'
Caso deseje, modifique as configurações e observe os gráficos gerados abaixo.

Processo de Instalação

Instale as bibliotecas necessárias (pip install), incluindo:
- sqlite3
- pandas
- plotly.express
- streamlit

Disclaimer: Frontend do código app.py modificado com auxílio de IA, mais especificadamente o ChatGPT.

