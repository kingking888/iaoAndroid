function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}


function hook_java(){
    Java.perform(function(){
        console.log('Hook Start ！');

        var SigEntity = Java.use('com.meitu.secret.SigEntity');
        var BaseApplication = Java.use('com.meitu.library.application.BaseApplication');

        var str1 = "search/feeds.json";
        var strArr =  ["1616145087477", "China Mobile GSM", "GMT+8", "0", "2478324565", "taobao", "VOG-AL00", "HUAWEI", "720*1280", "zh_CN", "fa:a3:eb:47:34:97", "1089867602", "256", "4.26.10", "7.1.2", "normal", "0", "凌霄", "1", "0", "wifi", "mtxx-9130-HUAWEI-VOG-AL00-android-7.1.2-ab57e38e", "3546", "12", "1", "0", "9.1.3.0", "0", "2.0.0", "CN", "1", "153", "25", "0", "861912558390245", "0", "ef766507d4c2b6e3", "2"];
        var str2 = "6184556633574670337";
        var content = BaseApplication.getApplication()

        var signResult = SigEntity.generatorSig(str1, strArr, str2, content);
        console.log("结果 SigEntity.sig : ", signResult.sig.value)
        console.log("结果 SigEntity.sigTime : ", signResult.sigTime.value)
        console.log("结果 SigEntity.sigVersion : ", signResult.sigVersion.value)



        var helloAddr = Module.findExportByName("librelease_sig.so", "_ZN7_JNIEnv12NewStringUTFEPKc");
        console.log(helloAddr);
        // if(helloAddr != null){
        //     Interceptor.attach(helloAddr,{
        //         onEnter: function(args){
        //             //console.log(args[0]);
        //             //console.log(args[1]);
        //             console.log(args[2]);
        //             //console.log(this.context.x2);
        //             //console.log(args[3]);
        //             //console.log(args[4].toInt32());
        //         },
        //         onLeave: function(retval){
        //             //console.log(retval);
        //             //console.log("retval", retval.toInt32());
        //         }
        //     });
        // }












        // SigEntity.nativeGeneratorSig.overload('java.lang.String', '[[B', 'java.lang.String', 'java.lang.Object').implementation = function(arg1, arg2, arg3, arg4){
        //     console.log("参数 SigEntity arg1 : ", arg1)
        //     console.log("参数 SigEntity arg2 : ", arg2)
        //     console.log("参数 SigEntity arg3 : ", arg3)
        //     console.log("参数 SigEntity arg4 : ", arg4)
        //     var signResult = this.nativeGeneratorSig(arg1, arg2, arg3, arg4);
        //     console.log("结果 SigEntity.sig : ", signResult.sig.value)
        //     console.log("结果 SigEntity.sigTime : ", signResult.sigTime.value)
        //     console.log("结果 SigEntity.sigVersion : ", signResult.sigVersion.value)
        //     return signResult;
        // };

        // SigEntity.generatorSig.overload('java.lang.String', '[Ljava.lang.String;', 'java.lang.String', 'java.lang.Object').implementation = function(arg1, arg2, arg3, arg4){
        //     console.log("参数 SigEntity arg1 : ", arg1)
        //     console.log("参数 SigEntity arg2 : ", arg2)
        //     console.log("参数 SigEntity arg3 : ", arg3)
        //     console.log("参数 SigEntity arg4 : ", arg4)
        //     var signResult = this.generatorSig(arg1, arg2, arg3, arg4);
        //     console.log("结果 SigEntity.sig : ", signResult.sig.value)
        //     console.log("结果 SigEntity.sigTime : ", signResult.sigTime.value)
        //     console.log("结果 SigEntity.sigVersion : ", signResult.sigVersion.value)
        //     return signResult;
        // };


        
        // var Map = Java.use('java.util.Map');
        // Map.put.implementation = function(a, b){
        //     if(a == 'sig'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigTime'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigVersion'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'client_timestamp'){
        //         showStacks();
        //         console.log(a, b);
        //     };
    
        //     return this.put(a, b);
        // };
    
        // var HashMap = Java.use('java.util.HashMap');
        // HashMap.put.implementation = function(a, b){
        //     if(a == 'sig'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigTime'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigVersion'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'client_timestamp'){
        //         showStacks();
        //         console.log(a, b);
        //     };
    
        //     return this.put(a, b);
        // };

        // var ConcurrentHashMap = Java.use('java.util.concurrent.ConcurrentHashMap');
        // ConcurrentHashMap.put.implementation = function(a, b){
        //     if(a == 'sig'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigTime'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'sigVersion'){
        //         showStacks();
        //         console.log(a, b);
        //     };
        //     if(a == 'client_timestamp'){
        //         showStacks();
        //         console.log(a, b);
        //     };
    
        //     return this.put(a, b);
        // };
    
    })
}

setImmediate(hook_java);