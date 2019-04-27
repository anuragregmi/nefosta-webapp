function getImage(photo) {
  return photo ? photo : '/assets/img/desk.jpg'
}

function makeArticleBox(article) {
  return `
  <div class="col-sm-6 col-md-4 item">
    <a href="#">
      <img class="img-fluid" src="${getImage(article.photo)}">
    </a>
    <h3 class="name" style="font-family:'Averia Serif Libre', cursive;color:#126ea2;">
      ${$.escapeHTML(article.title)}
    </h3>
    <p class="description" style="font-family:'Source Sans Pro', sans-serif;font-size:15px;color:rgb(0,0,0);">
      ${$.escapeHTML(article.content)}
    </p>
      <a href="/articles/${article.id}" class="action">
        <i class="fa fa-angle-double-right" style="font-size:34px;"></i>
      </a>
  </div>
  `
}