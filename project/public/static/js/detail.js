$( document ).ready(function() {

  $("body").on("click", "#add_fav", function(){
    var url = "/films/change_fav";
    var movie_id = $(this).attr("data-id");
    $.post( url, {
      movie_id : movie_id
    }).done(function(data){
      if(data.success){
        if($("#add_fav").val() == "Ajouter aux favoris") {
          $("#add_fav").val("Retirer des favoris");
        } else {
          $("#add_fav").val("Ajouter aux favoris");
        }
        popMessage(data.message);
      } else {
        popErrorMessage(data.error_message);
      }
    });
  });

});
