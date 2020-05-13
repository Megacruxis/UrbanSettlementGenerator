# Logs 

Week two (13/04/2020 - 19/04/2020) :
Monday : My task for this week is to add a new building and then to work on some kind of adaptability. I choose to add a greenhouse. Creation of the design and implementation of the function which create the floor (see picture 0) 
Tuesday : Spent the day coding the function which create the glass dome and the facade of the greenhouse. 
Wednesday : Implementation of a population system in the city. One greenhouse spawn for every 12 inhabitants (see pictures 1, 2 and 3). With the help of Eduardo, correction of a bug where the generation fail if there were a river which separated the selection in two blocks.
Thursday : Begin my work on adaptability. I choose to implement a system which find the types of wood in the area where we are going to build the city and only use one those types to building my greenhouse (for example if there is birch wood in the area, the green house foundation can only be built in birch wood). I spent the day coding a first version of the function which count the number of blocks of each type of wood found in the selected area 
Friday : Resolve my big issue with python heritage (thank to Eduardo and a member of the GDMC Discord server) which unable me to complete the function I start yesterday. Implementation of the utilization of the found wood for the generation of the greenhouse, thus finishing my weekly objectives (see pictures 4 to 7).

Week three (20/04/2020 - 26/04/2020) :
Monday : My first task of the week was to determine which aspect of the generator I wanted to improve during the rest of my internship. I spent my day finding ideas of improvement in order to share them with my supervisor. I also improved my used of the found wood : now, the wood used is chosen with the proportion of each type of wood (if there is 90% oak, the foundation of the greenhouse have 90% chance to be built in oak wood)
Thuesday : Using the feedback my supervisor gave on my improvement ideas I make a Planing (see planing file) of my upcoming work. I then begin my work on the first goal of the planning : being able to determine in which biome is the selected area. The first step of this work was to make research in the official Minecraft wiki in order to identify some properties of the different major biome (which are going to lead to a way to identify them). For example, you can only find cocoa in a jungle.
Wednesday : Programming of the function which count the numbers of block of each type of ground block and plant of the selected area. With the help of the research I made Tuesday I write the first part of the function which determine the biome of the selected area.
Thursday : I finished the programming of the function which determine the biome. Then, I performed test on random generated maps (most of the test were successful). I spent the rest of the day writing the log and the Planning files.
Friday : I begin my work on the improvement of the building. Spend most of my day understanding how the code work and working on the design of the first floor.

Week four (27/04/2020 - 03/05/2020) :
Monday : After the weekly meeting I lost the rest of the morning trying to understand why the building never had even depth or width (was due to python integer division). Understanding this allows me to start working on a new type of floor for the skyscraper : a floor with two small apartments instead of one big. At the end of the day my floor with two apartments was generated (see pictures 8 and 9) but I still had some bug on the generation of the furniture of both apartment. 
Thuesday : I finish the programming for the generation of the furniture in the small apartment (see picture 10 and 11). I then begin my work on the spawn generation of balcony for the apartment. The first step was to design different type of balcony. Then I add the code to generate them and the code which determine when to spawn a balcony. At the end of the day I was able to generate balcony for both big or small apartment but the block use for their construction was always the same (no adaptability) (see pictures 12 and 13).
Wednesday : Thank to my function which determine the biome, I was able to program the adaptability for the balconies (see picture 14 and 15). I then continue my work on the design of the first floor (he gave me a lot of trouble, see picture 16) and then begin my programming of its generation. Currently, the first floor is almost generated properly (I have a problem with the flower pot) and it adapts to is environment (if we are in a desert the plant are going to be cactus instead of bush, see picture 17 and 18).
Thursday : I Spend most of my day understanding how to put flower in flower pot and turns out the code to do it was not implemented. I ask for help on the discord, i'm still waiting for an answer. The rest of the day was spent to add the adaptability to the furniture of the apartment and work on the design of the roof (which is going to be my last building upgrade for now).
Friday : I use my whole day to implement the generation of the roof. The roof generation currently lack of adaptability since it's always generated the same way but it is working (see picture 19 and 20).

Week five (04/05/2020 - 10/05/2020) :
Monday : I begin the day by correcting the generation of the plants with a height of two blocks (I was only spawning the first block) when creating the roof. I then spent the rest of the day programming the adaptability of the roof (see picture 21)
Thuesday : I begin my work on the adaptability of the houses. The furniture of the house now use blocks depending on the environment. But I still have some work left in order for the whole house to be adaptive.
Wednesday : -
Thursday : -
Friday : -

Week six (11/05/2020 - 17/05/2020) :
Monday : The blocks used for the walls of the house, the pillars and the roof now depend on the environment. I also made some change to the roof design (replace the full blocks with stairs). This complete the adaptability of the house (see picture 22 to 24). 
Thuesday : I have completed the Greenhouses adaptability (see picture 25 to 27) which mean that all the current buildings have adaptability. I then begin working on the creation of a new building : the well (which will only spawn in dry areas like deserts). At the end of the day half of the well generation was programmed.
Wednesday : I used my morning to complete the code which generate wells (so they are now generated during the creation of the city, see picture 28 and 29).  

updated the 13/05/2020 
