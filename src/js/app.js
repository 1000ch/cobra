$(function () {

  var $entry = $('#js-entry');
  var $entries = $entry.find('a');
  var $feed = $('#js-feed');
  var $feeds = $feed.find('li');

  $entry.on('touchstart', 'a', function (e) {
    this.classList.add('active');
  }).on('touchend', 'a', function (e) {
    this.classList.remove('active');
  });

  $feed.on('click', 'li', function (e) {
    this.classList.toggle('active');
    var selected = [];
    $feeds.each(function (index, element) {
      if (element.classList.contains('active')) {
        selected.push(element.getAttribute('data-feed'));
      }
    });
    if (selected.length === 0) {
      $entries.removeClass('hidden');
    } else {
      $entries.each(function (index, element) {
        var name = element.getAttribute('data-feed');
        if (selected.indexOf(name) !== -1) {
          element.classList.remove('hidden');
        } else {
          element.classList.add('hidden');
        }
      });
    }
  });

  var $search = $('#js-search');
  $search.on('keyup', _.throttle(function (e) {
    var value = $search.val();
    $entries.each(function (index, element) {
      var title = element.querySelector('h4').textContent;
      if (title.indexOf(value) !== -1) {
        element.classList.remove('hidden');
      } else {
        element.classList.add('hidden');
      }
    });
  }, 300));
});