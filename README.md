💬 Collaboration Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

🗓 Date: 6/03/25

📌 Course: Spr25_CS_034 CRN 39575

# 🌳 Lab 15 – Balanced Trees in Action: Two-Track Options

🔧 Option 1: Reflect, Refactor, and Rebuild

## 🧪 Option 2: Build a B-Tree from Scratch in Python

- Create a 2-3-4 Tree node structure
  
       - Each node support up to 3 keys
       - Each node has 1, 2 or 3 children
- Implement a 2-3-4 Tree structure with dynamic node splitting and merging
  
       - Dynamic node splitting
       - Merging & Rotation to maintain balance
       - In Order Traversal logic


🧾 Grading Rubric – Option 2
```
Category	                               Points
Core Tree Methods Functionality	           10 pts
Balancing Logic & Node Splits	           10 pts
Code Quality & Comments	                   5 pts
Output Demonstration & README	           5 pts
Total	                                   30 pts
```
### 🧠 Design & Structure
```
Lab15 2-3-4 Tree
├── main.py:
├           visualize_tree()
├── 234Tree.py: 
├           Node234 class, Tree234 class
├── tests/
├           test_BTree.py
├           test_main.py
├           __init__.py  
├── sample_output_01.png
├── sample_output_02.png
└── README.md
```
### 🔨Implemented Methods
```
- insert(int key)
     Add a new key to the tree

- contains(int key)
     Check whether a key exists

- inOrderTraversal()
     Store and Print all keys in sorted order

- ⭐ remove(int key) (Bonus)
     Delete a key and rebalance if necessary

- ⭐ visualize_tree() (Bonus)
     Visualize BTree structure graphically
```
### ✅ Input
```
Random generated values list
keys = [4, 7, 41, 50, 57, 71, 72, 73, 81, 97]
Random value to test contains() for non-existent key:
Random_value = 90
```
```
Use a test driver to insert 15–20 random integers
```

### 📤 Insertion, Search & Deletion Sample Output
```
Inserted 4
      [4]

Inserted 72
    [4, 72]

Inserted 71
  [4, 71, 72]

Inserted 41
              [71]
         [4, 41]  [72]

Inserted 81
              [71]
       [4, 41]  [72, 81]

Inserted 7
              [71]
      [4, 7, 41]  [72, 81]

Inserted 97
              [71]
    [4, 7, 41]  [72, 81, 97]

Inserted 73
                    [71, 81]
           [4, 7, 41]  [72, 73]  [97]

Inserted 57
                           [7, 71, 81]
                  [4]  [41, 57]  [72, 73]  [97]

Inserted 50
                               [71]
                            [7]  [81]
                [4]  [41, 50, 57]  [72, 73]  [97]

In-Order Traversal:
[4, 7, 41, 50, 57, 71, 72, 73, 81, 97]

Searching for 4: Found

Searching for 72: Found

Searching for 71: Found

Searching for 41: Found

Searching for 81: Found

Searching for 7: Found

Searching for 97: Found

Searching for 73: Found

Searching for 57: Found

Searching for 50: Found

Searching for a random value 90: Not Found

Removed 4
                               [71]
                            [41]  [81]
                  [7]  [50, 57]  [72, 73]  [97]
Removed 72
                               [71]
                            [41]  [81]
                    [7]  [50, 57]  [73]  [97]
Removed 71
                    [41, 73]
             [7]  [50, 57]  [81, 97]


Removed 41
                    [50, 73]
               [7]  [57]  [81, 97]


Removed 81
                    [50, 73]
                 [7]  [57]  [97]


Removed 7
              [73]
         [50, 57]  [97]


Removed 97
              [57]
           [50]  [73]


Removed 73
   [50, 57]


Removed 57
     [50]


Removed 50
<empty tree>
<empty tree>

In-Order Traversal:
[]
```
![Sample Output](sample_output_01.png)

![Sample Output](sample_output_02.png)

### 📊 Test
To run the unit tests for the repository, run the commands below
```
python -m pip install pytest
python -m pytest
```

💡 Implementation Tips
Start with a Node class to hold keys and children

Use a test driver to insert 15–20 random integers

Print in-order results to validate the structure

 Extra Credit
Add a visual print method that shows the tree level by level

📤 Submission Requirements
Submit your code files, output screenshots, and a short README through zyBooks

Ensure your code is commented, especially around node splitting logic

📤🧾✅✅✅Submission Requirements


