package io.github.apis035;

public class App {
    public static void main(String[] args) {
        System.out.println("--- Aplikasi banking ---");

        AkunBank akun = new AkunBank(10000);
        System.out.println("Saldo anda saat ini adalah " + akun.getSaldo());

        akun.tarik(2000);
        System.out.println("Anda menarik 2000, sisa saldo anda adalah " + akun.getSaldo());

        akun.deposit(34000);
        System.out.println("Anda menyetor 34000, sisa saldo anda adalah " + akun.getSaldo());
    }
}
