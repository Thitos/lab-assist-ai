# BioLab Research Center

# POP-ADM-003 - Aquisição, Recebimento e Validação de Insumos Críticos

## Informações do documento

|Campo|Valor|
|---|---|
|Código|POP-ADM-003|
|Categoria|Procedimento Administrativo|
|Setor|Gestão & Compras|
|Nível de Biossegurança|NB1 / NB2|
|Responsável| Dra. Helena Vasconcelos, Head de Suprimentos|
|Revisão Técnica|Dr. Carlos Eduardo Buarque, Diretor Administrativo-Financeiro|
|Versão|2.1|
|Data da revisão|Agosto/2026|
|Palavras-chave|Requisição de Reagentes, Cadeia de Frio, Validação de Lote, Suprimentos Biotecnológicos, NFe|

# Procedimento Operacional Padrão: Aquisição, Recebimento e Validação de Reagentes e Insumos Críticos

## 1. Objetivo e Âmbito de Aplicação

Este Procedimento Operacional Padrão (POP) estabelece o fluxo administrativo e operacional compulsório para a requisição, cotação, homologação de fornecedores, recebimento físico e validação de qualidade de reagentes, insumos de biologia molecular e materiais consumíveis no **BioLab Research Center**.

As diretrizes deste documento aplicam-se a todos os projetos de pesquisa, contratos de inovação aberta, plataformas de sequenciamento de nova geração (NGS) e rotinas de transformação vegetal conduzidos nos blocos de laboratório NB1 e NB2. O objetivo fundamental é garantir a rastreabilidade integral dos insumos, assegurar a manutenção ininterrupta da cadeia de frio (_cold chain_) e evitar desperdícios ou contaminações cruzadas que comprometam a reprodutibilidade dos ensaios científicos.

## 2. Responsabilidades Operacionais

A gestão da cadeia de suprimentos biotecnológicos no BioLab opera sob um modelo de responsabilidade compartilhada entre a equipe científica e o setor administrativo:

- **Solicitante (Pesquisador / Técnico Responsável):** Identificar a necessidade do insumo, especificar as características técnicas (grau de pureza, concentração, compatibilidade com equipamentos), emitir a Requisição de Compra (RC) via sistema e realizar o teste de validação de lote.
- **Gestor do Projeto / Liderança de Bloco:** Avaliar a pertinência técnica, aprovar o orçamento do projeto e verificar se a requisição está alinhada com as estimativas de consumo do período.
- **Setor de Gestão & Compras:** Conduzir as cotações no mercado nacional e internacional, negociar prazos de entrega, emitir ordens de compra (OC), fiscalizar o cumprimento das licenças sanitárias/ambientais do fornecedor e gerenciar a logística de transporte.
- **Almoxarifado Central e Recebimento:** Realizar a conferência física inicial, inspecionar a integridade da embalagem externa, checar os registradores de temperatura da cadeia de frio e dar entrada na Nota Fiscal eletrônica (NFe).
- **Comissão Interna de Biossegurança (CIBio):** Fiscalizar a aquisição de reagentes controlados (ex.: fenol, clorofórmio, precursores sob controle da Polícia Federal e exército) e assegurar que a compra de novos vetores ou agentes biológicos cumpra o disposto no **MAN-BIO-001**.


## 3. Fluxo de Requisição e Aprovação Financeira

Toda solicitação de aquisição deve ser iniciada com antecedência mínima de **15 dias úteis** para reagentes de fabricação nacional e **45 dias úteis** para insumos importados ou sob encomenda (_custom synthesis_, como primers e sondas fluorescentes).

```
[Solicitante] ──> Emissão da RC via ERP (Especificações técnicas e FISPQ)
       │
       ▼
[Líder de Projeto] ──> Validação de Orçamento e Pertinência Científica
       │
       ▼
[Setor de Compras] ──> Cotação Tripla / Validação de Licenças de Fornecedor
       │
       ▼
[Emissão de OC] ──> Logística e Agendamento da Entrega (Janela de Frio)
```

### 3.1. Requisitos para Emissão da Requisição de Compra (RC)

