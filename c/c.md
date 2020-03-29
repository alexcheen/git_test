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

常见的调用约定有：
  *  stdcall
  * cdecl
  * fastcall
  * thiscall
  * naked call

_CDEDL调用约定：
1.  参数从右到左依次入栈
2.  调用者负责清理堆栈
3.  参数的数量类型不会导致编译阶段的错误

stdcall很多时候被称为pascal调用约定，因为pascal是早期很常见的一种教学用计算机程序设计语言，其语法严谨，使用的函数调用约定就是stdcall。在Microsoft C++系列的C/C++编译器中，常常用PASCAL宏来声明这个调用约定，类似的宏还有WINAPI和CALLBACK。

    stdcall调用约定声明的语法为(以前文的那个函数为例）：

    int __stdcall function(int a,int b)

    stdcall的调用约定意味着：1）参数从右向左压入堆栈，2）函数自身修改堆栈 3)函数名自动加前导的下划线，后面紧跟一个@符号，其后紧跟着参数的尺寸

