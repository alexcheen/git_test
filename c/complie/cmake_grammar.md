set(var [value][CACHE TYPE DOCSTRING [FORCE]])
message([SEND_ERROR|STATUS|FATAL_ERROR] "message to display" ...)
SEND_ERROR, 产生错误，生成过程被跳过。
STATUS， 输出前缀为--的信息。
FATAL_ERROR， 立即终止所有cmake过程。
