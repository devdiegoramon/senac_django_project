1. Criar uma Nova Branch a partir de dev

Para começar, você e seus colaboradores devem sempre criar uma nova branch a partir da dev (que é onde todo o desenvolvimento ocorre).

Passo 1: Certifique-se de que você está na branch dev e que ela está atualizada:

bash

git checkout dev
git pull origin dev

Passo 2: Agora, crie uma nova branch para a funcionalidade em que você vai trabalhar. O nome da branch deve ser descritivo para que todos saibam o que está sendo feito nela. Exemplo de nomenclatura:

    feature/descrição-da-nova-funcionalidade
    bugfix/corrigir-erro-no-login
    hotfix/corrigir-erro-crítico

Então, para criar uma nova branch, use o comando:

bash

git checkout -b feature/nova-funcionalidade

Isso cria e já muda para a nova branch.
2. Fazer Commits Semânticos

Os commits semânticos ajudam a tornar o histórico do Git mais legível e organizado, o que facilita a manutenção do projeto e a colaboração entre a equipe.

Formato do commit semântico:

scss

tipo(escopo): mensagem

    tipo: Define a natureza do commit (pode ser feat, fix, docs, chore, refactor, etc.).
    escopo (opcional): É uma descrição curta de qual parte do código foi afetada (ex: auth, database, ui).
    mensagem: Uma descrição clara e objetiva do que foi feito.

Exemplos de commits semânticos:

    Adicionar uma nova funcionalidade de login:

    bash

git commit -m "feat(auth): adicionar login com Google"

Corrigir um erro no formulário de login:

bash

git commit -m "fix(auth): corrigir erro no login com e-mail inválido"

Atualizar a documentação:

bash

git commit -m "docs: atualizar readme com instruções de configuração"

Refatorar código na parte de autenticação:

bash

    git commit -m "refactor(auth): melhorar validação de senha"

O objetivo é que qualquer pessoa lendo o histórico de commits consiga entender rapidamente o que foi feito e por quê.
3. Subir a Branch para o Repositório Remoto

Após fazer seus commits locais, o próximo passo é enviar sua branch para o repositório remoto para que outros possam acessar e colaborar.

Passo 1: Envie sua branch para o repositório remoto (suba sua branch):

bash

git push origin feature/nova-funcionalidade

Substitua feature/nova-funcionalidade pelo nome da sua branch.
4. Criar um Pull Request (PR)

Após subir a branch para o repositório remoto, vá até o GitHub e crie um Pull Request (PR) para integrar as mudanças da sua branch de volta para a dev. Isso permite que outros revisem seu código antes de mesclar.

Passo 1: Vá até o repositório no GitHub e clique em "Compare & Pull Request" para a sua branch.

Passo 2: Escreva uma descrição do que foi feito na sua branch e clique em "Create Pull Request".
5. Dicas para Colaboradores

Aqui estão algumas boas práticas para os colaboradores:

    Sempre faça git pull antes de começar a trabalhar: Antes de iniciar qualquer trabalho, garanta que sua branch dev esteja atualizada para evitar conflitos de merge:

    bash

git checkout dev
git pull origin dev

Crie uma nova branch para cada tarefa: Não trabalhe diretamente na dev ou main. Crie sempre uma nova branch com um nome claro e descritivo da funcionalidade ou bug que está sendo tratado.

bash

git checkout -b feature/nova-funcionalidade

Commits pequenos e frequentes: Evite fazer commits grandes. Comite frequentemente para que as mudanças sejam facilmente rastreáveis e não sobrecarreguem outros colaboradores.

Sempre faça git pull antes de git push: Antes de enviar suas alterações, sempre faça um git pull para garantir que sua branch local esteja atualizada com a remota.

bash

    git pull origin dev

    Crie Pull Requests para revisão: Depois de terminar uma tarefa ou funcionalidade, envie um Pull Request para a branch dev. Isso facilita a revisão do código e a detecção de erros antes de integrar à branch principal.

    Respeite o fluxo semântico de commits: Como mencionei antes, utilize mensagens de commit semânticas para manter um histórico claro.

    Resolução de Conflitos: Caso haja conflitos ao fazer o merge, você precisará resolvê-los manualmente. Após a resolução, comite as mudanças e envie a branch novamente.

    Use tarefas pequenas e bem definidas: Evite começar tarefas grandes sem dividi-las em subtarefas pequenas. Isso facilita o trabalho em equipe e a revisão de código.

Resumo do Fluxo de Trabalho:

    Inicie o projeto sempre da branch dev.
    Crie uma nova branch para trabalhar em uma nova funcionalidade ou correção.
    Faça commits semânticos e frequentemente.
    Suba a branch para o repositório remoto.
    Crie um Pull Request para que os colaboradores revisem as mudanças.
    Revise e mescle os Pull Requests com o código da dev.