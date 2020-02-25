# linux读写文件操作GPIO
## 几个目录的说明
 * /sys/class/gpio/export文件用于通知系统需要导出控制的GPIO引脚编号
 * /sys/class/gpio/unexport 用于通知系统取消导出
 * /sys/class/gpio/gpiochipX目录保存系统中GPIO寄存器的信息，包括每个寄存器控制引脚的起始编号base，寄存器名称，引脚总数 导出一个引脚的操作步骤
 * 