// Place at /static/js/csrf.js
// using jQuery
function csrfSafeMethod(method) {
// These HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
crossDomain: false, // Obviates need for sameOrigin test
beforeSend: function(xhr, settings) {
if (!csrfSafeMethod(settings.type)) {
xhr.setRequestHeader("X-CSRFToken", csrftoken);
}
}
});