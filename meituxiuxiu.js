// 美图秀秀app version 9.1.3.0

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
    
    })
}

setImmediate(hook_java);
