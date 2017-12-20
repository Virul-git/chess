# This is a sample readme


	- Note:
	- A README file is frequently updated with every commit.
	- Though the README may seem to be a tedious work, after first 
	few commits the additions are miniscule, but the effort is worth it.
	- A proper guidelines are essential for collaborative projects.
	- below are some guidelines.


---

### Updates:


	- In this section we mention the chages done from the previous commit.
	- This is done only to the master branch as it is changed less frequently 


- change in SPI ISR:
	- delay of 50ms introduced.
	- PB1 is set high for external interrupt to OBC
- function "func3" added in the housekeeping routine
- change of variable names:
	- m1_v2 to f1_v4O
	- m1_v3 to f1_v5


---


## FILES AND FOLDERS

	- all files and folders presesnt in the given folder are mentioned here
	- folder names are followed by "/" to differentiate them from files


- main.c
- file.h
- file.c
- file1.h
- file1.c
- Makefile
- README.md
- include/ 


---

### main.c

	- description of files in this folder are done here
	- a short description of the contents in the folders is also given.
	- details about the files in the folder are given in the README file in the respective folder


- small description about what the code in the file performs.

###### dependencies:

	- mentioning the dependencies is essential, this enables 
	the person making a change to a file has an idea of the files he will be affecting. 

- details about the include files used and also specify the functions for which that file was included.

###### functions  in main.c:

	- mention the functions being used in the file
	- filling in a table helps to know a lot about a function
	- this table resembles close to a header file

| function name | return type of function | argument 1 | argument 1 type | argument 2 | argument 2 type |
|   --- 		| 			--- 		  |		---    |	--- 		 |	--- 	  | 	--- 		|
|   func1 		| 			void 		  |		arg1    |	int 		 |	arg2  	  | 	char* 		|
|   func2 		| 			int 		  |		arg1    |	size_t 		 | ---    	  | 	   --- 		|
|   func3 		| 			char 		  |		  ---   |	 ---   		 | ---	     	  | --- 	    		|

###### variables in main.c :

	- mentioning about the variables being used can come in handy at times
	- It is not necessary to mention redundant variables like "i,a,x" use use for a 
	for loop or any iterative loop.
	- local variables that die inside a function can also be safely discarded from writing
	in this table
	- every function can have a table of this sort

|		| function 		|	var1	|	var2	|	var3	|	var4	|	var5	|	var6	|
|	---	|	---			|	---		|	---		|	---		|	---		|	---		|	---		|
| name	|	func1		|	f1_v1	|	f1_v2	|	f1_v3	|	f1_v4	|	f1_v5	|	---		|
| type	|	void		|	int		|	char	|	char*	|	int\[-\]	|	char\[-\]	|	---		|
| size	|	---			|	---		|	---		|	---		|	5		|	6		|	---		|
| desc	|	---			|	status variable		|	data address		|	eeprom write pointer	|	position variable [x,y,z,t1,t2]		|	spi data buf	|	---		|


