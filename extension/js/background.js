sendData = function(str) {
    var query = str.selectionText
    $.post("tlng-dr.herokuapp.com/api", {text: query}, function(data) {
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