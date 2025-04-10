# Ternary Search Tree Implementation

## Overview

This project implements a **Ternary Search Tree (TST)**, a type of trie-based data structure that efficiently supports search, insertion, and deletion operations. The project is developed in Python using an **object-oriented approach** to ensure modularity, clarity, and scalability. The implementation is tested for correctness and performance and is intended for use both in Jupyter notebooks for demonstrations and Python scripts for benchmarking on HPC infrastructure.


## Project Structure
```
/TernarySearchTree
    ├── README.md                 
    ├── ternary_search_tree.py      
    │   ├── test_tst.py          
    ├── benchmarks
    │   ├── benchmark.py          
    ├── job_script.sh              
    ├── requirements.txt           
```
Below is the directory structure for the Ternary Search Tree project:
- `README.md`: This file, which provides an overview of the project, installation instructions, and usage guidelines.
- `ternary_search_tree.py`: The main implementation of the Ternary Search Tree, including `insert`, `search`, and `delete` methods.
- `tests/test_tst.py`: Unit tests for the Ternary Search Tree to ensure its correctness.
- `benchmarks/benchmark.py`: A script for benchmarking the performance of the Ternary Search Tree on large datasets.
- `job_script.sh`: A shell script for running benchmarking on the HPC infrastructure.
- `requirements.txt`: A file containing the list of Python dependencies required for the project.

