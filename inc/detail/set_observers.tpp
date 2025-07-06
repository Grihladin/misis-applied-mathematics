#ifndef SET_OBSERVERS_TPP
#define SET_OBSERVERS_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::allocator_type
set<Key, Compare, Allocator>::get_allocator() const noexcept {
  return m_allocator;
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::size_type
set<Key, Compare, Allocator>::size() const {
  return m_size;
}

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::empty() const {
  return size() == 0;
}

} // namespace custom

#endif // SET_OBSERVERS_TPP
