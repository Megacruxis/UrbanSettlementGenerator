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
Wednesday : I used my morning to complete the code which generate wells (so they are now generated during the creation of the city, see picture 28 and 29). I Then added adaptability on the path creation (the block used to create the path depend on the biome) and begin to work on some improvements for the function which flatt the lots.    
Thursday : Flattening the lot is way harder than I expected. Even after spending the day experimenting, I still haven't found a consistent way to flatten lots properly.
Friday : After a quick talk with Eduardo I implemented a new way of flattening the lots (using random area selected the same way as lot but with less constraint). This method is not perfect and have some problem so it still needs some change. During the afternoon I was stress by a half cut tree, so I decide to code the cleaning of the tree earlier than planned in my planning. At the end of the day my function which clean tree was not working.

Week seven (18/05/2020 - 24/05/2020) :
Monday : I continued my work on the elimination of the trees with a new idea. Spent the whole day programming it and it's not finished. Currently, it deletes all the trees with a trunk inside a lot but it's not able to clean trees who have only some of their leaf in the plots.
Thuesday : I finally finish a first version of a working function which clean tree properly. The process is the following : Before doing any earthwork, all the tree in the modified area are saved (in an array containing all the block of the trees). After the earthwork all the tree are place again in the area and if the area is in a lower position than before the flattening all the tree which have block outside the area are deleted (we don't place them back). When cleaning the area before building we only delete the tree with trunk inside the building area or those who have leaf inside the building area. The current version of the function is not able to delete Acacia tree and have some problem with big oak tree (those with a 2×2 blocks trunk)and dark oak tree.
Wednesday : I begin to program the deletion of the "special" tree and clean the code of the first version. The function is now able to delete and delete properly the Acacia tree and the Jungle tree.
Thursday : I add the case of the oak tree and the dark oak tree which mean that the function is now able to handle all type of tree. Since I still have not test all the case the function could have some bug but it should be working. I also have to redo my function which locate the trunk of a tree from one of its leave blocks. The second version of the tree deletion is almost ready (still need some test and one more special function).
Friday : I have begun the long process of testing my tree deletion. I found some bugs that I corrected during the morning. The deletion of the oak tree is not working properly when he is adjacent to other oak tree, so I spent the rest of the day trying to solve this issue. I have come to the conclusion that the most optimal way is to delete all the adjacent trees even if it's not what I originally wanted (since I want to keep as many trees as possible in order to have some kind of "green" city). I will change my function in the upcoming days.

Week height (25/05/2020 - 31/05/2020) :
Monday : I use my day to correct the bug for the deletion of the acacia, the acacia and the oak tree. I also upgraded the function which find the trunk of a tree from the position of one leaf block. The only tree that the function cannot delete properly is the size two jungle tree.
Thuesday : Had difficulty to work today. I found the problems in the jungle tree deletion but I did not correct them.
Wednesday : I have corrected all the bugs in the jungle tree deletion and continue the testing. At the end of the day, I still had a few tests to do.
thursday : I think I'm starting to be exhaust by a lot of different things. I did not find the motivation to work or even left my bed from the day. 
Friday : I'm still unable to work. I just need this day and after I will begin to work again. 

Week Nine (01/06/2020 - 07/06/2020) :
Monday : I begin to work on my Internship report. Also, I continue the debugging of my tree deletion function.
Thuesday : I found a new bug in my tree deletion function which took me a lot of time to correct then I continue my work on my Internship report.
Wednesday :
thursday :
Friday :

updated the 03/06/2020 
