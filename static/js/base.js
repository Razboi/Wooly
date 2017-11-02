$(document).ready(function(){

  $("html").click(function() {
    $("#cart_wrapper").hide();
  });

  $("#cart_icon").click(function(event){
    event.stopPropagation();
    $("#cart_wrapper").toggle();
  });

  $("#cart_wrapper").click(function(event)
  {
    event.stopPropagation();
});

});
