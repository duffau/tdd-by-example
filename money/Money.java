interface Expression;

public class Money implements Expression {
    private int amount;
    private String currency;
    
    public Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }
    
    String currency() {
        return currency;
    }
    
    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && currency().equals(money.currency());
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
    
    Expression plus(Money addend) {
        return new Money(amount + addend.amount, currency);
    }
    
}

public class Bank {
    Money reduce(Expression source, String to) {
        return null;
    }
}   
