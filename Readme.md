### Features

- Graph matrices imported from CSV can be used
- Enter the graph by hand
- BFS with tail
- DFS with stack

![](https://i.imgur.com/8zosppo.png)

# Uninformed Search

DFS and BFS in python in which you can be the one to decide which graph you want to go through, this shows the route to be taken depending on the algorithm.


## CSV 

**Which in excel or others should look like this**

![](https://i.imgur.com/pM1Qs9R.png "Excel CSV")

The correct way to edit the CSV is as follows
```csv
,a,b,j,p,d,e,c,g,f,i,h
a,0,1,15,4,0,0,0,0,0,0,0
b,1,0,0,0,2,2,3,0,0,0,0
j,15,0,0,0,0,0,0,0,0,0,0
p,4,0,0,0,0,0,0,0,0,0,0
d,0,2,0,0,0,0,0,3,0,0,0
e,0,2,0,0,0,0,2,4,5,0,0
c,0,3,0,0,0,2,0,0,5,20,0
g,0,0,0,0,3,4,0,0,10,0,1
f,0,0,0,0,0,5,5,10,0,0,0
i,0,0,0,0,0,0,20,0,0,0,0
h,0,0,0,0,0,0,0,1,0,0,0
```

## Manual input

Manual entry is done only by following the steps, which are indicated when selecting the option

