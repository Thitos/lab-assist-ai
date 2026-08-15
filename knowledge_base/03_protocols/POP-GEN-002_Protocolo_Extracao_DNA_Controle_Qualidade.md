# BioLab Research Center

# POP-GEN-002 - Extração de DNA e Controle de Qualidade de Amostras

## Informações do documento

|Campo|Valor|
|---|---|
|Código|POP-GEN-002|
|Categoria|Protocolo|
|Setor|Biologia Molecula|
|Nível de Biossegurança|NB1|
|Responsável|Dr. Marcelo Viegas, Especialista em Automação e Bancada|
|Revisão Técnica|Dr. Renato Guimarães, Pesquisador Sênior (Edição Gênica)|
|Versão|4.0|
|Data da revisão|Agosto/2026|
|Palavras-chave|Extração de DNA, Controle de Qualidade, Razão A260/A280, Razão A260/A230, CTAB, Column-based Purification, Genômica Vegetal|

# Protocolo de Extração de DNA e Controle de Qualidade de Amostras

## Objetivo

Padronizar a rotina operacional para o isolamento e a purificação de DNA genômico de alta integridade a partir de tecidos vegetais (*Glycine max* e *Solanum lycopersicum*) e biomassa bacteriana. Este procedimento visa garantir a remoção completa de inibidores da polimerase (como polifenóis e polissacarídeos) através de um método híbrido (CTAB e colunas de sílica), preparando as amostras para o fluxo de triagem molecular via qPCR (**POP-GEN-003**) e sequenciamento de nova geração (**POP-SEQ-001**).

## Aplicação

Este procedimento operacional padrão aplica-se a todos os pesquisadores, técnicos e analistas de bancada do **BioLab Research Center** que realizam a extração de ácidos nucleicos destinados a ensaios downstream de genômica funcional, validação de edições via CRISPR-Cas9 e genotipagem em larga escala.

## Biossegurança

### EPIs obrigatórios

- Jaleco de algodão com punho elástico de ribana conforme o **POP-BIO-002**.
- Luvas de nitrilo descartáveis (livres de DNase/RNase). Nota: Substituir imediatamente as luvas se houver contato direto com clorofórmio.
- Óculos de proteção contra respingos químicos com ventilação indireta.
- Máscara cirúrgica descartável (uso obrigatório durante a pesagem e manipulação de tecidos vegetais triturados).

### Cuidados

- **Manipulação de Voláteis Orgânicos:** As etapas que envolvem Clorofórmio:Álcool Isoamílico (24:1) e Beta-mercaptoetanol devem ser executadas obrigatoriamente no interior de uma Capela de Exaustão Química devidamente certificada, nunca em bancadas abertas ou Cabines de Segurança Biológica.
- **Prevenção de Contaminação:** Utilizar reagentes de grau biologia molecular estéreis e ponteiras com filtro hidrofóbico. Alíquotas de trabalho devem ser feitas para evitar a contaminação cruzada de frascos de estoque.

## Materiais e Reagentes

### Equipamentos

- Extrator automatizado de tecidos / Homogeneizador de alta performance (TissueLyser ou equivalente).
- Microcentrífuga refrigerada de bancada com capacidade para 14.000 g e controle térmico (4 °C a 65 °C).
- Espectrofotômetro microvolume (NanoDrop One ou equivalente).
- Fluorímetro de alta precisão (Qubit 4 ou equivalente).
- Bloco de aquecimento seco (*Termobloco*) com agitação.

### Reagentes

- Tampão de Lise CTAB 2% (2% w/v CTAB, 1,4 M NaCl, 100 mM Tris-HCl pH 8,0, 20 mM EDTA).
- Beta-mercaptoetanol (99%).
- Mistura Clorofórmio:Álcool Isoamílico (24:1 v/v).
- Tampão de Ligação (Binding Buffer comercial à base de Cloridrato de Guanidina 6 M).
- Tampão de Lavagem (Wash Buffer: Etanol 70% em água de grau biologia molecular).
- Tampão de Eluição (Tampão TE: 10 mM Tris-HCl, 1 mM EDTA, pH 8,0).
- Ribonuclease A (RNase A, 10 mg/mL).
- Microcolunas de centrifugação com membrana de sílica e tubos de coleta de 2 mL.
- Microtubos de 1,5 mL livres de nucleases.

