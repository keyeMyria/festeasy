var history = require('connect-history-api-fallback')

module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    connect: {
      server: {
        options: {
          port: 8000,
          base: 'dist',
          keepalive: true,
          middleware: function(connect, options, middleware) {
            middleware.unshift(history())
            return middleware
          },
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-connect');

  grunt.registerTask('default', []);
};
