#ifndef UTILS_H
#define UTILS_H

#include <memory>

namespace std {
template <class T, class... Args>
static constexpr T *construct_at(T *p, Args &&...args) {
  return reinterpret_cast<T *>(new (static_cast<void *>(p))
                                   T(std::forward<Args>(args)...));
}
} // namespace std

namespace custom {

template <class _Alloc, class S> struct __rebind_alloc_helper;

template <template <class, class...> class _Alloc, class New, class Old,
          class... OtherArgs>
struct __rebind_alloc_helper<_Alloc<Old, OtherArgs...>, New> {
  typedef
      typename std::allocator_traits<_Alloc<New, OtherArgs...>>::allocator_type
          type;
};

} // namespace custom

#endif // UTILS_H
