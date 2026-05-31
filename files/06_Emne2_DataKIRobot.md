---
title: "Emne 2 — Datalogi, Kunstig Intelligens og Robotteknologi"
course: "Ingeniørfagets Videnskabsteori"
lecturer: Norbert Krüger
date_lectures: [2025-02-03, 2025-02-10]
pages: 133
tags: [KI, AI, robotteknologi, datalogi, kursusslides, SDU, deep-learning, neurale-netværk]
---

# Emne 2 — Datalogi, Kunstig Intelligens og Robotteknologi

> En historisk og begrebslig gennemgang af samspillet mellem KI, computer- og robotteknologi — fra mytologi og Leibniz-regnemaskinen frem til ChatGPT, embodiment og spørgsmålet om superintelligens.

**Relaterede noter:**
- [[05_Emne1_HvadErVidenskabsteori]] — kursets indledning
- [[01_Amato_DataWillSolveRobotics]] — pensum-artikel
- [[03_Biever_AIIntelligenceTest]] — pensum-artikel
- [[09_Tidslinje]] — kronologisk tidslinje

---

## Overblik (slidens egne emner)

1. Hvad er intelligens? Hvad er kunstig intelligens?
2. Trekant: KI, Robot- og Computerteknologi.
3. Indtil 2. Verdenskrig.
4. **1940–1956:** Begyndelsen.
5. **1957–1984:** Kampen mellem symbolske og subsymbolske metoder.
6. **1985–2005:** Evolutionære fremskridt og bias/variance-dilemmaet.
7. **2005–:** Deep Neural Networks tager over.
8. ChatGPT og embodiment.

---

## Hvad er intelligens?

**Den Danske Ordbog:** *"Evnen til at tilegne sig viden, opfatte og forstå sammenhænge mellem forskellige fænomener, tænke abstrakt og løse problemer."*

Etymologi: latin *intelligere* = "at forstå". Typiske betydninger: evnen til at lære og evnen til at løse nye opgaver uden forhåndsviden om fremgangsmåden.

**Arbejdsdefinition på KI (Krügers):** *"Kunstig intelligens modellerer intelligent adfærd på computere og/eller robotter."*

---

## ChatGPT som anker for diskussionen

