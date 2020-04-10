## Qt 对象树
当创建的对象在堆区时候，如果指定的父亲是QObject派生下来的类或者QObject子类派生下来的类，可以不用管理释放的操作，将对象会放入到对象树中。


### 设置窗口的几何位置
```cpp
QWidget::setGeometry(x,y,w,h);
```
### qss文件的使用
```cpp
QFile file(":/res/qss/main.qss");
    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    file.close();
```
### 在Qt中使用自定义类使用Qss
在Qt中使用自定义类，其继承QWdiget或QWidget的派生类时，需重载paintEvent
```cpp
//https://forum.qt.io/topic/25142/solved-applying-style-on-derived-widget-with-custom-property-failes
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget,&opt,&p, this);
```


### connect

如果连接了信号和槽，但不用时需断开，多次连接会注册对此调用。
有时连接信号和槽时，不能找到对应的信号或者槽时，有可能时对应的类在头文件声明中没有使用Q_OBJECT宏。
### Qt widget 关闭时的释放

 - 删除：是指窗口被销毁，也就是说窗口不存在了。比如窗口使用new创建的，则表示窗口被delete了，被销毁的窗口不能被再次使用，否则会发生内存错误。
 - 隐藏：是指窗口不可见，但窗口并未被销毁，使用show()等函数，可以让该窗口再次可见。
 - 关闭：是指窗口不可见，但窗口有可能是被删除了，也有可能是被隐藏了，这要视情况而定。
 - 窗口被删除时，会同时删除其子对象，而隐藏则不会。
在close()函数调用后，如果希望Widget对象自动释放内存，需要在widget设置相应属性。
```cpp
widget->setAttribute(Qt::WA_DeleteOnClose);
```