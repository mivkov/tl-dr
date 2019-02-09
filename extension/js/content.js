chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.requested == "createDiv"){
            //Code to create the div
            sendResponse({confirmation: "Successfully created div"});
            return true;
        }
    });