## Tempo estimado

- Maceração e Lise Térmica Celular: 45 minutos.
- Separação de Fases e Ligação à Sílica: 30 minutos.
- Lavagens Centrifugadas e Secagem: 20 minutos.
- Eluição e Controle de Qualidade: 25 minutos.
- **Tempo Total Estimado:** 2 horas.

## Procedimento

### Lise Celular

1. Pesar exatamente 100 mg de tecido vegetal jovem (folhas) congelado em nitrogênio líquido e transferir para um microtubo contendo esferas de aço inoxidável. Homogeneizar no TissueLyser por 2 minutos a 30 Hz até obter um pó fino e uniforme.
2. Adicionar instantaneamente ao tubo 500 μL de Tampão de Lise CTAB 2% previamente aquecido a 65 °C, suplementado com 1.0% v/v de Beta-mercaptoetanol (adicionado imediatamente antes do uso dentro da capela química).
3. Vorticar vigorosamente o tubo por 10 segundos para ressuscitar completamente a biomassa triturada.
4. Incubar a mistura no termobloco a 65 °C por 30 minutos sob agitação constante de 300 rpm. Inverter o tubo manualmente a cada 10 minutos para homogeneizar.
5. Adicionar 2 μL de RNase A (10 mg/mL), misturar por inversão e incubar a 37 °C por 15 minutos para degradar o RNA endógeno contaminante.

### Purificação do DNA

1. Na capela de exaustão química, adicionar às amostras resfriadas à temperatura ambiente 500 μL de Clorofórmio:Álcool Isoamílico (24:1).
2. Misturar a emulsão por inversão lenta e contínua durante 5 minutos. Não centrifugar ou vorticar agressivamente nesta etapa para evitar o cisalhamento mecânico do DNA genômico de alto peso molecular.
3. Centrifugar as amostras a 12.000 g por 10 minutos a 4 °C para provocar a separação das fases físico-químicas.
4. Recolher cuidadosamente a fase aquosa superior clara (aproximadamente 400 μL) utilizando uma micropipeta com ponteira de filtro ajustada para calibração de fluxo lento, transferindo-a para um novo microtubo de 1,5 mL. Evitar tocar a interfase proteica esbranquiçada.
5. Adicionar à fase aquosa recuperada um volume equivalente (1:1) de Tampão de Ligação (Binding Buffer). Vorticar por 5 segundos.
6. Transferir o volume total de 800 μL para uma microcoluna de centrifugação com membrana de sílica acoplada a um tubo de coleta de 2 mL.
7. Centrifugar a 10.000 g por 1 minuto à temperatura ambiente. Descartar o efluente líquido do tubo de coleta e reacomodar a coluna.

### Lavagem

1. Adicionar 500 μL de Tampão de Lavagem (Wash Buffer com Etanol) à membrana de sílica da coluna.
2. Centrifugar a 10.000 g por 1 minuto. Descartar o efluente líquido do tubo de coleta.
3. Repetir a lavagem adicionando mais 500 μL de Tampão de Lavagem à coluna. Centrifugar a 10.000 g por 1 minuto e descartar o efluente.
4. Recolocar a coluna vazia no tubo de coleta e centrifugar a rotação máxima de 14.000 g por 2 minutos seguidos. Esta etapa de centrifugação seca é crítica para eliminar traços residuais de etanol, que atuam como potentes inibidores das reações de polimerização downstream, como o qPCR (**POP-GEN-003**).

### Eluição

