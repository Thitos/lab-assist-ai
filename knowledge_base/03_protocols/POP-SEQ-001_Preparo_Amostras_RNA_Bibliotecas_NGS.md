# BioLab Research Center

# POP-SEQ-001 - Preparo de Amostras de RNA e Bibliotecas para NGS

## Informações do documento

|**Campo**|**Valor**|
|---|---|
|Código|POP-SEQ-001|
|Categoria|Protocolo|
|Setor|Biologia Molecular|
|Nível de Biossegurança|NB1|
|Responsável|Dr. Marcelo Viegas, Especialista em Automação e Bancada|
|Revisão Técnica|Dra. Daiane Prestes, Analista de Sequenciamento de Nova Geração|
|Versão|2.1|
|Data da revisão|Agosto/2026|
|Palavras-chave|Sequenciamento de Nova Geração, NGS, Preparo de Biblioteca, RNA-Seq, Illumina, Illumina Stranded mRNA, Transcriptômica Vegetal|

# Protocolo de Preparo de Amostras de RNA e Bibliotecas para Sequenciamento NGS

## Objetivo

Padronizar de forma estrita as etapas físico-químicas e enzimáticas para o isolamento, fragmentação e conversão de RNA mensageiro (mRNA) de espécimes vegetais (_Glycine max_ e _Solanum lycopersicum_) em bibliotecas de DNA complementares (cDNA) duplamente indexadas. Este procedimento visa assegurar a máxima eficiência de conversão e a eliminação de vieses de amostragem, gerando bibliotecas de alta complexidade prontas para o sequenciamento de nova geração (NGS) em plataformas Illumina e Oxford Nanopore operadas no **BioLab Research Center**.

## Aplicação

Este Procedimento Operacional Padrão (POP) aplica-se a todos os especialistas de bancada, tecnologistas e pesquisadores vinculados à Unidade de Genômica Funcional e Transcriptômica. O protocolo detalhado abaixo é otimizado para o kit _Illumina Stranded mRNA Prep_, operado manualmente ou via Estação Automatizada de Pipetagem epMotion 5075, utilizando como input inicial RNA total purificado de alta integridade.

## Biossegurança

### EPIs obrigatórios

- Jaleco de algodão com fechamento total e punho elástico, conforme preconizado no **POP-BIO-002**.
- Luvas de nitrilo descartáveis certificadas como livres de RNase (_RNase-free_). As luvas devem ser trocadas a cada transição entre os blocos térmicos e após o contato com superfícies externas à capela.
- Óculos de segurança de policarbonato com vedação lateral.
- Máscara cirúrgica tripla descartável para contenção de aerossóis salivares ricos em RNases humanas.

### Cuidados

- **Controle Onipresente de RNases:** O preparo de bibliotecas de RNA exige um ambiente de pureza molecular absoluta. Limpar as superfícies da capela de fluxo laminar, os conjuntos de micropipetas e os racks magnéticos com soluções descontaminantes enzimáticas comerciais (ex.: RNaseZap) antes de dispor os insumos.
- **Estabilidade Térmica:** O RNA total e os intermediários de fita simples são extremamente termolábeis. Manter todas as frações líquidas acondicionadas em blocos térmicos refrigerados a 4 °C ou gelo picado ao longo de toda a manipulação de bancada.
- **Manuseio de Agentes Magnéticos:** Os beads magnéticos de purificação (Agencourt AMPure XP ou similares) devem ser completamente homogeneizados por vórtex até atingirem uma coloração marrom homogênea antes da dispensação. Nunca congelar os estoques de beads magnéticos.

## Materiais e Reagentes

### Equipamentos

- Termociclador de precisão com tampa aquecida programável (verificação de rampa térmica em conformidade com o **MAN-EQP-003**).
- Rack Magnético de Alta Afinidade para microtubos de 0,2 mL e placas de 96 poços.
- Fluorímetro Qubit 4 (Applied Biosystems).
- Bioanalyzer 2100 ou TapeStation 4150 (Agilent Technologies).
- Microcentrífuga refrigerada com adaptador para fitas de PCR e placas de microtitulação.

### Reagentes

- Amostras de RNA total vegetal com RIN (_RNA Integrity Number_) ge 8,0 e concentração ge 50 ng/μL validadas previamente via **POP-GEN-002**.
- Kit _Illumina Stranded mRNA Prep_ (contendo: Oligo(dT) Magnetic Beads, Fragment Mix [Frag Mix], First Strand Synthesis Mix, Second Strand Marking Mix, Ligation Mix, Resuspension Buffer [RSB]).
- Kit de Índices Combinatórios duplos (Illumina RNA UD Indexes).
- Beads Magnéticos de Purificação de DNA (AMPure XP XP Beads).
- Etanol 80% de grau molecular, preparado fresco diariamente utilizando água livre de nucleases.
- SuperScript IV Reverse Transcriptase (200 U/μL).
- Kit Qubit RNA HS Assay e Kit Qubit dsDNA HS Assay.
- Agilent RNA ScreenTape e Agilent D1000 ScreenTape.

