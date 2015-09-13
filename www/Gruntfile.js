module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    clean: ["dist/*"],
    bower_concat: {
      all: {
        dest: 'dist/bower.js',
        cssDest: 'dist/bower.css',
        devDependencies: true,
        mainFiles: {
          bootstrap: ['dist/css/bootstrap.css']
        }
      }
    },
    coffee: {
      all: {
        files: {
          'dist/festeasy.js': ['src/**/*.coffee']
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
            'revision': process.env.CIRCLE_SHA1 || 'local',
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
