#!/usr/bin/node
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, (data, status) => {
  if (status) {
    $('DIV#hello').text(data.hello);
  }
});
