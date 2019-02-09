sendData = function(str) {
    var query = str.selectionText
    $.post("localhost/api:3000", {text: query}, function(data) {
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