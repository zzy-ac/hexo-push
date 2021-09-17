'use strict';

const fs = require('hexo-fs');

hexo.extend.generator.register('custom', function() {
  return ['custom.css', 'custom.js'].map(item => ({
    path: item,
    data: function() {
      return fs.existsSync(`source/${item}`) ? fs.createReadStream(`source/${item}`) : '';
    }
  }));
});

function uuid() {
  function S4() {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
  }
  return S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4();
}
