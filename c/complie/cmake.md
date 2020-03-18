## Concepts
CMakeList.txt，默认执行该目录下的此文件，如果没有则报错。

### Minimum CMake version
最低CMake版本
```cmake
cmake_minimum_required(VERSION 3.5)
```
### Projects
```cmake
project (hello_cmake)
```
该命令会创建一个变量${PROJECT_NAME} 值为hello_cmake。

### Creating an Executable
```cmake
add_executable(hello_cmake main.cpp)
add_executable(${PROJECT_NAME} main.cpp)
```
上面两条命令等价。

## Building
```shell
cmake
make
```
### Directory Paths

|Variable	|Info|
|-|-|
|CMAKE_SOURCE_DIR |The root source directory|
|CMAKE_CURRENT_SOURCE_DIR |The current source directory if using sub-projects and directories.|
|PROJECT_SOURCE_DIR |The source directory of the current cmake project.|
|CMAKE_BINARY_DIR |The root binary / build directory. This is the directory where you ran the cmake command.|
|CMAKE_CURRENT_BINARY_DIR |The build directory you are currently in.|
|PROJECT_BINARY_DIR |The build directory for the current project.|

这里cmake系统会同时预定义PROJECT_BINARY_DIR和PROJECT_SOURCE_DIR变量，其值分别与<project_name>_BINARY_DIR和<project_name>_SOURCE_DIR变量一致。
```cmake
set(SOURCES
    src/Hello.cpp
    src/main.cpp
    )
add_executable(${PROJECT_NAME} ${SOURCES})
```
or an alternative method
```cmake
file(GLOB SOURCES "src/*.cpp")
```

### Including Directories

```cmake
target_include_directories(target
    PRIVATE
        ${PROJECT_SOURCE_DIR}/include
)
```
### Building the Example
```
make
or
make VERBOSE=1
```

### Adding a Static Library
```cmake
add_library(hello_library STATIC
    src/Hello.cpp
)
```
This will be used to create a static library with the name libhello_library.a with the sources in the add_library call.

### Populating Including Directories
```cmake
target_include_directories(hello_library
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)
```
### Linking a Library
```cmake
add_executable(hello_library
    src/main.cpp
)
```
target_link_libraries(hello_binary)



### import targets

```cmake
project(imported_targets)

find_package(Boost 1.46.1 REQUIRED COMPONENTS filesystem system)

# check if boost was found
if(Boost_FOUND
    message("boost found")
else()
    message(FATAL_ERROR "Cannot find Boost")
endif()

add_executable(imported_targets main.cpp)

target_link_libraries(imported_targets
    PRIVATE
        Boost::filesystem
)
```

### cpp standard
CHECK_CXX_COMPILER_FLAG(<flag> <var>)
<flag> the compiler flag
<var> variable to store the result

include(<file|module> [OPTIONAL] [RESULT_VARIABLE <VAR>]
                     [NO_POLICY_SCOPE])
```cmake
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0x)

if(COMPILER_SUPPORTS_CXX11)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0x)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
else()
    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

add_executable(hello_cpp11 main.cpp)
```
The line include(CheckCXXCompilerFlag) tells CMake to include this function to make it available for use.

```cmake
project(hello_cpp11)

set(CMAKE_CXX_STANDARD 11)

add_executable(hello_cpp11 main.cpp)
```

```cmake
cmake_minimum_required(VERSION 3.1)
project (hello_cpp11)
add_executable(hello_cpp11 main.cpp)
target_compile_features(hello_cpp11 PUBLIC cxx_auto_type)
message("list of compile features: ${CMAKE_CXX_COMPILE_FEATURES}")
```
### sublibrary
```shell
$ tree
.
├── CMakeLists.txt
├── subbinary
│   ├── CMakeLists.txt
│   └── main.cpp
├── sublibrary1
│   ├── CMakeLists.txt
│   ├── include
│   │   └── sublib1
│   │       └── sublib1.h
│   └── src
│       └── sublib1.cpp
└── sublibrary2
    ├── CMakeLists.txt
    └── include
        └── sublib2
            └── sublib2.h
```

```cmake
# Top level CMakeLists.txt
cmake_minimum_required(VERSION 3.5)

project(subprojects)

add_subdirectory(sublibrary1)
add_subdirectory(sublibrary2)
add_subdirectory(sublibrary)

# make executable
project(sublibrary)
add_executable(${PROJECET_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME}
    sub::lib1
    sub::lib2
)

# make a static library
project(sublibrary1)
add_library(${PROJECT_NAME} src/sublib1.cpp)
add_library(sub::lib1 ALIAS ${PROJECT_NAME})

target_include_directories(${PROJCET_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/include
)

# setup header only library
project(sublibrary2)
add_library(${PROJECT_NAME} INTERFACE)
add_library(sub::lib2 ALIAS ${PROJECT_NAME})
target_include_directories(${PROJECT_NAME}
    INTERFACE
        ${PROJECT_SOURCE_DIR}/include
)
```

