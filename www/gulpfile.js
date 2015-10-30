var gulp = require('gulp')
var wiredep = require('wiredep').stream
var del = require('del')
var mainBowerFiles = require('main-bower-files')
var debug = require('gulp-debug')
var gulpFilter = require('gulp-filter')
var concat = require('gulp-concat')
var less = require('gulp-less')


gulp.task('clean', function () {
	return del(['./dist/*'])
});

gulp.task('wiredep', function () {
	gulp.src('./src/index.html')
		.pipe(wiredep())
		.pipe(gulp.dest('./dist'));
});

gulp.task('bower', function () {
	var jsFilter = gulpFilter(['**/*.js'], {restore: true});
	var lessFilter = gulpFilter(['**/*.less'], {restore: true});
	gulp.src(mainBowerFiles(), {base: 'bower_components'})
		.pipe(jsFilter)
		.pipe(concat('bower.js'))
		.pipe(jsFilter.restore)
		.pipe(lessFilter)
		.pipe(less())
		.pipe(concat('bower.css'))
		.pipe(lessFilter.restore)
		.pipe(debug())
		.pipe(gulp.dest('./dist'));
});
