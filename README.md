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
keys = [12, 22, 32, 54, 59, 72, 74, 76, 90, 98]
```
```
Use a test driver to insert 15–20 random integers
```

### 📤 Insertion Sample Output
```
will update after fixing bugs
```
![Sample Output](sample_output_01.png)

### 📤 Search & Deletion Sample Output
```
will update after fixing bugs
```
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


