##  set
set(var [value][CACHE TYPE DOCSTRING [FORCE]])
message([SEND_ERROR|STATUS|FATAL_ERROR] "message to display" ...)
SEND_ERROR, 产生错误，生成过程被跳过。
STATUS， 输出前缀为--的信息。
FATAL_ERROR， 立即终止所有cmake过程。

## option
option可接受三个参数：
option(<option_variable> "help string" [initial value])
 * <option_variable>表示该选项的变量的名称。
 * "help string"记录选项的字符串，在CMake的终端或图形用户界面中可见。
 * [initial value]选项的默认值，可以是ON或OFF。

