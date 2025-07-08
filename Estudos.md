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

### 2.3 LCEL (LangChain Expression Language)
LCEL é uma linguagem declarativa introduzida no LangChain para criar chains de forma mais simples, legível e eficiente. É a abordagem mais moderna e recomendada atualmente.

Por que migrar do LLMChain para o LCEL?

- Orquestração declarativa: Você descreve o fluxo desejado, e o LangChain otimiza a execução.
- Melhor desempenho: Com suporte a execuções paralelas, processos assíncronos e gerenciamento de estado mais simples.
- Maior clareza: A orquestração se torna mais transparente, facilitando a compreensão do que acontece a cada passo da cadeia de processamento.

LCEL é fundamental para construir cadeias de processamento robustas e eficientes no LangChain, oferecendo suporte a funcionalidades avançadas como streaming, execução paralela e observabilidade. Utilizando LCEL, desenvolvedores podem criar e adaptar cadeias de processamento para atender às necessidades específicas de suas aplicações, desde a prototipagem até a produção.

Características principais do LCEL
Suporte a streaming: melhora o tempo até a primeira saída, sendo ideal para processamento em tempo real.
Suporte assíncrono: permite execução tanto síncrona quanto assíncrona, adequada para prototipagem e produção.
Execução paralela otimizada: executa etapas paralelas automaticamente para reduzir a latência.
Retentativas e alternativas: melhora a confiabilidade em escala com configurações de retentativa e alternativa.
Acesso a resultados intermediários: permite monitoramento e depuração em cadeias complexas.
Esquemas de entrada e saída: facilita a validação com esquemas Pydantic e JSONSchema.
Integração com Langsmith e Langserve: oferece observabilidade e facilita a implantação.

### 3 OutputParser
O output parser no LangChain é uma ferramenta essencial para processar a saída dos modelos de linguagem (LLMs), transformando respostas em formatos variáveis em estruturas de dados consistentes e utilizáveis. Isso é crucial, especialmente em cenários onde é necessário que máquinas processem essas respostas de forma automatizada (como a saída de uma API).

### 3.1 DatetimeOutputParser

O DatetimeOutputParser é outro exemplo útil para transformar texto em dados de data e hora. No entanto, desafios podem surgir se o formato de data e hora esperado não for diretamente suportado pelo parser.

### 3.2 JsonOutputParser e PydanticOutputParser
O JsonOutputParser é particularmente útil quando a saída necessita ser mapeada em diferentes categorias ou itens. Suporta classes Pydantic, facilitando a transformação da saída do LLM em objetos estruturados e prontos para uso em aplicações. Isso é extremamente útil para sumarizar dados complexos, como tickets de suporte, em categorias distintas como Issue, Root Causes e Resolution.

- Exemplo:
parseador= JsonOutputParser(pydantic_object=Destino)
modelo_cidade= PromptTemplate(
    template="""Sugira uma cidade dado meu interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=['interesse'],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()})

-> parseador.get_format_instructions(): gera automaticamente instruções que dizem ao modelo da OpenAI para retornar a resposta no formato JSON esperado.

### 3.3 StrOutputParser()
O StrOutputParser() é um parser que:

Converte para string: Transforma a resposta do modelo em uma string limpa
Remove metadados: Elimina informações técnicas desnecessárias
Formato simples: Retorna apenas o conteúdo textual da resposta

### 4 ChatPromptTemplate.from_messages()
Serve para criar um "prompt estruturado" para um modelo de chat a partir de uma lista de mensagens simulando uma conversa.
Permite montar esse prompt como uma sequência de mensagens, de forma organizada, podendo incluir variáveis dinâmicas no meio do processo.