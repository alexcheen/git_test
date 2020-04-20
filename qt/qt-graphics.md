<!--
 * @Author: your name
 * @Date: 2020-04-14 18:08:30
 * @LastEditTime: 2020-04-20 16:10:19
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \git_test\qt\qt-graphics.md
 -->
# 三要素
1. View QGraphicsView
2. Scene QGraphicsScene
3. Item QGraphicsItem



常见的 QGraphicsItem
为方便起见，Qt 为最常见的形状提供了一组典型的标准 item。它们是：

QGraphicsSimpleTextItem：提供了一个简单的文本标签项
QGraphicsTextItem：提供了一个格式化的文本项
QGraphicsLineItem：提供了一个直线项
QGraphicsPixmapItem：提供了一个图像项
QGraphicsRectItem：提供了一个矩形项
QGraphicsEllipseItem：提供了一个椭圆项
QGraphicsPathItem：提供了一个路径项
QGraphicsPolygonItem：提供了一个多边形项

# placeholder

# saving a scene to an image

```cpp
    QRect rect = scene.sceneRect().toAlignedRect();
    QImage image(rect.size(), QImage::Format_ARGB32);
    image.fill(Qt::transparent);
    QPainter painter(&image);
    scene.render(&painter);
    image.save("scene.png");
```

# Widgets inside Graphics View
```cpp
    QSpinBox *box = new QSpinBox;
    QGraphicsProxyWidget *proxyItem = new QGraphicsProxyWidget;
    proxyItem->setWidget(box);
    scene()->addItem(proxyItem);
    proxyItem->setScale(2);
    proxyItem->setRotation(45);
```
# event
|Event types|Description|
|-|-|
|QEvent::keyPress，<br>QEvent::keyRelease<br/>|A keyboard button was pressed or released.|
|QEvent::MouseButtonPress ,<br> QEvent::MouseButtonRelease , <br/> QEvent::MouseButtonDblClick|The mouse buttons were pressed or released.|
|QEvent::Wheel|The mouse wheel was rolled.|
|QEvent::Enter|The mouse cursor entered the object's boundaries.|
|QEvent::MouseMove|The mouse cursor was moved.|
|QEvent::Leave|The mouse cursor left the object's boundaries.|
|QEvent::Resize|The widget was resized (for example, because the user resized the window or the layout changed).|
|QEvent::Close|The user attempted to close the widget's window.
|QEvent::ContextMenu|The user requested a context menu (the exact action depends on the operating system's way to open the context menu).
|QEvent::Paint|The widget needs to be repainted.|
|QEvent::DragEnter, <br> QEvent::DragLeave , <br/> QEvent::DragMove ,<br> QEvent::Drop<br/> |The user performs a drag and drop action.|
|QEvent::TouchBegin ,<br>QEvent::TouchUpdate ,<br/>QEvent::TouchEnd ,<br>QEvent::TouchCancel<br/>|A touchscreen or a trackpad reported an event.|

# mouse whell scale
```cpp
void View::wheelEvent(QWheelEvent *event)
{
    QGraphicsView::wheelEvent(event);
    if (event->isAccepted()) {
        return;
    }
    const qreal factor = 1.1;
    //deside zoom in or zoom out 
    if (event->angleDelta().y() > 0) {
        scale(factor, factor);
    } else {
        scale(1 / factor, 1 / factor);
    }
    event->accept();
}
```

# zoom level
```cpp
const qreal detail = QStyleOptionGraphicsItem::levelOfDetailFromTransform(painter->worldTransform());
```
If the item is zoomed in 2:1, the level of detail is 2, and if the item is zoomed out 1:2, the level of detail is 0.5.
