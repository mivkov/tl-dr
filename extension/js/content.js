console.log("injected")

closeDiv = function(){
    this.parentNode.parentNode
    .removeChild(this.parentNode);
    return false;
};

createPopup = function(str) {
    var frag = document.getElementById("fragment-text")
    if(frag != null) {
        frag.innerHTML = str
        return;
    }

    var div = document.createElement("div")
    div.setAttribute('class', 'fragment')
    var close = document.createElement("span")
    close.innerHTML = "x"
    close.setAttribute('id', 'close')
    close.onclick = closeDiv

    var title = document.createElement("h3")
    title.innerHTML = "Simplification"
    var txt = document.createElement("p")
    txt.setAttribute('id', 'fragment-text')
    txt.innerHTML = str

    div.appendChild(close)
    div.appendChild(title)
    div.appendChild(txt)

    document.body.appendChild(div);
}

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.requested == "createDiv"){
            createPopup(request.data)
            console.log(request.data)
            sendResponse({confirmation: "Successfully created div"});
            return true;
        }
    });