document.addEventListener('DOMContentLoaded', function () {
  var input = document.getElementById('input');

  input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
      alert('Você pressionou Enter!');
    }
  });
});