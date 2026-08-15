# BioLab Research Center

# POP-GEN-003 - Amplificação e Quantificação via qPCR

## Informações do documento

|**Campo**|**Valor**|
|---|---|
|Código|POP-GEN-003|
|Categoria|Protocolo|
|Setor|Biologia Molecular|
|Nível de Biossegurança|NB1|
|Responsável|Dr. Marcelo Viegas, Especialista em Automação e Bancada|
|Revisão Técnica|Dr. Renato Guimarães, Pesquisador Sênior (Edição Gênica)|
|Versão|3.2|
|Data da revisão|Agosto/2026|
|Palavras-chave|qPCR, Reação em Cadeia da Polimerase em Tempo Real, SYBR Green, Quantificação Relativa, Automação de Pipetagem, Validação de CRISPR, Expressão Gênica|

# Protocolo de Amplificação e Quantificação via qPCR

## Objetivo

Padronizar a rotina operacional para amplificação, monitoramento em tempo real e quantificação absoluta ou relativa de ácidos nucleicos via Reação em Cadeia da Polimerase de Alta Precisão (qPCR). Este protocolo visa mitigar variações inter-operador por meio do uso de sistemas automatizados de pipetagem, garantindo a reprodutibilidade dos dados de expressão gênica de cultivares de _Glycine max_ e _Solanum lycopersicum_ editadas via CRISPR-Cas9 no **BioLab Research Center**.

## Aplicação

Este procedimento aplica-se a todos os ensaios de validação de nocaute gênico, triagem de eventos transgênicos agroindustriais, quantificação de carga viral/bacteriana fitopatogênica e análise de expressão diferencial de mRNAs e miRNAs conduzidos nas plataformas analíticas do BioLab. O protocolo é otimizado para placas de microtitulação de 96 ou 384 poços em sistemas de detecção por intercalantes fluorescentes (SYBR Green / EvaGreen) ou sondas de hibridização cliváveis (TaqMan).

## Biossegurança

### EPIs obrigatórios

- Jaleco de algodão (manga longa com punho elástico) em conformidade com as normas do **POP-BIO-002**.
- Luvas de nitrilo descartáveis livres de amido e certificadas como livres de DNase/RNase (trocar obrigatoriamente a cada transição de área de fluxo).
- Óculos de segurança com proteção lateral e lente antiembaçante.
- Máscara cirúrgica descartável ou respirador semifacial PFF2 (indicado para a etapa de ressuspensão de oligonucleotídeos liofilizados).

### Cuidados

- **Segregação Espacial Restrita:** O preparo da reação de qPCR deve ocorrer exclusivamente na "Área Limpa / Pré-PCR" (Sala 104-A), dotada de pressão positiva e capelas de fluxo laminar UV. É terminantemente proibido introduzir DNA molde (_template_), cDNA ou produtos de PCR amplificados nesta sala.
- **Descontaminação por Radiação e Agentes Químicos:** Antes de iniciar a manipulação, as superfícies internas da capela de pipetagem robótica devem receber radiação UV-C por 15 minutos, seguida de fricção mecânica com eliminador de nucleases comercial e purga com Álcool 70%, conforme as diretrizes do **POP-BIO-001**.
- **Prevenção de Aerossóis:** Utilizar unicamente ponteiras com filtro de barreira hidrofóbica de retenção molecular de alta densidade.

## Materiais e Reagentes

### Equipamentos

- Sistema de PCR em Tempo Real QuantStudio 5 (Applied Biosystems) ou homólogo calibrado para os canais de emissão FAM, SYBR/FAM, VIC/HEX e ROX.
- Estação Automatizada de Pipetagem de Alta Precisão (Eppendorf epMotion 5075 ou equivalente).
- Microcentrífuga de bancada com rotor oscilante para placas de microtitulação (capacidade de aceleração de até 2.000 g).
- Agitador tipo vórtex para microtubos.
- Cubas de gelo picado ou blocos térmicos refrigerados para manutenção de reagentes a 4 °C na bancada.

### Reagentes

- 2X qPCR Master Mix comercial contendo DNA polimerase termostável quimicamente modificada (_Hot-Start_), dNTPs (com dUTP incorporado), MgCl e corante fluorescente intercalante (SYBR Green / EvaGreen) ou formulação passiva de referência (ROX).
- Oligonucleotídeos Iniciadores (_Primers_) Forward e Reverse estocados em concentração de trabalho de 10 µM em Água ultra-pura grau biologia molecular (Livre de DNase/RNase).
- Amostras de cDNA sintetizadas ou moldes de DNA genômico de alta pureza (razão de absorbância A260/A280 entre 1,8 e 2,0, validada de acordo com o **POP-GEN-002**).
- Kit de Controle Interno/Gene Normalizador Endógeno validado para o organismo alvo (ex: _Actina_, _GAPDH_ ou _EF1-alpha_).

