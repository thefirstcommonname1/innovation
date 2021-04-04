$(document).ready(function () {

  $("#sidebar").mCustomScrollbar({
      theme: "minimal"
  });

  $('#dismiss, .overlay').on('click', function () {
      // hide sidebar
      $('#sidebar').removeClass('active');
      // hide overlay
      $('.overlay').removeClass('active');
  });

  $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
      $('.overlay').addClass('active');
  });

});