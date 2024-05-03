#!/usr/bin/node
$(document).ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  function sendFetch (urlApi) {
    $.get(urlApi, (data, status) => {
      if (status) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      sendFetch(url + $('INPUT#language_code').val());
    }
  });
  $('INPUT#btn_translate').on('click', () => {
    sendFetch(url + $('INPUT#language_code').val());
  });
});
