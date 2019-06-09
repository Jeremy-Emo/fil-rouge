/* ======================================
*            Variables                  *
=======================================*/

let mode;


/* ======================================
*            Général                    *
=======================================*/

function popErrorMessage(message){
  if(screen.width <= 768){
    toastr.options = {
      "positionClass": "toast-bottom-full-width"
    }
  }
  toastr.error(message);
}

function popMessage(message){
  if(screen.width <= 768){
    toastr.options = {
      "positionClass": "toast-bottom-full-width"
    }
  }
  toastr.success(message);
}

$( document ).ready(function() {

    if(localStorage.getItem('successMessage')){
      popMessage(localStorage.getItem('successMessage'));
      localStorage.removeItem('successMessage');
    }

    if(localStorage.getItem('errorMessage')){
      popErrorMessage(localStorage.getItem('errorMessage'));
      localStorage.removeItem('errorMessage');
    }

    $('[data-toggle="popover"]').popover();
    $('[data-toggle=popover]').on('click', function(e){
       $('[data-toggle=popover]').not(this).popover('hide');
    });

    $('body').on('click', '.togglable .card-header', function(){
        $(this).next().slideToggle("fast");
        if($(this).children('i').hasClass('fa-angle-down')){
            $(this).find('.fa-angle-down').removeClass('fa-angle-down').addClass('fa-angle-up');
        } else {
            $(this).find('.fa-angle-up').removeClass('fa-angle-up').addClass('fa-angle-down');
        }
    });

    $('body').on('click', '.popover', function(){
        var origin = $(this).attr('id');
        $('[aria-describedby="'+origin+'"]').popover('hide');
    });

});
