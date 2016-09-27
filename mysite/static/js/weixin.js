var nature = ["不限","全职","兼职","实习"];
var pn = 1;
var select_name = ["工作城市","行政区","商区","工作种类","详细分类","工作","工作经验","学历要求","融资阶段","行业领域","月薪","工作性质"];
$(document).ready(function(){   
    console.log("ok");
    menu_refer();
    //选择控计改变的事件，根据上面的菜单渲染下面的select
    $(".select0").change(function(event) {
        $(".select1").empty();
        /* Act on the event */
        city_n = $(this).children('option:selected').val();
        $(".select1").append("<option value=\"\"></option>");
        for(var district in city_data[city_n]){
            $(".select1").append("<option value=\""+district+"\">"+district+"</option>");
        }
    });
    $(".select1").change(function(event) {
        /* Act on the event */
        $(".select2").empty();
        city_n = $(".select0").children('option:selected').val();
        district = $(this).children('option:selected').val();
        if(district != "不限")
            $(".select2").append("<option value=\"\"></option>");
        for(var bz in city_data[city_n][district]){
            $(".select2").append("<option value=\""+city_data[city_n][district][bz]+"\">"+city_data[city_n][district][bz]+"</option>");
        }
    });
    $(".select3").change(function(event) {
        $(".select4").empty();
        /* Act on the event */
        job_fn = $(this).children('option:selected').val();
        for(var fn in job_data[job_fn]){
            $(".select4").append("<option value=\""+fn+"\">"+fn+"</option>");
        }
    });
    $(".select4").change(function(event) {
        $(".select5").empty();
        /* Act on the event */
        job_fn = $(".select3").children('option:selected').val();
        job_sn = $(this).children('option:selected').val();
        for(var sn in job_data[job_fn][job_sn]){
            $(".select5").append("<option value=\""+job_data[job_fn][job_sn][sn]+"\">"+job_data[job_fn][job_sn][sn]+"</option>");
        }
    });
    $(".query-button").click(function(event) {
        /* Act on the event */
        var data = {};
        data["location"] = $(".select0").children('option:selected').val();
        if (data["location"] != "全国"){
            data["loc_adminarea"] = $(".select1").children('option:selected').val();
            if(data["loc_adminarea"] != ""&&data["loc_adminarea"] != "不限"){
                data["loc_busarea"] = $(".select2").children('option:selected').val();
            }
            else{
                data["loc_busarea"] = "";
            }
        }
        else{
            data["loc_adminarea"] = "";
            data["loc_busarea"] = "";
        }
        if($(".select3").children('option:selected').val() != ''){
            data["job"] = $(".select5").children('option:selected').val();
        }
        else{
            data["job"] = "";
        }
        if($(".select6").children('option:selected').val() != ''&&$(".select6").children('option:selected').val() != "不限"){
            data["job_exp"] = $(".select6").children('option:selected').val();
        }
        else{
            data["job_exp"] = "";
        }
        if($(".select7").children('option:selected').val() != ''&&$(".select7").children('option:selected').val() != "不限"){
            data["edu"] = $(".select7").children('option:selected').val();
        }
        else{
            data["edu"] = "";
        }
        if($(".select8").children('option:selected').val() != ''&&$(".select8").children('option:selected').val() != "不限"){
            data["FinancingStage"] = $(".select8").children('option:selected').val();
        }
        else{
            data["FinancingStage"] = "";
        }
        if($(".select9").children('option:selected').val() != ''&&$(".select9").children('option:selected').val() != "不限"){
            data["IndustrySectors"] = $(".select9").children('option:selected').val();
        }
        else{
            data["IndustrySectors"] = "";
        }
        if($(".select10").children('option:selected').val() != ''&&$(".select10").children('option:selected').val() != "不限"){
            data["salary"] = $(".select10").children('option:selected').val();
        }
        else{
            data["salary"] = "";
        }
        if($(".select11").children('option:selected').val() != "不限"){
            data["job_nature"] = $(".select11").children('option:selected').val();
        }
        else{
            data["job_nature"] = "";
        }
        data["pn"] = pn+""
        $.getJSON('/test/', data, function(json_content_s) {
            json_content = $.eval("("+json_content_s+")")
            /*optional stuff to do after success */
            if (job_content[result] == []){
                $("#content").append("<div class=\"no-result\"><h2>没有您想找的工作</h2></div>");
            }
            else {
                for (var d in json_content.result){
                    job_c = "<div class=\"job-content "+json_content.result[d]["positionId"]+"\"></div>";
                    $("#content").append(job_c);
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-nameAndLocation\"><a href=\"#\">"+json_content.result[d]["positionName"]+"["+json_content.result[d]["city"]+"]</a></span>");
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-company-name\">"+json_content.result[d]["companyFullName"]+"</span>");
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-company-ifAndFs\">"+json_content.result[d]["industryField"]+" / "+json_content.result[d]["financeStage"]+"</span>");
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-salary\">"+json_content.result[d]["salary"]+"</span>");
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-expAndEdu\">"+json_content.result[d]["workYear"]+" / "+json_content.result[d]["education"]+"</span>");
                    $("."+json_content.result[d]["positionId"]).append("<span class=\"job job-advantage\">"+json_content.result[d]["positionAdvantage"]+"</span>");
                    for (var job_d in json_content.result[d]["companyLabelList"]){
                        $("."+json_content.result[d]["positionId"]).append("<span class=\"job-company-label\">"+json_content.result[d]["companyLabelList"][job_d]+"</span>");
                    }

                }

            }
        })

    });
});
//菜单渲染
function menu_refer(){
    for (var sn=0;sn<select_name.length;sn++){
        console.log(select_name[sn]);
        var select_group = "<div class=\"select-group\"><span>"+ select_name[sn] +"</span><select name=\"job-category"+ sn +"\" class=\"select-default select"+ sn +"\"></select></div>"
        $("#container").append(select_group);
        if (select_name[sn] == "工作城市"){
            $(".select0").append("<option value=\"全国\">全国</option>");
            for (var city in city_data){
                $(".select0").append("<option value=\""+city+"\">"+city+"</option>");
            }
        }
        else if(select_name[sn] == "工作种类"){
            $(".select3").append("<option value=\"\"></option>");
            for (var job_f in job_data){
                $(".select3").append("<option value=\""+job_f+"\">"+job_f+"</option>");
            }
        }
        else if(select_name[sn] == "工作经验"){
            $(".select6").append("<option value=\"\"></option>");
            for (var job_exp in other_parameter.工作经验){
                $(".select6").append("<option value=\""+other_parameter.工作经验[job_exp]+"\">"+other_parameter.工作经验[job_exp]+"</option>");
            }
        }
        else if(select_name[sn] == "学历要求"){
            $(".select7").append("<option value=\"\"></option>");
            for (var edu in other_parameter.学历要求){
                $(".select7").append("<option value=\""+other_parameter.学历要求[edu]+"\">"+other_parameter.学历要求[edu]+"</option>");
            }
        }
        else if(select_name[sn] == "融资阶段"){
            $(".select8").append("<option value=\"\"></option>");
            for (var fs in other_parameter.融资阶段){
                $(".select8").append("<option value=\""+other_parameter.融资阶段[fs]+"\">"+other_parameter.融资阶段[fs]+"</option>");
            }
        }
        else if(select_name[sn] == "行业领域"){
            $(".select9").append("<option value=\"\"></option>");
            for (var ifi in other_parameter.行业领域){
                $(".select9").append("<option value=\""+other_parameter.行业领域[ifi]+"\">"+other_parameter.行业领域[ifi]+"</option>");
            }
        }
        else if(select_name[sn] == "月薪"){
            $(".select10").append("<option value=\"\"></option>");
            for (var salary in other_parameter.月薪){
                $(".select10").append("<option value=\""+other_parameter.月薪[salary]+"\">"+other_parameter.月薪[salary]+"</option>");
            }
        }
        else if(select_name[sn] == "工作性质"){
            for (var na in nature){
                $(".select11").append("<option value=\""+nature[na]+"\">"+nature[na]+"</option>");
            }
        }
    }
    $("#container").append("<button class=\"query-button\">查询</button>");
}