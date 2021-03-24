// com.candidate.doupin 抖聘 5.1

function showStacks(){
    var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    // var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
    console.log(stack);
}

Java.perform(function(){
    console.log('Hook Start ！');

    // var JobUtils = Java.use('com.candidate.doupin.utils.JobUtils');
    // JobUtils.getSign.overload('android.content.Context', 'long').implementation = function(arg1, arg2){
    //     console.log('arg1 : ', arg1);
    //     console.log('arg2 : ', arg2);
    //     var retval = this.getSign(arg1, arg2);
    //     console.log('retval : ', retval);
    //     return retval;
    // }
    // String valueOf = String.valueOf(System.currentTimeMillis());
    // String user_id = RoleManager.Companion.getInstance().getUser().getUser_id();
    // String company_id = RoleManager.Companion.getInstance().getCompany().getCompany_id();
    // public static final String FLAVOR = "doupin";
    // String encryptToSHA1 = StringUtil.encryptToSHA1(valueOf + user_id + company_id + BuildConfig.FLAVOR);

    // job_type	near
    // page_id	1
    // position_id	0
    // city_name	上海
    // device	HUAWEI
    // androidid	ef766507d4c2b6e3
    // sign	aff057a4f5695dfea622af30b586f281626b2c90
    // company_id	266854
    // timestamp	1615972864685
    // os	7.1.2
    // lng	121.480834
    // app_version	5.1
    // openudid	-1478571035
    // client_type	android
    // imei	861912558390245
    // link_type	user
    // channel	doupin
    // channel_type	dp
    // lat	31.226273
    // user_id	266912

    // 标准算法sha1
    // 1615972864685266912266854doupin  明文
    // 1615972864685 266912 266854 doupin
    // aff057a4f5695dfea622af30b586f281626b2c90  结果

    // var StringUtil = Java.use('com.zhen22.base.util.StringUtil');
    // StringUtil.encryptToSHA1.implementation = function(arg1){
    //     console.log('arg1 : ', arg1);
    //     var retval = this.encryptToSHA1(arg1);
    //     console.log('retval : ', retval);
    //     return retval;
    // }


//     console.log('Success！');

//     });

