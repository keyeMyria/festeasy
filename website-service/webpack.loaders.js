const ExtractTextPlugin = require('extract-text-webpack-plugin');
const { srcPath } = require('./webpack.paths')


const preLoaders = [
  {
    include: [srcPath],
    test: /\.jsx$/,
    loader: 'eslint-loader',
  },
]

const loaders = [
  {
    include: [srcPath],
    test: /\.js$/,
    loaders: ['babel-loader'],
  },
  {
    include: [srcPath],
    test: /\.jsx$/,
    loaders: [
      'react-hot', 'babel-loader',
    ],
  },
  {
    test: /\.css$/,
    loader: ExtractTextPlugin.extract('style-loader', 'css-loader'),
  },
  {
    test: /\.(eot|woff|woff2|ttf|svg|png|jpg)$/,
    loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]',
  },
]


module.exports = { loaders, preLoaders }
