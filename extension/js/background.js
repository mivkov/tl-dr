sendData = function(str) {
    var query = str.selectionText

    url = "https://tlng-dr.herokuapp.com/api"
    $.post(url, {data: query}, function(response) {
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