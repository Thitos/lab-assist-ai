# BioLab Research Center

# POP-SEQ-002 - Preparo de Amostras de Solo para Metagenômica

## Informações do documento

|**Campo**|**Valor**|
|---|---|
|Código|POP-SEQ-002|
|Categoria|Protocolo|
|Setor|Biologia Molecular|
|Nível de Biossegurança|NB1|
|Responsável|Dr. Marcelo Viegas, Especialista em Automação e Bancada|
|Revisão Técnica|Dra. Daiane Prestes, Analista de Sequenciamento de Nova Geração|
|Versão|3.0|
|Data da revisão|Agosto/2026|
|Palavras-chave|Metagenômica, Microbioma do Solo, Extração de DNA, Bead Beating, Fenol-Clorofórmio, Ácidos Húmicos, Sequenciamento de Nova Geração|

# Protocolo de Preparo de Amostras de Solo para Metagenômica

## Objetivo

Padronizar a rotina operacional para a extração, purificação e controle de qualidade de DNA metagenômico a partir de matrizes complexas de solo (rizosfera de _Glycine max_ e solos de cerrado). O protocolo visa a lise uniforme de microrganismos gram-positivos, gram-negativos, esporos e fungos, garantindo a eliminação total de interferentes químicos co-extraídos (como ácidos húmicos e fúlvicos), gerando DNA de alto peso molecular e pureza compatível com o preparo de bibliotecas para sequenciamento NGS de alta cobertura.

## Aplicação

Este procedimento operacional padrão é de cumprimento mandatório para técnicos, analistas de automação e pesquisadores do **BioLab Research Center** alocados na Unidade de Microbiomas e Bioinsumos. O protocolo destina-se ao isolamento do DNA genômico total da comunidade microbiana presente em amostras de solo agrícola antes dos ensaios de sequenciamento de amplicons (16S rRNA / ITS) ou shotgun metagenomics.

## Biossegurança

### EPIs obrigatórios

- Jaleco de brim ou gabardine com punhos elásticos ajustados, em conformidade com o **POP-BIO-002**.
- Luvas de nitrilo de alta densidade (livres de nucleases). _Nota:_ Efetuar a troca das luvas imediatamente se ocorrer contato com fenol ou clorofórmio.
- Óculos de proteção contra respingos químicos com ventilação indireta.
- Máscara de proteção respiratória PFF2/N95 (obrigatória durante o fracionamento e pesagem do solo seco para evitar a inalação de bioaerossóis e material particulado).

### Cuidados

- **Contenção de Vapores Tóxicos:** As etapas contendo Fenol:Clorofórmio:Álcool Isoamílico (25:24:1) e Clorofórmio puro devem ser rigorosamente conduzidas no interior de uma capela de exaustão de gases químicos com velocidade de face calibrada.
- **Inibição de Nucleases:** Lavar racks, pipetas e superfícies com agentes químicos de descontaminação antes do início das atividades, conforme as instruções do **POP-BIO-001**.
- **Gerenciamento Químico:** Sais de guanidina e fenol são incompatíveis com hipoclorito de sódio; reações acidentais liberam gases altamente letais. Siga estritamente o protocolo de segregação de efluentes.

## Materiais e Reagentes

### Equipamentos

- Lise mecânica por agitação tridimensional (TissueLyser II, FastPrep-24 ou equivalente).
- Microcentrífuga refrigerada para microtubos de 1,5 mL e 2,0 mL com capacidade de aceleração de até 16.000 g.
- Vórtice com adaptador horizontal para múltiplos tubos de 2 mL.
- Termobloco digital com agitação orbital.
- Espectrofotômetro microvolume (NanoDrop One) e Fluorímetro (Qubit 4).

### Reagentes

