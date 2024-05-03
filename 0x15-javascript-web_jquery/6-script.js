#!/usr/bin/node
const selector = $('header');
const tag = $('DIV#update_header');
tag.on('click', function (event) {
  selector.text('New Header!!!');
});
