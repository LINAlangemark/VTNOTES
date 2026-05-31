---
title: "Data will solve robotics and automation: True or false?"
authors: [Nancy M. Amato, Seth Hutchinson, Animesh Garg, Aude Billard, Daniela Rus, Russ Tedrake, Frank Park, Ken Goldberg]
publication: Science Robotics
volume: "10, eaea7897"
date: 2025-08-27
type: Viewpoint / Debat
tags: [robotik, AI, foundation-models, paradigmeskifte, ICRA, debat]
---

# Data will solve robotics and automation: True or false? — A debate

> Et redaktionelt referat af en konference-debat afholdt ved IEEE International Conference on Robotics and Automation (ICRA) 2025 i Atlanta, 26.–29. maj 2025. Seks førende forskere debatterer den langsigtede indflydelse af model-frie metoder, som bruger store mængder demonstrationsdata til at træne generative modeller til robotstyring.

---

## Overordnet kontekst og rammesætning

Robotikfeltet oplever, hvad videnskabshistorikeren **Thomas Kuhn** ville kalde et "paradigmeskifte". Siden 2012 har dybe neurale netværk + store datamængder + GPU'er givet gennembrud i computer vision og talegenkendelse. Med ChatGPT (2022) og store vision-language modeller (VLMs) er der opstået et "end-to-end" / model-frit paradigme, der udfordrer den klassiske algoritmiske ("model-baserede") tilgang.

Debatten formuleret af Goldberg:
> "Will the future of robotics and automation be written in code or in data? Is the Handbook of Robotics obsolete? Are home humanoids overhyped? Join us for a high-voltage debate about physics vs pixels, theory vs terabytes."

Tre deltagere argumenterede for **TRUE** (Garg, Rus, Tedrake) og tre for **FALSE** (Billard, Kaelbling, Park) i klassisk Oxford-debat stil. Over 1000 tilskuere. Resultatet: få ændrede holdning, men alle blev tvunget til at tænke dybere. Flere af debattørerne udtrykte respekt for **hybride metoder**.

Debatten fokuserede på software/styring og berørte ikke hardware, materialer, design eller indsamling af datasæt.

---

## Synspunkter — individuelt

### Animesh Garg (TRUE) — "Data er ikke blot fordelagtige, men uundværlige og fundamentale"

**Hovedpåstande:**
- Menneskeheden har ofte udviklet *know-how* før *know-why* (metalbearbejdning, sejlskibe, forbrændingsmotorer, fly).
- Vi opbygger nu "computational and physical intelligence" via data-drevne empiriske metoder.
- Fire kritiske perspektiver:
  1. **Generel intelligens** i fysiske robotter er tvetydig og under-specificeret. Data giver vejledning til "distributional similarity" når lukket-form løsning for sund fornuft mangler.
  2. **Nøjagtige modeller fremmer innovation** — ufuldstændige modeller hindrer opdagelse af ægte optima.
  3. Robotik er **udviklingen af computing** ud i den fysiske verden — vi må anvende abstraktionsprincipper fra andre computing-domæner.
  4. Data har **forenet diverse problemer** i sprog og vision; "foundation model perspektivet" kunne forene robotik.

### Aude Billard (FALSE) — "Modeller giver mening til data"

**Hovedpåstande:**
- Al videnskab er funderet i data, men data alene er ikke nok.
- **Astronomi-analogi:** Millioner ser himlen, men det var astronomerne, der med få men omhyggeligt indsamlede datapunkter og ved konstant vekselvirkning mellem hypotetiske modeller og data afkodede fysikkens love.
- Robotik forsøger at gøre alt på én gang — drømmer om et magisk værktøj, der kan styre alle robotkroppe og endow dem med LLM-niveau kognition.
- Hvis robotik lykkes via ren computerkraft anvendt på store datasæt **uden** udvikling af underliggende teoretiske principper, så bliver *Springer Handbook of Robotics* ikke forældet — det bliver vores eneste tilbageværende ressource, fordi vi ikke længere kan producere ny teori.
- Hvad der betyder noget er **samspillet** mellem dataindsamling og modeludvikling — ellers bygger vi blot endnu et Babelstårn.

### Daniela Rus (TRUE, men nuanceret) — "Vi har brug for begge dele"

