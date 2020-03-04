

## Concepts
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

