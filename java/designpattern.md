# Observer
# Decorator
```java
public abstract class Beverage {
    String description = "Unkonwn Beverage";
    public String getDescription() {
        return description;
    }
    public double cost();
}
public abstract class CondimentDecorator extends Beverage{
    public abstract String getDescription();
}

public class Epresso extends Beverage {
    public Epresso () {
        description = "Espresso";
    }
    public double cost() {
        return 1.99;
    }
}

pulic class Mocha extends CondimentDecorator {
    Beverage beverage;
    public Mocha(Beverage beverage) {
        this.beverage = beverage;
    }
    public String getDescription() {
        return beverage.getDescription()+", Mocha";
    }
    public cost() {
        return .20+beverage.cost();
    }
}

pulic class Test{
    public static void main(String arg[]) {
        Beverage beverage = new Epresso();
        beverage = new Mochar(beverage);
        System.out.println(beverage.getDescription()+" $"
            beverage.cost());
    }
}
```