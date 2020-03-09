# cmake find_package concept

当编译工程需要一个第三方库的时候需要知道库文件，头文件的信息。
例如需要第三方库curl, CMakeLists.txt需要指定头文件目录和库文件。
```cmake
include_directories(/usr/include/cur)
target_link_libraries(my_project path/curl.so)
```
借助cmake提供的finder，即查找cmake目录下的FindCURL.cmake,相应的CMakeLists.txt如下
```cmake
find_package(CURL REQUIRED)
include_directories(${CURL_INCLUDE_DIR})
target_link_libraries(my_project ${CURL_LIBRARY})
```
## cmake 查找方式
find_package()命令首先会在模块路径中寻找Find.cmake，这是查找库的一个典型方式。具体查找路径依次为${CMAKE_MODULE_PATH}中的所有目录。如果没有，然后在查看它自己的模块目录/share/cmake-x.y/Modules/${CMAKE_ROOT}。
```cmake
#cmake demo
find_path(CURL_INCLUDE_DIR NAMES curl/curl.h)
mark_as_advanced(CURL_INCLUDE_DIR)
find_library(CURL_LIBRARY NAMES
            curl
            curlib
            libcurl_imp
            curllib_static
            libcurl)
```
```cmake
project(helloworld)
add_executable(helloworld hello.c)
find_package(BZip2)
if(BZIP2_FOUND)
    include_directories(${BZIP_INCLUDE_DIRS})
    target_link_libraries(helloworld ${BZIP2_LIBRARIES})
endif(BZIP2_FOUND)
```
## 自定义cmake module
```shell
.
├── cmake
│   └── FindDEMOLIB.cmake
├──CMakeLists.txt
├──demo.cpp
├──demo.h
└── demo_main.cpp
```
```cmake
# FindDEMOLIB.cmake
message("using cmake to find demo.lib")
FIND_PATH(DEMOLIB_INCLUDE_DIR demo.h /usr/include/demo/
        /usr/local/demo/include/)
message("./h dir ${DEMOLIB_INCLUDE_DIR}")
FIND_LIBRARY(DEMOLIB_LIBRARY libdemo_lib.a /usr/local/demo/lib/)
message("lib dir: ${DEMOLIB_LIBRARY}")

if(demoLIB_INCLUDE_DIR AND DEMOLIB_LIBRARY)
    # 设置变量结果
    set(DEMOLIB_FOUND TRUE)
endif(DEMOLIB_INCLUDE_DIR AND DEMOLIB_LIBRARY)
```
```cmake
#main cmakelists.txt
cmake_minimum_required(VERSION 3.5)

project(demo)

# create libdemo_lib.a
set(SRC_LIB demo.cpp)
add_library(demo_lib STATIC ${SRC_LIB})

# install it
install(TARGETS demo_lib DESTINATION demo/lib)
install(FILES demo.h DESTINATION demo/include)

# create demo_main exectuable
set(SRC_EXE demo_main.cpp)

# set demo_lib cmake module path
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
message("cmake_module_path: ${CMAKE_MODULE_PATH}")
find_package(demoLIB)

if(demoLIB_FOUND)
    add_executable(demo_main ${SRC_EXE})
    message("found demo ${demoLIB_INCLUDE_DIR} ${demoLIB_LIBRARY}")
    include_directories(${demoLIB_INCLUDE_DIR})
    target_link_libraries(demo_main ${demoLIB_LIBRARY})
else()
    message("not found demoLIB_FOUND")
endif(demoLIB_FOUND)
```


https://blog.csdn.net/haluoluo211/article/details/80559341