### static library and shared library
目录树：
```shell
├── CMakeLists.txt
└── lib
    ├── CMakeLists.txt
    ├── hello.c
    └── hello.h
```
```cmake
# CMakeLists.txt
project(hellolib)
add_sublibrary(lib)
```
```cmake
# lib/CMakeLists.txt
set(HELLO_SRC hello.c)
add_library(hello SHARED ${HELLO_SRC})
set_target_properties(hello PROPERTIES VERSION 1.2 SOVERSION 1)
#error :duplicate name
#add_library(hello STATIC ${HELLO_SRC})
add_library(hello_static STATIC ${HELLO_SRC})
set_target_properties(hello_static PROPERTIES CLEAN_DIRECT_OUTPUT 1 OUTPUT_NAME "hello")

install(TARGETS hello hello_static
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
install(FILES hello.h DESTINATION include/hello)
```
对于测试工程：
```cmake
project(demo)
add_executable(demo main.c)
# eq: -L/usr/include/hello
INCLUDE_DIRECTORIES(/usr/include/hello)
# eq: -lhello
TARGET_LINK_LIBRARIES(demo hello)
```
### FIND INSTRUCTION 
```cmake
FIND_FILE(<VAR> name1 path1 path2 ...)

FIND_LIBRARY(<VAR> name1 path1 path2 ...)

FIND_PATH(<VAR> name1 path1 path2 ...)

FIND_PROGRAM(<VAR> name1 path1 path2 ...)

FIND_PACKAGE(<name> [major.minor] [QUIET] [NO_MODULE] [[REQUIRED|COMPONENTS] [componets...]])
```

```cmake
#find_library demo
FIND_LIBRARY(libX X11 /usr/lib)
IF(NOT libX)
MESSAGE(FATAL_ERROR "libX not found")
ENDIF(NOT libX)

#if SET(CMAKE_ALLOW_LOOSE_LOOP_CONSTGRUCTS ON)
IF(WIN32)
ELSE()
ENDIF()
```
CMake接受其他值作为add_library的第二个参数的有效值:
 * STATIC：用于创建静态库，即编译文件的打包存档，以便在链接其他目标时使用，例如：可执行文件。

 * SHARED：用于创建动态库，即可以动态链接，并在运行时加载的库。可以在CMakeLists.txt中使用`add_library(message SHARED Message.hpp Message.cpp) `从静态库切换到动态共享对象(DSO)。

 * OBJECT：可将给定add_library的列表中的源码编译到目标文件，不将它们归档到静态库中，也不能将它们链接到共享对象中。如果需要一次性创建静态库和动态库，那么使用对象库尤其有用。我们将在本示例中演示。

 * MODULE：又为DSO组。与SHARED库不同，它们不链接到项目中的任何目标，不过可以进行动态加载。该参数可以用于构建运行时插件。

需要保证编译的目标文件与生成位置无关。可以通过使用set_target_properties命令，设置message-objs目标的相应属性来实现。
```cmake
set_target_properties(message-objs
    PROPERTIES
        POSITION_INDEPENDENT_CODE 1
    )
​
add_library(message-shared
    SHARED
        $<TARGET_OBJECTS:message-objs>
    )
​
add_library(message-static
    STATIC
        $<TARGET_OBJECTS:message-objs>
    )
```
生成同名的静态库与动态库
```cmake
add_library(message-shared
  SHARED
    $<TARGET_OBJECTS:message-objs>
    )
​
set_target_properties(message-shared
    PROPERTIES
        OUTPUT_NAME "message"
    )
​
add_library(message-static
    STATIC
        $<TARGET_OBJECTS:message-objs>
    )
​
set_target_properties(message-static
    PROPERTIES
        OUTPUT_NAME "message"
    )
```

