var gulp = require('gulp');
var concat = require('gulp-concat');

gulp.task('default', [
  'js:lib',
  'js:app',
  'css:lib',
  'css:app'
]);

gulp.task('js:lib', function () {

  return gulp.src([
    'bower_components/jquery/dist/jquery.min.js',
    'bower_components/bootstrap/dist/js/bootstrap.min.js',
    'bower_components/underscore/underscore-min.js'
  ])
    .pipe(concat('lib.min.js'))
    .pipe(gulp.dest('cobra/static/js'));
});

gulp.task('js:app', function () {

  return gulp.src([
    'src/js/app.js'
  ])
    .pipe(concat('app.min.js'))
    .pipe(gulp.dest('cobra/static/js'));
});

gulp.task('css:lib', function () {

  return gulp.src([
    'bower_components/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concat('lib.min.css'))
    .pipe(gulp.dest('cobra/static/css'));
});

gulp.task('css:app', function () {

  return gulp.src([
    'src/css/app.css'
  ])
    .pipe(concat('app.min.css'))
    .pipe(gulp.dest('cobra/static/css'));
});