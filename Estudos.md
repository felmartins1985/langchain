### 1. Prompt Templates
Prompt templates são estruturas que facilitam a geração de prompts personalizados para modelos de linguagem, contendo variáveis que podem ser preenchidas dinamicamente. Eles são especialmente úteis em aplicações que demandam a personalização de mensagens ou a automação de tarefas repetitivas.

### 1.1 Composição de prompts com LangChain
Além de criar templates simples, a LangChain suporta a composição de prompts, permitindo a união de diferentes partes para formar prompts complexos. Isso é útil para criar diálogos ou cenários mais elaborados em chats ou outras interações baseadas em texto.

### 2. ChatPromptTemplate
O ChatPromptTemplate é uma classe do LangChain que serve para criar templates de prompts estruturados especificamente para modelos de chat.
### 2.1 LLMChain
O LLMChain é uma classe fundamental do LangChain que combina um modelo de linguagem (LLM) com um template de prompt. Ele serve para:

Estruturar interações com LLMs: Permite definir um formato específico para as perguntas/comandos que serão enviados ao modelo
Reutilização de prompts: Você pode criar templates que podem ser reutilizados com diferentes parâmetros
Padronização: Garante que as interações com o LLM sigam um padrão consistente.
### 2.2 SimpleSequentialChain
O SimpleSequentialChain é usado para encadear múltiplas operações de forma sequencial. Ele serve para:

Automatizar fluxos de trabalho: Executa uma série de chains em sequência
Passar resultados automaticamente: A saída de uma chain se torna a entrada da próxima
Criar pipelines complexos: Permite construir sistemas que executam múltiplas tarefas relacionadas

obs: Ele utiliza o output da operação anterior como paramêtro do prompt atual.