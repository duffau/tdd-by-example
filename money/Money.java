
public class Money {
    private int amount;
    private String currency;
    
    public Money(int amount, String currency) {
        amount = amount;
        currency = currency;
    }
    
    String currency() {
        return currency;
    }
    
    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && currency() == money.currency();
    }
    
    static Money dollar(int amount) {
        return new Money(amount, "USD");
    }
    
    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }
    
    Money times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }
    
    
}