## Tempo estimado

- Purificação de mRNA e Fragmentação Térmica: 1 hora e 15 minutos.
- Síntese de cDNA (Primeira e Segunda Fitas): 2 horas.
- Ligação de Adaptadores e Purificação de Intermediários: 1 hora e 30 minutos.
- Amplificação por PCR e Validação Quali/Quanti Final: 1 hora e 45 minutos.
- **Tempo Total Estimado:** 6 horas e 30 minutos (dividido em dois turnos operacionais).

## Procedimento

### Fragmentação do RNA

1. **Enriquecimento de mRNA:** Iniciar com 500 ng de RNA total diluído em um volume final de 25 μL de água livre de nucleases em um microtubo de PCR strip de 0,2 mL.
2. Adicionar 25 μL de Oligo(dT) Magnetic Beads à amostra para capturar as caudas poli-A dos transcritos maduros. Homogeneizar por pipetagem 10 vezes.
3. Incubar o tubo no termociclador a 65 °C por exatamente 5 minutos para desnaturar as estruturas secundárias do RNA, seguido de incubação a 4 °C por 5 minutos para promover a hibridização do oligo(dT) ao mRNA.
4. Posicionar o strip de PCR no rack magnético por 2 minutos até que a solução clareie por completo. Aspirar e descartar o sobrenadante sem perturbar o pellet de beads.
5. Remover o strip do ímã, ressuscitar os beads em 200 μL de Tampão de Lavagem de RNA, misturar homogeneamente e recolocar no rack magnético por mais 2 minutos. Descartar o efluente.
6. **Fragmentação Química/Térmica:** Adicionar 11 μL de Frag Mix (contendo cátions divantes de zinco) diretamente sobre o pellet de beads secos. Homogeneizar por pipetagem vigorosa.
7. Incubar a mistura no termociclador configurado para **94 °C por exatamente 8 minutos** (parâmetro crítico calibrado para gerar fragmentos com distribuição mediana de 200 a 300 pares de bases). Esfriar imediatamente a 4 °C.
8. Colocar o strip no rack magnético por 2 minutos. Transferir exatamente 10 μL do sobrenadante limpo (contendo o mRNA fragmentado eluído) para um novo tubo de PCR livre de nucleases.

### Síntese de cDNA

1. **Síntese da Primeira Fita:** Adicionar 8 μL de First Strand Synthesis Mix e 1 μL de SuperScript IV Reverse Transcriptase ao mRNA fragmentado (10 μL). Homogeneizar por pipetagem 10 vezes.
2. Incubar no termociclador utilizando o programa enzimático sequencial:
	- Hibridização de Primers Aleatórios: 25 °C por 10 minutos.
	- Extensão da Transcriptase Reversa: 50 °C por 15 minutos.
	- Inativação Enzimática: 70 °C por 15 minutos. Queda térmica para 4 °C.
3. **Síntese e Marcação da Segunda Fita:** Adicionar diretamente ao produto da primeira fita 5 μL de Second Strand Marking Mix e 20 μL de Second Strand Synthesis Mix (formulação contendo dUTP para marcação da fita antissentido, garantindo a preservação da informação da fita/direcionalidade do transcrito vegetal). Volume final: 45 μL.
4. Incubar no termociclador a **16 °C por exatamente 1 hora**, com a tampa aquecida desligada ou ajustada para no máximo 40 °C.
5. Adicionar 90 μL de AMPure XP Beads homogeneizados à reação (45 μL, proporção de 2,0x). Incubar por 5 minutos em temperatura ambiente para ligar o dsDNA.
6. Colocar no rack magnético por 5 minutos. Descartar o sobrenadante. Lavar o pellet duas vezes com 200 μL de Etanol 80% fresco, mantendo o tubo fixo no ímã.
7. Secar o pellet ao ar por 3 a 5 minutos. Eluir o dsDNA adicionando 22 μL de Resuspension Buffer (RSB). Colocar no ímã e transferir 20 μL do eluído limpo para um novo poço.

### Ligação de Adaptadores

