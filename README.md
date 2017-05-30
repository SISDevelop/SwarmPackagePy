
# SwarmPackagePy
**SwarmPackagePy** is a Library of swarm optimization algorithms. It includes 14 optimization algorithms and each can be used for solving specific optimization problem. You can find the principles they operate on and pseudo codes  below.<br>

Provides:<br>
- Swarm optimization algorithms.
- Test functions for swarm algorithms.
- Animation of minimum find process.<br>
<br>Every algorithm has arguments listed below:<br>
- **n**: number of agents
- **function**: test function
- **lb**: lower limits for plot axes
- **ub**: upper limits for plot axes
- **dimension**: space dimension
- **iteration**: number of iterations<br>
<br>Every algorithm has methods listed below:<br>
- **get_agents()**: returns a history of all agents of the algorithm
- **get_Gbest()**: returns the best position of algorithm<br>
<br>If an algorithm accepts some additional arguments or methods they will be described in its "Arguments" or "Methods" section.

For all questions and suggestions contact us at swarm.team.dev@gmail.com. For more info you could also write to:<br>
* team leads - vllitskevich@gmail.com, polly.bartoshevic@gmail.com,
* programmers - alexeymaleyko@gmail.com, b317.forinko@gmail.com, vladislaw.kapustin@gmail.com.

