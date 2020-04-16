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