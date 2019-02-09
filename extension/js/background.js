sendData = function(str) {
    var query = str.selectionText
    js = JSON.stringify({"text": query})

    url = "https://tlng-dr.herokuapp.com/api"
    $.ajax({
        type: 'POST',
        url: url,
        contentType: "application/json; charset=utf-8",
        data: {"text": query},
        success: success
      });
}

success = function(str) {
    alert("Success!")
}

chrome.contextMenus.create({
      title: "Simplify!",
      contexts: ["selection"],
      onclick: function(str) {
          sendData(str)
      }
});