# Discrete Mathematics Coursework (MISIS)
## Red-Black Tree Implementation

A self-balancing Red-Black tree implementation in C++ with modular design and terminal visualization.

## Features

- **Self-balancing Red-Black Tree**: Maintains O(log n) operations
- **Modular Design**: Split into logical components for maintainability
- **Terminal Visualization**: Beautiful tree display in console
- **STL-style Interface**: Similar to `std::set`
- **Template-based**: Works with any comparable type

## Implementation Details

The red-black tree maintains these properties:
1. Every node is either red or black
2. The root is always black
3. Red nodes cannot have red children
4. Every path from root to leaf contains the same number of black nodes

This ensures O(log n) time complexity for insertions, deletions, and searches.

## Getting Started

### Prerequisites
- C++17 compatible compiler (g++, clang++)
- Make build system

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Grihladin/red-black-tree.git

# Navigate to project directory
cd red-black-tree

# Build and run the demo
make run
```

## Project Structure

```
red-black-tree/
├── inc/                           # Headers
│   ├── set.hpp                    # Main set class interface and declarations
│   ├── set_node.hpp               # Node class with color and tree operations
│   ├── utils.hpp                  # Memory utilities and type helpers
│   └── detail/                    # Template implementations (internal)
│       ├── set.tpp                # Master include for all implementations
│       ├── set_constructors.tpp   # Constructor implementations
│       ├── set_modifiers.tpp      # Insert and erase operations
│       ├── set_observers.tpp      # Size, empty, and accessor methods
│       ├── set_debug.tpp          # Tree visualization and debug output
│       ├── set_helpers.tpp        # Helper methods (uncle, is_root, etc.)
│       ├── set_balance.tpp        # Red-black tree balancing algorithms
│       └── set_operations.tpp     # Core tree operations (find, insert)
├── src/
│   └── main.cpp                   # Demo program with tree operations
└── Makefile                       # Build system with targets (all, run, clean, fclean)
```