## Tempo estimado

- Preparação da capela e calibração de sensores do robô: 20 minutos.
- Preparo das diluições, curvas padrão e formulação do Master Mix: 30 minutos.
- Distribuição automatizada de alíquotas na placa de reação: 15 minutos.
- Corrida termo-analítica (Ciclagem e Curva de Melt): 1 hora e 20 minutos.
- Análise de dados e exportação de relatórios via LIMS: 15 minutos.
- **Tempo Total Estimado:** 2 horas e 40 minutos.

## Procedimento

### Preparo das Amostras e Curva de Diluição Padrão

1. Higienizar a área de trabalho interna da capela dedicada e dispor os microtubos de amostras pré-selecionados em blocos térmicos refrigerados a 4 °C.
2. Retirar as alíquotas de cDNA ou DNA molde do ultrafreezer -80 °C, proceder ao descongelamento lento em gelo e submeter os tubos a uma agitação rápida em vórtex por 3 segundos, seguida de uma centrifugação rápida (_spin_) de 5 segundos a 1.500 g para homogeneização do gradiente interno de solutos.
3. Para experimentos de quantificação absoluta ou determinação da eficiência dos iniciadores, preparar uma curva de diluição seriada de base 5 ou base 10 a partir de um pool de amostras de controle ou plasmídeo padrão. Gerar no mínimo 5 pontos de concentração (ex: 100 ng/µL; 10 ng/µL; 1 ng/µL; 0,1 ng/µL; 0,01 ng/µL) utilizando água livre de nucleases como diluente. Substituir as ponteiras a cada passo de transferência de volume.

### Formulação do Master Mix de Reação e Distribuição na Placa

1. Retirar o frasco de 2X qPCR Master Mix do armazenamento a -20 °C, mantendo-o ao abrigo da luz direta para evitar o fotocareamento (_photobleaching_) crônico do fluoróforo intercalante. Homogeneizar por inversão suave 10 vezes (não utilizar vórtex vigoroso na polimerase para evitar a denaturação mecânica da enzima).
2. Em um tubo estéril de polipropileno de 1,5 mL livre de nucleases, preparar o Coquetel de Reação Geral (Master Mix Multi-Amostras), considerando sempre um excesso técnico de 10% no volume total para compensar perdas por retenção capilar nas ponteiras de pipetagem.
3. Estruturar a reação unitária baseando-se nos parâmetros volumétricos discriminados na tabela abaixo:

### Tabela 2: Balanço Volumétrico para Reação de qPCR (Volume Final: 10 µL)

|**Componente da Reação**|**Concentração Inicial**|**Concentração Final**|**Volume por Poço (µL)**|
|---|---|---|---|
|2X qPCR Master Mix (com ROX)|2X|1X|5,0 µL|
|Primer Forward (F)|10 µM|400 nM|0,4 µL|
|Primer Reverse (R)|10 µM|400 nM|0,4 µL|
|Água Livre de Nucleases|-|-|2,2 µL|
|Amostra de cDNA / DNA Molde|Varíavel|10 a 50 ng|2,0 µL|

4. Programar a estação automatizada de pipetagem epMotion para transferir 8,0 µL do Coquetel de Reação Geral para cada poço da placa de microtitulação óptica de 96 poços, seguindo rigorosamente o leiaute de triplicata técnica previamente desenhado e indexado no caderno eletrônico (**MAN-LAB-002**).
5. Transferir a placa para a capela de fluxo da "Área de Amostras" e adicionar 2,0 µL de cDNA correspondente a cada poço preenchido. Adicionar 2,0 µL de água livre de nucleases nos poços designados como Controle Negativo de Reação (NTC - _No Template Control_).
6. Selar a placa hermeticamente utilizando um selador óptico adesivo sensível à pressão. Passar o aplicador plástico (_compressor de filme_) com firmeza sobre toda a superfície da placa para garantir a vedação completa e evitar evaporações diferenciais durante a fase de rampa térmica.
7. Centrifugar a placa selada a 2.000 g por exatamente 2 minutos para precipitar o menisco líquido, eliminar microbolhas residuais nas paredes dos poços e concentrar os componentes no fundo óptico.

### Programação do Termociclador e Ciclagem Térmica