**Hovedpåstande:**
- Tildelt at argumentere for TRUE, men hendes faktiske position er nuanceret: **både data OG matematiske modeller** er nødvendige.
- Fysik giver elegante modeller til simple opgaver (gribning, stabilisering). Når man forlader laboratoriet, kollapser antagelserne.
- Reelle opgaver er multimodale, kontekst-afhængige, fyldt med tvetydighed (bløde objekter, okkluderede syn, uforudsigelige mennesker).
- Data fanger virkelighedens kompleksitet; muliggør robotter, der responderer intelligent når noget går galt — ikke ved forprogrammerede regler men via tidligere erfaring.
- Eksempel: hendes lab har bygget et fysisk køkken-testbed med sensorer der opfanger kropsholdning, muskelaktivitet, kraftinteraktioner og blikretning under reelle opgaver.
- **Konklusion:** "Fremtiden for robotik vil blive drevet af ligninger ved siden af erfaring."

### Russ Tedrake (TRUE) — "Manipulation kræver sund fornuft; store data og store modeller kan give det"

**Hovedpåstande:**
- De næste mest virkningsfulde skridt mod at "løse" robotik ligger i storskala-dataindsamling og store fortrænede modeller.
- Hos Toyota Research Institute (TRI) har de set robotter programmeret via imitationslæring udføre fingerfærdige manipulationsopgaver, der var utænkelige få år tidligere.
- Storskala-fortræning fra diverse multitask-data er den bedste (eneste?) måde at programmere "sund fornuft" på.
- **Eksempel:** En bimanuel robot ved TRI lærte at kerne og skære æbler — ingen æbler er ens, og robotten viste imponerende subtile recovery-bevægelser når æblestykker gled eller skvattede.
- Disse recovery-bevægelser opstår nu automatisk via transfer fra demonstrationer på andre opgaver → det Tedrake kalder **sund fornuft for fingerfærdig manipulation**.
- At "løse" robotik er en meget langsigtet agenda. Vi er i tidlige, rodede faser. Optimistisk om at få teoremer engang, der vil guide os.

### Frank Park (FALSE) — "En mere jordnær strategi er nødvendig"

**Hovedpåstande:**
- Multimodale foundation modeller er et transformationsmoment, men at forvente en parallel revolution i robotik er **for tidligt** eller **ønsketænkning**.
- Robotik er et andet bæst: data er sparsomme, simuleringer er upålidelige, robotter har endeløs variation af miljøer/opgaver, og krav er ubønhørlige.
- Foundation modeller er værd at forfølge — men en mere jordnær strategi er nødvendig.
- Henviser til **Goyal & Bengio (2022):** bedre induktive biaser er nøglen til kognition på menneskeniveau.
- I robotik har vi allerede et væld af induktive biaser:
  - **Biologi:** menneskelig motorkontrol gennem abstraktionslag
  - **Fysik:** modeller af bevægelse, kraft, kompliance
  - **Geometri:** lavdimensionelle repræsentationer, udnyttelse af symmetrier
  - **Programmering:** motion description languages
- Eksempel: studér ikke endeløse timers video af rengøring — studér nuancerne i hvordan en kok skærer en gulerod (taktil feedback, kompliance i håndled/albue, komplekse kræfter).
- CNNs og transformere var ikke serendipitøse opdagelser fra blind skalering — de blev designet af forskere der forstod symmetri og ækvivarians.
- **Robotik fortjener intentionelt design**, ikke force-fitting af modeller udviklet til vision og sprog.

---

## Tværgående temaer

| Tema | TRUE-siden | FALSE-siden |
|------|------------|-------------|
| Data | Indispensable, fundamentale | Nødvendige men utilstrækkelige |
| Modeller | Udspringer af data | Giver mening til data |
| Sund fornuft | Læres via storskala-data | Kræver induktive biaser |
| Foundation modeller | Vejen frem | Premature; krav om "grounded strategy" |
| Hybrider | Bredt accepteret | Bredt accepteret |

---

## Nøglepersoner

### Moderatorer / arrangører
- **Nancy M. Amato** (University of Illinois) — co-chair ICRA 2025.
- **Seth Hutchinson** (Northeastern University) — co-chair ICRA 2025.
- **Ken Goldberg** (UC Berkeley) — moderator; aktiv i 40 år inden for model-baseret robotik og robotlæring; nyvalgt præsident for Robot Learning Foundation; formulerede debattens titel.

