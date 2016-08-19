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
    test: /\.(jpe?g|png|gif|svg)$/i,
    loaders: [
      'file?hash=sha512&digest=hex&name=[hash].[ext]',
      'image-webpack?bypassOnDebug&optimizationLevel=8&interlaced=false',
    ],
  },
  {
    test: /\.(eot|woff|woff2|ttf)$/,
    loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]',
  },
]


module.exports = { loaders, preLoaders }