1. **Adição de Adenina terminal (A-tailing) e Ligação:** Adicionar 10 μL de Ligation Mix e 2,5 μL de adaptadores de sequenciamento Illumina ancorados contendo a cauda de timidina complementar (T-overhang). Volume: 32,5 μL.
2. Adicionar 2,5 μL do Índice Único Dual designado na planilha de planejamento do LIMS para a respectiva amostra, de forma a individualizar as bibliotecas para o processo de multiplexação.
3. Incubar no termociclador a **30 °C por exatamente 10 minutos**, seguido de inativação térmica a 70 °C por 5 minutos.
4. **Purificação Pós-Ligação (Seleção de Tamanho):** Adicionar 35 μL de AMPure XP Beads à reação. Incubar por 5 minutos. Colocar no rack magnético por 5 minutos e remover o sobrenadante.
5. Efetuar dois ciclos de lavagem com 200 μL de Etanol 80%. Secar o pellet por 3 minutos.
6. Eluir a biblioteca ligada adicionando 22 μL de RSB. Misturar, magnetizar por 2 minutos e recuperar 20 μL do sobrenadante líquido contendo a biblioteca bruta para transferência.

### Amplificação da Biblioteca NGS

1. Montar o coquetel de amplificação adicionando 20 μL de PCR Master Mix comercial (fornecido no kit) aos 20 μL de biblioteca eluída. Homogeneizar.
2. Submeter as amostras ao programa de PCR de enriquecimento seletivo no termociclador:
	- Desnaturação Inicial: 98 °C por 30 segundos (1 ciclo).
	- **Ciclagem de Amplificação (12 Ciclos):**
		- Desnaturação: 98 °C por 10 segundos.
		- Anelamento: 60 °C por 30 segundos.
		- Extensão: 72 °C por 30 segundos.
	- Extensão Final: 72 °C por 5 minutos. Queda térmica estável para 4 °C.
3. **Purificação Final da Biblioteca Amplificada:** Adicionar 36 μL de AMPure XP Beads homogeneizados ao produto de PCR (40 μL, proporção de 0,9× calibrada para exclusão estrita de fragmentos curtos e dímeros de adaptadores de 120 pb).
4. Incubar por 5 minutos. Colocar no rack magnético por 5 minutos. Descartar o sobrenadante contendo os subprodutos eliminados.
5. Lavar o pellet de contas duas vezes com Etanol 80%. Secar por 3 minutos até que o pellet apresente um aspecto fosco (rachaduras visíveis indicam supersecagem e reduzem o rendimento da eluição).
6. Eluir a biblioteca final purificada adicionando 22 μL de Resuspension Buffer (RSB). Incubar por 2 minutos, aplicar o campo magnético por mais 2 minutos e transferir os 20 μL finais de biblioteca purificada para um microtubo criogênico de baixa retenção de 1,5 mL com identificação de código de barras bidimensional.

### Armazenamento

As bibliotecas NGS finalizadas e purificadas devem ser estocadas imediatamente a -20 °C em caixas organizadoras à prova de luz por um período máximo de até 3 meses. Para estocagem de longo prazo superior a 90 dias, os tubos devem ser transferidos para ultrafreezers a -80 °C. Evitar a execução de mais de 3 ciclos consecutivos de congelamento e descongelamento para mitigar riscos de desnaturação física das estruturas de dsDNA.

## Resultado esperado

- **Perfil de Distribuição de Tamanho (Eletroforese Capilar):** A análise das amostras no Agilent TapeStation utilizando o chip D1000 deve exibir um pico eletroforético único, de distribuição gaussiana suave, centrado estritamente na faixa de **280 a 350 pares de bases (pb)**. A presença de picos proeminentes na região de 120 a 130 pb indica a persistência indesejada de dímeros de adaptadores, exigindo uma rodada adicional de purificação magnética com beads 0,9x.
- **Concentração Mínima Requerida:** A quantificação absoluta via Qubit dsDNA HS Assay deve reportar uma concentração de biblioteca final 4 nM (o que equivale a aproximadamente ge 1,5 ng/μL para fragmentos com distribuição de 300 pb), métrica necessária para viabilizar o cálculo exato de pooling e a geração eficiente de clusters na célula de fluxo do sequenciador.

## Descarte de resíduos

- **Rejeitos Químicos e Soluções Hidroalcoólicas:** O etanol 80% residual e os efluentes orgânicos gerados no descarte das lavagens magnéticas devem ser descartados na **Bombona B1 (Solventes Orgânicos Não-Halogenados)**, em conformidade com as diretrizes do **POP-BIO-004**.
- **Consumíveis Plásticos:** Ponteiras com filtros de barreira, microtubos de tiras de PCR utilizados e remanescentes de membranas ou colunas plásticas de descarte devem ser depositados nos recipientes de descarte de resíduos químicos secos do Grupo B para posterior incineração pela empresa licenciada contratada pelo BioLab.

## Referências

- **POP-BIO-002:** Uso Correto de Equipamentos de Proteção Individual (EPI) e Coletiva (EPC).
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-002:** Protocolo de Extração de DNA e Controle de Qualidade de Amostras.
- **MAN-EQP-003:** Manual de Operação e Manutenção Preventiva do Termociclador.
- Illumina, Inc. (2021). _Illumina Stranded mRNA Prep Reference Guide (Document # 1000000124518 v02)_. San Diego, CA.