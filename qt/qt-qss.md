# qt 样式的盒子模型
MARGIN->BORDER->PADDING->CONTENT



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

## QLineEdit
```css
QLineEdit[echoMode="2"] {
      lineedit-password-character: 9679;
  }
```

# 自定义空间的qss设置

```cpp qt
Q_PROPERTY(QColor m_checkedColor READ checkedColor WRITE setCheckedColor DESIGNABLE true)
//对于 颜色属性m_checkedColor的设置
// 并在类中实现 checkedColor的读方法
// 以及 setCheckedColor的写方法
QColor CustomWidget::checkedColor()
{
    return m_checkedColor;
}

void CustomWidget::setCheckedColor(QColor new_color)
{
    m_checkedColor = new_color;
}
```
对应的QSS文件写法
```css
.CustomWidget{
    qproperty-m_checkedColor: white;
}

```

### qt4 不支持rgba