Ao cadastrar uma solicitação no sistema LIMS/ERP do BioLab, o solicitante deve preencher obrigatoriamente:

1. Código de catálogo exato do fabricante e nome comercial completo.
2. Grau de pureza exigido (ex.: _HPLC grade_, _Molecular Biology Grade_, _Free of DNase/RNase_).
3. Apresentação e volumetria (ex.: kit para 500 reações, frasco de 500 mL, alíquotas de 100 nmol).
4. Ficha de Informações de Segurança de Produtos Químicos (FISPQ/GHS) atualizada em anexo.
5. Indicação do centro de custo e do projeto patrocinador.


## 4. Requisitos Específicos para a Cadeia de Frio (_Cold Chain_)

Reagentes de biologia molecular, enzimas de restrição, polimerases de alta fidelidade, transcriptases reversas e reagentes de sequenciamento NGS exigem monitoramento rigoroso da temperatura durante todo o trânsito logístico.

### Tabela 1: Categorias de Armazenamento e Condições de Transporte

|Classe de Temperatura|faixa Nominal|Reagentes Típicos|Exigência Mínima de Embalagem Logística|
|---|---|---|---|
|**Ambiente (CRT)**|15 °C a 25 °C|Tampones de corrida, sais analíticos, colunas de sílica secas, agarose.|Caixa de papelão reforçada com proteção contra umidade relativa.|
|**Refrigerado (COLD)**|2 °C a 8 °C|Anticorpos secundários, meios de cultura prontos, soluções de hibridização.|Caixa de poliestireno expandido (EPS) com géis reificantes (_ice packs_) condicionadas a 4 °C.|
|**Congelado (FROZ)**|-20 °C|Enzimas (_Taq_, _Cas9_), _mastermixes_, dNTPs, marcadores de peso molecular.|Container de EPS de alta densidade com gelox recarregado ou gelo seco com monitor de temperatura.|
|**Ultracongelado (CRYO)**|-80 °C ou Nitrogênio|Amostras RNA-Seq, bibliotecas NGS, células competentes (_A. tumefaciens_).|Shipper de nitrogênio em fase de vapor (_dry shipper_) ou caixa isotérmica com carga excedente de gelo seco.|

### 4.1. Regras para Fornecedores e Transportadoras

- Entregas de reagentes congelados (-20 °C e -80 °C) só serão aceitas no Almoxarifado Central de **segunda a quinta-feira, das 08h00 às 15h00**. É proibido o recebimento de cargas congeladas às sextas-feiras ou vésperas de feriados para evitar perda de gelo seco durante o final de semana.
- A caixa de transporte deve conter um **indicador de temperatura de irreversibilidade** ou datalogger para comprovar que não ocorreu descongelamento parcial durante o frete.


## 5. Protocolo de Recebimento, Inspeção Física e Entrada

No ato da entrega pelo fornecedor ou transportadora, o técnico do almoxarifado deve seguir rigorosamente a sequência de triagem:

### 5.1. Triagem Externa e Documental

1. Verificar se o volume físico corresponde exatamente ao número de caixas indicado no Conhecimento de Transporte (CT-e) e na Nota Fiscal (NFe).
2. Inspecionar a caixa externa em busca de amassados, vazamentos, sinais de umidade extrema ou violação de lacres de segurança.
3. Checar a NFe quanto à razão social, CNPJ do BioLab, número da Ordem de Compra e descrição literal do produto.


### 5.2. Abertura do Container Isotérmico e Verificação de Temperatura

1. Abrir a caixa de transporte e medir imediatamente a temperatura interna utilizando termômetro de mira infravermelha calibrado ou checar o histórico do datalogger.
2. Confirmar a presença de gelo seco suficiente (para insumos -20 °C e -80 °C). Caso o gelo seco esteja totalmente sublimado e o reagente em temperatura ambiente, o recebimento deve ser **recusado imediatamente no canhoto da NFe**.
3. Inspecionar a embalagem primária do reagente (frasco, tubo, placa) para garantir que não há trincas, vazamentos de líquido ou formação de cristais indevidos.


## 6. Homologação, Validação de Lote e Armazenamento