1. Inicializar o sistema de PCR em tempo real e proceder ao login institucional associado ao projeto cadastrado.
2. Posicionar a placa centrifugada no berço do termociclador, certificando-se do alinhamento correto do poço A1 com o canto superior esquerdo do bloco térmico. Fechar a tampa aquecida pressurizada automática.
3. Configurar o software de aquisição óptica de dados com os seguintes parâmetros padrão de ciclagem térmica (_Fast Run Profile_):
	- **Ativação Inicial da Polimerase (Hot-Start):** 95 °C por 2 minutos (1 ciclo).
	- **Fase de Amplificação (40 Ciclos):**
		- Desnaturação Térmica: 95 °C por 15 segundos.
		- Anelamento de Primers e Extensão: 60 °C por 1 minuto (com leitura de fluorescência ativada no término desta subetapa).
	- **Fase de Curva de Dissociação (_Melt Curve_):** 95 °C por 15 segundos; queda térmica para 60 °C por 1 minuto; elevação gradual e contínua de temperatura até 95 °C a uma taxa de rampa de 0,05 °C por segundo, mantendo a aquisição de dados de fluorescência ativa durante toda a rampa de aquecimento.
4. Nomear o arquivo com o código do experimento gerado pelo LIMS e clicar no comando "Iniciar Corrida".

### Armazenamento

Ao término da corrida de qPCR, retirar a placa do equipamento. Caso seja necessária a purificação subsequente do produto para sequenciamento Sanger ou checagem em gel de poliacrilamida, a placa contendo os amplicons deve ser estocada a -20 °C por um período máximo de 48 horas. Caso contrário, proceder ao fluxo imediato de descarte. Os estoques de cDNA originais devem retornar imediatamente para caixas criogênicas identificadas a -80 °C.

## Resultado esperado

- **Curvas de Amplificação:** Devem apresentar perfil sigmoide clássico composto por fase basal, fase exponencial estrita, fase linear e fase de platô bem delimitadas nas triplicatas térmicas.
- **Triplicata Técnica:** A variação do ciclo de quantificação (Cq ou Ct) entre as triplicatas de uma mesma amostra não deve exceder o desvio padrão limite de DP <= 0,2. Valores acima deste limiar indicam erro humano ou mecânico de pipetagem, exigindo a invalidação e repetição do poço afetado.
- **Curva de Dissociação (Melt Curve):** Para reações utilizando SYBR Green/EvaGreen, deve ser observado um pico único de dissociação térmica (Tm específica), indicando a presença de um único amplicom puro. A detecção de picos secundários ou ombros térmicos em temperaturas inferiores a 75 °C denota a formação deletéria de dímeros de iniciadores (_primer-dimers_) ou amplificações inespecíficas, comprometendo a fidelidade dos cálculos de quantificação.
- **Controle Negativo (NTC):** Deve apresentar ausência completa de amplificação ou exibir um sinal residual tardio com valor de Cq > 38**, sem pico definido na curva de dissociação.
- **Parâmetros de Eficiência Analítica:** A curva padrão gerada pelas diluições deve apresentar um coeficiente de determinação linear R² >= 0,99. A inclinação da reta (_slope_) deve situar-se entre os valores limite de -3,58 e -3,10, o que corresponde a uma eficiência de reação calculada entre 90% e 110%. A expressão gênica relativa será calculada utilizando o método comparativo imutável da taxa de variação (método 2^-Delta Delta Cq), desde que as eficiências do gene alvo e do endógeno sejam equivalentes.

## Descarte de resíduos

- **Resíduos Plásticos e Químicos Intercalantes:** As placas de microtitulação seladas contendo os amplicons e resíduos de SYBR Green/EvaGreen são classificadas como rejeitos químicos mutagênicos e biológicos combinados. É expressamente proibido remover o filme óptico selante após a reação para evitar a contaminação da atmosfera do laboratório com amplicons voláteis.
- **Destinação Final:** Descartar a placa íntegra e fechada diretamente nos contêineres rígidos coletores do **Grupo B (Resíduos Químicos)** com identificação de toxicidade/mutagenicidade, conforme as regras estabelecidas no gerenciamento institucional de descartes em **POP-BIO-004**. Ponteiras e microtubos utilizados na fase de preparação do coquetel devem seguir o mesmo fluxo de descarte químico-biológico segregado.

## Referências

- **MAN-LAB-002:** Manual do Usuário para o Sistema LIMS e Caderno Eletrônico (ELN).
- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.
- **POP-BIO-002:** Uso Correto de Equipamentos de Proteção Individual (EPI) e Coletiva (EPC).
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-002:** Protocolo de Extração de DNA e Controle de Qualidade de Amostras.
- Bustin, S.A. et al. (2009). _The MIQE Guidelines: Minimum Information for Publication of Quantitative Real-Time PCR Experiments_. Clinical Chemistry, 55(4), 611-622.