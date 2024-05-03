#!/usr/bin/node
const uri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(uri, function (data, status) {
  if (status) {
    $('DIV#character').text(data.name);
  }
});
