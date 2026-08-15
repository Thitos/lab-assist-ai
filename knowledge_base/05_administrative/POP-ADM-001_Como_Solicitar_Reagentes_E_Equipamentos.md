# BioLab Research Center

# POP-ADM-001 - Solicitação e Aquisição de Reagentes e Equipamentos

## Informações do documento

|**Campo**|**Valor**|
|---|---|
|Código|POP-ADM-001|
|Categoria|Procedimento Administrativo|
|Setor|Gestão & Compras|
|Nível de Biossegurança|Não Aplicável|
|Responsável|Dra. Helena Vasconcelos, Head de Suprimentos|
|Revisão Técnica|Dr. Carlos Eduardo Buarque, Diretor Administrativo-Financeiro|
|Versão|3.0|
|Data da revisão|Agosto/2026|
|Palavras-chave|Fluxo de Compras, Requisição de Insumos, Validação Orçamentária, Homologação de Fornecedores, LIMS, Cadeia de Suprimentos|

# POP-ADM-001: Procedimento Operacional Padrão para Solicitação e Aquisição de Reagentes e Equipamentos

## 1. Objetivo e Escopo

Este documento estabelece o fluxo oficial de requisição, análise, validação orçamentária e autorização final para a aquisição de reagentes, consumíveis e bens de capital (equipamentos) no **BioLab Research Center**. Este procedimento visa garantir a transparência fiscal, a conformidade com os orçamentos de projetos vigentes (FAPESP, FINEP, CNPq e parcerias privadas) e a manutenção da infraestrutura necessária para as rotinas de alta performance do centro.

A aplicação deste POP é obrigatória para todos os pesquisadores de bancada, pós-doutorandos, chefes de laboratório e assistentes administrativos vinculados a quaisquer dos blocos técnicos e operacionais da instituição.

## 2. Responsabilidades e Atores do Processo

Para o correto funcionamento do ecossistema de compras, ficam designados os seguintes papéis:

- **Solicitante (Pesquisador/Analista):** Identificar a necessidade técnica, realizar o levantamento descritivo do insumo e abrir o processo no sistema integrado.
- **Gestor de Patrimônio e Suprimentos (Almoxarifado):** Verificar a disponibilidade imediata em estoque e validar as especificações de mercado dos fornecedores.
- **Diretor de Administração e Infraestrutura (Setor Administrativo):** Avaliar a viabilidade orçamentária, rubricas disponíveis no projeto de destino e conformidade fiscal.
- **Coordenação Científica:** Emitir o parecer de mérito científico e a autorização de alta alçada para a liberação financeira do pedido.

## 3. Fluxo de Trabalho Passo a Passo

### Passo 3.1: Identificação da Necessidade e Pré-Verificação

1. O pesquisador de bancada, ao constatar a necessidade de um reagente para a execução de protocolos como o **POP-RNA-001** ou **POP-SEQ-002**, deve primeiramente consultar a lista de estoque físico atualizada através do documento **LST-ADM-002**.
2. Caso o insumo não esteja disponível ou tenha atingido o ponto de recompra mínimo, o solicitante deve coletar os dados técnicos necessários para o preenchimento da requisição: _CAS Number_, grau de pureza (ex: Grau Biologia Molecular, P.A.), nome do fabricante, código do catálogo internacional e as exigências térmicas de transporte (cadeia de frio).
3. Para equipamentos (bens de capital), o solicitante deve redigir um Termo de Referência Técnico simplificado contendo as especificações mínimas necessárias (ex: taxa de rampa para termocicladores, faixas espectrais para espectrofotômetros), justificando o ganho metodológico para as linhas de pesquisa do BioLab.

### Passo 3.2: Abertura da Solicitação no Sistema LIMS/ERP

1. O solicitante deve acessar o módulo de compras do sistema ERP/LIMS integrado do BioLab utilizando suas credenciais institucionais unívocas.
2. Selecionar o tipo de requisição: **[Insumo de Consumo Corrente]** ou **[Ativo Permanente/Equipamento]**.
3. Preencher todos os campos obrigatórios do formulário digital:
	- **Centro de Custo / Código do Projeto:** Inserir o número de registro do projeto de pesquisa financiador (ex: Processo FAPESP 2024/XXXXX-X).
	- **Justificativa Técnica:** Explicar sucintamente a aplicação do item (ex: "Aquisição de kit magnético AMPure XP para purificação de bibliotecas NGS de solo conforme demandas do **POP-SEQ-001**").
	- **Especificação Detalhada:** Anexar a ficha técnica do fabricante ou os links de catálogo oficiais para evitar inconformidades na cotação.
