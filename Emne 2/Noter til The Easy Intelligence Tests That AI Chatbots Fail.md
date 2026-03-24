Test consisting of a series of brightly coloured blocks arranged on a screen --> aim is to spot connecting patterns
	most people can spot the connecting patterns
	GPT-4, gets barely one-third of the puzzles right in one category of patterns 
	and as little as 3% correct in another

LLMS: They work simply by generating plausible next words when given an input text, based on the statistical correlations between words in bil- lions of online sentences (they are trained on)
	A problem:  they answer with words most likely to be associated with original question in training data --> rather than correcr answer to new scenario

**LLMs learn only from language;** without being embodied in the physical world, they do not experience language’s connection to objects, properties and feelings, as a person does. 
	
**Contamination:**
	Language models do well on benchmarks --> But often, the conclusion is not that they have surpassed humans in these general capacities, but that the **benchmarks are limited.**
	Researchers mention the challenge that models are trained on so much text they could already have similar questions in their training data  --> meaning **they are just looking up the answers *(this is contamination)***
	
OpenAI: (says  it) checked for contamination by looking for similar strings of words in the questions and training data. 
	When it tested the LLMs before and after removing the similar strings, there was little difference in performance, suggesting that successes couldn’t be attributed largely to contamination. 

Extrapolation
 [Mitchell] took a question from an **exam** (given to master’s students in business administration ). which ChatGPT had passed and  then rephrased it (the exam )slightly. 
	 A person who could answer this question would be able to answer the rephrased version. But ChatGPT flunked it.
	
 Another issue: LLMs’ success on exam questions can be brittle and might not translate into the robust capability needed to get examples right in the real world. 
	 "**Extrapolating** in the way that we extrapolate for humans won’t always work for AI systems,” 

	
 Turing test: proposed by the British mathematician and computing luminary **Alan Turing in 1950**
	  Turing suggested an assessment that he called the **imitation game 2** . 
	  This was a scenario in which human judges hold short, text-based conversations with a hidden computer and an unseen person. 
	  Could the judge reliably detect which was the computer? 
	  That was a question equivalent to ‘Can machines think?’, Turing suggested.

For several decades, the businessman and philanthropist **Hugh Loebner funded a**n annual Turing test event known as **the Loebner Prize.** 

*some researchers agree that GPT-4 and other LLMs would probably now pass the popular conception of the Turing test, in that they can fool a lot of people, at least for short conversations.*
(In May, researchers at the company AI21 Labs in Tel Aviv, Israel, reported that more than 1.5 million people had played their online game
	The players correctly identified bots just 60% of the time, which the researchers note is not much better than chance 3 .)

**Benchmark tests** should  reveal differences between capabilities of AI and people
	"Such benchmarks could help show what is missing in today’s machine-learning systems, and untangle the ingredients of human intelligence" -- Brenden Lake,
Instead of the Turing test researchers assess AI systems using this type of benchmark testing
intended to evaluate performance on specific capabilities 
	e.g. language, common sense reasoning, mathematical capacity
	
academic and proffesional examinations are also used to tune this (increasingly)
	Advanced Placement (exam to asses physicians clinical knowledge)
	Uniform bar exam 
	GRE

**ARC**
	In 2019, Chollet posted online a new kind of logic test for AI systems that he had created, called the **Abstraction and Reasoning Corpus (ARC)** 6
		Solvers look at several visual demonstrations of a grid of squares changing to another pattern --> then they should indicate how the next grid would transform (testing for abstract pattern recognition capabilities). 
		“It is supposed to test for your ability to adapt to things you have not seen before,” says Chollet, who argues that this is the essence of intelligence. 
		ARC captures a “hallmark of human intelligence”, says Lake: 
			*the ability to make abstractions from everyday knowledge, and apply those to previously unseen problems*.
The winning bot was an AI system that was specifically trained to solve ARC-like tasks
		it got 21%, people get 80%

**ConceptARC** 
  --> tests are easier: (Mitchell’s team) wanted to ensure the bench- mark would not miss progress in machines’ capabilities
To test the concept of "sameness"
	one puzzle requires the solver to keep objects in the pattern that have the same shapes; another to keep objects that are aligned along the same axis. 
	The goal of this was to ***reduce the chances that an AI system could pass the test without grasping the concepts*** *(see ‘An abstract-thinking test that defeats machines’).*

ConceptARC tasks were fed to GPT-4 and to 400 people enlisted online. 
The humans scored, on average, 91% on all concept groups (and 97% on one); 
GPT-4 got 33% on one group and less than 30% on all the rest
	 “It was surprising that it could solve some of the problems, because it had never been trained on them,” 
	 
GPT-4’s struggles with ConceptARC don’t prove that it lacks underlying capabilities in abstract reasoning. -->	ConceptARC is skewed against GPT-4 — among other things, because it is a visual test. 
	
 GPT-4 got an arrays of numbers that represented the images. (A blank pixel might be 0, and a colour- ful square a number, for instance.) 
	 By contrast, the human participants simply saw the images. 
	 
***“We are comparing a language-only system with humans, who have a highly developed visual system,” says Mitchell. “So it might not be a totally fair comparison.”***


When tested on: 
	A digital version of the board game Othello, in which two players compete by placing black and white discs on a 8 × 8 grid. 
	
The LLM became very good at spitting out accurate suggestions for next legal moves. 
***The researchers argued that they had evidence that the LLM was keeping track of the state of the board — and that it was using this representation to suggest moves, rather than just coming up with textual suggestions***
	-->as opposed to (Their aim was to examine whether LLMs rely on the memorized surface statistics of language to generate text, )

(There is no "Rubicon", no one line) --> Researchers need lots of tests to quantify the strengths and weaknesses of various systems. “These agents are great, but they break in many, many ways and probing them systematically is absolutely critical,”
	Rubicon er en flod "river"	
	ceasers act of crossing the rubicon is known as a daring act, now the expression:refers to: taking an irreversable step/ "point of no return"/"no one line" --> der er  ikke én test
	også en Sabaton sang
	
avoid what he (Wortham) calls the curse of **anthropomorphization.** 
	“We anthropomorphize anything which appears to demonstrate intelligence,” he says. “It is a curse, because we can’t think of things which display goal-oriented behaviour in any way other than using human models,” 
	"And we’re imagining that the reason it’s doing that is because it’s thinking like us, under the covers.”
