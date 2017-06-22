const path = require('path');
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: './tabbycat/templates/js-bundles/entry.js',
  output: {
    path: path.resolve(__dirname, './tabbycat/static/js/'),
    filename: 'entry.bundle.js',
  },
  plugins: [
  ],
};