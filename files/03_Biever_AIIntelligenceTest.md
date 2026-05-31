---
title: "The Easy Intelligence Tests That AI Chatbots Fail"
author: Celeste Biever
publication: Nature
volume: "619"
date: 2023-07-27
type: Feature article
tags: [AI, LLM, GPT-4, benchmarks, Turing-test, abstraktion, ConceptARC]
---

# The Easy Intelligence Tests That AI Chatbots Fail

> Nature-feature af **Celeste Biever** (Nature's chief news and features editor) om hvordan forskere kæmper med at finde nye måder at klargøre forskellene mellem menneskelige og LLM-evner.

---

## Hovedpåstand

Verdens bedste AI-systemer kan klare svære eksamener, skrive overbevisende menneskelignende essays og chatte så flydende, at mange ikke kan skelne dem fra mennesker. **Hvad kan de ikke?** Løse simple visuelle logiske puslespil. GPT-4 får knap 1/3 af opgaverne rigtige i én kategori, så lidt som 3 % i en anden — opgaver som mennesker scorer omkring 91 % på.

Artiklen behandler en konundrum: testet på én måde virker LLM'er imponerende; testet på en anden måde har de glaringe blinde pletter og kan ikke ræsonnere om abstrakte begreber.

---

## Kernekonflikt i feltet

Tomer Ullman (Harvard, kognitionsforsker): To lejre med modstridende synspunkter på hvad der foregår "under motorhjelmen" i LLM'er.
- **Lejr 1:** Algoritmernes præstationer skyldes glimt af ræsonnement og forståelse.
- **Lejr 2** (Ullman, Mitchell): Meget mere forsigtige.

> *"There's very good smart people on all sides of this debate... There's no Geiger counter we can point at something and say 'beep beep beep — yes, intelligent'."* — Ullman

Tests som de visuelle logikpuslespil, der afslører forskelle, er et skridt i den rigtige retning — accepteret af begge lejre.

---

## Turing-testen — er den død?

- Foreslået af **Alan Turing** i 1950 som "imitation game".
- Senere kom **Loebner Prize** (finansieret af Hugh Loebner) — årlig konkurrence; stoppede i 2019 efter Loebners død og pengemangel.
- **Rob Wortham** (UK Society for Study of AI; medkonsdirektør): LLM'er ville nu sandsynligvis bestå Turing-testen i populær forstand.
- **AI21 Labs-spil (maj 2023):** Over 1,5 mio. spillere; chattede 2 minutter med enten et menneske eller en LLM-bot. Korrekt identifikation af bots: kun **60 %** — ikke meget bedre end tilfældighed.
- **François Chollet** (Google): Han ville stadig nemt kunne afsløre en LLM ved at presse den uden for sin trænings­distribution. Hans kritik: Turing-testen incentiviserer udviklerne til at lære AI'er tricks i stedet for at udvikle reelle evner.

---

## Faldgruber ved benchmarks

OpenAI testede GPT-4 på mange benchmarks (læseforståelse, matematik, kodning) + 30 eksamener (Advanced Placement, lægeprøver, GRE, Uniform Bar Exam — top 10 % blandt mennesker).

**Problemer:**
1. **Kontaminering:** Modellerne kan have set lignende spørgsmål i træningsdata. OpenAI tjekkede for ordstrenge — Sam Bowman mener at det "complicates the claims a little bit, but I don't think it really changes the big picture that much."
2. **Skrøbelighed:** Mitchell ændrede let på et MBA-eksamensspørgsmål ChatGPT havde bestået → ChatGPT dumpede den omformulerede version.
3. **Ingen generalisering:** Hos mennesker indikerer høje eksamensresultater "general intelligens"; for LLM'er gælder den ekstrapolering ikke nødvendigvis.

> *"Extrapolating in the way that we extrapolate for humans won't always work for AI systems."* — Mitchell

**Hvorfor?** LLM'er lærer kun fra sprog; uden embodied erfaring forstår de ikke ord på samme måde som mennesker. På den anden side har de evner mennesker ikke — kender forbindelser mellem næsten alle ord, hvilket lader dem løse problemer ved sproglige særheder.

**Nick Ryder (OpenAI):** *"I don't think that one should look at an evaluation of a human and a large language model and derive any amount of equivalence."* OpenAI's scores er udsagn om hvordan modellen klarer den specifikke opgave, ikke menneskelignende kapacitet.

---

## Bubeck et al.: "Sparks of AGI" (marts 2023)

**Sébastien Bubeck** (Microsoft Research) m.fl. publicerede preprint *"Sparks of Artificial General Intelligence: Early experiments with GPT-4"*.
- Tidlig version af GPT-4 viste overraskende evner — bl.a. **theory of mind**-tests (psykologernes tests for at forudsige andres mentale tilstande).
- Bubeck til Nature: *"GPT-4 certainly does not think like a person, and for any capability that it displays, it achieves it in its own way."*

**Kritik fra Mitchell:** *"It's more like anthropology"* — ikke en systematisk undersøgelse.

**Ullman:** For at blive overbevist om at en maskine har theory of mind, skal han se bevis for en underliggende kognitiv proces — ikke blot at den giver samme svar som et menneske.

---

## ARC og ConceptARC

### ARC (Abstraction and Reasoning Corpus)
- Skabt af **François Chollet** i 2019.
- Visuelle puslespil: solvere ser flere demonstrationer af gitter, der ændres efter en regel, og skal vise reglen ved at forudsige næste transformation.
- *"It is supposed to test for your ability to adapt to things you have not seen before."* — Chollet
- **Brenden Lake** (NYU): fanger "hallmark of human intelligence" — abstraktion fra hverdagsviden anvendt på nye problemer.
- **2020-konkurrence** (før LLM'er var store): Vinder-bot (specifikt trænet på ARC) fik **21 %** rigtigt. Mennesker: **80 %**.

### ConceptARC (Mitchell et al., 2023)
- Mitchells team lavede en let modificeret version:
  1. **Lettere** — så den ikke missede småfremskridt hos maskinerne.
  2. **Konceptbaseret** — specifikke koncepter testet via mange variationer (fx "sameness" testet via flere puslespil: at beholde objekter med samme form, eller objekter på samme akse). Dette reducerer chancen for at klare testen uden at gribe konceptet.
- **Resultater:**
  - Mennesker (400 online): **91 %** gennemsnit på alle koncept-grupper; **97 %** på én.
  - GPT-4: 33 % på én gruppe; under 30 % på alle øvrige.
  - De bedste specialbots fra Chollets konkurrence: bedre end GPT-4, men dårligere end mennesker (top 77 % på én kategori, under 60 % på de fleste).

### Kritik fra Sam Bowman
- ConceptARC er skewed mod GPT-4 — bl.a. fordi det er en visuel test, og den offentlige version af GPT-4 kun tog tekst (forskerne måtte give arrays af tal som inputs).
- Mitchell venter på offentlig version af **multimodal GPT-4**, men forventer ikke stor forbedring.

### Andre tests
- **Sam Acquaviva** (MIT): et andet hold testede GPT-4 på **1D-ARC** (mønstre i én række) — formodet at fjerne den visuelle ulempe. GPT-4 forbedrede sig, men ikke nok til at sandsynliggøre at den greb den underliggende regel.

---

## Argument for ræsonnement: Othello-eksperimentet

**Kenneth Li** (Harvard) m.fl.: Trænede en LLM på lister af træk i en digital version af brætspillet **Othello**. Modellen blev god til at foreslå lovlige næste træk.

Forskerne argumenterede for at **modellen holdt styr på brættets tilstand** — byggede en intern repræsentation af verden snarere end blot at producere overfladiske tekstforslag.

**Sam Bowman:** Mener at det samlede bevis tyder på, at LLM'er har erhvervet **mindst en rudimentær evne** til at ræsonnere om abstrakte begreber — "spotty" og mere begrænset end hos mennesker, men forbedres med modelstørrelse. Forventer at fremtidige LLM'er bliver bedre. *"The basic capacity is there."*

---

## Konklusion og perspektiver

- Enighed på tværs af lejrene: at finde den bedste måde at teste LLM'er for abstrakt ræsonnement er et åbent problem.
- **Michael Frank** (Stanford): forventer ikke én catch-all test — "no Rubicon, no one line." Mange tests er nødvendige.
- **Wortham:** advarer mod "the curse of anthropomorphization":
  > *"We anthropomorphize anything which appears to demonstrate intelligence... It is a curse, because we can't think of things which display goal-oriented behaviour in any way other than using human models."*

---

## Nøglepersoner

### Forskere fokuseret på begrænsninger ved LLM'er

- **Melanie Mitchell** (Santa Fe Institute) — computerforsker; hendes team lavede **ConceptARC**; central kritisk stemme.
- **Tomer Ullman** (Harvard) — kognitionsforsker; "no Geiger counter for intelligence"; kritisk over for theory of mind-påstande om LLM'er.
- **François Chollet** (Google, Seattle) — software­ingeniør; skabte **ARC** i 2019; kritisk over for Turing-testen og blind skalering af deep learning.
- **Brenden Lake** (NYU) — kognitiv computational scientist; LLM'er har "very fluent language without genuine understanding".
- **Michael Frank** (Stanford) — kognitionsforsker; ingen enkelttest vil erstatte Turing-testen.
- **Sam Acquaviva** (MIT) — computational cognitive scientist; testede GPT-4 på 1D-ARC.
- **Rob Wortham** — co-director, UK Society for the Study of Artificial Intelligence and Simulation of Behaviour; medvirkede ved Loebner Prize indtil 2019; advarer mod antropomorfisering.

### Forskere mere positive over for LLM-kapaciteter

- **Sam Bowman** (NYU & Anthropic) — sprogteknolog; argumenterer at LLM'er har basal ræsonnementsevne; refererer til Kenneth Lis Othello-arbejde.
- **Sébastien Bubeck** (Microsoft Research, Redmond) — forfatter til "Sparks of AGI"-preprint; mener tidlig GPT-4 var en "early (yet still incomplete) version of an AGI system".
- **Kenneth Li** (Harvard) — viste at en LLM trænet på Othello-træk bygger interne brætrepræsentationer.

### Repræsentanter for OpenAI

- **Nick Ryder** (OpenAI) — forsker; understreger at evalueringerne ikke skal sammenlignes med menneskelige scores.

### Historiske personer

- **Alan Turing** (1950) — britisk matematiker; foreslog "imitation game" / Turing-testen.
- **Hugh Loebner** — forretningsmand og filantrop; finansierede Loebner Prize indtil sin død.

---

## Nøglebegreber

- **LLM (Large Language Model):** Stor sprogmodel, der genererer plausible næste ord baseret på statistiske korrelationer fra milliarder af sætninger.
- **GPT-4:** Den mest avancerede version (på artiklens tidspunkt) af systemet bag ChatGPT og Bing.
- **Chatbot:** LLM med ekstra menneskelig feedback-træning ("RLHF" implicit).
- **Turing-test / imitation game:** Test fra 1950 hvor en menneskelig dommer holder tekstsamtaler med en skjult computer og person og forsøger at skelne dem.
- **Loebner Prize:** Årlig Turing-test-konkurrence (1991–2019).
- **Benchmark:** Standardiseret test af AI-systemers ydeevne på specifikke evner.
- **Kontaminering (training data contamination):** Når modellen har set testspørgsmålene (eller meget lignende) i sine træningsdata → boostet score uden reel forståelse.
- **Theory of mind:** Evnen til at forudsige og ræsonnere om andres mentale tilstande.
- **AGI (Artificial General Intelligence):** Kunstig generel intelligens — AI med menneskelignende bredde og adaptivitet.
- **Generel intelligens:** Evnen til at præstere godt på tværs af mange opgaver og tilpasse sig forskellige kontekster.
- **ARC (Abstraction and Reasoning Corpus):** Chollets test fra 2019 — visuelle gitter-puslespil til at teste evnen til at tilpasse sig nye problemer.
- **ConceptARC:** Mitchell-teamets variant af ARC — lettere, men struktureret omkring specifikke koncepter testet via variationer.
- **1D-ARC:** Variant hvor mønstre er begrænset til én række — for at fjerne den visuelle ulempe.
- **Embodied / embodiment:** At være kropsligt situeret i den fysiske verden; vigtigt for hvordan mennesker forstår sprog (i kontrast til rene tekstbaserede LLM'er).
- **Multimodal model:** Model der kan tage flere typer input (fx tekst + billede).
- **Anthropomorphization:** At tilskrive maskiner menneskelignende egenskaber baseret på overfladiske ligheder; advarsel mod denne fælde fra Wortham.
- **Othello-eksperimentet:** Test af om en LLM bygger interne brætrepræsentationer snarere end blot at producere statistisk plausible sekvenser.
- **Sparks of AGI:** Bubecks 2023-preprint om GPT-4's overraskende evner — kontroversiel påstand om at GPT-4 udviste "tidlige (men ufuldstændige) tegn på AGI".

---

## Centrale referencer (numerering fra artiklen)

1. Moskvichev, Odouard, Mitchell — ConceptARC. arXiv:2305.07141 (2023).
2. Turing, *Mind* LIX, 433–460 (1950).
3. Jannai, Meron, Lenz, Levine, Shoham (AI21 Labs). arXiv:2305.20010 (2023).
4. OpenAI. arXiv:2303.08774 (2023).
5. Bubeck et al. "Sparks of AGI." arXiv:2303.12712 (2023).
6. Chollet — ARC. arXiv:1911.01547 (2019).
7. Johnson, Vong, Lake, Gureckis. arXiv:2103.05823 (2021).
8. Xu et al. 1D-ARC. arXiv:2305.18354 (2023).
9. Li et al. — Othello-eksperimentet. ICLR Proc. (2023).

---

## Mine observationer (som læser)

- Artiklen rammer en interessant balance: viser både LLM'ernes imponerende rækkevidde og deres skrøbelighed.
- Wormhams advarsel mod antropomorfisering er sandsynligvis det mest holdbare metodologiske point: vi har svært ved at tale om mål-orienteret adfærd uden menneskelignende sprog.
- ConceptARC-testen er metodologisk interessant fordi den **kontrollerer for konceptforståelse via variationer** — ikke kun via succes/fiasko på enkeltopgaver. Det er en design-pointe, der kunne udvides til andre evner.
- Spørgsmålet om kontaminering er stadig delvist åbent; OpenAI's tjek baseret på "lignende strenge" virker overfladisk.
- Det er bemærkelsesværdigt at artiklen er fra **juli 2023** — feltet har bevæget sig hurtigt siden. Mange af de specifikke påstande om GPT-4's kapaciteter er nu daterede, men de metodologiske pointer om evaluering består.
