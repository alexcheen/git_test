cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(rdn_test LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(rdn_test "")

target_sources(rdn_test
  PRIVATE
      main.cpp
)
