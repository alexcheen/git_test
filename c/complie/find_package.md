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
https://blog.csdn.net/haluoluo211/article/details/80559341