#include "set.hpp"
#include <iostream>

int main() {
  custom::set<int> the_set;

  std::cout << "🚀 Red-Black Tree Demo" << std::endl;
  std::cout << "======================" << std::endl;

  std::cout << "\n📥 Inserting values: 30, 20, 10, 40, 50, 6, 7, 8"
            << std::endl;
  the_set.insert(30);
  the_set.insert(20);
  the_set.insert(10);
  the_set.insert(40);
  the_set.insert(50);
  the_set.insert(6);
  the_set.insert(7);
  the_set.insert(8);

  the_set.print_terminal();

  std::cout << "🗑️  Erasing values: 7, 6, 30" << std::endl;
  the_set.erase(7);
  the_set.erase(6);
  the_set.erase(30);

  the_set.print_terminal();

  std::cout << "📥 Inserting values: 100, 33, 47, 7" << std::endl;
  the_set.insert(100);
  the_set.insert(33);
  the_set.insert(47);
  the_set.insert(7);

  the_set.print_terminal();

  std::cout << "🗑️  Erasing values: 50, 100" << std::endl;
  the_set.erase(50);
  the_set.erase(100);

  the_set.print_terminal();

  std::cout << "📥 Inserting values: 50, 100" << std::endl;
  the_set.insert(50);
  the_set.insert(100);

  the_set.print_terminal();

  std::cout << "🗑️  Erasing values: 47, 50" << std::endl;
  the_set.erase(47);
  the_set.erase(50);

  std::cout << "\n🎯 Final tree structure:" << std::endl;
  the_set.print_terminal();

  return 0;
}