## Table of contents
* [Installation](#installation)<br>
* [Bacterial Foraging Optimization](#bacterial-foraging-optimization)<br>
* [Gray Wolf Optimization](#gray-wolf-optimization)<br>
* [Bat Algorithm](#bat-algorithm)<br>
* [Artificial Bee Algorithm](#artificial-bee-algorithm)<br>
* [Firefly Algorithm](#firefly-algorithm)<br>
* [Cuckoo Search Optimization](#cuckoo-search-optimization)<br>
* [Whale Swarm Algorithm](#whale-swarm-algorithm)<br>
* [Firework Algorithm](#firework-algorithm)<br>
* [Particle Swarm Optimization](#particle-swarm-optimization)<br>
* [Chicken Swarm Optimization](#chicken-swarm-optimization)<br>
* [Social Spider Algorightm](#social-spider-algorightm)<br>
* [Cat Algorithm](#cat-algorithm)<br>
* [Harmony Search](#harmony-search)<br>
* [Gravitational Search Algorithm](#gravitational-search-algorithm)<br>
* [Tests](#tests)<br>
* [Animation](#animation)<br>

### Installation
#### Requirements
- python (version >= 3.5 if you are going to run tests; for all other actions you can use python any version)<br>
- numpy<br>
- pytest (if you are going to run tests)<br> 
- matplotlib (if you are going to watch animation)<br> 
- pandas (if you are going to watch 3D animation)<br> 
#### Installation
You can install **SwarmPackagePy** from PyPI repositories using pip. Command bellow will do this:
```
pip install SwarmPackagePy
```
Or you can just clone this repository and at the main folder execute command:
```
cd SwarmPackagePy/
python setup.py install
```

### Bacterial Foraging Optimization
#### Description
The **Bacterial Foraging Optimization**, proposed by Passino is inspired by the social foraging behavior of Escherichia coli (next E.coli).<br>
During foraging of the real bacteria, locomotion is achieved by a set of tensile flagella.
Flagella help an E.coli bacterium to tumble or swim, which are two basic operations performed by a bacterium at the
time of foraging. When they rotate the flagella in the clockwise direction, each flagellum pulls
on the cell. That results in the moving of flagella independently and finally the bacterium tumbles with
lesser number of tumbling whereas in a harmful place it tumbles frequently to find a nutrient gradient.
Moving the flagella in the counterclockwise direction helps the bacterium to swim at a very fast rate.
In the above-mentioned algorithm the bacteria undergoes chemotaxis, where they like to move towards
a nutrient gradient and avoid noxious environment. Generally the bacteria move for a longer distance
in a friendly environment.<br>
When they get food in sufficient, they are increased in length and in presence of suitable temperature
they break in the middle to from an exact replica of itself. This phenomenon inspired Passino to
introduce an event of reproduction in BFO. Due to the occurrence of sudden environmental changes
or attack, the chemotactic progress may be destroyed and a group of bacteria may move to some other
places or some other may be introduced in the swarm of concern. This constitutes the event of
elimination-dispersal in the real bacterial population, where all the bacteria in a region are killed or a
group is dispersed into a new part of the environment.<br>
Bacterial Foraging Optimization has three main steps:
* Chemotaxis
* Reproduction
* Elimination and Dispersal
#### Mathematical model
_Chemotaxis:_ This process simulates the movement of an E.coli cell through swimming and
tumbling via flagella. Biologically an E.coli bacterium can move in two different ways. It can
swim for a period of time in the same direction or it may tumble, and alternate between these
two modes of operation for the entire lifetime.
_Reproduction:_ The least healthy bacteria eventually die while each of the healthier bacteria (those
yielding lower value of the objective function) asexually split into two bacteria, which are then
placed in the same location. This keeps the swarm size constant.
_Elimination and Dispersal:_ Gradual or sudden changes in the local environment where a
bacterium population lives may occur due to various reasons e.g. a significant local rise of
temperature may kill a group of bacteria that are currently in a region with a high concentration of
nutrient gradients. Events can take place in such a fashion that all the bacteria in a region are killed
or a group is dispersed into a new location. To simulate this phenomenon in BFO some bacteria
are liquidated at random with a very small probability while the new replacements are randomly
initialized over the search space.
#### Algorithm
<pre>
BEGIN
&nbsp;Initialize randomly the bacteria foraging optimization population
&nbsp;Calculate the fitness of each agent
&nbsp;Set global best agent to best agent
&nbsp;FOR number of iterations
&nbsp;&nbsp;FOR number of chemotactic steps
&nbsp;&nbsp;&nbsp;FOR each search agent
&nbsp;&nbsp;&nbsp;&nbsp;Move agent to the random direction
&nbsp;&nbsp;&nbsp;&nbsp;Calculate the fitness of the moved agent
&nbsp;&nbsp;&nbsp;&nbsp;FOR swimming length
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF current fitness is better than previous
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Move agent to the same direction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Move agent to the random direction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END IF
&nbsp;&nbsp;&nbsp;&nbsp;END FOR
&nbsp;&nbsp;&nbsp;END FOR
&nbsp;&nbsp;&nbsp;Calculate the fitness of each agent
&nbsp;&nbsp;END FOR
&nbsp;&nbsp;Compute and sort sum of fitness function of all chemotactic loops (health of agent)
&nbsp;&nbsp;Let live and split only half of the population according to their health
&nbsp;&nbsp;IF not the last iteration
&nbsp;&nbsp;&nbsp;FOR each search agent
&nbsp;&nbsp;&nbsp;&nbsp;With some probability replace agent with new random generated
&nbsp;&nbsp;&nbsp;END FOR
&nbsp;&nbsp;END IF
&nbsp;&nbsp;Update the best search agent
&nbsp;Calculate the fitness of each agent
END
</pre>
#### Arguments
The bfo method accepts the following arguments:<br>
**param Nc** number of chemotactic steps<br>
**param Ns** swimming length<br>
**param C** the size of step taken in the random direction specified by the tumble<br>
**param Ped** elimination-dispersal probability<br>
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.bfo(n, function, lb, ub, dimension, iteration, Nc, Ns, C, Ped)
```
### Gray Wolf Optimization
#### Description
The **Gray Wolf Optimization algorithm** mimics the leadership hierarchy and
hunting mechanism of gray wolves in nature. Wolves live in a pack.
The average pack consists of a family of 5–12 animals.
wolves have strict social hierarchy which is represented by the division of a pack into four
levels: alpha, beta, delta, and omega.<br>
_Alpha_ wolves are the leaders of their pack. They are responsible for making decisions, but sometimes
alphas can obey to other wolfes of the pack.<br>
_Beta_ wolves help alphas make decisions, every beta is a candidate
to become an alpha if an alpha has died or aged.
A beta respects an alpha and transfers commands to the pack, ensures discipline among inferior wolves
and provides a feedback from the pack to an alpha.<br>
_Delta_ wolves have to submit to alphas and betas, but they dominate the omega.<br>
Finally, _omega_ wolves have to obey all other wolves. Sometimes they play a role of caretakers.<br><br>
Gray wolf hunting has three main phases:
* Tracking, chasing, and approaching the prey
* Pursuing, encircling, and harassing the prey until it stops moving
* Attack towards the prey
#### Mathematical model
In mathematical model of the social hierarchy
of wolves is mapped to the solution fit. The fittest
solution is considered to be the alpha. Beta and delta are the second and
third best solutions respectively.
The rest of the candidate solutions are assumed to be omega.<br>
Alpha, beta and delta lead the hunting (optimization) and omega wolves follow these three wolves.
#### Algorithm
<pre>
BEGIN
&nbsp;&nbsp;Initialize randomly the gray wolf population
&nbsp;&nbsp;Find 1st, 2nd and 3rd best agents (&alpha;, &beta;, &delta;)
&nbsp;&nbsp;Set global best agent to the 1st best agent
&nbsp;&nbsp;Calculate the fitness of each search agent
&nbsp;&nbsp;WHILE count &lt; max number of iterations
&nbsp;&nbsp;&nbsp;&nbsp;FOR each search agent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update te position of the current search agent
&nbsp;&nbsp;&nbsp;&nbsp;END FOR
&nbsp;&nbsp;&nbsp;&nbsp;Update &alpha;, &beta; and &delta;
&nbsp;&nbsp;&nbsp;&nbsp;Calculate the fitness of all search agents
&nbsp;&nbsp;&nbsp;&nbsp;Update the best search agent, the 2nd best serach agent, and the 3rd best search agent
&nbsp;&nbsp;&nbsp;&nbsp;ADD 1 to count
&nbsp;&nbsp;END WHILE
&nbsp;&nbsp;RETURN the best search agent
END
</pre>
#### Arguments
The gwo method accepts the following arguments:<br>
**n**: number of agents<br>
**function**: test function<br>
**lb**: lower limits for plot axes<br>
**ub**: upper limits for plot axes<br>
**dimension**: space dimension<br>
**iteration**: number of iterations
#### Methods
The gwo method has the following additional methods:<br>
**get_leaders()**: return alpha, beta, delta leaders of grey wolfs
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.pso(n, function, lb, ub, dimension, iteration)
```
### Bat Algorithm
#### Description
The **Bat Algorithm** is based on the bats echolocation ability. By using echolocation bats can detect
their food and preys and even distinguish between the different kinds of insects in the darkness.
A bat emits a loud sound and listens to the echo which is created from the sound reflection from the surrounding objects.
Sounds emmited by a bat are vary in properties and can be used depending on the hunting strategy.<br>
Each sound impulse lasts from 8 to 10 milliseconds and has constant frequency between 25 and 150 KHz.
A bat can emit from 10 to 20 of supersonic impulses per second, an impulse lasts from 5 to 20 milliseconds.
The number of signals emited by a bat can be increased during a hunt to 200.
#### Mathematical model
The Bat Algorithm uses the following principles:
1. A bat uses echolocation for distance estimation and "knows" the difference between the food/prey and an obstacle
2. Bats fly randomly with a velocity of &nu;<sub>i</sub> in the position x<sub>i</sub>, fixed frequency f<sub>min</sub>, variable wavelength &lambda;  and loudness A<sub>0</sub> for the search of a prey. They can automatically adjust the wave length (or frequency) of emitted sound impulse and level of emission r &isin; [0, 1] depending on the proximity to the victim.
3. While the loudness can be changed by different means we assume that the loudness vary from big positive value A<sub>0</sub> to minimum constant A<sub>min</sub>.
In addition to these simplified principles, lets use the next approximations: frequency f from the segment [f<sub>min</sub>, f<sub>max</sub>] corresponds to the wavelength segment [&lambda;<sub>min</sub>, &lambda;<sub>max</sub>]. For instance, a frequency segment [20 KHz, 500 KHz] corresponds to wavelength segment [0.7 mm, 17 mm].<br>
For this tast any wave length can be used. Moreover, it is unnecessary to use wave lengths, instead we can change the frequency and leave the wave length to be constant.
#### Algorithm
<pre>
BEGIN
Objective function f(x), x=(x<sub>1</sub>, ...,x<sub>d</sub>)<sup>T</sup>
Initialize the bat population x<sub>i</sub> (i= 1, 2, ..., n) and v<sub>i</sub>
Define pulse frequency f<sub>i</sub> at x<sub>i</sub>
Initialize pulse rates r<sub>i</sub> and the loudness A<sub>i</sub>
  WHILE count &lt; max number of iterations
    Generate new solutions by adjusting frequency, and updating velocities and locations/solutions
    IF rand &gt; r<sub>i</sub>
      Select a solution among the best solutions
      Generate a local solution around the selected best solution
    END IF
    Generate a new solution by flying randomly
    IF rand &lt; A<sub>i</sub> AND f(x<sub>i</sub>) &lt; f(x<sub>*</sub>)
      Accept the new solutions
      Increase r<sub>i</sub> and reduce A<sub>i</sub>
    END IF
    Rank the bats and find the current best x<sub>*</sub>
  END WHILE
  Postprocess results and visualization
  </pre>
  #### Arguments
The ba method accepts the following arguments:<br>
- r0: level of impulse emission (default value is 0.9)<br>
- V0: volume of sound (default value is 0.5)<br>
- fmin: min wave frequency (default value is 0)<br>
- fmax: max wave frequency (default value is 0.02)<br>
  fmin = 0 and fmax =0.02 - the bests values<br>
- alpha: constant for change a volume of sound (default value is 0.9)<br>
- csi: constant for change a level of impulse emission (default value is 0.9)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.ba(n, function, lb, ub, dimension, iteration, r0, V0, fmin, fmax, alpha, csi)
```
  ### Artificial Bee Algorithm
The aim of a bee swarm is to find the area of a field with the highest density of flowers. WIthout any knoledge about a field bees begin the search of flowers from random positions with random velocity vectors. Each bee can remember positions where the maximul quantity of flowers was found and know where other bees found the maximum density of flowers. When a bee chooses between the place where it found the maximum quantity of flowers and the place which was reported by others, the bee rushes in direction between these two points and desides between personal memory and social reflex. On its way the bee can find a place with more high concentration of flowers than were found previously. In the future this place can be marked as the one with the highest concentration of flowers found by a swarm. After that the whole swarm will rush in the direction of this place, remembering though their own observations. Thus, bees research a field by flying to palces with the highest consentration of flowers. They also continuously compare places they flew over with previously found ones in order to found the absolute maxim concentration of flowers. In the end, a bee ends its flight in the place with the maximum concentration of flowers. Soon the whole swarm will locate in the neighborhood of that place.
#### Mathematical model
In the Artificial Bee Algorithm model, the colony consists of three groups of bees: employed bees, onlookers and scouts. Scouts perform random search, employed bees collect previously found food and onlookers watch the dances of employed bees and choose food sources depending on dances. Onlookers and scouts are called non-working bees. Communication between bees is based on dances. Before a bee starts to collect food it watches dances of other bees. A dance is the way bees describe where food is.<br>
Working and non-working bees search for rich food sources near their hive. A working bee keeps the information about a food source and share it with onlookers. Working bees whose solutions can't be improved after a definite number of attempts become scouts and their solutions are not used after that. The number of food sources represents the nuber of solutions in the population.  The position of a food source represents a possible solution to the optimization problem and the nectar amount of a food source corresponds to the quality (fitness) of the associated solution.
#### Algorithm
<pre>
BEGIN
Initialize the population
Find current best agent for the initial iteration
Calculate the number of scouts, onlookers and employed bees
SET global best to current best
FOR iterator = 0 : iteration
  evaluate fitness for each agent
  sort fitness in ascending order and get best agents
  from best agents list select agents from a to c
  Create new bees which will fly to the best solution
  Evaluate current best agent
  IF function(current best) &lt; function (global best)
    global best = current best
  END IF
END FOR
Save global best
</pre>
 #### Arguments
The aba method accepts only standard arguments<br>
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.aba(n, function, lb, ub, dimension, iteration)
```
  ### Firefly Algorithm
  Most species of fireflies are able to glow producing short flashes. It is considered that the main function of flashes are to attract fireflies of the opposite sex and potential preys. Besides, a signal flash can communicate to a predator that a firefly has a bitter taste.
  #### Mathematical model
  The Firefly Algorithm is based on two important things: the change in light intensity and attractiveness. For simplicity, it is assumed that the attractiveness of a firefly is defined by its brightness which is connected with the objective function.<br>
  The algorithm utilizes the following firefly behaviour model:<br>
1. All fireflies are able to attract each other independently of their gender;
2. A firefly attractiveness for other individuals is proportional to its brightness.
3. Less attractive fireflies move in the direction of the most attractive one.
4. As the distance between two fireflies increases, the visible brightness of the given firefly for the other decreases.
5. If a firefly sees no firefly that is brighter than itself, it moves randomly.
#### Algorithm
  <pre>
  Objective function f(x), x=(x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>d</sub>)<sup>T</sup>
  Initialize a population of fireflies x<sub>i</sub>(i = 1, 2, ... , n)
  Define light absorption coefficient gamma
  WHILE count &lt; MaximumGeneratons
    FOR i = 1 : n (all n fireflies)
      FOR j = 1 : i
      Light intensity Ii at x<sub>i</sub> is determined by f(x<sub>i</sub>)
      IF I<sub>i</sub> > I<sub>j</sub>
          Move firefly i towards j in all d dimensions
        ELSE
          Move firefly i randomly
        END IF
        Attractiveness changes with distance r via exp[-&gamma; r<sub>2</sub>]
      Determine new solutions and revise light intensity
      END FOR j
    END FOR i
    Rank the fireflies according to light intensity and find the current best
  END WHILE
  </pre>
   #### Arguments
The fa method accepts the following arguments:<br>
- csi: mutual attraction (default value is 1)
- psi: light absorption coefficient of the medium (default value is 1)
- alpha0: initial value of the free randomization parameter alpha (default value is 1)
- alpha1: final value of the free randomization parameter alpha (default value is 0.1)
- norm0: first parameter for a normal (Gaussian) distribution (default value is 0)
- norm1: second parameter for a normal (Gaussian) distribution (default value is 0.1)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.fa(n, function, lb, ub, dimension, iteration, csi, psi, alpha0, alpha1, norm0, norm1)
```
  ### Cuckoo Search Optimization
#### Mathematical model
In the CSO algorithm each egg in a nest represents the solution and a cuckoo's egg - the new one. The aim is to use potentially the best new solutions in order to substitute the less good solutions in nests. In the simliest case, each nest contains one egg.
The algorithm is based on the following rules:
1. Every cuckoo lay one egg in a time in a randomly chosen nest;
2. The best nests with the eggs of high quality pass into a new generation;
3. An egg laid by a cuckoo in a nest can be found by the nest owner with probability &xi;<sub>a</sub>&isin;(0,1) and removed from the nest.
The CSO algorithm scheme could be described in the following form:
1. Initialize the population S={s<sub>i</sub>, i&isin;[1:|S}]} from |S| foreign nests and a cuckoo, i.e. define the initial values of for vector components X<sub>i</sub>, i&isin;[:|S|]} and cuckoo's initial position vector X<sub>C</sub>;
2. Make a number of cuckoo's random moves in the search space by performing Levy flights and find the new cuckoo's position X<sub>C</sub>;
3. Randomly pick a newt s<sub>i</sub>, i&isin;[1:|S|] and if f(X<sub>C</sub>) &gt; f(X<sub>i</sub>) then substitute an egg in this nest to the cuckoo's egg, i.e. X<sub>i</sub> = X<sub>C</sub>;
4. With the probability &xi;<sub>a</sub> remove a nubmer of the worst randomely chosen nests (including probably s<sub>i</sub> nest) from population and create the same number of new nests according to the 1st step rules;
5. Until the stop condition is not sutisfied, proceed to the 2nd step.
#### Algorithm
 <pre>
  BEGIN
    Generate initial population of n nests x<sub>j</sub>, (j = 1, 2, ... ,n)
    REPEAT
      Place cuckoo to point x<sub>i</sub> randomly by performing Levy flights
      Choose nest j among n nests randomly
      IF F<sub>i</sub> &lt; F<sub>j</sub>
      Replace x<sub>j</sub> on new solution
      END IF
      Delete from the population nests found with pa probability and build the same number of new nests
      SAVE best solution (nest)
    UNTIL stop criteria
    Postprocess results and visualization
  END
  </pre>
#### Arguments
The cso method accepts the following arguments:<br>
- pa: probability of cuckoo's egg detection (default value is 0.5)
- nest: number of nests (default value is 100)
#### Methods
The cso method has the following additional methods:<br>
**get_nests()**: return a history of cuckoos nests
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.cso(n, function, lb, ub, dimension, iteration, pa=0.25, nest=100)
```
  ### Whale Swarm Algorithm
Whales are social animal and live in groups. Whales produces sounds of a very wide range. These sounds can often be linked to important functions such as their migration, feeding and mating patterns. Moreover, a large part of sounds made by whales are ultrasound. They determine foods azimuth and keep in touch with each other from a great distance by the ultrasound.<br>
When a whale has found food source, it will make sounds to notify other whales nearby of the quality and quantity of food. So each whale will receive lots of notifications from the neighbors, and then move to hte proper place to find food based on these notifications.
#### Mathematical model
The Whale Swarm Algorithm employes the following rules:<br>
1. All the whales communicate with each other by ultrasound in the search area;
2. Each whale has a certain degree of computing ability to calculate the distance to other whales
3. The quality and quantity of food found by each whale are associated to its fitness
4. The movement of a whale s guided by the nearest one among the whales that are better (judged by fitness) than it.
#### Algorithm:
 <pre>
 BEGIN
  Initialize agents
  Find current best
  global best = current best
  FOR t = 0 : number of iterations
    FOR each agent
      find better and nearest
      IF  Exists
        move current agent in direction of its better and nearest
      END IF
      find current best
      IF current best better than global best
        SET global best to current best
      END IF
    END FOR
   Save golobal best
 END
 </pre>
#### Arguments
The wsa method accepts the following arguments:<br>
- ro0: intensity of ultrasound at the origin of source
- eta: probability of message distortion at large distances
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.wsa(n, function, lb, ub, dimension, iteration, ro0=2, eta=0.005)
```
 ### Firework Algorithm
 The way fireworks explode is similar to the way an individual searches the optimal solution in swarm intelligence algorithms. As a swarm intelligence algorithm, fireworks algorithm consists of four parts, i.e., the explosion operator, mutation operator, mapping rule and selection strategy. The effect of the explosion operator is to generate sparks around fireworks. The number and amplitude of the sparks are governed by the explosion operator. After that, some sparks are produced by mutation operator. The mutation operator utilizes Gaussian operator to produce sparks in Gaussian distribution.
Under the effect of the two operators, if the produced spark is not in the feasible region, the mapping rule will map the new generated sparks into the feasible region.
To select the sparks for next generation, the selection strategy is used. Fireworks algorithm runs iteratively until it reaches the termination conditions
 #### Algorithm
 <pre>
 BEGIN
  Initialize agents
  Find current best
  global best = current best

  FOR i= 0 : nuber of agents
    evaluate function value for current best and worst
    FOR each agent
      perform explosion
      perform gausian mutation
   END FOR
   apply mapping rule
   Select new agents according to the selection strategy
   IF current best better than global best
        SET global best to current best
   END IF
   END FOR
  save global best
END
</pre>
#### Arguments
The fwa method accepts the following arguments:<br>
- m1: number of normal sparks
- m2: number of Gaussian sparks
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.wsa( n, function, lb, ub, dimension, iteration, m1, m2, eps, amp)
```
### Particle Swarm Optimization
A flock of birds is a good example of the collective behavior of animals. Flying in a big groups, they almost never collide with each other. A flock moves smoothly and is coordinated as if it is controlled by something and it's not about the leader of the flock. A flock of birds is  a swarm intelligence and birds in it act according to certain rules.<br>
The rules are the following:
1) Every bird tries to avoid collision with others;
2) Every bird moves in the close birds direction;
3) Birds try to move on the equal distance from each other;
4) A bird shares information with neighbours.
#### Mathematical model
In the PSO, agents are particles in the optimization task parameters space. On each iteration particles have some position and a velocity vector. For each position of a particle the corresponding objective function value is calculated and on the basis of that value a particle changes its position and velocity according to certain rules. The pso is a stochastic optimization method. It doesn't update existing populations but works with one static population which members steadily improve as they receive more information about the search space.
#### Algorithm
```
BEGIN
  Initialize agents
  Find current best
  Set global best = current best
  FOR i= 0 : number of iterations
    Calculate particle velocity
    Chage particles velocity
    Update particles positions
    Select new agents according to the selection strategy
    IF current best better than global best
      SET global best to current best
    END IF
  END FOR
  save global best
END
```
#### Arguments
The pso method accepts the following arguments:<br>
- w: balance between the range of research and consideration for suboptimal decisions found (default value is 0.5):<br> w&gt;1 the particle velocity increases, they fly apart and inspect the space more carefully <br> w&lt;1 particle velocity decreases, convergence speed depends on parameters c1 and c2<br>
- c1: ratio between "cognitive" and "social" component (default value is 1)
- c2: ratio between "cognitive" and "social" component (default value is 1)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.pso(n, function, lb, ub, dimension, iteration, w=0.5, c1=1, c2=1)
```
### Chicken Swarm Optimization
The CHSO algorithm mimics the hierarchal order in the chicken swarm and the behaviours of the chicken swarm. The chicken swarm can be divided into several groups, each of which consists of one rooster and many hens and chicks. Different chickens follow different laws of motions. There exist competitions between different chickens under specific hierarchal order.<br>
Domestic chickens live in flocks. There are over 30 distinct sounds for their communication by which they can communicate alot of information related to nesting, food discovery, mating and danger. Besides learning through trial and error, the chickens would also learn from their previous experience and others' for makein decisions.<br>
A hierarchal order palys a significant fole in the social lives of chickens. The preponderant chickens in a flock willl dominate the weak. There exist the more dominant hens that remain near to the head roosters as well as the more submissive hens nad roosters who stand at the periphery of the group. Removing or adding chickens from an existing group would causes a temporary disruption to the social order until a specific order is establicshed.<br>
#### Mathematical model
In the SHCO algorithm the chickens' behaviours are described by the following rules:
1. In the chicken swarm, there exist several groups. Each group comprises a dominant rooster, a couple of hens, and chicks.
2. How to divide the chicken swarm into several groups and determine the identity of the chickens (roosters, hens and chicks) all depend on the fitness values of the chickens themselves. The chickens with best several fitness values would be acted as roosters, each of which would be the head rooster in a group. The chickens with worst several fitness values would be designated as chick. the others would be the hens. The hens randomly choose which group to live in. The mother-child relationship between the hens and the chicks os also randomly established.
3. The hierarchal order, dominance relationship and mother-child relationship in a group will remain unchanged. These statuses only update every several time steps.
4. Chickens follow their group-mate rooster to search for food, while they may prevent the ones from eating their own food. Assume chickens would randomly steal the good food already found by others. The chicks search for food around their mother (hen). The dominant individuals have advantage in competition for food.
#### Algorithm
```
BEGIN
  Initialize a population of N chickens and define the related parameters
  Evaluate the N chickens' fitness values
  Find current best
  Set global best = current best
  FOR t = 0 : number of iterations
    IF(t % G == 0)
      Rank the chickens' fintess values and establish a hierarchal order in the swarm
      Divide the swarm into different groups, and determine the relationship
      between the chicks and mother hens in a goup
    END IF
    FOR i = 1 : N
      IF i == rooster
        Update its solution and location using equation for roosters
      END IF
      IF i == hen
        Update its solution and location using equation for hens
      END IF
      IF i == chick
        Update its solution and location using equation for chicks
      END IF
      Evaluate current best
      IF current best better than global best
        SET global best to current best
      END IF
  END FOR
END
```
#### Arguments
The chso method accepts the following arguments:<br>
- G: after what time relationship will be upgraded (default value is 5)
- FL: parameter, which means that the chick would follow its mother to forage for food (0 < FL < 2. Default value is 0.5)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.chso(n, function, lb, ub, dimension, iteration, G=5, FL=0.5)
```
### Social Spider Algorightm
The Social Spider Algorightm mimics the social spiders colony behaviour. These spiders form colonies which allow them to remain together on a communal network.<br>
A social spicer colony consists of two main components: its members and its communal network. All members are divided into two different groups: males and females.
#### Mathematical model
The SSO assumes that entire search space is a communal web, where all the social-spiders interact to each other. Each solution within the search space represents a spider position in the communal web. Every spider receives a weight according to the fitness value of the solution that is symbolized by the social-spider. The algorithm models two different search agents (spiders): males and females. Depending on gender, each individual is conducted by a set of different evolutionary operators which mimic different cooperative behaviors that are commonly assumed within the colony. One of characteristics of social-spiders is the highly female-biased populations.
In order to emulate this fact, the algorithm starts by defining the number of female and male spiders that will be characterized as individuals in the search space.
#### Algorithm
<pre>
BEGIN
  Create the population of spiders
  Initialize target vibration for each spider
  FOR i = 0 : number of iterations
    FOR each spider in population
      Evaluate the fitness values of a spider
      Generate a vibration at the position of the spider
    END FOR
    FOR each spider in population
      Calculate the intensity of the vibrations generated bu other spiders
      Select the strongest vibration from all vibrations
      IF the intensit of the strongest vibration is larger than target vibration
        target vibration = strongest vibration
      END IF
      Perform a random walk towards target vibration
      Generate a random number rn from [0,1)
      IF rn &lt; p<sub>j</sub>
        Assign a random position to the spider
      END IF
      Attenuate the intensity of target vibration
    END FOR
  END FOR
  Save the best solution
END
</pre>
#### Arguments
The ssa method accepts the following arguments:<br>
- pf: random parameter from 0 to 1 (default value is 0.4)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.ssa(n, function, lb, ub, dimension, iteration, pf=0.4)
```
### Cat Algorithm (Cat Swarm Optimization)
Cat Algorithm mimics the two aspects of cats behaviour: seeking mode and tracking mode. Every cat has its own position composed of M dimensions, velocities for each di-mension, a fitness value, which represents the accommodation of the cat to the fitness function, and a flag to identify whether the cat is in seeking mode or tracing mode. The final solution would be the best position in one of the cats due to CSO keeps the best solution till it reaches the end of iterations.
#### Mathematical model
**Seeking mode** is used to model the situation of the cat, which is resting, looking around and seeking the next position to move to. In seeking mode, the four essential factors are defined: seeking memory pool (SMP), seeking range of the selected dimension (SRD), counts of dimension to change (CDC), and self-position considering (SPC).<br>
For the seeking mode the following algorithm is proposed:
<pre>
FOR each cat-agent
  Create j = SMP copies
  IF SPC is true
    j = SMP - 1
    Save copies
  END IF
END FOR
FOR each copy
  Randomly add (or subtract) SRD
END FOR
FOR each copy
  Calculate fitness function value FS<sub>i</sub>
END FOR
IF all values of the fitness function are not equal to each other
  Calculate P<sub>i</sub>
END IF
IF FS<sub>i</sub> are equal
  P<sub>i</sub> = 1
END IF
FS<sub>b</sub> = FS<sub>min</sub>
Replace cat-agent with its copy
</pre>
**Tracing mode** is the second mode of a cat. In this mode the cat tracks down and attacks its prey.<br>
In tracing mode the algorithm works as follows:
<pre>
Calculate new velocity vector value for each cat
Calculate new position of a cat
</pre>
#### Algorithm
<pre>
Initialize n cats in the domain D randomly (Initially each cat has zero velocity vector)
Generate a flag for each cat
FOR number of iterations
  Calculate Pbest
  Move each cat considering its flag:
    IF flag = 0
      Perform seeking mode
    ELSE
      Perform tracing mode
    END IF
  Redistribute the flags
END FOR
</pre>
#### Arguments
The ca method accepts the following arguments:<br>
- mr: number of cats that hunt (default value is 10)
- smp: seeking memory pool (default value is 2)
- spc: self-position considering (default value is False)
- cdc: counts of dimension to change (default value is 1)
- srd: seeking range of the selected dimension (default value is 0.1)
- w: constant (default value is 0.1)
- c: constant (default value is 1.05)
- csi: constant (default value is 0.6)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.ca(n, function, lb, ub, dimension, iteration, mr=10, smp=2,
                 spc=False, cdc=1, srd=0.1, w=0.1, c=1.05, csi=0.6)
```
### Harmony Search
This algorithm mimics the jazz play technique. In its base lays the observation that an experienced musician can quickly adapt to play with other musicians or improvise a good melody.
#### Mathematical model
Each musician corresponds to an attribute in a candidate solution from a problem domain, and each instrument's pitch and range corresponds to the bounds and constraints on the decision variable. The harmony between the musicians is taken as a complete candidate solution at a given time, and the audiences aesthetic appreciation of the harmony represent the problem specific cost function. The musicians seek harmony over time through small variations and improvisations, which results in an improvement against the cost function.
The information processing objective of the technique is to use good candidate solutions already discovered to influence the creation of new candidate solutions toward locating the problems optima. This is achieved by stochastically creating candidate solutions in a step-wise manner, where each component is either drawn randomly from a memory of high-quality solutions, adjusted from the memory of high-quality solutions, or assigned randomly within the bounds of the problem. The memory of candidate solutions is initially random, and a greedy acceptance criteria is used to admit new candidate solutions only if they have an improved objective value, replacing an existing member.
#### Algorithm
<pre>
Step 1. Randomly generate initial harmony in the domain D {h<sub>i</sub> &isin; D}.
Step 2. On each iteration generate new zero harmony h<sub>new</sub>
Step 3. For each component of a new harmony generate a random number &epsilon; from 0 to 1. If &epsilon; is less than HMCR, then write in the current component the corresponding copmonent from a randomly chosen existing harmony. After that modify the component.
Step 4. IF f(h<sub>new</sub>) is better than Gbest, h<sub>new</sub> = h<sub>Gbest</sub>
</pre>
#### Arguments
The hs method accepts the following arguments:<br>
- pitch adjusting rate (default value is 0.5)
- hmcr: harmony consideration rate (default value is 0.5)
- bw: bandwidth (default value is 0.5)
#### Method invocation
The method can be invoked by passing the arguments in the following order:
```
SwarmPackagePy.hs(n, function, lb, ub, dimension, iteration, par=0.5, hmcr=0.5, bw=0.5)
```
### Gravitational Search Algorithm
The Gravitational Search Algorithm is based on the laws of gravitation and mass interaction. Basically, this algorithm is similar to Particle Swarm Optimization (PSO), since they are both based on the development of a multi-agent system.
#### Mathematical model
GSA operates with two laws:<br>
* law of gravitation: each particle attracts other particles and force of gravity betweent two particles is directly proportional to the product of their masses and inversly proportional to the distance between them (one should pay attention to the fact that, unlike the law of universal gravitation, we don't use the square of the distance, as it results in better results of the algorithm).<br>
<br>F<sub>1</sub> = F<sub>2</sub> = G * (m1&#9587;m2)*r<sup>-2</sup><br>

* law of motion: the current velocity of any particle is equal to the sum of the part of the velocity at the previous instant of time and to the change in velocity which is equal to the force the system affects the particle with divided by the inertial mass of the particle.
#### Algorithm
<pre>
1. Generate the system randomly;
2. Determine the fitness of each particle;
3. Update the value of the gravitational constant, masses and the best and the worst particle values;
4. Calculate the resultant force in different directions;
5. Calculate accelerations and velocities;
6. Update particles' positions;
7. Repeat steps 2 to 6 until the stop condition is reached.

</pre>

### Tests
All algorithms were tested with different test functions. In fact, you can run tests for all the algorithms on your own. All you need to do is to open terminal (console) and insert the following line:
```
pytest -v —tb=line test.py
```
Every algorithm is tested with the following set of test functions:<br>
- Ackley function
- Bukin function
- Cross in tray function
- Sphere function
- Bohachevsky function
- Sum squares function
- Sum of different powers function
- Booth function
- Matyas function
- McCormick function
- Dixon price function
- Six hump camel function
- Three hump camel function
- Easom function
- Michalewicz function
- Beale function
- drop wave function

### Animation
There are 2D animation and 3D animation of search process. The general way to start it is (example for pso algorithm):<br>
#### 2D animation
```
# Compute the algorithm
function = SwarmPackagePy.testFunctions.easom_function
alh = SwarmPackagePy.pso(15, function, -10, 10, 2, 20)
# Show animation
animation(alh.get_agents(), function, 10, -10)
```
#### 3D animation
```
# Compute the algorithm
function = SwarmPackagePy.testFunctions.easom_function
alh = SwarmPackagePy.pso(15, function, -10, 10, 2, 20)
# Show animation
animation3D(alh.get_agents(), function, 10, -10)
```
#### Save the animation
You can also save the animation of the search process. To do this, add as an animation argument sr=True. The example of saving animation:
```
# Compute the algorithm
function = SwarmPackagePy.testFunctions.easom_function
alh = SwarmPackagePy.pso(15, function, -10, 10, 2, 20)
# Show animation
animation(alh.get_agents(), function, 10, -10, sr=True)
```
