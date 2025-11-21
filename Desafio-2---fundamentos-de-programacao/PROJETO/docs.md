## Documentação — Sistema de Sessões de Reforço Escolar

 # 1.0 Visão Geral

Este projeto é uma aplicação em Python executada pelo terminal com o objetivo de registrar, visualizar, atualizar e excluir sessões de reforço escolar.  
As informações são armazenadas no arquivo `sessoes.json`, garantindo persistência dos dados entre execuções.



#  2.0 Estrutura do Projeto:

sessoes.py -> código principal do sistema
sessoes.json -> armazenamento das sessões (gerado automaticamente)


#  2.1 Estrutura do arquivo `sessoes.json`

Cada sessão é salva no seguinte formato:
 json
{
  "id": 1,
  "aluno": "Nome do Aluno",
  "professor": "Nome do Professor",
  "materia": "Matéria",
  "data": "DD/MM/AAAA"
}


 # 3. Funcionamento do Sistema

Ao iniciar o programa, um menu interativo é exibido:

    1 - Cadastrar Sessão
    2 - Listar Sessão
    3 - Atualizar Sessão
    4 - Excluir Sessão
    5 - Sair

# 3.1 Ações do menu

    Opção	Descrição
    1 - Cadastra uma nova sessão e salva no JSON
    2 - Lista todas as sessões existentes
    3 - Permite atualizar os dados de uma sessão pelo ID
    4 - Remove uma sessão pelo ID
    5 - Encerra o sistema

# 4. Público-Alvo

    Professores/voluntários de reforço escolar

    Instituições educacionais

    Estudantes de Python aprendendo CRUD

    Projetos acadêmicos e escolares

# 5. Licença

Projeto de uso livre. Pode ser modificado ou ampliado conforme necessidade.