## 条件编译
```cmake
# set minimum cmake version
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# project name and language
project(recipe-04 LANGUAGES CXX)

# introduce a toggle for using a library
set(USE_LIBRARY OFF)

message(STATUS "Compile sources into a library? ${USE_LIBRARY}")

# BUILD_SHARED_LIBS is a global flag offered by CMake
# to toggle the behavior of add_library
set(BUILD_SHARED_LIBS OFF)

# list sources
list(APPEND _sources Message.hpp Message.cpp)

if(USE_LIBRARY)
  # add_library will create a static library
  # since BUILD_SHARED_LIBS is OFF
  add_library(message ${_sources})

  add_executable(hello-world hello-world.cpp)

  target_link_libraries(hello-world message)
else()
  add_executable(hello-world hello-world.cpp ${_sources})
endif()
```
以上方式不允许用户改变设置。
```cmake
# set(USE_LIBRARY OFF)
option(USE_LIBRARY "Compile sources into a library" OFF)
```
```shell
cmake -D USE_LIBRARY=ON ..
```
## 指定编译器

## 切换构建类型
cmake可以配置构建类型，CMAKE_BUILD_TYPE:
  * Debug: 用于在没有优化的情况下，使用带有调试符构建库或可执行文件。
  * Release: 构建优化的库或可执行文件，不包含调试符号。
  * RelWithDebInfo: 构建较少的优化库或可执行文件，并包含调试符号。
  * MinSizeRel： 用于不增加目标代码大小的优化方式，来构建库或可执行文件。
  
```cmake
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(recipe07 LANGUAGES C CXX)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Realse CACHE STRING "Build type" FORCE)
endif()
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
```
```shell
# build type in default Release
mkdir -p build
cd build
cmake ..

# build type in debug mode
cmake -D CMAKE_BUILD_TYPE=Debug ..
```
当评估编译器优化级别的效果时，Release和Debug配置中构建项目非常有用。
Cmake也支持符合配置生成器。
```shell
mkdir -p build
cd build
cmake .. -G"Visual Studio 12 2017 Win64" -D CMAKE_CONFIGURATION_TYPE="Release;Debug"
```
构建时来决定构建其中哪一个：
```shell
cmake --build . --config Release
```
## 设置编译器选项

```cmake 
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(recipe-08 LANGUAGES CXX)
message("C++ compiler flags: ${CMAKE_CXX_FLAGS}")
list(APPEND flags "-fPIC" "-Wall")
if(NOT WIN32)
  list(APPEND flags "-Wextra" "-Wpedantic")
endif()
add_library(geometry
  STATIC
    geometry_circle.cpp
    geometry_circle.hpp
    geometry_polygon.cpp
    geometry_polygon.hpp
    geometry_rhombus.cpp
    geometry_rhombus.hpp
    geometry_square.cpp
    geometry_square.hpp
  )
target_compile_options(geometry
  PRIVATE
    ${flags}
)
add_executable(compute-areas compute-areas.cpp)
target_compile_options(compute-areas
  PRIVATE
    "-fPIC"
)
target_link_libraries(compute-areas geometry)
```

编译选项
 * -Wall 选项意思是编译后显示所有警告。
 * -fPIC 产生与位置无关代码(Position-Independent Code)
 * -Wextra 打印一些额外的警告信息
 * -Wpedantic 允许发出ANSI C标准所列的全部警告信息
 * -fno-rtti 禁用RTTI
 * -fno-exception 禁用异常
 * -Wsuggest-final-types (GNU)
 * -Wsuggest-final-methods (GNU)
 * -Wsuggest-override (GNU)
 * -03 优化级别
 * -Wno-unused 禁用未使用警告

控制编译器标志的第二种方法：
```shell
cmake -D CMAKE_CXX_FLAGS="-fno-exceptions -fno-rtti" ..
```

```camke
set(COMPILER_FLAGS)
set(COMPILER_FLAGS_DEBUG)
set(COMPILER_FLAGS_RELEASE)

if(CMAKE_CXX_COMPILER_ID MATCHES GNU)
  list(APPEND CXX_FLAGS "-fno-rtti" "-fno-exceptions")
  list(APPEND CXX_FLAGS_DEBUG "-Wsuggest-final-types" "-Wsuggest-final-methods" "-Wsuggest-override")
  list(APPEND CXX_FLAGS_RELEASE "-O3" "-Wno-unused")
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES Clang)
  list(APPEND CXX_FLAGS "-fno-rtti" "-fno-exceptions" "-Qunused-arguments" "-fcolor-diagnostics")
  list(APPEND CXX_FLAGS_DEBUG "-Wdocumentation")
  list(APPEND CXX_FLAGS_RELEASE "-O3" "-Wno-unused")
endif()

#使用生成器表达式来设置编译器标志的基础上，为每个配置和每个目标生成构建系统
target_compile_option(compute-areas
  PRIVATE
    ${CXX_FLAGS}
    "$<$<CONFIG:Debug>:${CXX_FLAGS_DEBUG}>"
    "$<$<CONFIG:Release>:${CXX_FLAGS_RELEASE}>"
  )
```