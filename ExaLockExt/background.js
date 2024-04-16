chrome.tabs.onCreated.addListener(function (tab) {
    chrome.tabs.remove(tab.id);
})

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab){
    console.log(tab.url.includes("chrome://"))
    if(tab.url.includes("chrome://")){
        chrome.tabs.update(tab.id, { url: "about:blank" });
    }
})