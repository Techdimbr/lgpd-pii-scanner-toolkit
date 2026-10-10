# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — LGPD PII Scanner Toolkit

**Repositório Oficial:** `https://github.com/Techdimbr/lgpd-pii-scanner-toolkit`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** LGPD PII Scanner Toolkit
- **Identificador (Slug):** `lgpd-pii-scanner-toolkit`
- **Categoria:** Governança de Dados & Conformidade Regulatória (LGPD Lei 13.709/2018)
- **Stack Tecnológica:** Python 3 (stdlib puro), Regex determinístico, SQLite3, Algoritmo Módulo 11 (CPF), Algoritmo de Luhn
- **Objetivo Central:** Fornecer um scanner offline e determinístico para rastrear e inventariar dados pessoais e sensíveis em repositórios, bases de dados e diretórios locais, calculando riscos regulatórios da ANPD e gerando relatórios RIPD.

### Casos de Uso Reais
1. **Auditoria de Conformidade em Arquivos Antigos:** Varredura de pastas de rede legadas em busca de planilhas de RH e cadastros com CPFs e dados médicos expostos.
2. **Prevenção de Vazamento em Código-Fonte:** Pre-commit hook para barrar commits contendo dados de teste com CPFs reais de clientes.
3. **Mapeamento de Dados para o DPO:** Inventário automatizado para embasar o Relatório de Impacto à Proteção de Dados (RIPD).

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── lgpd_scanner.py                    # Motor de varredura, validação de dígitos e mascaramento
├── pii_rules.py                       # Expressões regulares e regras de negócio para dados brasileiros
├── ripd_generator.py                  # Gerador de relatório de conformidade em formato Markdown
└── database.py                        # Persistência de achados em tabela SQLite segura
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS DO SCANNER LGPD -->
- [x] Algoritmo matemático de validação de CPF (rejeição de 111.111.111-11 e cálculo dos 2 dígitos verificadores);
- [x] Mascaramento de dados em memória para privacidade do relatório;
- [ ] Suporte a varredura dentro de arquivos compactados (.zip, .tar.gz);
- [ ] Exportação do RIPD em PDF através do Pandoc.
