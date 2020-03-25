## 处理与平台相关的代码
```cpp
std::string say_hello()
{
#ifdef IS_WINDOWS
    return std::string("Hello from Windows!");
#elif IS_LINUX
    return std::string("Hello from Linux!");
#else
    return std::string("hello from unknown system!");
}
```
```cmake
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    target_compile_definitions(hello_world PUBLIC "IS_LINUX")
endif()
if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    target_compile_definitions(hello_world PUBLIC "IS_WINDOWS")
endif()
```
注意这里的 **[PRIVATE|PUBLIC|INTERFACE]** 限定符
 * PRIVATE，编译定义只限定于给定的目标，而不应用于相关的其它目标。
 * INTERFACE， 对给定目标的编译定义只应用于使用它的目标。
 * PUBLIC， 编译定义应用于给定的目标和使用它的所有目标。
  
## 处理于编译器相关的代码
```cmake
if(CMAKE_CXX_COMPILER_ID MATCHES Intel)
  target_compile_definitions(hello-world PUBLIC "IS_INTEL_CXX_COMPILER")
endif()
```
## 检测处理器体系结构
CMake定义了CMAKE_HOST_SYSTEM_PROCESSOR变量，以包含当前运行的处理器的名称。可以设置为“i386”、“i686”、“x86_64”、“AMD64”等等，当然，这取决于当前的CPU。CMAKE_SIZEOF_VOID_P为void指针的大小。
> **NOTE:使用CMAKE_SIZEOF_VOID_P是检查当前CPU是否具有32位或64位架构的唯一“真正”可移植的方法。**
```cmake
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
  target_compile_definitions(arch-dependent PUBLIC "IS_64_BIT_ARCH")
else()
  target_compile_definitions(arch-dependent PUBLIC "IS_32_BIT_ARCH")
endif()
target_compile_definitions(arch-dependent
  PUBLIC "ARCHITECTURE=${CMAKE_HOST_SYSTEM_PROCESSOR}"
  )
```
```cpp
#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

std::string say_hello()
{
  std::string arch_info(TOSTRING(ARCHITECTURE));
  arch_info += std::string(" architecture. ");
#ifdef IS_32_BIT_ARCH
  return arch_info + std::string("Compiled on a 32 bit host processor.");
#elif IS_64_BIT_ARCH
  return arch_info + std::string("Compiled on a 64 bit host processor.");
#else
  return arch_info + std::string("Neither 32 nor 64 bit, puzzling ...");
#endif
}
```

## 检测处理器指令集
```cpp
#include "config.h"

#include <cstdlib>
#include <iostream>

int main()
{
  std::cout << "Number of logical cores: "
            << NUMBER_OF_LOGICAL_CORES << std::endl;
  std::cout << "Number of physical cores: "
            << NUMBER_OF_PHYSICAL_CORES << std::endl;
  std::cout << "Total virtual memory in megabytes: "
            << TOTAL_VIRTUAL_MEMORY << std::endl;
  std::cout << "Available virtual memory in megabytes: "
            << AVAILABLE_VIRTUAL_MEMORY << std::endl;
  std::cout << "Total physical memory in megabytes: "
            << TOTAL_PHYSICAL_MEMORY << std::endl;
  std::cout << "Available physical memory in megabytes: "
            << AVAILABLE_PHYSICAL_MEMORY << std::endl;
  std::cout << "Processor is 64Bit: "
            << IS_64BIT << std::endl;
  std::cout << "Processor has floating point unit: "
            << HAS_FPU << std::endl;
  std::cout << "Processor supports MMX instructions: "
            << HAS_MMX << std::endl;
  std::cout << "Processor supports Ext. MMX instructions: "
            << HAS_MMX_PLUS << std::endl;
  std::cout << "Processor supports SSE instructions: "
            << HAS_SSE << std::endl;
  std::cout << "Processor supports SSE2 instructions: "
            << HAS_SSE2 << std::endl;
  std::cout << "Processor supports SSE FP instructions: "
            << HAS_SSE_FP << std::endl;
  std::cout << "Processor supports SSE MMX instructions: "
            << HAS_SSE_MMX << std::endl;
  std::cout << "Processor supports 3DNow instructions: "
            << HAS_AMD_3DNOW << std::endl;
  std::cout << "Processor supports 3DNow+ instructions: "
            << HAS_AMD_3DNOW_PLUS << std::endl;
  std::cout << "IA64 processor emulating x86 : "
            << HAS_IA64 << std::endl;
  std::cout << "OS name: "
            << OS_NAME << std::endl;
  std::cout << "OS sub-type: "
            << OS_RELEASE << std::endl;
  std::cout << "OS build ID: "
            << OS_VERSION << std::endl;
  std::cout << "OS platform: "
            << OS_PLATFORM << std::endl;
  return EXIT_SUCCESS;
}
```

```cpp
// config.h
#pragma once

#define NUMBER_OF_LOGICAL_CORES @_NUMBER_OF_LOGICAL_CORES@
#define NUMBER_OF_PHYSICAL_CORES @_NUMBER_OF_PHYSICAL_CORES@
#define TOTAL_VIRTUAL_MEMORY @_TOTAL_VIRTUAL_MEMORY@
#define AVAILABLE_VIRTUAL_MEMORY @_AVAILABLE_VIRTUAL_MEMORY@
#define TOTAL_PHYSICAL_MEMORY @_TOTAL_PHYSICAL_MEMORY@
#define AVAILABLE_PHYSICAL_MEMORY @_AVAILABLE_PHYSICAL_MEMORY@
#define IS_64BIT @_IS_64BIT@
#define HAS_FPU @_HAS_FPU@
#define HAS_MMX @_HAS_MMX@
#define HAS_MMX_PLUS @_HAS_MMX_PLUS@
#define HAS_SSE @_HAS_SSE@
#define HAS_SSE2 @_HAS_SSE2@
#define HAS_SSE_FP @_HAS_SSE_FP@
#define HAS_SSE_MMX @_HAS_SSE_MMX@
#define HAS_AMD_3DNOW @_HAS_AMD_3DNOW@
#define HAS_AMD_3DNOW_PLUS @_HAS_AMD_3DNOW_PLUS@
#define HAS_IA64 @_HAS_IA64@
#define OS_NAME "@_OS_NAME@"
#define OS_RELEASE "@_OS_RELEASE@"
#define OS_VERSION "@_OS_VERSION@"
#define OS_PLATFORM "@_OS_PLATFORM@"
```

```cmake
# 查询主机系统信息获取后存入对应的变量中 -${key}
foreach(key
  IN ITEMS
    NUMBER_OF_LOGICAL_CORES
    NUMBER_OF_PHYSICAL_CORES
    TOTAL_VIRTUAL_MEMORY
    AVAILABLE_VIRTUAL_MEMORY
    TOTAL_PHYSICAL_MEMORY
    AVAILABLE_PHYSICAL_MEMORY
    IS_64BIT
    HAS_FPU
    HAS_MMX
    HAS_MMX_PLUS
    HAS_SSE
    HAS_SSE2
    HAS_SSE_FP
    HAS_SSE_MMX
    HAS_AMD_3DNOW
    HAS_AMD_3DNOW_PLUS
    HAS_IA64
    OS_NAME
    OS_RELEASE
    OS_VERSION
    OS_PLATFORM
  )
  cmake_host_system_information(RESULT _${key} QUERY ${key})
endforeach()
configure_file(config.h.in config.h @ONLY)
```
