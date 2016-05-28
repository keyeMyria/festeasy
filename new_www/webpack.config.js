const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
  devtool: 'source-map',
  entry: './src/entry.jsx',
  output: {
    path: 'build',
    filename: 'bundle.js',
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.ejs',
      inject: 'body',
      title: 'iFix REPS',
    }),
    new webpack.ProvidePlugin({
      _: 'lodash',
      jQuery: 'jquery',
    }),
  ],
  devServer: {
    historyApiFallback: true,
  },
  module: {
    preLoaders: [
      {
        test: /\.jsx$/,
        loader: 'eslint-loader',
      },
    ],
    loaders: [
      {
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
