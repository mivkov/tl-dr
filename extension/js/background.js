sendData = function(str) {
    var query = str.selectionText
    alert(`Query: ${query}`)
    $.post("https://tlng-dr.herokuapp.com/api", {data: query}, function(data) {
        alert(`Received response: ${data.response}`);
    });
}

chrome.contextMenus.create({
      title: "Simplify!",
      contexts: ["selection"],
      onclick: function(str) {
          sendData(str)
      }
});