### TRUE-debattører
- **Animesh Garg** (Georgia Tech) — argumenterer for data som uundværlige; foundation-model perspektiv.
- **Daniela Rus** (MIT) — kendt for arbejde med soft robotics og embodied AI; argumenterer for hybrid tilgang.
- **Russ Tedrake** (MIT / Toyota Research Institute) — kendt for Underactuated Robotics og fysik-baseret control; nu fortaler for Large Behavior Models (LBM); forfatter til TRI LBM Team paper (arXiv:2507.05331).

### FALSE-debattører
- **Aude Billard** (EPFL) — kendt for learning from demonstration og menneske-robot interaktion.
- **Leslie Kaelbling** (MIT) — nævnt som debattør (skrev ikke selvstændigt afsnit i artiklen).
- **Frank Park** (Seoul National University) — kendt for geometriske metoder i robotik.

### Andre nævnte
- **Thomas Kuhn** — videnskabshistoriker; *The Structure of Scientific Revolutions* (1962); konceptet "paradigmeskifte".
- **Aniruddh Goyal & Yoshua Bengio** — forfattere til "Inductive biases for deep learning of higher-level cognition" (2022); refereret af Park.

---

## Nøgleord og definitioner

- **Model-baseret robotik:** Tilgang baseret på eksplicitte matematiske modeller (fysik, geometri, dynamik) og algoritmer; "physics, theory, code".
- **Model-fri robotik / End-to-end:** Tilgang hvor styringspolitikker læres direkte fra data (typisk demonstrationer) uden eksplicitte mellemmodeller.
- **Paradigmeskifte (Kuhn):** Fundamental ændring i de grundlæggende koncepter og eksperimentelle praksisser i en videnskabelig disciplin.
- **Foundation model:** Stor model fortrænet på brede data, som kan tilpasses mange nedstrøms-opgaver (jf. GPT, store VLMs).
- **VLM (Vision-Language Model):** Model der kombinerer billed- og sprogforståelse.
- **Imitation learning:** Læring fra demonstrationer (typisk menneskelige).
- **Multitask pretraining:** Fortræning på mange opgaver samtidigt for at opnå overførbar kompetence.
- **Common sense (i robotik):** Generisk situationsforståelse, der tillader robusthed under nye omstændigheder og recovery efter fejl.
- **Inductive bias:** Forudgående antagelser, præferencer eller strukturer indbygget i en model, som styrer hvad den lærer.
- **Generalizable autonomy:** Evnen til autonom adfærd, der generaliserer på tværs af opgaver og miljøer.
- **Self-supervised learning:** Læring uden eksplicit etiketterede data, ved at modellen genererer sine egne mål fra data-strukturen.
- **Large Behavior Model (LBM):** Tedrakes/TRI's term for store fortrænede modeller for fingerfærdig manipulation.
- **Equivariance / symmetry (CNN, transformer):** Strukturelle egenskaber der gør modeller robuste over for translation (CNN) eller permutation (transformer).
- **Motion description language:** Programmeringssprog der formaliserer manipulationsopgaver enhedsuafhængigt.

---

## Centrale referencer fra artiklen

1. T. Kuhn, *The Structure of Scientific Revolutions* (1962).
2. K. Goldberg, "How to close the 100,000 year data gap in robotics and automation?" *Sci. Robot.* 10, eaea7390 (2025).
3. R. Tedrake, "Multitask transfer in TRI's large behavior models for dexterous manipulation," Stanford-seminar, 25 april 2025.
4. TRI LBM Team, "A careful examination of large behavior models for multitask dexterous manipulation." arXiv:2507.05331 (2025).
5. A. Goyal, Y. Bengio, "Inductive biases for deep learning of higher-level cognition." *Proc. R. Soc. A* 478, 20210068 (2022).

Video af debatten: https://youtu.be/PfvctjoMPk8

---

## Mine observationer (som læser)

- Selvom debatten er polariseret i overskriften, ender alle reelt med en hybrid-position — uenigheden er om **vægtning og rækkefølge**, ikke om enten/eller.
- Rus' position er åbent erklæret som "nuanceret" på trods af tildelt TRUE-rolle — viser at en sand "ren" position er svær at forsvare.
- Park's pointe om at CNN/transformer ikke var serendipitøse er stærk: den minder os om, at induktive biaser har gjort den nuværende dyb læring mulig.
- Et tema ingen af debattørerne fuldt belyser: hvor kommer de massive demonstrationsdata fra, og hvad er omkostningerne ved at indsamle dem (jf. Goldbergs reference til "100,000 year data gap").
