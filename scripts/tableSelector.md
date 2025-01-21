@author JM Wittenberger
@date 2024-1-20
### takePhoto()
### getPrediction()
### findPiecePositions()
findLocators()

```python
point1 = Point(x,y)
point2 = Point(x,y)
point3 = Point(x,y)
peice = Point(x,y)
```
        
### doMath()
```python
import numpy as np

v = Point((point2.x - point3.x), (point2.y - point2.y))
u = Point((point1.x - point3.x), (point1.y - point2.y))
```

Make a function to find constants in a system of equations

```python
def solveForConstants():

    # solveing for constants

    a = np.array([[(point2.x - point3.x), (point1.x - point3.x)], [(point2.y- point3.y), (point1.x - point3.x)]])

    b = np.array([piece.x - point3.x, piece.y - point3.y])

    x = np.linalg.solve(a, b)

    return x
```

```python
    c1 = solveForConstants()[0]
    c2 = solveForConstants()[1]
```
    
### applyRobpotConversion(){
    
}
### selectPiece()
### moveRobot()