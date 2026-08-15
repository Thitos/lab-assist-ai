# BioLab Research Center

# POP-RNA-001 - Extração de RNA Total via TRIzol

## Informações do documento

|**Campo**|**Valor**|
|---|---|
|Código|POP-RNA-001|
|Categoria|Protocolo|
|Setor|Biologia Molecular|
|Nível de Biossegurança|NB1|
|Responsável|Dr. Marcelo Viegas, Especialista em Automação e Bancada|
|Revisão Técnica|Dra. Daiane Prestes, Analista de Sequenciamento de Nova Geração|
|Versão|4.1|
|Data da revisão|Agosto/2026|
|Palavras-chave|Extração de RNA, TRIzol, Isotiocianato de Guanidínio, Fenol-Clorofórmio, Transcriptômica, Clivagem de RNases, _Glycine max_|

# POP-RNA-001: Protocolo de Extração de RNA Total via Método TRIzol

## Objetivo

Padronizar de forma estrita e minuciosa a rotina operacional para o isolamento e purificação de RNA total de alta integridade a partir de tecidos vegetais complexos (_Glycine max_ e _Solanum lycopersicum_) e suspensões celulares utilizando o reagente mono-fásico TRIzol (Isotiocianato de Guanidínio-Fenol). Este protocolo visa a inibição instantânea e irreversível das ribonucleases (RNases) endógenas e exógenas, garantindo a obtenção de frações de RNA íntegras e livres de contaminantes químicos ou genômicos para aplicações downstream de alta sensibilidade, como o preparo de bibliotecas para sequenciamento NGS (**POP-SEQ-001**) e RT-qPCR (**POP-GEN-003**).

## Aplicação

Este procedimento aplica-se a todos os técnicos de laboratório, analistas, pesquisadores e estagiários do **BioLab Research Center** vinculados às atividades da Unidade de Biologia Molecular e Transcriptômica Vegetal. O protocolo é otimizado para o processamento de amostras foliares, radiculares, calos celulares e tecidos recalcitrantes (ricos em polifenóis e polissacarídeos) submetidos ou não a edições gênicas via sistema CRISPR-Cas9.

## Biossegurança

### EPIs obrigatórios

- Jaleco de brim de alta gramatura, 100% algodão, com mangas longas e punhos elásticos ajustados, conforme estipulado no **POP-BIO-002**.
- Óculos de segurança contra impactos e respingos químicos com proteção lateral integral.
- Máscara facial cirúrgica tripla descartável (para prevenção de contaminação da amostra com aerossóis salivares ricos em RNases e proteção contra particulados de tecido vegetal atomizado).
- Duplo par de luvas de nitrilo descartáveis, livres de amido (_powder-free_) e certificadas como _RNase-free_. _Nota:_ O par de luvas externo deve ser trocado obrigatoriamente a cada 15 minutos ou imediatamente após o contato físico direto com respingos de TRIzol ou Clorofórmio.

### Cuidados

> ### ALERTA CRÍTICO DE BIOSSEGURANÇA
>
> O reagente TRIzol contém Fenol líquido (38% w/v) e Isotiocianato de Guanidínio (8 M), substâncias altamente tóxicas, corrosivas e mutagênicas, capazes de causar queimaduras químicas graves por contato dérmico e intoxicação sistêmica por inalação.
> - **Uso Obrigatório de Capela de Exaustão de Gases:** Todas as etapas que envolvem a abertura de frascos, pipetagem, homogeneização e separação de fases com TRIzol, Clorofórmio ou misturas fenólicas devem ser executadas **exclusivamente** no interior de uma Capela de Exaustão de Gases Químicos em perfeito estado de calibração, com o exaustor ativo e o vidro frontal posicionado abaixo da linha de segurança.
> - **Controle de RNases exógenas:** Limpar as superfícies internas da capela, os corpos das micropipetas, racks e minicentrífugas com soluções comerciais eliminadoras de nucleases (ex: RNaseZap) antes de iniciar o protocolo. Utilizar estritamente ponteiras com barreira hidrofóbica e microtubos certificados como livres de DNase/RNase.
> - **Evitar Reações Perigosas:** O isotiocianato de guanidínio reage violentamente com agentes oxidantes fortes (como o hipoclorito de sódio) liberando gás cianídrico altamente letal. É **terminantemente proibido** limpar derramamentos de TRIzol ou efluentes deste protocolo utilizando água de sanitização ou alvejante clorado. Em caso de acidentes, seguir o plano de contenção química estipulado no **POP-BIO-004**.

## Materiais e Reagentes

### Equipamentos

