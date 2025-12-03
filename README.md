Desafio-2---fundamentos-de-programacao
Plataforma de apoio ao reforço escolar

Alunos: Ana Beatriz de Oliveira; 
Bruna Ferreira; 
Drielly Santiago dos Santos; 
Elisa Martins; 
Hilton Resende; 
Fernando Araújo;
Maria Eduarda Vasconcelos;

Líder: Bruna Ferreira Tiburtino

Desafio Escolhido: Desafio 2 == Plataforma de Apoio ao reforço escolar ==

** Separação de tarefas: 
CRUD Alunos = Ana Beatriz e Maria Eduarda
CRUD Professores = Bruna, Fernando e Elisa
CRUD Sessões de Reforço = Drielly e Hilton;
Relatórios, integração dos CRUDs, Lista de disciplinas = Bruna 


 Sistema de Cadastro de Reforço Escolar – CRUD em Python


 Descrição Geral

Este projeto é um sistema completo de gestão escolar desenvolvido em Python, utilizando operações CRUD (Criar, Ler, Atualizar e Deletar) para organizar informações de professores, alunos e sessões de atendimento.
Todos os dados são armazenados em arquivos JSON, garantindo persistência mesmo após fechar o programa.

** Objetivo do Sistema **

O sistema foi criado para resolver um problema comum no ambiente escolar: a falta de organização e padronização no registro de informações importantes.

Ele permite que escolas, professores e estudantes:

Cadastrem informações com segurança

Organizem dados de forma digital

Evitem perda de registros em papel

Acessem informações rapidamente

Gerem relatórios de forma simples

O público-alvo inclui professores, alunos, coordenadores e equipes pedagógicas.


** Funcionalidades Principais **

📁 1. CRUD de Professores

Cadastro completo com ID automático

Nome, matrícula e disciplina

Lista de disciplinas previamente definidas

Edição e exclusão de registros

Listagem organizada de professores


👩‍🎓 2. CRUD de Alunos

Cadastro de informações básicas

Associação do aluno a uma disciplina

Alteração e exclusão

Exibição dos alunos cadastrados


🕒 3. CRUD de Sessões

Registro de sessões entre aluno e professor

Seleção da disciplina da sessão

Registro de data e observações

Consulta de histórico completo


📄 4. Relatórios

Relatórios automáticos com base nos arquivos JSON

Visualização clara das informações salvas

Facilitam apresentações, análises e revisões


💾 Persistência de Dados

Todo o armazenamento é feito em arquivos .json, o que garante: Facilidade de manutenção, Portabilidade, Leitura humana e Compatibilidade com outros sistemas

Arquivos utilizados:
alunos.json  
professores.json  
sessoes.json

📂 Estrutura do Projeto
📦 projeto-Desafio2
 ┣ 📁Alunos
 ┃ ┣ alunos.py
 ┃ ┣ alunos.json 
 ┃ ┗ arquivos.py
 ┃ ┗ main.py 
 ┃ ┗ menu_alunos.py
 ┣ 📁 professores
 ┃ ┣ professores.py
 ┃ ┣ arquivos.py
 ┃ ┗ main.py
 ┃ ┗ menu_professores.py
 ┃ ┗ professores.json
   📁Relatórios
 ┃ ┣ gerar_relatórios.py
 ┃ ┣ main.py
 ┃ ┗ menu_relatórios.py
 ┣ 📁 Sessões
 ┃ ┗ main.py
 ┃ ┣ sessao_reforco_escolar.py
 ┃ ┗ sessoes.json
 ┃ 
 ┣ menu_principal.py
 ┗ README.md
 ┗ disc.py


** Instruções de Instalação e Execução **
🔽 1. Baixar o Projeto do GitHub

Opção 1 — Via Git (recomendado):

git clone https://github.com/seu-usuario/seu-repositorio.git


Opção 2 — Download ZIP:

Entre no repositório

Clique em Code → Download ZIP

Extraia a pasta no computador

📦 2. Instalar Dependências

Este projeto não usa bibliotecas externas.
Basta ter Python 3.9 ou superior instalado.

Verificar versão:

python --version

▶️ 3. Executar o Sistema

No terminal:

python main.py


ou

python3 main.py


O menu principal aparecerá com as opções:

Professores

Alunos

Sessões

Relatórios

Sair

🛠️ Tecnologias Utilizadas

Python 3

JSON para armazenamento

Estrutura modular (arquivos separados para organização)

Programação estruturada


📌 Observações Finais

✔ Código simples e fácil de entender
✔ Ideal para aprendizagem de programação
✔ Segue boas práticas de organização de projeto
✔ Totalmente editável e expansível
