const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');


module.exports = {
  devtool: 'source-map',
  entry: './src/entry.jsx',
  output: {
    path: 'build',
    filename: 'bundle.js',
    publicPath: '/',
  },
  plugins: [
    new ExtractTextPlugin('[name].css'),
    new CopyWebpackPlugin([
      {
        from: '_redirects',
      },
    ]),
    new HtmlWebpackPlugin({
      template: './src/index.ejs',
      inject: 'body',
      title: 'FestEasy',
    }),
    new webpack.ProvidePlugin({
      _: 'lodash',
      jQuery: 'jquery',
    }),
  ],
  resolve: {
    modulesDirectories: ['node_modules', './src'],
  },
  devServer: {
    historyApiFallback: true,
  },
  module: {
    preLoaders: [
      {
        include: [path.join(__dirname, './src')],
        test: /\.jsx$/,
        loader: 'eslint-loader',
      },
    ],
    loaders: [
      {
        include: [path.join(__dirname, './src')],
        test: /\.jsx$/,
        loaders: ['react-hot', 'babel-loader?presets[]=es2015&presets[]=react'],
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader',
      },
      {
        test: /\.(eot|woff|woff2|ttf|svg|png|jpg)$/,
        loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]',
      },
    ],
  },
};
