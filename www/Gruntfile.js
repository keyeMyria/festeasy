module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    bower_concat: {
      all: {
        dest: 'build/bower.js',
        cssDest: 'build/bower.css',
        devDependencies: true,
        mainFiles: {
          bootstrap: ['dist/css/bootstrap.css']
        }
      }
    },
    coffee: {
      all: {
        files: {
          'build/my.js': ['**/*.coffee']
        },
        options: {
          basePath: 'src',
          sourceMap: true,
        }
      }
    },
  });

  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-coffee');

  grunt.registerTask('default', ['bower_concat', 'coffee']);

};
