# 
### 自定义Qt事件ID type值在(1000,65535)之间。
```cpp
bool FilterObject::eventFilter(QObject *object, QEvent *event)
{
    if (object == target && event->type() == QEvent::KeyPress) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        if (keyEvent->key() == Qt::Key_Tab) {
            ......
            return true;
        } else {
            return false;
        }
    }
    return false;
}
```
### 事件的发送
```cpp
bool QCoreApplication::sendEvent(QObject *receiver, QEvent *event)
void QCoreApplication::postEvent(QObject *receiver, QEvent *event, int priority = Qt::NormalEventPriority)
void QCoreApplication::sendPostedEvents(QObject *receiver = Q_NULLPTR, int event_type = 0)
```
#### 直接发送事件：sendEvent;
直接发送给receiver事件event;
#### 发送到事件队列：posEvent;
```cpp
int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argc);
    return a.exec();
}
```
以上开启了Qt事件循环来维护一个事件队列，exec本质上就是不停的调用processEvent()函数从队列中获取事件来处理。而posEvent()的作用就是把事件发送到这个队列中去。
这里要注意要在堆(heap)上创建event对象，post后事件队列会获取事件所有权，并释放掉。
#### 在队列中立即处理：sendPostedEvents
函数的作用就是立刻、马上将队列中的 event_type 类型的事件立马交给 receiver 进行处理。需要注意的是，来自窗口系统的事件并不由这个函数进行处理，而是 processEvent()。

## 事件的处理

事件传递给了QObject对象的event()函数。
```cpp
bool event(QEvent* e) override
{
    //process event e
}
```
event()函数本身不会处理事件，而是根据事件类型调用不同的事件处理函数。
## 事件的接受和忽略

在对应的事件处理函数中调用accept()或者ignore()来接收或者忽略事件。
## 事件的过滤
```cpp
QObject::installEventFilter(QObject*);
```