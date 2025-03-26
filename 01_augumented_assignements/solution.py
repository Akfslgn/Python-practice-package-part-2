# do not change the method name
def main():
    balance = 5000
    print("================== BALANCE ====================", end="\n\n")
    print(f"Current Balance: ${balance:.1f}")
    # write your code here with 4 space intentation
    deposit_amount = float(input("How much do you want to deposit: $"))
    balance += deposit_amount
    print(f"Balance Successfully Updated: ${balance:.1f}")
    withdrawal_amount = float(input("How much do you want to withdraw: $"))
    withdrawal_fee = withdrawal_amount * 0.03
    print("There is a 3% transaction fee on the withdrawal.")
    print(f"Withdrawal: ${withdrawal_amount:.1f} - Fee: ${withdrawal_fee:.1f}")
    total_withdrawal = withdrawal_amount + withdrawal_fee
    if total_withdrawal > balance:
        print("Error: Insufficient funds for this withdrawal.")
    else:
        balance -= total_withdrawal
        print(f"Balance Successfully Updated: ${balance:.1f}")
    print("")
    print("============ TRANSACTION COMPLETED ============")


# do not change the following lines:
if __name__ == "__main__":
    main()
