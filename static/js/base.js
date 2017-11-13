$( document ).ready(function() {

  $("html").click(function() {
    $("#cart_wrapper").slideUp();
  });

  $("#cart_icon").click(function( event ) {
    event.stopPropagation();
    $("#cart_wrapper").slideToggle();
  });

  $("#cart_wrapper").click(function( event ) {
    event.stopPropagation();
  });

  $(".btn.categories").click(function() {
    $(".sidebar_wrapper").toggle();
  });

});
