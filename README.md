# EngSoft-TP1

## Escopo do Projeto
Teremos uma plataforma para usuários registrarem, avaliarem e compartiharem suas experiências com videogames. 

O usuário poderá adicionar jogos à sua lista de "jogados" ou "quero jogar", e também poderá fazer reviews dos games jogados, dando 0 a 5 estrelas e fazendo um breve comentário. Além disso, o usuário poderá seguir outras pessoas, e ter acesso a biblioteca de jogos e às avaliações dos seus amigos.

Também será possível entrar no sistema como administrador, para adicionar games ao banco de dados e gerenciar usuários.

Cada jogo terá uma página que sumariza todas as avaliações em uma nota global e apresenta as reviews.

Gostaríamos também de implementar uma interface de usuário limpa e que evidencie principalmente a capa e as artes dos jogos disponíveis.


## Equipe
* César de Paula Morais (2021031521): Frontend
* Matheus Grandinetti Barbosa (2021067496): Backend
* Pedro Henrique Fernandes Baptista (2021031610): Fullstack

## Tecnologias Utilizadas
Utilizaremos o framework Django, na linguagem Python, para o backend, e HTML/CSS/JavaScript para o frontend. O banco de dados do framework, por default, é SQLite.
Também utilizaremos o GitHub, tecnologia obrigatória do trabalho, para repositório de código.

## Histórias
### História #1: Login e Esqueci minha senha
- Tarefas e Responsáveis:
* [Back]: Criar rotas para listagem de jogos por usuário
* [Front]: Página estática do perfil
* [Front]: Conexão do perfil com o back
* [Front]: Página estática da Home Page (com listagem dos jogos)
* [Front]: Conexão da Home Page com o back
* [Front]: Página de jogo (com ou sem review)
* [Front]: Conexão do perfil de jogo com o back

### História #2: Perfil e biblioteca de jogos
- Tarefas e Responsáveis:
* [Back]: Criar rotas para listagem de jogos por usuário
* [Front]: Página estática do perfil
* [Front]: Conexão do perfil com o back
* [Front]: Página estática da Home Page (com listagem dos jogos)
* [Front]: Conexão da Home Page com o back
* [Front]: Página de jogo (com ou sem review)
* [Front]: Conexão do perfil de jogo com o back

### História #3: Visualizar outros perfis
- Tarefas e Responsáveis:
* [Back]: Criar rotas retornando outros usuários
* [Front] Criar botão de procura na Home Page
* [Front] Criar lógica de pesquisa de usuários
* [Front] Criar página de perfil de outros usuários

### História #3: Visualizar outros perfis
- Tarefas e Responsáveis:
* [Back]: Criar rotas retornando outros usuários
* [Front] Criar botão de procura na Home Page
* [Front] Criar lógica de pesquisa de usuários
* [Front] Criar página de perfil de outros usuários

### História #4: Adicionar review
- Tarefas e Responsáveis:
* [Back]: Criar rota para seleção ou adição de jogos para review
* [Back]: Adicionar review do jogo no banco de dados
* [Front] Criar página para adição de review
* [Front] Criar página para edição de review