$( document ).ready(function() {

  $('body').on('click', '#menu_account', function(){
      $('#submenu_account').toggle("slide", {direction:'right'});
  });

  $('body').on('click', '.toggle_menu', function(){
      $('#div-menu-mobile').toggle("slide");
      if($('#mobile_first_level').is(":hidden")){
        $('#mobile_first_level').show();
        $('#menu_mobile_account').hide();
      }
  });

  $('body').on('click', '#mobile_account', function(){
    $('#menu_mobile_account').toggle("slide");
    $('#mobile_first_level').toggle("slide");
  });

  $('body').on('click', '.bouton_retour_mobile', function(){
    $('#mobile_first_level').toggle("slide");
    $(this).parent().parent().toggle("slide");
  });

  $('body').on('click', '.bouton_retour_mobile_direct', function(){
    $('#mobile_first_level').toggle("slide");
    $(this).parent().toggle("slide");
  });

});
