#!/usr/bin/node

exports.esrever = function (list) {
  let i;
  const reverserList = [];
  for (i = list.length - 1; i >= 0; i--) {
    reverserList.push(list[i]);
  }
  return (reverserList);
};
