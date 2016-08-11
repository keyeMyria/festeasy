const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const { preLoaders, loaders } = require('./webpack.loaders');


module.exports = {
  devtool: 'eval-source-map',
  entry: './src/entry.jsx',
  output: {
    path: 'build',
    filename: 'bundle.js',
    publicPath: '/',
  },
  plugins: [
    new ExtractTextPlugin('[name].css'),
    new CopyWebpackPlugin([{
      from: '_redirects',
    }]),
    new HtmlWebpackPlugin({
      template: './src/index.ejs',
      inject: 'body',
      title: 'FestEasy',
    }),
  ],
  resolve: {
    root: path.resolve('./src'),
  },
  devServer: {
    historyApiFallback: true,
  },
  module: {
    preLoaders,
    loaders,
  },
};
