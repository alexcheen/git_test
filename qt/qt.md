## Qt 对象树
当创建的对象在堆区时候，如果指定的父亲是QObject派生下来的类或者QObject子类派生下来的类，可以不用管理释放的操作，将对象会放入到对象树中。

# QSS

```cpp
MainWidget::MainWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::MainWidget)
{
　　//应用样式 apply the qss style
    QFile file(":/qss/main.qss");
    file.open(QFile::ReadOnly);
    QTextStream filetext(&file);
    QString stylesheet = filetext.readAll();
    this->setStyleSheet(stylesheet);
 　　file.close();
}
```
```css
QPushButton{
    color:red;
    background-color: white
}
```