- Lanceret **30. november 2022** af OpenAI.
- Baseret på Large Language Models (LLM'er).
- Blandt de 10 mest besøgte hjemmesider på verdensplan (juli 2024).
- Outsourcede kenyanske arbejdere tjente under $2/time for at mærke skadeligt indhold.
- 1000 prompts koster ca. 1 DKK; hver prompt bruger 10× så meget energi som en Google-søgning.
- Genererer "the next most probable word" — kan ikke skelne sandt fra falskt → "post-truth world".

### Svagheder ved ChatGPT (Matthew Gibbons 2023)
- Kan ikke regne med semantiske enheder
- Er ikke kreativ
- Overholder ikke ordbegrænsninger
- Fejler i simpel matematik og logik
- Forstår ikke humor
- Falsificerer kilder
- Lyver om egne protokoller
- Hallucinerer
- Producerer biased svar

---

## Turing-testen

- **Alan Mathison Turing** (1912–1954), britisk matematiker. En af datalogiens grundlæggere. Konstruerede Turingmaskinen (matematisk model af beregning). Knækkede Enigma-koden under WW2 sammen med andre forskere.
- Turing-testen (1950): En person kan via fjernkommunikation ikke afgøre om hun taler med menneske eller maskine.
- Turing var homoseksuel; selvmord 7.6.1954 efter tvangsbehandling mod homoseksualitet. Premierminister Gordon Brown gav posthum undskyldning. Statue af Stephen Kettle (2007) i Bletchley Park.

### Loebner-prisen
- Startede 1990 — årlig konkurrence; standard Turing-test-format.
- $2.000 til mest menneskelige program; engangspriser på $25.000 og $100.000.
- **Stoppede i 2020** fordi stifteren døde.

### Består ChatGPT Turing-testen?
Krüger henviser direkte til **Biever, Nature 2023** ([[03_Biever_AIIntelligenceTest]]).

Centrale citater fra artiklen brugt i slides:
> *"LLMs work simply by generating plausible next words... For chatbots, there is an extra element: human trainers have provided extensive feedback..."*

> Melanie Mitchell: *"Extrapolating in the way that we extrapolate for humans won't always work for AI systems."*

> *"LLMs learn only from language; without being embodied in the physical world, they do not experience language's connection to objects, properties and feelings, as a person does."*

### ConceptARC
- AI-systemer klarer sig dårligt i ConceptARC.
- Spørgsmål: hvordan ændrer gittermønstre sig?
- Anvendelse af abstrakte koncepter (fx 'ensartethed').

### Filmen *Her* (2013) og *Ex Machina*
- Brugt som diskussionsanker: hvornår vil systemer som Samantha (sprogprogrammet i *Her*) være muligt?
- *Ex Machina*: en Turing-test med en robot.

### Uncanny Valley (Masahiro Mori, 1970)
- Hypotese om at en enhed der ser **næsten** menneskelig ud fremkalder uhyggelige følelser.

---

## Trekanten: KI ↔ Computerteknologi ↔ Robotteknologi

Tre teknologier der ifølge Krüger udvikler sig i tæt samspil. Slidene gennemgår trekanten i fire historiske faser.

---

## Fase 1 — Indtil 2. Verdenskrig

### Robotter i mytologi og litteratur
- **Talos** (græsk mytologi): gigantisk bronze-automat, der beskyttede Europa (kongedatter fra Tyros) på Kreta mod pirater. *(Filmen Jason and the Argonauts, 1963.)*
- **Golem** (jødisk mytologi): skabning af dødt materiale, givet liv ved Guds hemmelige navn. Versioner i Worms (12. årh.) og **Prag (1580)**.
- **Frankenstein** (Mary Shelley, 1818) — *Frankenstein; or, The Modern Prometheus*.
- **R.U.R.** — *Rossum's Universal Robots* (Karel Čapek, **1920**). Første brug af ordet "robot". Kunstige væsener gør oprør og arver jorden (motiv senere i *Blade Runner*; relateret til posthumanisme).

### Tidlige regnemaskiner
- **Leibniz' regnemaskine** (Gottfried Wilhelm Leibniz, 1646–1716): mekanisk; alle fire grundlæggende aritmetiske operationer. Det indviklede gear var ustabilt.
- **Babbages Analytical Engine** (Charles Babbage, 1791–1871): mekanisk regnemaskine til generelle anvendelser. Skulle drives af dampmaskine, 55.000 dele, 19 meter lang. Input: hulkort. **1878:** udvalg anbefalede ikke at bygge den; designet blev glemt.
- **"Skaktyrken"** (1770): foregav at være skakspillende maskine. Afsløret som svindel i **1820'erne**. Brændt 1854.

### Fakes i dag
- Optimus/Tesla-demonstrationer kan være styret af mennesker via teleoperator-headsets.

---

## Fase 2 — 1940–1956: Begyndelsen

### Forløbere under 2. Verdenskrig
- **Enigma:** elektromekanisk chiffermaskine, tysk militær. Tyskerne troede koden var umulig at knække — de tog fejl. Svaghed: et bogstav kunne ikke krypteres som sig selv.
- **Turing-bomben** (1940): elektromekanisk simulation af flere Enigma-maskiner. Brugt af britiske kryptologer. *(Film: The Imitation Game.)*

### Computer (definition)
En enhed der behandler data ved hjælp af programmerbare beregningsregler:
- Input-enhed(er) (fx tastatur).
- Bearbejdningsenhed (processor + hukommelse).
- Baggrundslager.
- Output-enhed(er).

### Turingmaskinen
Matematisk model. Opererer på et uendeligt hukommelsesbånd; kan implementere enhver computeralgoritme.

### De første rigtige computere
- **Z3** (Konrad Zuse, **1941**): første fungerende, programmerbare, fuldt automatiske maskine.
- **ENIAC** (Electronic Numerical Integrator and Calculator, **1945**): første amerikanske computer. 150 m², 30 tons. Programmer fastlagt ved kabler.

### Tidlige KI-succes: skak
- **MANIAC** computer (1951): tidlig skakcomputer.
- **IBM's Deep Blue** vinder mod **Garry Kasparov** i 1997. (Allerede beskrevet som "menneskehedens ydmygelse" i [[05_Emne1_HvadErVidenskabsteori]].)

### Transhumanisme / posthumanisme — begrebsindførelse
- Begrebet **transhumanisme** stammer fra **1957**, hvor biologen **Julian Huxley** brugte det i en artikel om biologiens nye muligheder.
- **AI takeover:** scenario hvor AI bliver dominerende intelligensform på Jorden. Stephen Hawking og Elon Musk har advokeret forsigtighedsforanstaltninger.

### Skakanalogi: hvorfor er det "let"?
- Diskret tilstandsrum (64 felter, 24 figurer).
- Figurernes bevægelser entydigt defineret.
- Klart hvornår man har vundet/tabt.
- Skak = perfekt eksempel på et **symbolsk system**.

**Komparativt eksempel: abeeksperimenter (Köhler):** Wolfgang Köhler studerede chimpansers løsning af stable-kasser-problemer (1963). *Ingen* robotter løser i dag denne type opgave uden masser af speciel programmering. Pointen: skak er nemt — fysisk verden er svært.

> "Hvad er sværest? At vinde mod Magnus Carlsen i skak, eller at tage en banan fra et højt sted?"

### Hjernen og neuroner
- Antal neuroner: ca. 10¹²
- Antal synapser: ca. 10¹⁵
- Hver neuron har i gennemsnit ~1000 synapser.
- Total længde af neurale forbindelser: > 100.000 km.
- Cortex organiseret som "kort" (homunculus); hænder og mund tager uforholdsmæssigt meget plads.

### Norbert Wiener: Palomilla (1949)
En af de første robotter. Kunne bevæge sig **mod** lys (som møl) eller **væk** fra lys (som insekt). Et af de første kunstige væsener der simulerede adfærd via integreret kredsløb.

### Kunstig neuron — McCulloch-Pitts (1943)
Simpel model af en neuron, stadig i brug:
- Inputs *x₁, x₂, …, xₙ* med vægte *w₁, w₂, …, wₙ*.
- z = Σ wᵢxᵢ; output y = H(z) (tærskelfunktion).

### Robot (definition)
- DK: *"En programmerbar maskine, der ved interaktion med sine omgivelser autonomt kan udføre en mangfoldighed af opgaver."*
- EN: *"An autonomous machine capable of sensing its environment, carrying out computations to make decisions, and performing actions in the real world."*

---

## Fase 3 — 1957–1984: Kampen mellem symbolsk og subsymbolsk KI

### Dartmouth-mødet (1956)
**John McCarthy** og **Marvin Minsky** mønter termet "artificial intelligence" i 1956. Hensigten: at modsætte sig den tidlige kybernetiks konnektionisme. **Symbolsk** AI: implementér regler i computere via programmer — manipulér højniveau-repræsentationer.

### Symbolsk vs. subsymbolsk
| Symbolsk tilgang | Subsymbolsk tilgang |
|---|---|
| Intelligens = diskrete symboler i formelle systemer | Behandling starter med sensorisk information |
| Skakcomputere, ekspertsystemer | Kunstige neurale netværk |

### Industrial Robotics
- **Unimate** (1961): første industrirobot, arbejdede på General Motors-samlebånd.
- 1973: første industrirobot med seks frihedsgrader.

### Ekspertsystemer
- Computerprogram der kan støtte eller udføre beslutnings- eller diagnoseprocesser som en menneskelig ekspert.
- De første kom allerede i 1950'erne.
- Eksempel: **MYCIN** (1970) — klassifikation af bakterier.
- Algoritmer baseret på symbolske regler.
- LISP-maskine Symbolics 3640 (1984).

### Subsymbolsk: kunstige neurale netværk
- McCulloch-Pitts-neuron (1943).
- Sigmoid-funktioner i stedet for tærskelfunktioner.
- **Hebbs regel:** "Neurons that fire together, wire together." (Donald Hebb, 1949 — slidene viser ikke årstal eksplicit, men reglen er fra 1949.)
- **Perceptron** (Frank Rosenblatt, 1957).
- **Backpropagation** (1970–1982): metode til at træne feed-forward neurale netværk via gradient af fejlmål.

### Første store angreb på neurale netværk
**Marvin Minsky og Seymour Papert** (1969): bogen *Perceptrons: An Introduction to Computational Geometry*. MIT Press.
- Slidene karakteriserer dette som "klog populisme: lav en korrekt udtalelse, som offentligheden dog vil overse, og dermed sikre finansiering i de næste 10 år."
- Bogen viste begrænsninger ved perceptroner (kunne fx ikke løse XOR).

### GOFAI
- "Good Old-Fashioned Artificial Intelligence."
- **John Haugeland**, *Artificial Intelligence: The Very Idea* (1985).

---

## Fase 4 — 1985–2005: Evolutionære fremskridt og bias/variance-dilemmaet

### Personal Computer og WWW
- **IBM PC (model 5150)** — 1981.
- **WWW** offentligt tilgængeligt fra 1990.

### Robotik
- **Asimo** (Honda, 2000–2022): humanoid robot.
- Kameraer kommer ind i robotløsninger.

### Status for KI
Mange forskellige metoder i brug:
- Support Vector Machines (SVM)
- Neurale netværk
- Statistiske metoder
- K-Nearest Neighbor (KNN)
- Meget tid gik til data pre-processing.

**Det store gennembrud kommer ikke i denne periode.**

### Andet store angreb på neurale netværk: Bias/variance-dilemmaet (1992)
**Geman, Bienenstock, Doursat:** *"Neural networks and the bias/variance dilemma"*, *Neural Computation* 4:1–58.
> *"Inferring this complexity from examples, that is, learning it, although theoretically achievable, is, for all practical matters, not feasible: too many examples would be needed."*

---

## Fase 5 — 2005–nu: Deep Neural Networks tager over

Tre faktorer der løser problemet:

1. **Deep Learning** (algoritmiske gennembrud).
2. **GPUs** (parallel processering, grafikkort).
3. **Big Data** (1 ZB = 10²¹ bytes).

### Hvorfor virker det nu?
Bias/variance-dilemmaet løses af **massive datamængder**. Geman et al. (1992) sagde "too many examples would be needed" — Big Data leverer netop dette.

### Mange succesrige applikationer med én dominerende metode
Deep Neural Networks dominerer billedgenkendelse, talegenkendelse, oversættelse osv.

### Robotteknologi i dag
- **Autonome biler.**
- **Cobots** (Universal Robots, dansk succes).

### Five reasons why robots won't take over the world (theconversation.com, 18.4.2018)
1. Mangler menneskelignende hænder.
2. Ingen pålidelig taktil perception.
3. Kompleksitet i kontrol ved manipulation.
4. Kompleksitet i menneske-robot-interaktion.
5. Mennesker kan altid beslutte sig for ikke at bruge en bestemt teknologi.

---

## ChatGPT og embodiment

### ChatGPT (gentaget her i kontekst)
Krüger spørger: ChatGPT klarer abeeksperimenterne (Köhler) som tankeeksperiment, men ikke i den fysiske verden.

### Embodiment-problemet
> *"GPT-3 ... doesn't have the foggiest idea what any of those words mean to a human being. Humans are biological entities that evolved with bodies that need to operate in the physical and social worlds."*

### Human-Robot Interaction (HRI)
- HCI (Human-Computer Interaction) er blevet stadig mere sofistikeret (ChatGPT).
- **Meningsfuld interaktion** mellem mennesker og kropsliggjorte agenter er endnu ikke vist mulig.
- Problemer: sociale signaler, opmærksomhed, håndtering af "personligt rum", socially aware navigation.

### Personal assistants og fremtiden
- Et "mere realistisk billede af fremtiden" end Hollywood-versionerne.

### Moores lov
- Hastigheden af computerprocessorer fordobles hver 18. måned.
- **Gordon Earle Moore** (født 1929), medstifter af Intel.

### Superintelligens
- En hypotetisk agent med intelligens langt over de mest begavede menneskelige sind.
- Survey af de 100 mest citerede AI-forfattere (maj 2013): hvornår vil maskiner kunne udføre de fleste menneskelige erhverv mindst lige så godt som et typisk menneske?
  - 10 % sikkerhed: 2024
  - 50 % sikkerhed: 2050
  - 90 % sikkerhed: 2070

### Reference til pensum-artikel
Slidene refererer eksplicit til [[01_Amato_DataWillSolveRobotics]] (Amato et al., ICRA 2025-debatten). Opgaven: læs indledningen samt Animesh Garg og Aude Billard.

---

## Nøglepersoner

### Pionerer
- **Alan Turing** (1912–1954) — Turing-test, Turingmaskine, Enigma-knækning.
- **Norbert Wiener** — kybernetik; Palomilla-robot (1949).
- **John McCarthy** og **Marvin Minsky** — mønter "AI" 1956 (Dartmouth-mødet).
- **Warren McCulloch** og **Walter Pitts** (1943) — første neuron-model.
- **Donald Hebb** — Hebbs regel.
- **Frank Rosenblatt** (1957) — Perceptron.
- **Konrad Zuse** — Z3 (1941).
- **Gordon Moore** (1929–) — Moores lov, Intel-medstifter.
- **Wolfgang Köhler** (1963) — abeeksperimenter (*Intelligenzprüfungen am Menschenaffen*).
- **Masahiro Mori** (1970) — Uncanny Valley.
- **Karel Čapek** (1920) — R.U.R., termet "robot".
- **Mary Shelley** (1818) — *Frankenstein*.
- **Gottfried Wilhelm Leibniz** (1646–1716) — regnemaskinen.
- **Charles Babbage** (1791–1871) — Analytical Engine.

### Kritikere af neurale netværk
- **Minsky & Papert** (1969) — *Perceptrons*.
- **Stuart Geman, E. Bienenstock, R. Doursat** (1992) — bias/variance-dilemmaet.

### Forskere i pensum-artikler refereret af slides
- **Melanie Mitchell** — citeret om LLM'er; også omtalt i [[03_Biever_AIIntelligenceTest]].
- **Animesh Garg, Aude Billard, Daniela Rus, Russ Tedrake, Frank Park** — debattører fra [[01_Amato_DataWillSolveRobotics]].

### Filosofiske/sociale figurer nævnt
- **Julian Huxley** (1957) — termet "transhumanisme".
- **John Haugeland** (1985) — "GOFAI".
- **Stephen Hawking** og **Elon Musk** — AI-takeover-forsigtighed.
- **Garry Kasparov** — taber mod Deep Blue (1997).
- **Magnus Carlsen** (Elo-rating 2831 i 2025) — sammenligning med skakcomputere.
- **Erik Brynjolfsson** — citeret om skak/AI-udvikling.

---

## Centrale begreber

- **LLM (Large Language Model):** Genererer plausible næste ord baseret på statistiske korrelationer.
- **Embodiment:** Det at være kropsligt situeret i den fysiske verden.
- **Symbolsk AI:** Manipulation af diskrete symboler i formelle systemer.
- **Subsymbolsk AI:** Behandling der starter med sensorisk information; neurale netværk.
- **Turingmaskine:** Matematisk model af beregning.
- **Turing-test:** Test for intelligens via skelnen mellem menneske og maskine.
- **Loebner-prisen:** Årlig Turing-test-konkurrence (1990–2020).
- **Uncanny Valley:** Følelse af uhygge ved næsten-menneskelige objekter.
- **Perceptron (Rosenblatt 1957):** Enkelt-lags neuralt netværk.
- **McCulloch-Pitts neuron (1943):** Tærskel-baseret kunstig neuron.
- **Hebbs regel:** Læringsregel for neurale netværk; synapser styrkes når neuroner fyrer sammen.
- **Backpropagation:** Træningsmetode for feed-forward neurale netværk via gradient.
- **GOFAI:** "Good Old-Fashioned AI"; symbolsk paradigme.
- **Bias/variance-dilemma:** Begrænsning af neurale netværk; løses kun med massive data.
- **Big Data:** Datamængder i størrelsen zettabytes (10²¹).
- **GPU:** Grafikkort; muliggør parallel processering i deep learning.
- **Deep Neural Network:** Neuralt netværk med mange skjulte lag.
- **Ekspertsystem:** Computerprogram der efterligner ekspertbeslutninger.
- **Moores lov:** Processorhastighed fordobles hver 18. måned.
- **Superintelligens:** Hypotetisk agent langt over menneskelige evner.
- **Transhumanisme / posthumanisme:** Bevægelser om at overskride menneskelige grænser via teknologi.
- **AI takeover:** Scenario hvor AI bliver dominerende intelligensform.
- **HRI (Human-Robot Interaction) / HCI (Human-Computer Interaction):** Forskningsfelter.
- **Robot (definition):** Programmerbar, autonom maskine der interagerer med sine omgivelser.
- **Cobot:** Kollaborativ robot (designet til at arbejde sammen med mennesker; jf. Universal Robots).
- **Elo-rating:** Statistisk metode til at måle styrkeforskel i to-personers spil.

---

## Mine observationer (som læser)

- Slidene tegner et bemærkelsesværdigt **cyklisk** billede: neurale netværk gennemgår to "angreb" (Minsky/Papert 1969 og Geman 1992) og kommer hver gang stærkere tilbage. Det er en illustration af [[07_Emne4_EuklidEinsteinKuhn|Kuhns]] mønster, men også af noget mere prosaisk: ingen vinder en gang for alle.
- Skak vs. abeeksperiment-pointen er central: vi har systematisk **undervurderet** den fysiske verdens kompleksitet relativt til den symbolske verden — det er præcis det punkt der genfindes i [[01_Amato_DataWillSolveRobotics|Amato-debatten]] (Tedrakes æble-pointe; Park's kok-skærer-gulerod-eksempel).
- Krügers periodisering (1940–1956, 1957–1984, 1985–2005, 2005–) er ikke standard, men den fungerer pædagogisk fordi den følger **paradigme-skifter** mere end teknologiske milepæle.
- Det er værd at bemærke at slidene flere steder eksplicit henviser til pensum-artiklerne (Biever, Amato) — slidene og artiklerne supplerer hinanden, snarere end at duplikere.
