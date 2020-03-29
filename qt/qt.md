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
