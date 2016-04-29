var webpack = require('webpack');


module.exports = {
    entry:  './src/index.jsx',
    output: {
        path:       'build',
        filename:   'bundle.js',
        publicPath: 'build/',
    },
    module: {
        loaders: [
    			  {
        				test: /\.jsx$/,
        				loader: 'babel-loader',
        				query: {
        	          presets: ['es2015', 'react'],
          	    },
            },
            {
                test:   /\.html/,
                loader: 'html',
            }
        ],
    },
};