A entrada do produto no Almoxarifado não conclui o processo de aquisição. O insumo permanece no status **"Em Quarentena"** no sistema LIMS até a validação técnica pela equipe de laboratório.

```
[Recebimento Físico] ──> Status: "Quarentena" no LIMS
       │
       ▼
[Notificação ao Solicitante] ──> Retirada de alíquota de teste
       │
       ▼
[Ensaio de Validação de Lote] ──> Teste de controle de qualidade (PCR/Cultura)
       │
       ├─── [Aprovado] ──> Alteração no LIMS para "Liberado" e Armazenamento Definido
       └─── [Reprovado] ──> Abertura de RNC e Devolução ao Fornecedor
```

### 6.1. Protocolo de Teste de Validação de Lote (Controle de Qualidade)

A equipe solicitante tem o prazo máximo de **5 dias úteis** para conduzir o ensaio de validação do novo lote recebido:

- **Enzimas e Mastermixes de PCR:** Realizar reação controle utilizando DNA padrão do BioLab para comparar a eficiência de amplificação (Cq na PCR em tempo real ou intensidade de banda no gel de agarose) em relação ao lote em uso.
- **Kits de Extração de RNA/DNA:** Avaliar o rendimento (μg/μL) e a pureza (razões A260/A280 e A260/A230) em espectrofotômetro Microvolume.
- **Meios de Cultura e Antibióticos:** Executar teste de esterilidade em estufa incubadora por 48 horas e verificar a eficiência de seleção na concentração recomendada.

### 6.2. Armazenamento e Identificação Interna

Assim que aprovado na validação de lote, o reagente recebe a **Etiqueta Interna de Rastreabilidade BioLab**, contendo:

- Código interno do reagente e número do lote do fabricante.
- Data de recebimento e data de abertura do frasco.
- Iniciais do responsável pela liberação.
- Condição de armazenamento definitiva conforme sinalização do bloco de biossegurança (verificar exigências em **MAN-BIO-001**).

## 7. Tratamento de Não Conformidades (RNC) e Devoluções

Caso o reagente seja recusado no recebimento ou reprovado no teste de validação de lote, o responsável deve abrir uma **Relatório de Não Conformidade (RNC)** no sistema interno em até 24 horas.

### Tabela 2: Matriz de Ação em Não Conformidades de Aquisição

|Evento Identificado|Causa Provável|Ação Corretiva Imediata|Responsável|
|---|---|---|---|
|Avaria na embalagem / Vazamento|Impacto logístico no transporte.|Recusa imediata da carga; foto anexa à NFe; notificação à transportadora.|Almoxarifado|
|Sublimação total de gelo seco|Atraso no trânsito / Falha no acondicionamento.|Devolução do produto; solicitação de reposição de urgência sem custo.|Compras / Almoxarifado|
|Reprovação no Teste de Eficiência|Degradação térmica ou falha na síntese do lote.|Emissão de laudo de reprovação; bloqueio do lote no LIMS; pedido de replacement ao fabricante.|Solicitante / Compras|
|Produto em desacordo com a OC|Erro no faturamento / Separação do fornecedor.|Recusa parcial ou total; emissão de nota de devolução.|Compras|

## 8. Conformidade Legal e Auditoria

Todas as aquisições de reativos químicos e biológicos devem cumprir rigorosamente as regulamentações governamentais vigentes:

- **Produtos Controlados (Polícia Federal e Exército):** A compra de solventes e reagentes sujeitos a controle especial só será liberada mediante apresentação do Certificado de Licença de Funcionamento (CLF) válido e lançamento da cota no mapa mensal de controle.
- **Organismos Geneticamente Modificados (OGMs) e Vetores:** A aquisição de plasmídeos, cepas recombinantes ou vetores virais exige aprovação prévia formal da Comissão Interna de Biossegurança (CIBio) e registro no livro de tombo do BioLab, sob risco de infração à Lei de Biossegurança (Lei nº 11.105/2005).


## 9. Referências Cruzadas do BioLab

- **MAN-BIO-001:** Manual de Biossegurança — Diretrizes de Contenção, Controles de Risco e Salvaguardas.
- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-002:** Protocolo de Extração de DNA e Controle de Qualidade de Amostras.