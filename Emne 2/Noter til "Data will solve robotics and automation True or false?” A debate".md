"Leading researchers debate the long-term influence of model-free methods that use large sets of demonstration data to train numerical generative models to control robots."

## Introduction – Key Points

- The robotics community is undergoing a **paradigm shift** from model-based to data-driven methods.
- Advances since 2012 in:
    - Deep neural networks
    - Large datasets
    - GPUs and scalable computation  
        have transformed vision, speech, and now robotics.
        
- The emergence of **foundation models** (e.g. large vision-language models) enables end-to-end, model-free control.
- The field is divided:
    - Some argue data-driven methods are overrated.
    - Others claim traditional model-based robotics is obsolete.
    - Many support **hybrid approaches** combining both.
        
- An Oxford-style debate was held at ICRA 2025 to explore these opposing views.
- While opinions remained polarized, most debaters acknowledged the importance of combining **data and models**.
    
    AmatoEtAl_DataWill_ICRA2025

---
The robotics and automation research community is experiencing  a “paradigm shift” (Thomas Kuhn). 
--> This was the subject of a featured debate at the IEEE International Conference on Robotics and Automation (ICRA)

This is said do tue advancements in:
	Deep “neural” networks that combine unprecedented amounts of example data, advances in stochastic gradient descent techniques, and advances in computing, 
	in particular GPUs (graphics processing units), 
	have produced remarkable results in computer vision and speech recognition

The paradigm of “end-to-end” (also known as “model- free”) approaches to perception and control suggest an entirely new, data-driven approach to robotics and automation.
*“Will the future of robot- ics and automation be written in code or in data? Is the Handbook of Robotics obsolete? Are home humanoids overhyped?"*

Some researchers believe, at one extreme, that the data-driven paradigm is overrated, and some at the other extreme believe that model-based approaches are outdated and should be retired. Many researchers take less extreme positions, believing both paradigms have merit a
	The debaters focused on software and control and did not address the many unsolved issues related to hardware, materials, and design, nor did they have timeo discuss how such massive datasets can be collected and processed.

---
DATA ARE NOT MERELY BENEFICIAL; RATHER, THEY ARE INDISPENSABLE AND FOUNDATIONAL
Animesh Garg: Humanity has frequently developed “know- how” before the “know-why.” 
	We engineered technologies mainly using observational understanding —yet preceding a thorough understanding of their underlying sciences.
	We are in the midst of building next- generation technology—“computational and physical intelligence” with data-driven empirical methods.
	Using Modern Computing as a tool of scientific discovery
	*"In our quest to understand intelligence and “solve” robotics, I contend that data are not merely beneficial; rather, they are indispensable and foundational. This necessity stems from several critical perspectives:"*

Hans kritiske perspektiver:
1) General-purpose intelligence, particularly in physical robots, is ambiguous, open ended, and underspecified....
2)  Accurate models foster innovation. Conversely, incomplete models can hinder the discovery of true optima, because these might be unrepresentable or unattainable with existing optimization tools....
 3) Robotics represents the evolution of computing, moving beyond desktop, mobile, and cloud environments into the physical world. Whereas data-driven approaches are often criticized for lacking elegance, the empirical process of data collection, creation, and curation is inherently a scientific endeavor. ...
 4) 4) Data-driven methods have successfully unified diverse problems in fields like language processing and computer vision....
---
## Animesh Garg – _Data are Indispensable_

- Data are **foundational**, not merely beneficial, for robotics.
- Historically, technology often precedes full scientific understanding (know-how before know-why).
- General-purpose physical intelligence is:
    - Ambiguous
    - Open-ended
    - Underspecified  
        → Closed-form models are insufficient.
        
- Large-scale data:
    - Enable learning without explicit programming.
    - Support self-supervised and sparse-feedback learning.
    - Improve robustness and discovery of novel behaviors.
        
- Incomplete or incorrect models can **block progress** and prevent reaching optimal solutions.
- Robotics is the next evolution of computing, moving into the physical world.
- Foundation models can:
    - Unify fragmented robotics subfields.
    - Exploit shared physical laws across tasks and robots.
- Priority should be to achieve **any workable solution** first; elegance and interpretability can come later.
    
    AmatoEtAl_DataWill_ICRA2025
---
MODELS GIVE MEANING TO DATA AND ARE ESSENTIAL FOR UNDERSTANDING ROBOT CONTROL
Aude Billard: All science is grounded in data, but data alone are insufficient. I do not believe that data alone will “solve” robotics and automation.
	Robotics today seems like an impatient child who wants it all, now and at all costs. It dreams of deploying a magic tool that will control a variety of robotic bodies... and to operate out- doors and indoors in all weather, with minimal changes to our homes and habits. 
	--> If this is what is meant by solving robotics, then the task may seem unsolvable with a traditional scientific approach, 
	given that *none* of the sciences we know today can capture, through mathematical laws, all of the world’s complexity—let alone the complexity of human beings. 
	*It is hence understand- able to seek an alternative road.* --> data
	
