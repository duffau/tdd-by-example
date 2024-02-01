class Sum implements Expression {
    Money augend;
    Money addend;
    
    public Sum(Money augend, Money addend) {
        this.augend = augend;
        this.addend = addend; 
    }
    
    public reduce(String to) {
        Sum sum = (Sum) source;
        int amount = augend.amount + addend.amount;
        return new Money(amount, to);
    }
}