# Pong
Pong built with Python implementing various levels of opponent difficulty. 

# Installation
Make a clone of this repository to your device or download the pong.exe file found in the distribution folder.

# Run
Open the pong.exe file on your device and choose your difficulty.

# Thoughts
This project was built to display how to make video game AI difficulties variable. Although this example is simple
compared to the 3D FPS games of today it still brings some valuable information. In this implementation there is 
two characteristics that change about the AI player with difficulty. Size and speed are these variables. As
difficulty increases these both increase to create a harder experience for the player. 

Making an engaging encounter with enemies in currently popular games also use factors like health, damage, shields,
and abilities (i.e stun the player, blind the player, poison the player). To make an encounter engaging it takes
more than simply cranking those knobs up to an impossible level. For a challenging experience these settings must
be balanced around the possibility of the player. If an encounter is truly impossible to complete because of AI
enemies than it is not engaging and players will often quit entirely. 

Players seek challenge to an achievable level, meaning that they want to overcome a barrier that has been placed
before them. Take for example the game Elden Ring, which release in 2022. This game had extremely difficult boss
mechanics to overcome as well as large health pools. Their speed, damage, health, and mobility where cranked to
the maximum and most mistakes lead to death for the player. Despite this the game was extremely popular and 
was loved by many people. The key to their success was the achievability of their encounters. Although the enemy
statistics were so high, they also had weaknesses and exhibited patterns that players could memorize. This led
to an extremely engaging experience that challenge seeking players spent hours on looking to beat the game. 

In summary, game AI can make or break the games experience for players. If they are too difficulty with no recourse
for players than it becomes something that is impossible and players will quit. On the other hand, if they are too
easy and players can achieve victory without pushing themselves then the encounters will become dull to most players.
AI encounters used as a mechanic to engage the player should strive to achieve a middle ground where the difficulty 
creates a barrier for player progress but has a clearly achievable success condition. Consider balancing high stats
with weaknesses or mechanics that can exploited after memorized. Also, look to encounter difficult long-widned 
mechanics with lower health to reward players for dodging/surviving this all. 

# Known Bugs
Currently when the pong ball begins to move too fast it will phase through paddles and result in a point. This bug is
likely caused by the way that I am checking for collision using pixel zones. This is a limitation of my knowledge of
the turtle library. If I return I will look into using another library to help draw and play the game. 
