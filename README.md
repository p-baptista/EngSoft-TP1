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

## Versão Revisada do Backlog da Sprint
#### História #1: Como usuário, quero poder fazer login no sistema por uma landing page e redefinir minha senha caso a esqueça
**Tarefas e Responsáveis:**
* [Back]: Criar lógica de login e logout - Matheus
* [Back]: Criar lógica e middlewares de token JWT, autenticação de role, etc. - Pedro
* [Back]: Criar lógica de recuperação de senha através de código enviado por email - Pedro
* [Front]: Página estática de login - César
* [Front]: Conexão da página de login com o back - César
* [Front]: Página estática de esqueci minha senha - César
* [Front]: Conexão da página de esqueci minha senha com o back - César

#### História #2: Como usuário, quero poder ver meu perfil, incluindo os jogos na minha biblioteca e suas reviews
**Tarefas e Responsáveis:**
* [Back]: Criar rotas para listagem de jogos por usuário - Matheus
* [Front]: Página estática da Home Page (com listagem dos jogos) - César
* [Front]: Conexão da Home Page com o back - Pedro
* [Front]: Página de jogo (com ou sem review) - César
* [Front]: Conexão do perfil de jogo com o back - Pedro

#### História #3: Como usuário, quero visualizar o perfil de outros usuários, adicioná-los à lista de amigos e ver suas bibliotecas/reviews
**Tarefas e Responsáveis:**
* [Back]: Criar rotas retornando outros usuários - Matheus
* [Front] Criar botão de procura na Home Page - César
* [Front] Criar lógica de pesquisa de usuários - Pedro
* [Front] Criar página de perfil de outros usuários - César

#### História #4: Como usuário, quero poder adicionar um jogo à minha biblioteca de jogos a partir da lista de jogos disponíveis e fazer uma review desse jogo, vendo a nota média de um jogo a partir de todas as reviews do sistema
**Tarefas e Responsáveis:**
* [Back]: Criar rota para seleção ou adição de jogos para review - Matheus
* [Back]: Adicionar review do jogo no banco de dados - Pedro
* [Front] Criar página para adição de review - César
* [Front] Criar página para edição de review - César

## Diagramas UML
![alt text](<readme_images/diagrama_de_classe.png>)
![alt text](<readme_images/diagrama_de_seq.png>)
