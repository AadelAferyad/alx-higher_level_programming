#!/usr/bin/node
const btn = $('ul.my_list');
$('div#add_item').on('click', function (event) {
  btn.append('<li>Item</li>');
});
