module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    clean: ["build", "dist"],
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
          cwd: 'build',
          src: ['*', ],
          dest: 'dist/',
          expand: true,
        }, {
          cwd: 'src',
          src: ['app/components/**', ],
          dest: 'dist/',
          expand: true,
        }, {
          cwd: 'src',
          src: ['app/assets/**', ],
          dest: 'dist/',
          expand: true,
        },]
      }
    },
    template: {
      'process-html-template': {
        options: {
          data: {
            'buildNumber': process.env.CIRCLE_BUILD_NUM || 'local',
          },
        },
        files: {
          'dist/index.html': ['src/index.html.tpl']
        },
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-template');

  grunt.registerTask('default', ['clean', 'bower_concat', 'coffee', 'copy', 'template']);

};
