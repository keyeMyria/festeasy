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
    }
  });

  grunt.loadNpmTasks('grunt-bower-concat');

  grunt.registerTask('default', ['bower_concat']);

};
