# Red-Black Tree Makefile
# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Werror -Wextra -O2 -g -Iinc
LDFLAGS = 

# Directories
SRCDIR = src
INCDIR = inc
OBJDIR = obj

# Target executable (in root directory)
TARGET = red_black_tree

# Source files
SOURCES = main.cpp
OBJECTS = $(SOURCES:%.cpp=$(OBJDIR)/%.o)

# Header files (for dependency tracking)
HEADERS = $(INCDIR)/set.hpp $(INCDIR)/detail/set.tpp $(INCDIR)/set_node.hpp $(INCDIR)/utils.hpp

# Default target
all: $(TARGET)

# Create necessary directories
$(OBJDIR):
	mkdir -p $(OBJDIR)

# Build the target executable
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $@ $(LDFLAGS)

# Build object files
$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(HEADERS) | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Run the program and display tree in terminal
run: $(TARGET)
	@echo "Running Red-Black Tree program..."
	./$(TARGET)

# Clean object files
clean:
	rm -rf $(OBJDIR)

# Clean everything (objects and executable)
fclean: clean
	rm -f $(TARGET)

# Rebuild everything
re: fclean all

# Phony targets
.PHONY: all run clean fclean re
