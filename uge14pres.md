![[images/uge14pres/slide_001.png]]
- we know at the boundary, what the value of $u$ is. 
	- we want to find out what is in between. 
- $\alpha$ has to be positive.
- source term decaying exponentially to $t$
- left is initial, right is result. 
- at the boundary, $u$ is 0. 

![[images/uge14pres/slide_002.png]]
- $\Delta x=\frac{1}{N}$, propagation in time along discretized line $x_j$ 
- coupled through diffusion.... ?

![[images/uge14pres/slide_003.png]]
- $t_n = n \Delta t$ time discretization. 
- then approximation $u^n_j \sim u_j(t_n)$
- can just insert Euler. 
- from top left $u_j(0)$ becomes bottom mid $u^0_j$ discretized. 
- $y_{n+1}$ corrispond to $u^{n+1}_j$, $y_n$ corrispond to $u^n_j$ and so on.
- no terminal boundary for final time $t$.


![[images/uge14pres/slide_004.png]]
- Discretization error comes from Euler Method. 
- limit in information issue: the red dot doesn't get enough information, only from 3 points. missing the upper and lower ones. 
	- doesn't get information that it maybe should have had. Meaning idealy it should have information from all dots in the entire colomn. 
- but we know $\alpha$ so we know how small to put $\Delta t$, which is an advantage, but if we want good accuracy, $\Delta t$ needs to be very small. also for the discretization error. 
- Need to improve this, go back to previous, but new method $\downarrow$

![[images/uge14pres/slide_005.png]]
- trapezoidal method. (Crank-Nicolson)
- disadvantage is $y_{n+1}$ appears on the right-hand side. 
- abbreviation is the second order something of u something 

![[images/uge14pres/slide_006.png]]
- remember $r=\alpha \Delta t / (\Delta x)^2$
- System of linear equations, enter linearly on the right-hand side (the long cunt)
- any structure of this set of linear equations that can be exploited?
	- tri-diagonal system of linear equations. 

![[images/uge14pres/slide_007.png]]
- put the constant, $c$, to 1, unless its stated in the exercise.
- common mistake, remember to put $r=2r$, each time you increase N, because when you subdivide the two of them, r goes back to 2r in this ($r=\alpha \Delta t / (\Delta x)^2$) 
- can run with much larger $\Delta t$. 
- so, there is absolutely no reason to use Eulers method. 
![[images/uge14pres/slide_008.png]]
- 

# Quiz
![](Pasted%20image%2020260513081810.png)
Svar: korrekt
	[link](uge13pres#^quiz-question-one)
![](Pasted%20image%2020260513082122.png)
svar: (N-1)(N+1)
![](Pasted%20image%2020260513082255.png)
svar: korrekt
[link](uge13pres#^quiz-question-three)

![](Pasted%20image%2020260513082808.png)
svar: $O(n*(mR^2))$ 
- since mR is less than mC, we should go row by row. 	
