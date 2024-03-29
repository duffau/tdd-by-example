interface Expression {
    Money reduce(Bank bank, String to);
    Expression plus(Expression addend);
    Expression times(int multiplier);
}

public class Money implements Expression {
    public int amount;
    private String currency;
    
    public Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }
    
    public String toString() {
        String className = this.getClass().getSimpleName();
        return className + "(" + amount + ", " + currency +")";    
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
    
    public Expression times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }
    
    public Expression plus(Expression addend) {
        return new Sum(this, addend);
    }
    
    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(currency, to);
        return new Money(amount / rate, to);
    }
    
}
