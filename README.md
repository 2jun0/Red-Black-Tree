# Red Black Tree
Red Black Tree made of python

# Requirement
binarytree : [Link](https://pypi.org/project/binarytree/)

Use the package manager pip to install binarytree.

```bash
pip install binarytree
```
# Execution Screen
## Insertion
Insert 10 value to tree
```bash
---Test of red black tree---
Select mode : (1. insert, 2. delete, 3. search, 4. exit): 1
mode : 1
Enter the key: 10
----tree----

   _B10_
  /     \
B-1     B-1
```
---
Then, insert 20 value to tree
```
Select mode : (1. insert, 2. delete, 3. search, 4. exit): 1
mode : 1
Enter the key: 20
----tree----

   _B10_____
  /         \
B-1        _R20_
          /     \
        B-1     B-1
```
---
Finally, insert 30 value to tree
```
Select mode : (1. insert, 2. delete, 3. search, 4. exit): 1
mode : 1
Enter the key: 30
----tree----

       _____B20_____
      /             \
   _R10_           _R30_
  /     \         /     \
B-1     B-1     B-1     B-1
```
## Deletion
Delete 10 value node of tree
```
Select mode : (1. insert, 2. delete, 3. search, 4. exit): 2
mode : 2
Enter the key: 10
----tree----

   _B20_____
  /         \
B-1        _R30_
          /     \
        B-1     B-1
```
## Search
Search 30 value node of tree
```
Select mode : (1. insert, 2. delete, 3. search, 4. exit): 3
mode : 3
Enter the key: 30

   _R30_
  /     \
B-1     B-1
```
