💬 Collaboration Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

🗓 Date: 6/03/25

📌 Course: Spr25_CS_034 CRN 39575

# 🌳 Lab 15 – Balanced Trees in Action: Two-Track Options

🔧 Option 1: Reflect, Refactor, and Rebuild

## 🧪 Option 2: Build a B-Tree from Scratch in Java

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
├           ??
├           ??
├           ??
├           ??
├           ??
├── BTree.py: 
├           Node234 class, Tree234 class
├── tests/
├           test_BTree.py
├           test_main.py
├           __init__.py  
├── sample_output.png
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
keys = [15, 17, 18, 24, 18, 15, 46, 24, 44, 92]
```
```
Use a test driver to insert 15–20 random integers
```

### 📤 Insertion Sample Output
```
Inserted 18
     [18]

Inserted 46
   [18, 46]

Inserted 89
 [18, 46, 89]

Inserted 56
              [46]
         [18]  [56, 89]

Inserted 95
              [46]
       [18]  [56, 89, 95]

Inserted 15
              [46]
     [15, 18]  [56, 89, 95]

Inserted 24
              [46]
   [15, 18, 24]  [56, 89, 95]

Inserted 44
                             [18, 46]
            [15]  [24, 44]  [15, 18, 24]  [56, 89, 95]

Inserted 92
                           [18, 18, 46]
                  [15]  [24]  [15]  [24, 44, 92]

Inserted 17
                               [18]
                            [18]  [46]
                [15, 17]  [24]  [15]  [24, 44, 92]

In-Order Traversal:
[15, 17, 18, 24, 18, 15, 46, 24, 44, 92]
```


### 📤 Search & Deletion Sample Output
```
Searching for 18: Found

Searching for 46: Found

Searching for 89: Not Found

Searching for 56: Not Found

Searching for 95: Not Found

Searching for 15: Found

Searching for 24: Not Found

Searching for 44: Not Found

Searching for 92: Found

Searching for 17: Found

Removed 18
                               [15]
                            [18]  [24]
                [15, 17]  [24]  [15, 46]  [44, 92]

Removed 46
                               [15]
                            [18]  [24]
                [15, 17]  [24]  [15, 46]  [44, 92]

Removed 89
                               [15]
                            [18]  [24]
                [15, 17]  [24]  [15, 46]  [44, 92]

Removed 56
                               [15]
                            [18]  [24]
                [15, 17]  [24]  [15, 46]  [44, 92]

Removed 95
                               [15]
                            [18]  [24]
                [15, 17]  [24]  [15, 46]  [44, 92]

Removed 15
                               [15]
                            [18]  [24]
                  [15, 17]  [24]  [46]  [44, 92]

Removed 24
                               [15]
                            [18]  [44]
                    [15, 17]  [24]  [46]  [92]

Removed 44
                      [15]
                    [18]  []
          [15, 17]  [24]  [46, 92, 92]

Removed 92
                      [15]
                    [18]  []
            [15, 17]  [24]  [46, 92]

Removed 17
                      [15]
                    [18]  []
            [15, 17]  [24]  [46, 92]

In-Order Traversal:
[15, 17, 18, 24, 15, 46, 92]
```


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


