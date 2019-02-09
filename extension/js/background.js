sendData = function(str) {
    var query = str.selectionText
    js = JSON.stringify({"text": query})

    url = "https://tlng-dr.herokuapp.com/api"
    $.ajax({
        url: url,
        method: 'POST',
        dataType: "json",
        processData: false,
        contentType: "application/json; charset=utf-8",
        data: js,
        success: success
      });
}

success = function(res) {
    alert("Response from server: " + res.data)
}

chrome.contextMenus.create({
      title: "Simplify!",
      contexts: ["selection"],
      onclick: function(str) {
          sendData(str)
      }
});