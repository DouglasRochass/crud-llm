# Geração Automática de Queries SQL com LLM

Este projeto foi desenvolvido como um primeiro experimento para entender, na prática, como utilizar modelos de linguagem (LLM) para gerar queries SQL automaticamente a partir de perguntas em linguagem natural, inspirado no vídeo do Eduardo Inocencio.

## Descrição

A aplicação conecta um modelo de IA generativa (Google Gemini) a um banco de dados MySQL, permitindo que o usuário faça perguntas ou comandos simples (como inserir, consultar, deletar ou atualizar dados) e receba a query SQL correspondente, que é então executada automaticamente no banco de dados.

O objetivo principal é tornar a interação com bancos de dados mais acessível, mesmo para quem não domina SQL, e explorar o potencial dos LLMs na automação de tarefas do dia a dia.

## Principais Funcionalidades

- Geração de queries SQL a partir de perguntas em linguagem natural.
- Execução automática das queries no banco de dados MySQL.
- Interface interativa via terminal para inserir, consultar, deletar e atualizar dados.
- Limpeza automática do output para garantir que apenas a query SQL seja executada.
- Pipeline modular utilizando LangChain e integração com o modelo Google Gemini.

## Como funciona

1. **Usuário faz uma pergunta ou comando** (por exemplo: "Quantos usuários existem na tabela?").
2. O sistema utiliza o modelo Gemini para gerar a query SQL correspondente.
3. A query é limpa para remover eventuais marcações de markdown.
4. A query é executada no banco de dados e o resultado é exibido ao usuário.

## Requisitos

- Python 3.10+
- MySQL em execução e acessível localmente
- Conta e chave de API do Google Gemini
- Variáveis de ambiente configuradas (`GOOGLE_API_KEY` e `DB_PASSWORD`)
- Bibliotecas:
  - langchain
  - langchain_community
  - langchain_google_genai
  - python-dotenv
  - mysql-connector-python

## Instalação

1. Clone este repositório.

2. Instale as dependências:
   ```bash
   pip install langchain langchain_community langchain_google_genai python-dotenv mysql-connector-python
Configure as variáveis de ambiente em um arquivo .env:

text
GOOGLE_API_KEY=SuaChaveAqui
DB_PASSWORD=SenhaDoMySQL
Certifique-se de que o banco MySQL está rodando e acessível.

Como usar
Execute o script principal:

bash
python teste.py

text

Siga as instruções no terminal para escolher a ação desejada:

- Inserir dados
- Consultar dados
- Deletar dados
- Atualizar dados

Digite sua pergunta ou comando, e o sistema irá gerar, limpar e executar a query automaticamente.

## Estrutura do Projeto

- `teste.py`: Script principal com toda a lógica de integração entre LLM, banco de dados e interface interativa.

## Observações

- Este projeto tem caráter experimental e educativo, sendo ideal para quem deseja dar os primeiros passos em IA generativa aplicada a bancos de dados.
- Recomenda-se não utilizar em ambientes de produção sem as devidas validações de segurança, pois queries são geradas e executadas automaticamente.

## Inspiração

Projeto inspirado pelo vídeo do Eduardo Inocencio sobre como criar queries automáticas com LLM, combinando aprendizado prático e exploração de novas tecnologias.
