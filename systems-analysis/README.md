# Systems Analysis

Six Python exercises completed for the Systems Analysis course at MISIS in
2023.

## What was implemented

1. Reading tabular data and representing hierarchies as trees.
2. Tree traversal, search, serialization, and display.
3. Management-relationship matrices and structural entropy.
4. Probability distributions and information measures for dice sums and
   products.
5. Ranking comparison and contradictory preference detection.
6. Agreement estimation for expert rankings using a Kendall-style coefficient.

## Technologies

- Python
- NumPy
- Tabulate for optional terminal tables
- JSON and CSV data

## Running the exercises

```bash
pip install numpy tabulate
python task3/task.py
python task4/task.py
python task5/task.py
python task6/task.py
```

Tasks 1 and 2 contain tree examples and sample input files:

```bash
python task1/task1.py
python task2/task.py
```

## Known limitations

- The exercises use hard-coded demonstration inputs rather than a consistent
  command-line interface.
- Task 5 contains placeholder ranking-compilation logic and should not be
  treated as a complete algorithm.
- The Kendall-style calculation in Task 6 is an educational implementation and
  should be independently verified before analytical use.
- There is no shared package structure or automated test suite.

## Historical note

The exercises were written by hand before generative AI coding assistants
became widely available. They are preserved as educational work rather than a
maintained analysis library.
