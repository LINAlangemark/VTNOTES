Back to: [[00_Index]]

[[AmatoEtAl_DataWill_ICRA2025.pdf]]
[[Biever_TheEasyIntelligentTest_Nature2023.pdf]]
[[ANewHeavenAndNewEarth.pdf]]
[[Kennefick_Phystoday_2009.pdf]]


# Nye litteraturnoter — AI, robotteknologi og videnskabens fremkomst

tags:: #eksamen #litteratur #videnskabsteori #kunstig_intelligens #robotteknologi #videnskabshistorie #relativitetsteori #paradigmeskift

## Litteratur

### [[AmatoEtAl_DataWill_ICRA2025.pdf]]

source:: Nancy M. Amato, Seth Hutchinson, Animesh Garg, Aude Billard, Daniela Rus, Russ Tedrake, Frank Park & Ken Goldberg, “Data will solve robotics and automation: True or false?”, *Science Robotics*, 2025.  
type:: debat / viewpoint / robotteknologi  
keywords:: [[02_Emne_2_Datalogi_KI_og_robotteknologi|robotteknologi]], [[andre 1#data-driven robotics|data-driven robotics]], [[andre 1#model-free methods|model-free methods]], [[andre 1#model-based methods|model-based methods]], [[andre 1#foundation models|foundation models]], [[andre 1#demonstration data|demonstration data]], [[andre 1#imitation learning|imitation learning]], [[andre 1#inductive bias|inductive bias]], [[andre 1#embodied data|embodied data]], [[andre 1#dexterous manipulation|dexterous manipulation]], [[05_Emne_4_Euklid_Einstein_og_Kuhn|paradigmeskift]]

- Artiklen er en debat fra ICRA 2025 om, hvorvidt store datamængder og model-free metoder kan “løse” robotteknologi og automatisering.
- Introduktionen rammesætter robotforskningen som et muligt [[05_Emne_4_Euklid_Einstein_og_Kuhn|paradigmeskift]]: fra klassiske algoritmiske og [[andre 1#model-based methods|model-based]] tilgange mod datadrevne, [[andre 1#end-to-end learning|end-to-end]] systemer.
- Animesh Garg argumenterer for, at data er fundamentale, fordi fysisk intelligens, commonsense og generaliserbar autonomi er for komplekse til at specificere fuldt med lukkede matematiske modeller.
- Aude Billard argumenterer imod ideen om, at data alene kan løse problemet. Hendes pointe er, at data først får videnskabelig mening, når de kobles til modeller, hypoteser og forståelse.
- Daniela Rus indtager en mellemposition: robotter har brug for både fysiske/matematiske modeller og rige, multimodale erfaringsdata fra virkelige opgaver.
- Russ Tedrake fremhæver [[andre 1#imitation learning|imitation learning]], pretraining og store robotdatasæt som vejen til fysisk “common sense”, især i fleksibel manipulation.
- Frank Park advarer mod blind skalering. Han mener, at robotteknologi kræver stærkere [[andre 1#inductive bias|inductive biases]] fra fysik, geometri, biologi og kontrolteori.
- Vigtig pointe: teksten handler ikke bare om teknologi, men også om videnskabsteori — hvad tæller som forklaring, forståelse og gyldig viden, når systemer lærer fra data?
- Kritisk pointe: datadrevne modeller kan være stærke uden at være lette at forklare; klassiske modeller kan være forklarende, men for simple til komplekse hverdagsmiljøer.
- Eksamen-vinkel: brug teksten som case på nutidigt paradigmeskift i robotteknologi: [[andre 1#data-driven robotics|data-driven robotics]] udfordrer, men erstatter ikke nødvendigvis, klassisk modelbaseret ingeniørvidenskab.
- Kobling: passer godt sammen med Kuhn, fordi debatten viser en faglig kamp mellem to forskellige idealer for god videnskab: teori/modeller versus data/skalering.

Billard Astronomy Analogy:
> ([[AmatoEtAl_DataWill_ICRA2025.pdf#page=2&selection=91,0,109,40|AmatoEtAl_DataWill_ICRA2025, p.2]])
> Consider astronomy: It started off with the simple observation of the sky. But thousands of people look at the sky each day, and millions have before. Although they all marvel at its beauty, most of these people, if asked, would be incapable of explaining the reason why the stars are aligned as they are or distinguishing stars from planets. Astronomers from ancient civilizations ago did not use these millions of human eye observations to decipher the underlying laws of physics. Rather, they used few but meticulously gathered data points. Most importantly, they constantly went back and forth from building hypothetical models to data to test their theories. Some argue that what was true for hardcore science does not apply to robotics.

Garg, Foundation Models:
> ([[AmatoEtAl_DataWill_ICRA2025.pdf#page=2&selection=65,1,71,25|AmatoEtAl_DataWill_ICRA2025, p.2]])
> obotics remains a collection of disparate communities. A potential solution lies in adopting the foundation model perspective, which could unify many seemingly unrelated problems within the robotics community, given that all robots are governed by the same fundamental laws of physics.

End-to-end:
> ([[AmatoEtAl_DataWill_ICRA2025.pdf#page=1&selection=70,9,89,26&color=yellow|AmatoEtAl_DataWill_ICRA2025, p.1]])
> However, since 2012, advances in deep “neural” networks that combine unprecedented amounts of example data, advances in stochastic gradient descent techniques, and advances in computing, in particular GPUs (graphics processing units), have produced remarkable results in computer vision and speech recognition. And with the emergence of ChatGPT and associated large vision language models (VLMs) in 2022, with associated advances in natural language processing and denoising diffusion methods, the paradigm of “end-to-end” (also known as “modelfree”) approaches to perception and control suggest an entirely new, data-driven approach to robotics and automation


### [[Biever_TheEasyIntelligentTest_Nature2023.pdf]]

source:: Celeste Biever, “The easy intelligence tests that AI chatbots fail”, *Nature*, Vol. 619, 27 July 2023.  
type:: forskningsformidling / KI-benchmarking  
keywords:: [[02_Emne_2_Datalogi_KI_og_robotteknologi|Large Language Models / LLM]], [[02_Emne_2_Datalogi_KI_og_robotteknologi|Turing-testen]], [[andre 1#AI-benchmark|AI-benchmark]], [[andre 1#benchmarking|benchmarking]], [[02_Emne_2_Datalogi_KI_og_robotteknologi|ConceptARC]], [[andre 1#Abstraction and Reasoning Corpus|Abstraction and Reasoning Corpus]], [[andre 1#abstract reasoning|abstract reasoning]], [[andre 1#contamination|contamination]], [[andre 1#theory of mind|theory of mind]], [[andre 1#anthropomorphization|anthropomorphization]], [[02_Emne_2_Datalogi_KI_og_robotteknologi|Embodiment]]

- Artiklen undersøger, hvorfor avancerede [[02_Emne_2_Datalogi_KI_og_robotteknologi|LLMs]] kan klare eksamener, skrive overbevisende tekster og føre menneskelignende samtaler, men stadig fejle simple visuelle logikopgaver.
- Et centralt eksempel er [[02_Emne_2_Datalogi_KI_og_robotteknologi|ConceptARC]], hvor mennesker klarer sig langt bedre end GPT-4 på opgaver, der tester abstrakte begreber som “sammehed”, mønstre og regeloverførsel.
- Artiklen problematiserer [[02_Emne_2_Datalogi_KI_og_robotteknologi|Turing-testen]]: moderne chatbots kan ofte snyde mennesker i korte samtaler, men det viser ikke nødvendigvis robust intelligens eller forståelse.
- Biever forklarer, at traditionelle benchmarks kan være misvisende, fordi høje testscores ikke nødvendigvis generaliserer på samme måde for AI som for mennesker.
- Et vigtigt problem er [[andre 1#contamination|contamination]]: modeller kan have set lignende spørgsmål i træningsdata, hvilket gør det svært at vide, om de ræsonnerer eller bare genbruger mønstre.
- Artiklen viser også en debat i AI-forskningen: nogle forskere ser spirende ræsonnement i LLMs, mens andre mener, at deres evner er “brittle” og ikke menneskelignende.
- [[02_Emne_2_Datalogi_KI_og_robotteknologi|Embodiment]] bruges som mulig forklaring på forskellen mellem menneskelig og maskinel forståelse: mennesker lærer begreber gennem krop, sanser og fysisk verden, ikke kun tekst.
- En vigtig videnskabsteoretisk pointe er, at måling af intelligens afhænger af testens design. En test måler ikke “intelligens i sig selv”, men en bestemt operationalisering af intelligens.
- Kritisk pointe: artiklen advarer mod [[andre 1#anthropomorphization|anthropomorphization]] — at tolke menneskelignende output som bevis for menneskelignende tænkning.
- Eksamen-vinkel: brug teksten til at diskutere forholdet mellem performance, forståelse, benchmark-validitet og risikoen ved at overfortolke AI-resultater.
- Kobling: passer stærkt sammen med Turing, AI, [[02_Emne_2_Datalogi_KI_og_robotteknologi|embodiment]], og diskussionen om symbolsk/subsymbolsk intelligens.

> ([[Biever_TheEasyIntelligentTest_Nature2023.pdf#page=1&selection=43,0,52,37&color=yellow|Biever_TheEasyIntelligentTest_Nature2023, p.686]])
> For chatbots built on LLMs, there is an extra element: human trainers have provided extensive feedback to tune how the bots respond. What’s striking is the breadth of capabilities that emerges from this autocomplete-like algorithm trained on vast stores of human language. Other AI systems might beat the LLMs at any one task, but they have to be trained on data relevant to a specific problem, and cannot generalize from one task to another.


> ([[Biever_TheEasyIntelligentTest_Nature2023.pdf#page=1&selection=62,0,68,13&color=yellow|Biever_TheEasyIntelligentTest_Nature2023, p.686]])
> “There’s very good smart people on all sides of this debate,” says Ullman. The reason for the split, he says, is a lack of conclusive evidence supporting either opinion. “There’s no Geiger counter we can point at something and say ‘beep beep beep — yes, intelligent’,” Ullman adds.

> ([[Biever_TheEasyIntelligentTest_Nature2023.pdf#page=1&selection=106,0,113,12&color=yellow|Biever_TheEasyIntelligentTest_Nature2023, p.686]])
> Turing did not specify many details about the scenario, notes Mitchell, so there is no exact rubric to follow. “It was not meant as a literal test that you would actually run on the machine — it was more like a thought experiment,” says François Chollet, a software engineer at Google who is based in Seattle, Washington.

"Eksamener indikerer generel intelligens ved at teste kognitive færdigheder som problemløsning, kritisk tanke, hukommelse og tilpasningsevne. De måler, hvordan en person forstår komplekse sammenhænge og anvender viden, snarere end blot evnen til udenadslære."

> ([[Biever_TheEasyIntelligentTest_Nature2023.pdf#page=4&selection=15,0,29,8&color=yellow|Biever_TheEasyIntelligentTest_Nature2023, p.689]])
> Bowman, however, says GPT-4’s struggles with ConceptARC don’t prove that it lacks underlying capabilities in abstract reasoning. He says ConceptARC is skewed against GPT-4 — among other things, because it is a visual test. “Even if you suppose that these models are very good at this kind of reasoning, I don’t think you’d really expect this experiment to have worked,” he says. Limitations to the way the test is done probably made it harder for GPT-4. The publicly available version of the LLM can accept only text as an input, so the researchers gave GPT-4 arrays of numbers that represented the images. 

> ([[Biever_TheEasyIntelligentTest_Nature2023.pdf#page=4&selection=105,0,111,19&color=yellow|Biever_TheEasyIntelligentTest_Nature2023, p.689]])
> “There’s no Rubicon, no one line,” he says. Rather, he thinks that researchers need lots of tests to quantify the strengths and weaknesses of various systems. “These agents are great, but they break in many, many ways and probing them systematically is absolutely critical,” he says.

### [[ANewHeavenAndNewEarth.pdf]]

source:: “Toward a New Heaven and a New Earth: The Scientific Revolution and the Emergence of Modern Science”, kapitel 16.  
type:: historisk oversigt / videnskabens fremkomst  
keywords:: [[03_Videnskabens_fremkomst|Kopernikus]], [[03_Videnskabens_fremkomst|heliocentrisk verdensbillede]], [[03_Videnskabens_fremkomst|geocentrisk verdensbillede]], [[andre 1#Ptolemæisk-Aristotelisk verdensbillede|Ptolemæisk-Aristotelisk verdensbillede]], [[andre 1#naturfilosofi|naturfilosofi]], [[andre 1#Renaissance humanism|Renaissance humanism]], [[andre 1#Hermeticism|Hermeticism]], [[04_Videnskabens_fremkomst_2|Keplers love]], [[04_Videnskabens_fremkomst_2|Galilei]], [[03_Videnskabens_fremkomst|videnskabelig metode]], [[04_Videnskabens_fremkomst_2|rationalisme]], [[04_Videnskabens_fremkomst_2|empirisme]], [[andre 1#Royal Society|Royal Society]], [[andre 1#French Royal Academy of Sciences|French Royal Academy of Sciences]], [[andre 1#sekularisering|sekularisering]]

- Kapitlet handler om den videnskabelige revolution som et brud med det middelalderlige, kristent forankrede og [[andre 1#Ptolemæisk-Aristotelisk verdensbillede|Ptolemæisk-Aristoteliske verdensbillede]].
- Baggrunden var ikke, at middelalderen var “uvidenskabelig”, men at skolastikken var bundet af teologi og autoriteter som Aristoteles, Galen og Ptolemæus.
- Renæssancens humanisme, kunst, tekniske problemer, nye instrumenter, matematik og trykpressen var med til at skabe betingelserne for ny videnskab.
- Astronomien er kapitlets hovedcase: [[03_Videnskabens_fremkomst|Kopernikus]] flyttede centrum fra Jorden til Solen, Brahe leverede præcise observationer, Kepler formulerede elliptiske planetbaner, og Galileo brugte teleskopet til at udfordre idéen om perfekte himmellegemer.
- Newton samler udviklingen i en mekanisk og matematisk naturforståelse, hvor de samme love gælder både på Jorden og i himlen.
- Kapitlet viser også medicinske fremskridt: Vesalius udfordrede Galens anatomi gennem dissektion, og William Harvey forklarede blodets kredsløb.
- Kvinder som Margaret Cavendish, Maria Sibylla Merian og Maria Winkelmann bruges til at vise, at kvinder bidrog til tidlig moderne videnskab, men ofte blev udelukket fra universiteter og akademier.
- Descartes og Bacon repræsenterer to vigtige metodiske idealer: rationalistisk deduktion og empirisk/induktiv undersøgelse.
- Konflikten mellem Galileo og kirken viser spændingen mellem bibelsk autoritet og naturvidenskabelig observation.
- Scientific societies, især [[andre 1#Royal Society|Royal Society]] og [[andre 1#French Royal Academy of Sciences|French Royal Academy of Sciences]], gjorde videnskab mere institutionel, offentlig og kollektiv.
- Vigtig pointe: den videnskabelige revolution ændrede ikke kun teorier om naturen, men også menneskets selvforståelse og Europas overgang mod et mere sekulært, rationelt og materialistisk verdensbillede.
- Eksamen-vinkel: brug kapitlet som oversigt over, hvordan moderne videnskab opstår gennem samspil mellem observation, matematik, teknologi, institutioner og autoritetskritik.
- Kobling: passer direkte til emner om [[03_Videnskabens_fremkomst|videnskabens fremkomst]], [[04_Videnskabens_fremkomst_2|rationalisme/empirisme]], Galileo, Descartes og Kuhns idé om videnskabelige revolutioner.

### [[Kennefick_Phystoday_2009.pdf]]

source:: Daniel Kennefick, “Testing relativity from the 1919 eclipse—a question of bias”, *Physics Today*, 2009.  
type:: historisk/videnskabsteoretisk artikel  
keywords:: [[andre 1#Eddington|Eddington]], [[04_Videnskabens_fremkomst_2|Einstein]], [[05_Emne_4_Euklid_Einstein_og_Kuhn|generel relativitetsteori]], [[andre 1#light bending|light bending]], [[andre 1#bias|bias]], [[andre 1#predictor effect|predictor effect]], [[andre 1#data analysis|data analysis]], [[andre 1#data reduction|data reduction]], [[andre 1#instrumentfejl|instrumentfejl]], [[andre 1#reanalyse|reanalyse]], [[andre 1#empirical test|empirical test]]

- Kennefick analyserer den senere kritik af Eddington-ekspeditionerne under solformørkelsen i 1919.
- Eksperimentets formål var at teste, om stjernelys blev afbøjet nær Solen, sådan som Einsteins generelle relativitetsteori forudsagde.
- Kritikken går især på to ting: at målingerne ikke var præcise nok til at skelne Newton fra Einstein, og at Eddington muligvis sorterede data til fordel for Einstein.
- Kenneficks hovedargument er, at denne bias-fortælling er for simpel. Eddington og Dyson havde rimelige videnskabelige grunde til at afvise bestemte datasæt, især på grund af instrumentelle problemer.
- Artiklen viser, at databehandling i praksis kræver faglig dømmekraft: data skal vægtes, renses, reduceres og fortolkes i lyset af instrumenter og kontekst.
- En senere reanalyse fra 1979 støttede vurderingen af, at de problematiske Sobral-plader havde tekniske fejl.
- Kennefick understreger også, at Dyson og Eddington ikke anså 1919-resultatet som sidste ord; de forsøgte at få eksperimentet replikeret ved solformørkelsen i 1922.
- Vigtig pointe: eksperimenter er ikke mekaniske “sandhedsmaskiner”. De kræver fortolkning, og konteksten er afgørende for, hvad der tæller som god evidens.
- Kritisk pointe: teksten nuancerer både positivisme og Kuhn. Den viser, at observationer er centrale, men også at observationer aldrig er helt uafhængige af teori, instrumenter og forventninger.
- Eksamen-vinkel: brug Kennefick som case på forholdet mellem [[andre 1#måling|måling]], [[andre 1#bias|bias]], databehandling, teori og videnskabelig autoritet.
- Kobling: passer sammen med Eddington-eksperimentet i emne 4 og med diskussioner om [[andre 1#objektivitet|objektivitet]], [[03_Videnskabens_fremkomst|verifikation]] og [[05_Emne_4_Euklid_Einstein_og_Kuhn|paradigmeskift]].

## Samlende stikord

- [[02_Emne_2_Datalogi_KI_og_robotteknologi|kunstig intelligens]]
- [[02_Emne_2_Datalogi_KI_og_robotteknologi|Large Language Models / LLM]]
- [[andre 1#benchmarking|benchmarking]]
- [[02_Emne_2_Datalogi_KI_og_robotteknologi|ConceptARC]]
- [[andre 1#abstract reasoning|abstract reasoning]]
- [[andre 1#data-driven robotics|data-driven robotics]]
- [[andre 1#model-based methods|model-based methods]]
- [[andre 1#model-free methods|model-free methods]]
- [[andre 1#foundation models|foundation models]]
- [[andre 1#inductive bias|inductive bias]]
- [[03_Videnskabens_fremkomst|videnskabens fremkomst]]
- [[03_Videnskabens_fremkomst|heliocentrisk verdensbillede]]
- [[04_Videnskabens_fremkomst_2|rationalisme]]
- [[04_Videnskabens_fremkomst_2|empirisme]]
- [[andre 1#Royal Society|Royal Society]]
- [[andre 1#sekularisering|sekularisering]]
- [[andre 1#Eddington|Eddington]]
- [[05_Emne_4_Euklid_Einstein_og_Kuhn|generel relativitetsteori]]
- [[andre 1#bias|bias]]
- [[andre 1#data reduction|data reduction]]
- [[05_Emne_4_Euklid_Einstein_og_Kuhn|paradigmeskift]]

## Mulig eksamensformulering

De fire tekster kan bruges til at vise, hvordan videnskab både handler om data, modeller, målinger og fortolkning. Kapitlet om den videnskabelige revolution viser, hvordan moderne naturvidenskab opstod gennem brud med ældre autoriteter og gennem nye metoder, instrumenter og institutioner. Kennefick viser, at selv et berømt eksperiment som Eddingtons solformørkelsesobservation ikke kan forstås som “rene data”, fordi instrumentfejl og databehandling kræver vurdering. Biever viser samme pointe i nutidig AI: benchmarks kan give imponerende resultater, men de skal fortolkes kritisk. Amato et al. fører diskussionen videre til robotteknologi, hvor spørgsmålet er, om store datamængder kan erstatte modeller, eller om fremtidens robotter kræver en hybrid mellem data, fysik og ingeniørmæssig forståelse.
