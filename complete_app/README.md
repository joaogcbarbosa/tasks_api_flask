<h1>API gerenciadora de tarefas em Python com auxílio do framework Flask</h1>
<ul>
    <li>A API está ligada a um banco de dados SQLite, o qual possui as tabelas Pessoa e Tarefa;</li>
    <li>A API permite listar todas as tarefas e também incluir novas;</li>
    <li>Através do Id, a API permite consultar, alterar status ou deletar uma tarefa;</li>
    <li>Para todas consultas e alterações acima, foi criada uma interface básica com HTML, CSS e JavaScript, com o objetivo de tornar a interação com os dados mais atrativa;</li>
</ul>
<p><strong>*A API não está seguindo o modelo REST. Os formulários HTML permitem apenas os métodos HTTP GET e POST, portanto, o código foi todo implementado baseando-se nesses dois métodos, mesmo que em momentos a lógica por trás seja para PUT e DELETE.*</strong></p>

