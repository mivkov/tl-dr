sendData = function(str) {
    var query = str.selectionText
    js = JSON.stringify({ "data": query})

    url = "https://tlng-dr.herokuapp.com/api"
    $.post(url, js, function(response) {
        alert(`Received response: ${response.data}`);
    });
}

chrome.contextMenus.create({
      title: "Simplify!",
      contexts: ["selection"],
      onclick: function(str) {
          sendData(str)
      }
});