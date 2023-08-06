# QuickSelectionResearch

## Description
Files used to gather empirical results for the complexity of Default and Dynamic Quickselect, as well as the Floyd-Rivest Algorithm. Each of their corresponding .py files contains a class for that algorithm. The reductionConstant.py file collects the values of the average reduction constant of each of the algorithms, and the timeCollection.py collects the average running time of each algorithm. 

## Using the Program
If you want to perform these tests yourself (or see the actual python code I wrote for Dynamic Quickselect), you can pull or download the folder and open it in your IDE. In timeCollection.py, on line 25, you can modify the values for the maximum value in the array, the size of the array, and the number of times each algorithm is run and averaged. If you run the file with whatever values you have input, the program should output the resulting times and operations in the terminal. You can modify these same values on line 21 of reductionConstant.py, which will also output the results to the terminal. In both files you should also be able to change the bounds used by dynamic when the dynamic object is initialized (right now it is set to .4 and .6). 
