var gulp = require('gulp');
var wiredep = require('wiredep').stream;
var del = require('del');
var mainBowerFiles = require('main-bower-files');
var debug = require('gulp-debug');
var gulpFilter = require('gulp-filter');
var concat = require('gulp-concat');
var less = require('gulp-less');
var coffee = require('gulp-coffee');
var flatten = require('gulp-flatten');
var order = require('gulp-order');
var livereload = require('gulp-livereload');


gulp.task('clean', function (cb) {
	return del(['./dist/*'], cb);
});

gulp.task('html', function () {
	return gulp.src('./src/**/*.partial.html')
		.pipe(flatten())
		.pipe(gulp.dest('./dist/partials'));
});

gulp.task('coffee', function () {
	return gulp.src('./src/**/*.coffee')
		.pipe(coffee({bare: true}))
		.pipe(order([
			"**/*.module.js"
		]))
		.pipe(concat('src.js'))
		.pipe(gulp.dest('./dist'));
});

gulp.task('assets', function () {
	return gulp.src('./src/app/assets/**')
		.pipe(gulp.dest('./dist/assets'));
});

gulp.task('index', function () {
	return gulp.src('./src/index.html')
		.pipe(gulp.dest('./dist'));
});

gulp.task('bootstrap-fonts', function () {
	return gulp.src('./bower_components/bootstrap/fonts/**')
		.pipe(gulp.dest('./dist/fonts'));
});

gulp.task('bower', ['bootstrap-fonts'], function () {
	var jsFilter = gulpFilter(['**/*.js'], {restore: true});
	var lessFilter = gulpFilter(['**/*.less'], {restore: true});
	return gulp.src(mainBowerFiles(), {base: 'bower_components'})
		.pipe(jsFilter)
		.pipe(concat('bower.js'))
		.pipe(jsFilter.restore)
		.pipe(lessFilter)
		.pipe(less())
		.pipe(concat('bower.css'))
		.pipe(lessFilter.restore)
		.pipe(gulp.dest('./dist'));
});

gulp.task('watch', function () {
	gulp.watch('./src/index.html', ['index']);
	gulp.watch('./bower_components/**', ['bower']);
	gulp.watch('./src/**/*.partial.html', ['html']);
	gulp.watch('./src/**/*.coffee', ['coffee']);
	gulp.watch('./src/app/assets/**', ['assets']);
	livereload.listen();
	gulp.watch('./dist/**').on('change', livereload.changed);
})

gulp.task('default', ['clean'], function () {
	gulp.start('html', 'coffee', 'assets', 'bower', 'index');
});
