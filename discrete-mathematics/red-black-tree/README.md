# Red-Black Tree

A self-balancing tree implementation created for a Discrete Mathematics course
at MISIS in 2022 and later reorganized into a clearer C++ project.

## What was implemented

- template-based storage for comparable types;
- insertion, deletion, lookup, and balancing;
- an interface inspired by `std::set`;
- terminal visualization of the tree structure;
- a demonstration program covering several insert and erase sequences.

The implementation maintains the standard red-black tree properties:

1. Every node is red or black.
2. The root is black.
3. A red node cannot have a red child.
4. Every path from a node to a leaf contains the same number of black nodes.

These constraints keep insertion, deletion, and lookup at `O(log n)`.

## Technologies

- C++17
- Template-based headers
- Make

## Running the project

```bash
cd red-black-tree
make run
```

From the consolidated repository root, use:

```bash
cd discrete-mathematics/red-black-tree
make run
```

Use `make fclean` to remove the executable and object files.

## Structure

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

## Known limitations

- This is an educational implementation and has no automated test suite.
- The API covers the operations needed by the demonstration rather than the
  complete `std::set` interface.
- Terminal output includes Unicode symbols and assumes a compatible terminal.

## Historical note

The original implementation was written by hand before generative AI coding
assistants became widely available. Its later cleanup retained the underlying
student implementation.
