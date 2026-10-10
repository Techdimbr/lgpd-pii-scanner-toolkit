# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — LGPD PII Scanner Toolkit

**Repositório Oficial:** `https://github.com/Techdimbr/lgpd-pii-scanner-toolkit`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Estrutura Base Canônica Homologada — Aguardando Desenvolvimento da Função  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** LGPD PII Scanner Toolkit
- **Identificador (Slug):** `lgpd-pii-scanner-toolkit`
- **Categoria:** Governança de Dados & Conformidade Regulatória (LGPD)
- **Stack Tecnológica:** Python puro (stdlib), Regex determinístico, SQLite, Pandoc
- **Objetivo Central:** Scanner automatizado para varredura de dados pessoais sensíveis (CPF, RG, cartões, e-mails, endereços) em repositórios, bases de dados e arquivos locais, gerando relatórios de conformidade e matriz de risco regulatório.

### Principais Casos de Uso Previstos
- Varredura estática de repositórios e pastas compartilhadas em busca de vazamentos de CPFs e senhas
- Geração de relatórios de impacto à proteção de dados (RIPD) em formato Markdown e PDF
- Classificação determinística de bases de dados conforme artigos da LGPD (Lei 13.709/2018)

---

## 2. Estrutura Operacional Canônica
Este repositório foi construído sobre a arquitetura canônica **PRJ-TECHDIM-PUBLIC-v1.0.0**:
- `00_AUDITORIA/`: Verificação criptográfica de integridade SHA-256 (`./00_AUDITORIA/verificar_integridade.sh`).
- `01_SOBRE_O_PROJETO/`: Documentação de requisitos, casos de uso e roadmap de desenvolvimento.
- `02_COMO_USAR/`: Procedimentos operacionais padrão (SOP), pré-requisitos e configurações.
- `03_APLICACAO/`: Núcleo de código (`src/`) e suite de testes automatizados (`tests/`).
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Decisões de arquitetura (ADRs) e regras de contexto para agentes de IA.
- `05_VERSOES/`: Controle semântico de versões (`CHANGELOG.md`).
- `06_MIDIA/`: Material de apresentação executiva e ficha técnica.

---

## 3. Instruções Iniciais para Início do Desenvolvimento
Quando for iniciar o desenvolvimento da função específica:
1. **Ativação e Validação Inicial:**
   ```bash
   ./iniciar.sh
   ```
   *O bootstrap verificará o ambiente Debian/Linux, dependências e ativará os pre-commit hooks de proteção Zero Leaks.*

2. **Implementação do Core:**
   - Codifique a lógica da solução dentro do diretório `03_APLICACAO/src/`.
   - Mantenha o código modular, desacoplado e documentado.

3. **Criação e Execução de Testes:**
   - Escreva testes unitários e de integração em `03_APLICACAO/tests/`.
   - Valide a execução com:
     ```bash
     python3 -m unittest discover 03_APLICACAO/tests
     ```

4. **Auditoria de Integridade Criptográfica:**
   - Antes de efetuar novos commits de versão, atualize o manifesto SHA-256 executando:
     ```bash
     ./00_AUDITORIA/verificar_integridade.sh --gerar
     ```

---

## 4. Diretrizes e Regras de Negócio a Preencher
<!-- PREENCHA ESTA SEÇÃO COM AS DIRETRIZES ESPECÍFICAS DA FUNÇÃO QUANDO FOR INICIAR O DESENVOLVIMENTO -->
> **[ESPAÇO RESERVADO PARA DETALHAMENTO DA FUNÇÃO]**
> - Inserir aqui os casos de uso detalhados;
> - Inserir aqui parâmetros de entrada, saída e esquemas de dados;
> - Inserir requisitos específicos de bibliotecas e integração de APIs externas;
> - Inserir regras de segurança específicas para o ambiente de execução.
