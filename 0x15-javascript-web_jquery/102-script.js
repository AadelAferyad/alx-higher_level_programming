#!/usr/bin/node
$(document).ready(() => {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').on('click', (event) => {
    const val = $('INPUT#language_code').val();
    $.get(apiUrl + val, (data, status) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
