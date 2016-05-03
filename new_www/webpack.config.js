var webpack = require('webpack');


module.exports = {
    devtool: 'source-map',
    entry:  './src/index.jsx',
    output: {
        path:       'build',
        filename:   'bundle.js',
        publicPath: 'build/'
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        })
    ],
    devServer: {
      historyApiFallback: true
    },
    module: {
       preLoaders: [
            {test: /\.js$/, loader: "eslint-loader"}
        ],
        loaders: [
            {
                test: /\.jsx$/,
                loaders: ['react-hot', 'babel-loader?presets[]=es2015&presets[]=react']
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /\.(eot|woff|woff2|ttf|svg|png|jpg)$/,
                loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]'
            }
        ]
    }
};