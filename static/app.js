function sendResponse(rawText) {
    // var url = "http://127.0.0.1:5000/get_response"
    var url = window.location.origin + "/get_response";
    $.post(url,{
        user_text:rawText
    },function(data, status){
        if(data !== "undefined"){
            console.log(data['bot_response'])
            var image = '<div><img class="imgB1" style="width:10% !important;float:left !important;" src="/static/image/robot.png"></img>';
            var botHtml = '<p class="botText" style="width:90% !important;"><span>' + data['bot_response'] + '</span></p></div>';
            $("#chatbox").append(image);
            $("#chatbox").append(botHtml);
            document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
            return data['bot_response']
            
        }
    })
  }