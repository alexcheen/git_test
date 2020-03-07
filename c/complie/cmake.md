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

