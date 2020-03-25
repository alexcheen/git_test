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
绘制背景图片
```cpp
    QPixmap pixmap = QPixmap(":/res/img/background.png").scaled(this->size());
    QPalette palette(this->palette());
    palette.setBrush(QPalette::Background, QBrush(pixmap));
    this->setPalette(palette);
```
字体设置
```css
    font-size: 14px;
    font-family: "Microsoft YaHei";
    font-weight: 400;
    text-align: center;
```
组件的大小设置，必须用 min-width/max-width;min-height/max-height;
```css
    min-width: 491px;
    min-height: 180px;
    max-width: 491px;
    max-height: 180px;
```