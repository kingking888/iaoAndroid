package com.qdf_01;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.TreeMap;

public class xhsSign {

    public static String signMapToString(TreeMap<String, String> treeMap) {


        ArrayList<String> arrayList = new ArrayList<String>();
        arrayList.addAll(treeMap.keySet());
//		System.out.println(arrayList);
        StringBuilder sb = new StringBuilder();
        Iterator<String> it = arrayList.iterator();
        while (it.hasNext()) {
            String str2 = (String) it.next();
            sb.append(str2);
            sb.append("=");
            sb.append(treeMap.get(str2));
        }

//		System.out.println(sb.toString());
        return sb.toString();
    }

    public static String getURLEncoderString(String str) {
        String result = "";
        if (null == str) {
            return "";
        }
        try {
            result = java.net.URLEncoder.encode(str, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
//		System.out.println(result);
        return result;
    }

    public static String stringToMD5(String plainText) {
        byte[] secretBytes = null;
        try {
            secretBytes = MessageDigest.getInstance("md5").digest(plainText.getBytes());
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("没有这个md5算法！");
        }
        String md5code = new BigInteger(1, secretBytes).toString(16);
        for (int i = 0; i < 32 - md5code.length(); i++) {
            md5code = "0" + md5code;
        }
//		System.out.println(md5code);
        return md5code;
    }

    public static String signResult(TreeMap<String, String> treeMap) throws UnsupportedEncodingException {
        String _signMapToString = signMapToString(treeMap);
        String _getURLEncoderString = getURLEncoderString(_signMapToString);

        byte[] bArr = new byte[1];
        byte[] bytes = _getURLEncoderString.getBytes("UTF-8");
        bArr = bytes;
        String str = treeMap.get("deviceId");
        byte[] bytes2 = str.getBytes("UTF-8");

        StringBuilder sb2 = new StringBuilder();
        int i2 = 0;
        for (byte b2 : bArr) {
            sb2.append(Byte.valueOf((byte) (b2 ^ bytes2[i2])));
            i2 = (i2 + 1) % bytes2.length;
        }
        String sb4 = sb2.toString();
        String _stringToMD5_result = stringToMD5(stringToMD5(sb4) + str);
        return _stringToMD5_result;

    }

    public static void main(String[] args) {
        TreeMap<String, String> treeMap = new TreeMap<String, String>();
        String phone = "16636857856";
        String password = "123456";
//		treeMap.put("password", "e10adc3949ba59abbe56e057f20f883e");
        treeMap.put("password", stringToMD5(password));
        treeMap.put("zone", "86");
//		treeMap.put("phone", "16636857856");
        treeMap.put("phone", phone);
        treeMap.put("imsi", "unknow");
        treeMap.put("android_version", "27");
        treeMap.put("type", "phone");
        treeMap.put("android_id", "3632a884c39d0b8d");
        treeMap.put("mac", "ac:37:43:4c:11:3b");
        treeMap.put("platform", "android");
        treeMap.put("deviceId", "6324f43c-c2f3-37b3-b89a-30e84297faa1");
        treeMap.put("device_fingerprint", "20200930234755c974816086d953ec14b52cb6740970ab012a7a13c6155e83");
        treeMap.put("device_fingerprint1", "20200930234755c974816086d953ec14b52cb6740970ab012a7a13c6155e83");
        treeMap.put("versionName", "6.44.0");
        treeMap.put("channel", "Store360");
        treeMap.put("sid", "session.1601809768031405442384");
        treeMap.put("lang", "zh-Hans");
        treeMap.put("t", "1601813958");
        treeMap.put("fid", "160181037510cc5135fee74076a4fc529237cd0b1db2");
//		treeMap.put("sign", "cd8f8400a1cc94edd2bab455f8c8d437");
        try {
            String sign = signResult(treeMap);
            System.out.println("sign : " + sign);
        } catch (UnsupportedEncodingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}

