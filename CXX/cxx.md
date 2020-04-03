# 菱形继承问题
```cpp
class A{
public:
    void func();
};
class B : virtual public A{
public:
    void func();
    void funcB();
};
class C : virtual public A{
public:
    void func();
    void funcC();
};
class D : public B, public C{
public:
    void func();
    void funcD();
};
```