1. Transferir a coluna de sílica seca para um microtubo de 1,5 mL livre de nucleases devidamente etiquetado com o código indelével gerado pelo LIMS do projeto.
2. Aplicar exatamente 50 μL de Tampão TE pré-aquecido a 65 °C diretamente no centro da membrana de sílica. Certificar-se de que a ponteira não toque a superfície da membrana.
3. Incubar a coluna em repouso na bancada por 5 minutos à temperatura ambiente para permitir a reidratação e liberação eficiente do DNA adsorvido na matriz de sílica.
4. Centrifugar a 12.000 g por 1 minuto para eluir o DNA purificado. Descartar a coluna plástica e manter o microtubo contendo o eluído em bloco refrigerado.

### Controle de Qualidade

1. **Limpeza e Calibração:** Limpar o pedestal óptico do espectrofotômetro microvolume utilizando lenço de papel texturizado macio embebido em água destilada. Pipetar 1,5 μL do Tampão TE utilizado na eluição diretamente sobre o pedestal e realizar a leitura de calibração basal (Blank).
2. **Análise Espectrofotométrica:** Homogeneizar a amostra de DNA eluído por agitação suave e pipetar 1,5 μL no pedestal do equipamento. Executar a varredura espectral na faixa de 220 nm a 350 nm.
3. **Avaliação da Razão A260/A280:** Verificar o índice de pureza proteica. Os valores aceitáveis devem estar rigorosamente situados na janela de **1,8 a 2,0**. Razões abaixo de 1,8 indicam contaminação residual por proteínas ou fenol, requerendo nova etapa de lavagem com clorofórmio.
4. **Avaliação da Razão A260/A230:** Verificar o índice de contaminantes orgânicos. Os valores ideais devem situar-se entre **2,0 e 2,2**. Valores inferiores a 2,0 evidenciam a presença de carboidratos complexos, polissacarídeos celulares ou sais de guanidina remanescentes das soluções de lise/ligação.
5. **Quantificação Fluorimétrica (Validação de Rendimento):** Para amostras destinadas ao NGS (**POP-SEQ-001**), mensurar a concentração absoluta utilizando o fluorímetro Qubit com o ensaio dsDNA Broad Range (BR). Preparar os dois padrões exigidos pelo fabricante (190 μL de Qubit Working Solution + 10 μL de Standard) e as amostras analíticas (198 μL de Working Solution + 2 μL de DNA eluído). Medir a concentração expressa em ng/μL.

## Resultado esperado

- **Amostras de Alta Pureza:** Espectro de absorbância limpo com picos bem definidos a 260 nm, exibindo índices A260/A280 >= 1,8 e A260/A230 >= 2,0.
- **Concentração Mínima Requerida:** Rendimento final de DNA igual ou superior a 20 ng/μL avaliado por fluorometria, sem evidências de degradação visível (smear) quando submetido a eletroforese em gel de agarose 1%.

## Descarte de resíduos

- **Resíduos Líquidos Orgânicos:** O efluente gerado na fase de separação contendo clorofórmio e Beta-mercaptoetanol deve ser vertido e armazenado temporariamente na **Bombona B2 (Solventes Orgânicos Halogenados)** localizada sob a capela química.
- **Resíduos Químicos de Ligação:** O efluente das primeiras centrifugações de colunas contendo sais de guanidina deve ser armazenado na **Bombona B4 (Soluções Ácidas/Alcalinas)**. Jamais misturar sais de guanidina com hipoclorito de sódio, sob risco de liberação de gás cianídrico tóxico.
- **Sólidos Contaminados:** As ponteiras plásticas, luvas e microtubos descartáveis que entraram em contato com os solventes devem ser encaminhados para os recipientes rígidos de descarte químico do Grupo B, conforme o plano logístico do **POP-BIO-004**.

## Referências

- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.
- **POP-BIO-002:** Uso Correto de Equipamentos de Proteção Individual (EPI) e Coletiva (EPC).
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-003:** Protocolo de Amplificação e Quantificação via qPCR.
- **POP-SEQ-001:** Protocolo de preparo de amostras de RNA e bibliotecas para sequenciamento NGS.
- Sambrook, J., & Russell, D. W. (2001). *Molecular Cloning: A Laboratory Manual*. Cold Spring Harbor Laboratory Press.