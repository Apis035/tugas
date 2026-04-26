package io.github.apis035;

public class AkunBank {
    private int saldo;

    public AkunBank(int saldoAwal) {
        if (saldoAwal < 0) {
            throw new IllegalArgumentException("Saldo awal tidak boleh negatif");
        }
        this.saldo = saldoAwal;
    }

    public void deposit(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Deposit tidak valid");
        }
        saldo += jumlah;
    }

    public void tarik(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Penarikan tidak valid");
        }
        if (jumlah > saldo) {
            throw new IllegalStateException("Saldo tidak mencukupi");
        }
        saldo -= jumlah;
    }

    public int getSaldo() {
        return saldo;
    }
}