package com.qdf_01;

import java.math.BigInteger;
import java.security.SecureRandom;
// 平安健康 登录 loginPwd
public class pajkLoginPwd {
    public static void main(String[] args) {
        System.out.println(encrypt("123456"));
    }

    public static String encrypt(String str) {
        BigInteger modPow;
        BigInteger bigInteger = new BigInteger("D275807D2EAD211604D5A5EC42B9EB4F9BD7AE0624A8D1CBAF577CC9656CE5BEC2C31ABC4271C1368447EBC79B62F84117CE87DD00767DF8A3F506C3693843003AC55DA4745C48C70F3045A00CDF6F44A187FFDA5527B4F65CE2519AE11E2AD2907E78AE2B5C8B4F5F0FE680D93D40148893829A9188E4B1F5A74B96DFAFD5F5", 16);
        BigInteger bigInteger2 = new BigInteger("10001", 16);
        BigInteger a2 = getA2(str, (bigInteger.bitLength() + 7) >> 3);
        if (a2 == null || (modPow = a2.modPow(bigInteger2, bigInteger)) == null) {
            return null;
        }
        String upperCase = modPow.toString(16).toUpperCase();
        int length = 256 - upperCase.length();
        for (int i2 = 0; i2 < length; i2++) {
            upperCase = "0" + upperCase;
        }
        return upperCase;

    }

    private static BigInteger getA2(String str, int i2) {
        if (i2 < str.length() + 11) {
            return null;
        }
        byte[] bArr = new byte[i2];
        int length = str.length() - 1;
        while (length >= 0 && i2 > 0) {
            int i3 = length - 1;
            char charAt = str.charAt(length);
            if (charAt < 128) {
                i2--;
                bArr[i2] = (byte) charAt;
            } else if (charAt <= 127 || charAt >= 2048) {
                int i4 = i2 - 1;
                bArr[i4] = (byte) ((charAt & '?') | 128);
                int i5 = i4 - 1;
                bArr[i5] = (byte) (128 | ((charAt >> 6) & 63));
                i2 = i5 - 1;
                bArr[i2] = (byte) ((charAt >> 12) | 224);
            } else {
                int i6 = i2 - 1;
                bArr[i6] = (byte) (128 | (charAt & '?'));
                i2 = i6 - 1;
                bArr[i2] = (byte) ((charAt >> 6) | 192);
            }
            length = i3;
        }
        int i7 = i2 - 1;
        bArr[i7] = 0;
        SecureRandom secureRandom = new SecureRandom();
        byte[] bArr2 = new byte[i7];
        while (i7 > 2) {
            bArr2[0] = 0;
            while (bArr2[0] == 0) {
                secureRandom.nextBytes(bArr2);
            }
            i7--;
            bArr[i7] = bArr2[0];
        }
        int i8 = i7 - 1;
        bArr[i8] = 2;
        bArr[i8 - 1] = 0;
        return new BigInteger(bArr);
    }

}