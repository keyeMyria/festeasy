var gulp = require('gulp')
var wiredep = require('wiredep').stream
var del = require('del')
var mainBowerFiles = require('main-bower-files')
var debug = require('gulp-debug')
var gulpFilter = require('gulp-filter')
var concat = require('gulp-concat')


gulp.task('clean', function () {
	return del(['./dist/*'])
});

gulp.task('wiredep', function () {
	gulp.src('./src/index.html')
		.pipe(wiredep())
		.pipe(gulp.dest('./dist'));
});

gulp.task('default', function () {
	var jsFilter = gulpFilter(['**/*.js']);
	gulp.src(mainBowerFiles(), {base: 'bower_components'})
		.pipe(jsFilter)
		.pipe(concat('bower.js'))
		.pipe(debug())
		.pipe(gulp.dest('./dist'));
});
