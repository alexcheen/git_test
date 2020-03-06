

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