- Tampão de Lise de Solo (100 mM Tris-HCl pH 8,0, 100 mM EDTA pH 8,0, 100 mM Fosfato de Sódio, 1,5 M NaCl, 1% w/v CTAB).
- Solução de SDS 20% w/v e Proteinase K (20 mg/mL).
- Mistura Fenol:Clorofórmio:Álcool Isoamílico (25:24:1 v/v/v), saturada com Tris, pH 8,0.
- Acetato de Potássio 5 M (pH 5,5) ou Solução Comercial de Precipitação de Inibidores (PPS - _Protein Precipitation Solution_₎.
- Isopropanol P.A. (99,5%) resfriado a -20 °C e Etanol 70% preparado fresco.
- Kits de Colunas de Sílica para Clean-up de DNA Metagenômico (Remoção de Ácidos Húmicos).
- Tubos de Lise Rígidos de 2 mL contendo esferas de zircônia/sílica de diâmetros mistos (0,1 mm e 0,5 mm).

## Tempo estimado

- Pesagem e Lise Mecânica (Bead Beating): 30 minutos.
- Extração com Fenol-Clorofórmio: 40 minutos.
- Precipitação, Lavagem e Purificação em Coluna: 50 minutos.
- Controle de Qualidade Espectrofotométrico e Fluorimétrico: 20 minutos.
- **Tempo Total Estimado:** 2 horas e 20 minutos.

## Procedimento

### Pesagem e Lise Mecânica do Solo (Bead Beating)

1. Limpar a balança analítica e a bancada adjacente com Álcool 70%. Pesar exatamente 0,25 g de amostra de solo homogeneizada diretamente dentro de um tubo de lise rígido contendo a matriz de esferas de zircônia/sílica.
2. Adicionar 500 μL de Tampão de Lise de Solo aquecido a 60 °C e 50 μL de solução de SDS 20%.
3. Adicionar 20 μL de Proteinase K (20 mg/m). Misturar por inversão suave e incubar no termobloco a 60 °C por 15 minutos sob agitação de 300 rpm.
4. Acoplar os tubos firmemente no suporte do TissueLyser II. Executar a **lise mecânica (bead beating) por 2 minutos na frequência de 30 Hz**. Esta etapa é crítica: tempos superiores a 2 minutos provocam o cisalhamento excessivo do DNA metagenômico, inviabilizando bibliotecas shotgun; tempos inferiores reduzem a representatividade de bactérias Gram-positivas.
5. Centrifugar os tubos a 12.000 g por 3 minutos a 4 °C para assentar a terra fragmentada e a matriz de esferas no fundo do tubo.

### Extração com Fenol-Clorofórmio

1. Transferir o sobrenadante líquido bruto obtido (aproximadamente 450 μL) para um novo microtubo estéril de 1,5 mL livre de nucleases.
2. Na capela de exaustão química, adicionar à amostra um volume equivalente (1:1) de Fenol:Clorofórmio:Álcool Isoamílico (25:24:1). Vorticar o tubo em rotação média por 5 segundos até obter uma emulsão leitosa uniforme.
3. Centrifugar a amostra a 14.000 g por 5 minutos a 4 °C para separar as fases hidrofóbica e hidrofílica.
4. Recuperar a fase aquosa superior contendo os ácidos nucleicos (cuidado extremo para não tocar na interfase proteica compactada) e transferi-la para um novo tubo de 1,5 mL.
5. Adicionar 200 μL de Acetato de Potássio 5 M (pH 5,5) para precipitar polissacarídeos e complexos de ácidos húmicos remanescentes. Vorticar por 5 segundos e incubar em gelo por 10 minutos.
6. Centrifugar a 16.000 g por 10 minutos a 4 °C. Recuperar o sobrenadante límpido e transferi-lo para um tubo limpo.

### Precipitação e Purificação de Ácidos Nucleicos Totais

1. Adicionar ao sobrenadante recuperado um volume equivalente de Isopropanol P.A. resfriado a -20 °C. Inverter o tubo manualmente 15 vezes para homogeneizar a solução e induzir a precipitação do DNA.
2. Incubar a amostra a -20 °Cpor 30 minutos (ou a -80 °C por 15 minutos).
3. Centrifugar a 16.000 g por 15 minutos a 4 °C para consolidar o pellet de DNA no fundo do tubo. O pellet gerado a partir de solos ricos em matéria orgânica pode apresentar uma coloração marrom clara decorrente da co-precipitação de ácidos húmicos.
4. Descartar o sobrenadante por decantação cuidadosa. Adicionar 500 μL de Etanol 70% fresco sobre o pellet. Centrifugar a 14.000 g por 5 minutos a 4 °C. Decantar o etanol e repetir esta etapa de lavagem mais uma vez.
5. Secar o pellet ao ar na bancada por 5 minutos até a evaporação completa dos traços de etanol.
6. Ressuspender o pellet em 100 μL de água livre de nucleases.
7. **Clean-up Final (Remoção Absoluta de Inibidores):** Para garantir o sucesso do sequenciamento NGS, passar os 100 μL de DNA bruto por uma microcoluna de purificação à base de sílica comercial otimizada para remoção de polifenóis/ácidos húmicos. Seguir o fluxo de lavagem com os tampões específicos do kit e eluir o DNA metagenômico purificado em 50 μL de Tampão TE (10 mM Tris-HCl, 1 mM EDTA, pH 8,0).

### Armazenamento

O DNA metagenômico eluido deve ser estocado imediatamente a -20 °C para uso em curto prazo (até 30 dias). Para armazenamento de longo prazo destinado a ensaios de sequenciamento NGS estruturados, as amostras devem ser indexadas e guardadas em ultrafreezers a -80 °C.

## Resultado esperado

- **Métricas Espectrofotométricas de Pureza:** A quantificação no NanoDrop deve apresentar razões de absorbância limpas. A razão **A260/A280 deve estar entre 1,8 e 2,0**, garantindo a remoção de proteínas. A razão **A260/A230 deve ser ge 2,0**. Valores inferiores a 1,5 no índice 260/230 indicam forte presença de ácidos húmicos e sais residuais, o que inibe a polimerase na amplificação via qPCR (**POP-GEN-003**) ou o preparo de bibliotecas NGS (**POP-SEQ-001**), exigindo uma nova rodada de clean-up na coluna.
- **Rendimento Mínimo:** Concentração mínima de 10 ng/μL mensurada via ensaio fluorimétrico Qubit dsDNA HS.

## Descarte de resíduos

- **Efluentes Halogenados e Tóxicos:** O descarte de resíduos líquidos contendo a mistura Fenol-Clorofórmio deve ser direcionado exclusivamente para a **Bombona B2 (Solventes Orgânicos Halogenados)** sob a capela, em conformidade com o plano integrado de rejeitos do **POP-BIO-004**.
- **Efluentes não-halogenados:** Frações líquidas contendo isopropanol e etanol devem ser descartadas na **Bombona B1**.
- **Insumos Sólidos Contaminados:** Ponteiras, tubos de lise exauridos, esferas e luvas descartáveis devem ser segregados em sacos amarelos rígidos destinados a Resíduos Químicos Perigosos do Grupo B.

## Referências

- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.
- **POP-BIO-002:** Uso Correto de Equipamentos de Proteção Individual (EPI) e Coletiva (EPC).
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-003:** Protocolo de Amplificação e Quantificação via qPCR.
- **POP-SEQ-001:** Protocolo de preparo de amostras de RNA e bibliotecas para sequenciamento NGS.
- **MAN-EQP-003:** Manual de Operação e Manutenção Preventiva do Termociclador.