The success of large language models re- lies on the fact that humans had put at the disposal of computers billions of pieces of information...
However, existing interfaces for transferring knowledge from humans to robots...offer only a crude approximation of human sensing,
Yet, suppose robotics does succeed in this endeavor, but only through sheer computational power applied to vast datasets, without the development of any underlying general theoretical principles. 
Then the only thing of importance is knowing how best to use ai

Per- haps what matters is neither alone but rather the interplay between gathering data and re- fining models that is essential to building an understanding of how robots can act in the world. Failing this, we may just be building another tower of Babel.

---
## Aude Billard – _Models Give Meaning to Data_

- Data alone are **insufficient** to solve robotics.
- Scientific progress requires:
    - Carefully selected data
    - Continuous interaction between data and theoretical models.
- Example from astronomy:
    - Understanding came from models guiding data collection, not massive raw observation.
- Robotics risks seeking an unrealistic “universal” data-driven solution.
- The physical world and human behavior are too complex to be captured solely through data.
- Large language models succeed because:
    - Human knowledge is largely symbolic and text-based.
    - Physical intelligence cannot be transferred as easily.        
- If robotics advances without theory:
    - Scientific understanding may stagnate.
    - Knowledge may be reduced to opaque engineering practices.
        
- Sustainable progress requires **models to structure, interpret, and constrain data**.
- Data without models risks producing systems that work but are not understood.
    
    AmatoEtAl_DataWill_ICRA2025

---


I BELIEVE THAT WE NEED BOTH DATA AND MATHEMATICAL MODEL
Daniela Rus: Although I was assigned to argue in favor of data “solving” robotics and automation, my actual position is more nuanced: I believe that we need both data and mathematical models.
	The challenge is complexity. Real-world tasks are multimodal, context- dependent, and filled with ambiguity. They involve soft, deformable objects; occluded or partial views; unpredictable humans; and environments that shift over time
	To function in these settings, robots need more than structure—they need experience. And experience comes from data.

MANIPULATION REQUIRES “COMMON SENSE”; LARGE DATA AND LARGE MODELS CAN PROVIDE IT
Russ Tedrake: I do believe that the next most impactful steps toward “solving” robotics lie in large-scale data collection and large pretrained models. How could I not? The advances in large mod- els for language, vision, and now video are undeniable.
	 have seen more and more examples of robots pro- grammed via imitation learning performing dexterous manipulation tasks that would have been impossible to imagine even a few years ago;
	Most peo- ple agree that large models are useful for ma- nipulation tasks that require common-sense language understanding (e.g., “pick up the extinct animal”), but many people underesti- mate how essential common sense is for low- level control.
	For me, “solving” robotics is a very long- term agenda. Well after we have general- purpose robots out in the open world performing useful work, we will still have a lot more work to do to deeply understand the laws of robotics. We are in the early phases, where everything feels messy. I am optimistic that we will quickly deepen our empirical un- derstanding of these new capabilities and that we will eventually have theorems that guide us. 

MORE GROUNDED STRATEGY IS NEEDED 
Frank Park: There is no doubt that multimodal founda- tion models represent a transformational moment in human history, but expecting a parallel revolution in robotics is premature at best and wishful thinking at worst. Robotics is a different beast entirely: Real-world data are scarce, simulations remain unreliable, and robots in their many embodiments must contend with an endless variety of environ- ments and tasks
	to say noth- ing of the massive computing, energy, and data demands of today’s foundation models. None of this is to say that foundation models for robotics are not worth pursuing— they are, but a more grounded strategy is needed. 
	Fortunately, in robotics, we already have a wealth of such inductive biases. Biology of- fers insights into how humans control move- ment through layers of abstraction, as well as the interplay between feedforward versus feedback and internal versus external coor- dinates. Physics provides models of motion, force, and compliance. Geometry helps to simplify complex movements into lower- dimensional representations and to exploit any underlying symmetries. Programming gives us tools like motion description lan- guages that formalize manipulation tasks in a device-independent manner. Current robot foundation models do not sufficiently exploit these inductive biases.
	Robotics deserves the same level of intentional design. Rather than force-fitting models developed for vision and language to robots, new mod- els that capture the inductive biases inherent to robotics are needed. It is time we treated robotics not as an extension of deep learning but as its own grand challenge.