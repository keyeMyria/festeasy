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
          'build/my.js': ['src/**/*.coffee']
        },
        options: {
          sourceMap: true,
        }
      }
    },
    copy: {
      main: {
        files: [{
          cwd: 'src',
          src: ['index.html', ],
          dest: 'dist/',
          expand: true,
        }, {
          cwd: 'build',
          src: ['*', ],
          dest: 'dist/',
          expand: true,
        }, {
          cwd: 'src',
          src: ['app/components/**', ],
          dest: 'dist/',
          expand: true,
        },{
          cwd: 'src',
          src: ['app/assets/**', ],
          dest: 'dist/',
          expand: true,
        },]
      }
    },
  });

  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-copy');

  grunt.registerTask('default', ['bower_concat', 'coffee', 'copy']);

};
