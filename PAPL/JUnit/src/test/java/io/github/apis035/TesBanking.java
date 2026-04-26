package io.github.apis035;

import org.junit.Test;
import static org.junit.Assert.*;

public class TesBanking {
    @Test
    public void tesDeposit() {
        AkunBank akun = new AkunBank(10_000);
        akun.deposit(5_000);
        assertEquals(15_000, akun.getSaldo());
    }

    @Test
    public void tesPenarikan() {
        AkunBank akun = new AkunBank(10_000);
        akun.tarik(4_000);
        assertEquals(6_000, akun.getSaldo());
    }

    @Test
    public void testPenarikanBerlebih() {
        AkunBank akun = new AkunBank(10_000);
        assertThrows(IllegalStateException.class, () -> akun.tarik(20_000));
    }

    @Test
    public void tesDepositNegatif() {
        AkunBank akun = new AkunBank(10_000);
        assertThrows(IllegalArgumentException.class, () -> akun.deposit(-5_000));
    }
}
