# rubik_plane
A simple CML python game inspired by Rubik's cube. 

The winning sequence is to return the pattern to
[1,2,3],
[4,5,6],
[7,8,9]
There are 4 basic movements for the plane, up, down, left, and right, with entering the commend in short form u,d,l,r. The digits 0,1,2 indicate which row or column is from top to bottom or left to right. Using the example from above, if the command is “l1” the result is 

[1,2,3],
[5,6,4]
[7,8,9]

If the command is “u0”:

[5,2,3]
[7,6,4]
[1,8,9]

Level 1 is the easiest and level 3 is the hardest. Use the least steps to win the game.
