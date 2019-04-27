var TOKEN = undefined;
var USER_INFO = undefined;

$.redirect = function (url) {
  $(location).attr("href", url);
}

$.escapeHTML = function (text) {
  return document.createTextNode(text).textContent
}

function getToken(forceReload = false) {
  if (forceReload || !TOKEN) {
    TOKEN = Cookies.get('authToken');
  }
  return TOKEN
}

// include header in token 
$(document).ajaxSend(function (event, jqXHR, ajaxOptions) {
  let token = getToken()
  if (token) {
    jqXHR.setRequestHeader('Authorization', `Bearer ` + getToken());
  }
});

function getUserInfo() {
  // returns a promise 
  // on success calls success function with userinfo
  // else calls reject function
  return new Promise((resolve, reject) => {
    if (!USER_INFO) {
      $.get('/api/users/me/').done((data) => {
        USER_INFO = data.msg;
        resolve(USER_INFO);
      }).fail((jqXHR) => {
        reject(jqXHR)
      })
    } else {
      resolve(USER_INFO)
    }
  })
}

function checkLogin(redirectLogin) {
  // returns a promise 
  // on success calls success function with userinfo
  // if redirectLogin is set, redirects to login page
  // else calls reject function
  return new Promise((resolve, reject) => {
    getUserInfo().then((user_info) => {
      resolve(user_info)
    }).catch((jqXHR) => {
      if (redirectLogin) {
        $.redirect(`/users/login?next=${location.pathname}`)
      } else {
        reject(jqXHR)
      }
    })
  })
}


function logout() {
  TOKEN = undefined
  Cookies.remove('authToken')
}

function setNextElement(el, nextElement) {
  // appends given nextElement after given el
  return el.insertAdjacentHTML("afterend", nextElement);
}

function setErrorText(selector, errorMessage) {
  // set error message
  messageEl = `
  <div class="alert text-danger alert-dismissible fade show small p-0 m-0" role="alert">
      ${errorMessage}
      <span aria-hidden="true" class="close p-0 m-0" data-dismiss="alert" aria-label="Close">&times;</span>
  </div>
  `
  el = $(selector)[0]

  if (!el) {
    console.error(`No element with ${selector} found.`)
  }


  return setNextElement(el, messageEl)
}

$.postWithFile = function(url, data, callback, error) {
  return jQuery.ajax({
    'type': 'POST',
    'url': url,
    'contentType': 'application/json',
    'data': data,
    'processData': false,
    'contentType': false,
    'success': callback,
    'error': error
  });
}

$.postJSON = function (url, data, callback, error) {
  return jQuery.ajax({
    'type': 'POST',
    'url': url,
    'contentType': 'application/json',
    'data': JSON.stringify(data),
    'dataType': 'json',
    'success': callback,
    'error': error
  });
};