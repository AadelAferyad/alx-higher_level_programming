#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, status) {
  for (let i = 0; i < data.results.length; i++) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
