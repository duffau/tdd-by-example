
public class Money {
    private int amount;
    private String currency;
    
    static Money dollar(int amount) {
        return new Money(amount, "USD")
    }
    
    static Money franc(int amount) {
        return new Money(amount, "CHF")
    }
    
    Money times(int multiplier) {
        return new Money(amount * multiplier);
    }
    
    
}