- Homogeneizador de tecidos de alta performance (TissueLyser II ou FastPrep-24).
- Microcentrífuga de bancada refrigerada com rotor de ângulo fixo para microtubos de 1,5 mL e 2,0 mL, capaz de atingir acelerações de até 16.000 g com controle térmico preciso ajustado para 4 °C.
- Espectrofotômetro microvolume (NanoDrop One) calibrado.
- Bioanalyzer 2100 com módulo de RNA (Agilent Technologies) ou TapeStation 4150.
- Termobloco digital com controle de temperatura dinâmico.
- Cuba eletroforética horizontal com fonte de corrente contínua para géis de agarose.

### Reagentes

- Reagente TRIzol (Ambion / Thermo Fisher Scientific).
- Clorofórmio P.A. (99,8%) estável e livre de isoamílico para esta aplicação.
- Isopropanol P.A. (99,5%) previamente resfriado a -20 °C.
- Etanol Absoluto P.A. (99,8%) misturado com água de grau biologia molecular para obtenção de uma solução de Etanol 75% v/v (preparada fresca no dia do experimento e estocada a -20 °C).
- Água Ultra-pura grau biologia molecular (Água tratada com DEPC 0,1% v/v e autoclavada, livre de DNase/RNase).
- Kit de DNase I livre de RNase (_RNase-free DNase I Set_, 2 U/μL), acompanhado de seu respectivo Tampão de Reação 10X.
- Nitrogênio Líquido (para congelamento instantâneo e maceração física das amostras).
- Agarose UltraPure grau biologia molecular.

## Tempo estimado

- Molienda, Lise Térmica e Homogeneização: 30 minutos.
- Adição de Clorofórmio e Separação de Fases Centrifugada: 25 minutos.
- Precipitação Química do RNA Total: 20 minutos.
- Lavagem com Etanol e Secagem do Pelete: 20 minutos.
- Ressuspensão e Digestão Enzimática com DNase I: 45 minutos.
- Controle de Qualidade Espectrofotométrico e Eletroforético: 20 minutos.
- **Tempo Total Estimado:** 2 horas e 40 minutos.

## Procedimento

### Lise e Homogeneização da Amostra com TRIzol

1. Pesar exatamente 100 mg de tecido foliar ou radicular de _Glycine max_ jovem previamente congelado em nitrogênio líquido. Transferir o fragmento instantaneamente para um microtubo rígido de 2,0 mL contendo duas esferas de aço inoxidável pré-resfriadas.
2. Posicionar os tubos no TissueLyser II e executar a **moagem criogênica por 1 minuto e 30 segundos na frequência de 30 Hz** até que o tecido atinja o aspecto de um pó fino homogêneo esbranquiçado. O tubo não deve descongelar em nenhuma hipótese durante o processo.
3. Imediatamente após a moagem, abrir o tubo na capela de gases e adicionar **1,0 mL de Reagente TRIzol**.
4. Vorticar o tubo em velocidade máxima por 30 segundos para garantir o contato íntimo e instantâneo do reagente com os componentes celulares desintegrados, promovendo a desnaturação total das proteínas e estabilização estrutural do RNA.
5. Incubar a mistura homogeneizada em repouso na bancada da capela por exatamente **5 minutos à temperatura ambiente (22 °C a 25 °C)** para permitir a dissociação completa dos complexos de nucleoproteínas.

### Separação de Fases (Adição de Clorofórmio e Centrifugação)

1. Adicionar exatamente **200 μL de Clorofórmio P.A.** ao microtubo contendo o homogeneizado de TRIzol (1,0 mL).
2. Fechar a tampa do tubo firmemente e agitar vigorosamente o tubo manualmente de cabeça para baixo por **15 segundos**. Não utilizar o agitador tipo vórtex nesta etapa para evitar o cisalhamento excessivo do DNA genômico celular, o que dificultaria sua partição de fase.
3. Incubar o tubo em repouso na bancada da capela por **3 minutos à temperatura ambiente**. A solução apresentará uma turbidez rosada homogênea.
4. Centrifugar a amostra a **12.000 g por exatamente 15 minutos a 4 °C** na microcentrífuga refrigerada.
5. Após a centrifugação, remover o tubo com extremo cuidado para não agitar as fases separadas. A mistura estará dividida estruturalmente em três camadas distintas:
	- **Fase Aquosa Superior (Incolor):** Contém exclusivamente o RNA total purificado, correspondendo a aproximadamente 50% v/v do volume inicial de TRIzol (500 μL).
	- **Interfase (Película esbranquiçada e opaca):** Concentra o DNA genômico retido e detritos celulares insolúveis.
	- **Fase Orgânica Inferior (Vermelha):** Composta por fenol-clorofórmio saturado contendo proteínas e lipídios celulares desnaturados.
