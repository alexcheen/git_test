## 可变参数va_list

```c

 ///stdarg.h  compilor: vs2008
#define va_start _crt_va_start
#define va_arg _crt_va_arg
#define va_end _crt_va_end
  
///vadefs.h
#define _ADDRESSOF(v)   ( &reinterpret_cast<const char &>(v) )
typedef char *  va_list;
#define _INTSIZEOF(n)   ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )
#define _crt_va_start(ap,v)  ( ap = (va_list)_ADDRESSOF(v) + _INTSIZEOF(v) )
#define _crt_va_arg(ap,t)    ( *(t *)((ap += _INTSIZEOF(t)) - _INTSIZEOF(t)) )
#define _crt_va_end(ap)      ( ap = (va_list)0 )
```

_CDEDL调用约定：
1.  参数从右到左依次入栈
2.  调用者负责清理堆栈
3.  参数的数量类型不会导致编译阶段的错误

