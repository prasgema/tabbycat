const path = require('path');
var BundleTracker = require('webpack-bundle-tracker')

var config = require('./webpack.base.config.js')

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './tabbycat/webpack-stats.json'}),
])

module.exports = config