6. Utilizando uma micropipeta P-200 calibrada com ponteira de filtro de baixa retenção molecular, transferir com precisão e lentidão **450 μL da fase aquosa superior** para um novo microtubo de 1,5 mL livre de nucleases.
	- _Nota Operacional Crítica:_ Manter uma margem de segurança física de 50 μL acima da interfase. É expressamente proibido tocar ou aspirar qualquer fração da interfase esbranquiçada ou da fase fenólica inferior, sob risco de contaminação irremediável da amostra com DNA genômico e arrasto de fenol.

### Precipitação do RNA (Isopropanol)

1. Adicionar exatamente **500 μL de Isopropanol P.A. resfriado a -20 °C** à fase aquosa recuperada (450 μL).
2. Homogeneizar a mistura por inversão suave do microtubo por 10 vezes consecutivas até que o gradiente de refração líquida desapareça por completo.
3. Incubar a mistura líquida em repouso na bancada da capela por **10 minutos à temperatura ambiente** para consolidar a nucleação e precipitação molecular das cadeias poliméricas de RNA total.
4. Centrifugar o microtubo a **12.000 g por exatamente 10 minutos a 4 °C** na microcentrífuga refrigerada.
5. Remover o tubo com cuidado. O RNA total precipitado formará um pelete esbranquiçado, translúcido ou gelatinoso aderido firmemente ao fundo ou parede lateral inferior do microtubo. Orientar o tubo na centrífuga com a articulação da tampa voltada para cima para facilitar a localização visual do pelete.

### Lavagem do Pelete (Etanol 75%)

1. Aspirar cuidadosamente o sobrenadante líquido por sucção ou pipetagem lenta, descartando-o integralmente no frasco de rejeitos apropriado. Tomar precaução máxima para não tocar ou deslocar o pelete de RNA fixado.
2. Adicionar **1,0 mL de Etanol 75% v/v pré-resfriado** diretamente sobre o pelete de RNA.
3. Descolar o pelete do fundo do tubo por inversão suave ou por uma agitação rápida em vórtex em rotação baixa (3 segundos) para promover o contato completo do etanol com toda a superfície do pelete, removendo os sais residuais de isotiocianato de guanidínio e coprecipitados orgânicos.
4. Centrifugar o tubo a **7.500 g por exatamente 5 minutos a 4 °C** para re-sedimentar o pelete purificado no fundo do microtubo.
5. Remover cuidadosamente o sobrenadante alcoólico utilizando uma micropipeta P-1000 e, subsequentemente, uma micropipeta P-10 com ponteira fina para sugar os microvolumes remanescentes acumulados no fundo do tubo.
6. Deixar o microtubo aberto de cabeça para baixo sobre um lenço de papel absorvente estéril no interior da capela por **5 a 7 minutos à temperatura ambiente** para permitir a evaporação completa do etanol residual.
	- _Nota Prática de Bancada:_ Não permitir a supersecagem do pelete (quando ele se torna totalmente opaco e quebradiço), pois isso reduzirá drasticamente a solubilidade do RNA de alto peso molecular, impedindo sua ressuspensão homogênea.

### Ressuspensão e Tratamento com DNase

1. Adicionar exatamente **40 μL de Água ultra-pura grau biologia molecular** (livre de DNase/RNase) diretamente sobre o pelete de RNA parcialmente seco.
2. Ressuscitar as moléculas de RNA incubando o tubo no termobloco digital ajustado para **58 °C por exatamente 10 minutos**, auxiliando a dissolução por batidas leves com o dedo indicador na base do tubo (_flicking_). Retornar o tubo ao gelo imediatamente após a incubação.
3. Para eliminar resquícios submicroscópicos de DNA genômico que interferem nos ensaios quantitativos de RT-qPCR, estruturar a reação de digestão enzimática adicionando os seguintes componentes ao mesmo microtubo:
	- Tampão de Reação da DNase I (10X): 5,0 μL
	- DNase I livre de RNase (2 U/μL): 2,0 μL (4 U totais)
	- Água ultra-pura grau biologia molecular: 3,0 μL
	- **Volume Reacional Final:** 50,0 μL
4. Homogeneizar suavemente por pipetagem e incubar o microtubo no termobloco a **37 °C por exatamente 30 minutos**.
5. Inativar termicamente a enzima DNase I adicionando 1,0 μL de EDTA 500 mM e incubando a **65 °C por 10 minutos**. A amostra purificada de RNA total está pronta para as análises metrológicas de controle de qualidade.

### Armazenamento

Para uso em curto prazo (janela operacional de até 72 horas), estocar as alíquotas de RNA total em blocos de gelo seco ou em freezers domésticos a -20 °C. Para armazenamento de longo prazo (períodos superiores a 3 dias e até 12 meses), transferir obrigatoriamente as amostras divididas em alíquotas de trabalho de 5 μL (para evitar ciclos deletérios de congelamento/descongelamento) para caixas criogênicas herméticas armazenadas em ultrafreezers regulados para **-80 °C**.

