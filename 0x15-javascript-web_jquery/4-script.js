#!/usr/bin/node
const togl = $('div#toggle_header');
const header = $('header');
togl.on('click', function (event) {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
