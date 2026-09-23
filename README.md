<div align="center">

# 🎓 College Practical Codes

<p align="center">
  <strong>A curated collection of practical lab experiments, algorithms, and projects completed during B.Tech in Computer Science & Engineering.</strong>
</p>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Maintained-success?style=for-the-badge)](#)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue?style=for-the-badge)](#)

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-subjects-covered">Subjects</a> •
  <a href="#-repository-structure">Repository Structure</a> •
  <a href="#-technologies--tools">Tech Stack</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-author">Author</a>
</p>

---

</div>

## 📌 Overview

This repository serves as a centralized and structured archive of academic practicals, algorithm implementations, and hands-on projects developed throughout the **B.Tech Computer Science Engineering** curriculum. It covers fundamental and advanced topics across **Design & Analysis of Algorithms**, **Machine Learning**, and **Artificial Intelligence**.

---

## 📚 Subjects Covered

### ⚡ 1. Design & Analysis of Algorithms (DAA)

Implementations of classical algorithms with time complexity analysis and empirical benchmarking.

| Practical | Topic / Algorithm | Implementation Type | Key Concepts |
| :---: | :--- | :--- | :--- |
| **01** | **Sorting Algorithms Suite** | `.ipynb` / `.py` | Bubble, Selection, Insertion, Quick & Merge Sort (Time & Space Complexity) |
| **02** | **Searching Algorithms** | `.py` | Linear Search & Binary Search performance comparison |
| **03** | **Heap Sort** | `.py` | Max-Heap creation, heapify operations, $O(n \log n)$ complexity |
| **04** | **Factorial Analysis** | `.py` | Iterative vs. Recursive approaches & recursion overhead |
| **05** | **Making Change Problem** | `.py` | Dynamic Programming approach to coin change |
| **06** | **Matrix Chain Multiplication** | `.py` | Optimal parenthesization using dynamic programming |
| **07** | **Making Change (Optimized)** | `.py` | Optimal sub-structure and tabulation analysis |
| **08** | **Graph Traversals** | `.py` | Breadth-First Search (BFS) & Depth-First Search (DFS) |

---

### 🤖 2. Machine Learning (ML)

Practical exploratory data analysis, object-oriented implementations, and unsupervised machine learning projects.

- 📊 **Exploratory Data Analysis & Manipulation:** Data wrangling with `NumPy` & `Pandas`.
- 📈 **Data Visualization:** Statistical plotting and trend discovery using `Matplotlib`.
- 🧬 **Object-Oriented Programming:** Modular Python class & object design for data workflows.
- 🚗 **Featured Project — Automobile Market Segmentation:** Customer segmentation using clustering algorithms (K-Means / Unsupervised Learning) on vehicle datasets.

---

### 🧠 3. Artificial Intelligence (AI)

Intelligent agent design, search algorithms, game-theoretic adversarial search, and expert systems.

- 🎯 **Reflex & Goal-Based Agents:** Python environment setup and implementation of autonomous agents in toy environments.
- 🗺️ **Grid World Search & Navigation:** Pathfinding and spatial decision-making on discrete grids.
- ♟️ **Adversarial Search (Game Playing):** Minimax algorithm with $\alpha$-$\beta$ pruning for turn-based games (e.g., Tic-Tac-Toe).
- 💡 **Rule-Based Expert System:** Knowledge base representation with forward/backward inference logic.

---

## 📂 Repository Structure

```plaintext
college-practical-codes/
│
├── 🧠 AI LAB/
│   ├── AI_PRACTICAL 01 & 02.ipynb      # Reflex & Goal-based agent in toy environment
│   ├── AI_PRACTICAL_03.ipynb           # Grid world navigation & agent exploration
│   ├── AI_PRACTICAL_04.ipynb           # Minimax with Alpha-Beta pruning (Game Agent)
│   └── AI_PRACTICAL_05.ipynb           # Rule-based expert system
│
├── ⚡ DAA/
│   ├── DAA_PRACTICAL_01.ipynb          # Sorting algorithms comparison & analysis
│   ├── DAA_PRACTICAL_02.py             # Linear vs Binary Search
│   ├── DAA_PRACTICAL_03.py             # Heap Sort implementation
│   ├── DAA_PRACTICAL_04.py             # Iterative vs Recursive Factorial
│   ├── DAA_PRACTICAL_05.py             # Making Change (Dynamic Programming)
│   ├── DAA_PRACTICAL_06.py             # Matrix Chain Multiplication (DP)
│   ├── DAA_PRACTICAL_07.py             # Making Change Problem (Analysis)
│   ├── DAA_PRACTICAL_08.py             # Graph Traversals (BFS & DFS)
│   └── Practical 01-08 Read.me         # Detailed aims, complexity & sample outputs
│
├── 🤖 Machine Learning/
│   ├── MACHINE_LEARNING_ESSENTIALS (1).ipynb  # Pandas, Matplotlib & Preprocessing
│   ├── MLE_PROJECT.ipynb                      # Automobile Market Segmentation (Clustering)
│   ├── Python_class_and_object.ipynb          # Python OOP foundations
│   └── machine_learning_essentials (1).py     # Core script exports
│
├── 📄 College Practical Codes.pdf      # Complete academic laboratory documentation
└── 📖 README.md                        # Repository documentation & guide
```

---

## 🛠️ Technologies & Tools

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
</p>

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/mahendrapratap23/college-practical-codes.git
cd college-practical-codes
```

### 2. Set Up a Virtual Environment (Optional)

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn notebook
```

### 4. Running the Codes

- **To run Python scripts (e.g., DAA practicals):**
  ```bash
  python "DAA/DAA_PRACTICAL_02.py"
  ```

- **To launch Jupyter Notebooks (AI and ML experiments):**
  ```bash
  jupyter notebook
  ```

---

## 🎯 Purpose & Goals

- 💡 **Deep Conceptual Understanding:** Hands-on realization of abstract data structures, algorithms, and AI/ML theories.
- 🧹 **Clean & Readable Code:** Well-documented solutions following clean coding practices.
- 📦 **Academic Record:** Comprehensive single-source repository for college lab submissions and viva/exam preparation.

---

## 👨‍💻 Author

<div align="left">

**Mahendra Pratap**  
🎓 B.Tech Computer Science Engineering  
🔗 GitHub: [@mahendrapratap23](https://github.com/mahendrapratap23)

</div>

---

<div align="center">

⭐ **If you find this repository helpful for your coursework or revision, consider giving it a star!**

</div>
