sendData = function(str) {
    var query = str.selectionText
    js = JSON.stringify({"text": query})

    url = "https://tlng-dr.herokuapp.com/api"
    $.ajax({
        type: 'POST',
        url: url,
        data: {"text": query},
        success: success,
        async: false
      });
}

success = function() {
    alert("Success!")
}

chrome.contextMenus.create({
      title: "Simplify!",
      contexts: ["selection"],
      onclick: function(str) {
          sendData(str)
      }
});