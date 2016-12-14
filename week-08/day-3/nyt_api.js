'use strict';

let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=42414a7e048949439fc78f8267df605e&q=apollo11', true);
xhr.send(null);

xhr.onreadystatechange = initData;

function initData(timesData) {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    var articles = JSON.parse(xhr.response);
    // debugger; // NOTE: uncomment this to observe JSON objects
    // call display function here
    display(articles.response.docs);
  };
};

function display(articles) {
  articles.forEach(function(e) { // maybe better to map them
    var docType = e.document_type;
    var articleHeadline = e.headline.main;
    var articleSnippet = e.snippet;
    var articlePubDate = e.pub_date;
    var articlePermaLink = e.web_url;
    if (docType = 'article') {
      var articleToDisplay = document.createElement('article');
      var list = document.createElement('ul');
      var li1 = document.createElement('li');
      var li2 = document.createElement('li');
      var li3 = document.createElement('li');
      li1.textContent = articleHeadline;
      li2.textContent = articleSnippet;
      li3.textContent = articlePubDate;
      articleToDisplay.appendChild(list);
      list.appendChild(li1);
      list.appendChild(li2);
      list.appendChild(li3);
      document.body.appendChild(articleToDisplay);
    }
  });
}