## Resultado esperado

### Análise Espectrofotométrica (NanoDrop)

A avaliação espectral da amostra de RNA total purificada via NanoDrop One deve apresentar uma curva de absorbância limpa com um pico de absorção máximo centrado exatamente no comprimento de onda de 26 nm.

- **Índice de Pureza Proteica (A260/A280):** O valor calculado pelo software do equipamento deve situar-se estritamente na faixa de **2,0 a 2,2**. Índices inferiores a 2,0 revelam a presença crônica de contaminação proteica residual ou fenol livre decorrente de erro na coleta da fase aquosa.
- **Índice de Pureza Orgânica (A260/A230):** Os valores ideais devem situar-se na janela de **2,0 a 2,3**. Razões abaixo de 1,8 indicam arraste severo de sais de guanidínio, carboidratos complexos ou solventes orgânicos provenientes das lavagens defeituosas, exigindo purificação por precipitação secundária com acetato de sódio e etanol.
- **Rendimento:** Concentração final esperada entre 100 ng/μL e 800 ng/μL para tecidos foliares de _Glycine max_.

```
Espectro Típico de RNA Total Puro no NanoDrop:
Absorbância
  ^
  |          _---_  (Pico a 260 nm)
  |         /     \
  |        /       \
  |   _--_/         \____
  +-------------------------> Comprimento de onda (nm)
     230    260    280
```

### Avaliação de Integridade (Eletroforese e Capilaridade)

- **Eletroforese em Gel de Agarose (1,2 w/v):** Sob incidência de luz transiluminadora UV, a amostra deve evidenciar duas bandas nítidas, intensas e bem delimitadas correspondentes às subunidades do RNA ribossômico estrutural de plantas: a banda superior correspondente ao **rRNA 28S** (ou 25S em plastídeos) e a banda inferior referente ao **rRNA 18S**. A intensidade de fluorescência da banda 28S deve ser empiricamente o dobro (2:1) da intensidade observada na banda 18S. A visualização de um rastro fluorescente contínuo de baixo peso molecular (_smear_) indica degradação mecânica ou enzimática severa do RNA.
- **Eletroforese Capilar (Bioanalyzer/TapeStation):** O software de análise digital automatizada deve gerar um eletroferograma limpo, reportando um Índice de Integridade do RNA (**RIN - _RNA Integrity Number_**) estritamente **igual ou superior a 8,0** (RIN ge 8,0) para viabilizar o fluxo de sequenciamento de nova geração NGS (**POP-SEQ-001**).

## Descarte de resíduos

- **Efluentes Líquidos Fenólicos e Cloroforados (Grupo B):** O líquido residual gerado após a partição de fase (composto pelas fases orgânicas vermelhas inferiores, interfases com DNA desnaturado e isopropanol contaminado com fenol) deve ser vertido e coletado obrigatoriamente no interior da capela para o interior da **Bombona B2 (Solventes Orgânicos Halogenados)**, devidamente identificada com rótulo de risco químico perigoso, tóxico e corrosivo.
- **Efluentes Alcoólicos de Lavagem:** As frações líquidas contendo etanol 75% contaminado com microtraços orgânicos devem ser segregadas na **Bombona B1 (Solventes Orgânicos Não-Halogenados)**.
- **Insumos Sólidos Contaminados:** Ponteiras plásticas com filtro, microtubos descartáveis exauridos, lenços texturizados e luvas externas que entraram em contato com o TRIzol e clorofórmio constituem resíduos perigosos do Grupo B. Devem ser descartados em sacos plásticos laranjas rígidos para posterior coleta, incineração e disposição final por empresa especializada licenciada, conforme o plano integrado de resíduos do **POP-BIO-004**.

## Referências

- **POP-BIO-001:** Descontaminação e Sanitização de Áreas de Trabalho e Equipamentos.
- **POP-BIO-002:** Uso Correto de Equipamentos de Proteção Individual (EPI) e Coletiva (EPC).
- **POP-BIO-004:** Plano de Gerenciamento e Descarte de Resíduos Biológicos e Químicos (PGRSS).
- **POP-GEN-003:** Protocolo de Amplificação e Quantificação via qPCR.
- **POP-SEQ-001:** Protocolo de preparo de amostras de RNA e bibliotecas para sequenciamento NGS.
- Chomczynski, P., & Sacchi, N. (1987). _Single-step method of RNA isolation by acid guanidinium thiocyanate-phenol-chloroform extraction_. Analytical Biochemistry, 162(1), 156-159.