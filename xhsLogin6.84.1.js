function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}

function hook_java(){
    Java.perform(function(){
        console.log('Hook Start ！');

        // password    
        // 明文 123456
        // 算法md5
        // 密文 e10adc3949ba59abbe56e057f20f883e

        // imei_encrypted

        // var a = Java.use('n.d0.e.a');
        // var r = Java.use('n.d0.r1.j.r');
        // var d0 = Java.use('n.d0.r1.j.d0');
        // var q0 = Java.use('n.d0.r1.j.q0');
        
        // String string = sharedPreferences.getString("device_id", (String) null);
        // a = UUID.fromString(string); // 7A4717AD-4435-3A60-A675-A73051F7323F

         // public static String c() {
        //     return b(XYUtilsCenter.c()); // 7A4717AD-4435-3A60-A675-A73051F7323F
        // }

        // 7A4717AD-4435-3A60-A675-A73051F7323F  c().toUpperCase()
        //  8e2d6c0eb954

        // c().toUpperCase() + "8e2d6c0eb954"
        // 7A4717AD-4435-3A60-A675-A73051F7323F8e2d6c0eb954  明文
        // 算法md5
        //d0.b(c().toUpperCase() + "8e2d6c0eb954").toUpperCase()
        // A634A03223FF4A7DDD4A02ED6BFAA7EC 密文

        // f13583c = q0.a(c2, d0.b(c().toUpperCase() + "8e2d6c0eb954").toUpperCase());

        // var c = r.c().toUpperCase() + "8e2d6c0eb954"; // 7A4717AD-4435-3A60-A675-A73051F7323F8e2d6c0eb954
        // console.log("c : ", c);
        // var b = d0.b(c).toUpperCase(); // A634A03223FF4A7DDD4A02ED6BFAA7EC
        // console.log("b : ", b);

        // var content = a.$new().a();
        // console.log("content : ", content);
        // var c2 = r.c(content); // 861912558390245 是 IMEI
        // console.log("c2 : ", c2);

        // AES/CBC/PKCS5Padding 
        // ivParameterSpec : abcdef1234567890
        // secretKeySpec   : A634A03223FF4A7DDD4A02ED6BFAA7EC
        // 明文 861912558390245
        // 密文 MZoDOEv3BQICR9j9W/bPTA==

        // var imei_encrypted = q0.a(c2, b);    // MZoDOEv3BQICR9j9W/bPTA==
        // console.log("imei_encrypted : ", imei_encrypted);



        
        var Map = Java.use('java.util.Map');
        Map.put.implementation = function(a, b){
            if(a == 'x-b3-traceid'){
                showStacks();
                console.log(a, b);
            };
            return this.put(a, b);
        };
    
        var HashMap = Java.use('java.util.HashMap');
        HashMap.put.implementation = function(a, b){
            if(a == 'x-b3-traceid'){
                showStacks();
                console.log(a, b);
            };
            return this.put(a, b);
        };

        var ConcurrentHashMap = Java.use('java.util.concurrent.ConcurrentHashMap');
        ConcurrentHashMap.put.implementation = function(a, b){
            if(a == 'x-b3-traceid'){
                showStacks();
                console.log(a, b);
            };
            return this.put(a, b);
        };
    
    })
}

setImmediate(hook_java);




