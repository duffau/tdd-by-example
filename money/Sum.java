class Sum implements Expression {
    Money augend;
    Money addend;
    
    public Sum(Money augend, Money addend) {
        this.augend = augend;
        this.addend = addend; 
    }
    
    public Money reduce(Bank bank, String to) {
        int amount = augend.redude(bank, to).amount + addend.redude(bank, to).amount;
        return new Money(amount, to);
    }
}