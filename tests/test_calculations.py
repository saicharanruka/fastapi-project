import pytest
from app.calculations import add, subtract, multiply, BankAccount, InsufficientFunds

# Fixtures
@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize('num1, num2, expected', [
    (3,2,5), (4,5,9), (8,9,17)
    ])
def test_add(num1, num2, expected):
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(3,2) == 1

def test_multiply():
    assert multiply(3,2) == 6



def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


@pytest.mark.parametrize('deposited, withdraw, expected', [
    (200,50,150), (120,80,40), (40,40,0)
    ])
def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)

    assert zero_bank_account.balance == expected

def test_insuffcient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