4. Submeter o formulário. O sistema gerará automaticamente um número de protocolo sequencial (ex: REQ-2026-1402) e notificará o Setor de Suprimentos.

### Passo 3.3: Triagem de Estoque e Cotação de Mercado

1. O Setor de Suprimentos recebe a requisição e realiza uma dupla checagem no estoque central (**LST-ADM-001** / **LST-ADM-002**) para certificar-se de que não há lotes excedentes em outros blocos que possam ser remanejados.
2. Validada a real necessidade de compra, a Gestão de Suprimentos dispara solicitações de orçamento para no mínimo 03 (três) distribuidoras homologadas constantes no catálogo oficial de fornecedores da instituição (**LST-ADM-003**).
3. As propostas comerciais recebidas devem discriminar obrigatoriamente: preço unitário, impostos incidentes (IPI, ICMS, ST), prazo de entrega real, validade do lote (mínimo de 12 meses para enzimas e kits) e as condições logísticas especiais (ex: transporte em gelo seco).
4. O Setor de Suprimentos anexa o mapa comparativo de preços ao processo digital no LIMS e encaminha o processo para a próxima fase.

### Passo 3.4: Validação Orçamentária e Fiscal

1. O processo é direcionado ao Setor Administrativo, sob a responsabilidade do Diretor de Administração e Infraestrutura.
2. O analista administrativo realiza a conferência do saldo financeiro da rubrica indicada pelo pesquisador (ex: Rubrica de Material de Consumo ou Material Permanente).
3. **Regra de Bloqueio:** Se o valor total das propostas ultrapassar o saldo disponível na dotação orçamentária do projeto correspondente, a solicitação é travada automaticamente pelo sistema e devolvida ao solicitante para readequação de volumes ou troca de fonte de financiamento.
4. Estando o saldo positivo e em conformidade com as regras de prestação de contas das agências de fomento, o Setor Administrativo insere a certidão de reserva orçamentária no processo e o carimba como **[Aprovado Administrativamente]**.

### Passo 3.5: Autorização Final e Homologação Científica

1. O processo consolidado (justificativa + mapa de cotações + reserva de saldo) é enviado para a fila de deliberação da Coordenação Científica do BioLab.
2. O Coordenador Científico avalia o mérito do pedido, analisando se a aquisição está alinhada com os cronogramas de entrega das teses, dissertações e relatórios parciais do centro.
3. Para compras acima de R$ 50.000,00 (bens de capital ou grandes lotes de reagentes de sequenciamento), é exigida a assinatura digital qualificada de dois membros do comitê científico técnico.
4. Com o despacho favorável da Coordenação Científica, o status da requisição no LIMS é alterado para **[Autorizado para Emissão de Pedido de Compra]**.

```
[Pesquisador] Identifica Necessidade e Abre REQ no LIMS
      │
      ▼
[Suprimentos] Triagem de Estoque e Coleta 3 Cotações
      │
      ▼
[Administrativo] Valida Rubrica e Saldo do Projeto
      │
      ▼
[Coord. Científica] Emite Parecer de Mérito e Assinatura Final
      │
      ▼
[Compras] Emite Ordem de Compra e Envia ao Fornecedor
```

## 4. Emissão da Ordem de Compra e Recebimento

1. Após a autorização final, o Setor de Suprimentos converte a requisição em uma Ordem de Compra (OC) oficial do BioLab e a envia ao fornecedor vencedor.
2. No ato da entrega física no recebimento de cargas do Bloco A, o técnico conferente deve confrontar a Nota Fiscal com a OC e verificar as condições de temperatura das caixas térmicas utilizando termômetros infravermelhos.
3. Insumos biológicos refrigerados ou congelados devem ser guardados imediatamente em suas respectivas zonas de armazenamento descritas no **LST-ADM-002**, e a respectiva baixa ou entrada de estoque deve ser registrada no LIMS para concluir o ciclo do processo administrativo.

## 5. Referências Cruzadas

- **LST-ADM-001:** Inventário Consolidado e Controle de Ativos Patrimoniais de Laboratório.
- **LST-ADM-002:** Lista de Estoque Consolidada e Diretrizes de Gestão de Reagentes Laboratoriais.
- **LST-ADM-003:** Catálogo de Fornecedores e Prestadores de Serviços Técnicos.
- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.