$( document ).ready(function() {

  checkPrevAndNext();

  $("body").on('click', "#prev", function(){
    var searchString = $("#movie_name").val();
    var order = $("#tri").find(":selected").val();
    var page = $(this).attr("data-page");
    sendSearch(searchString, order, page);
    updatePrevAndNext("prev");
  });
  $("body").on('click', "#next", function(){
    var searchString = $("#movie_name").val();
    var order = $("#tri").find(":selected").val();
    var page = $(this).attr("data-page");
    sendSearch(searchString, order, page);
    updatePrevAndNext("next");
  });

  $("body").on("change", "#tri", function(){
    var searchString = $("#movie_name").val();
    var page = 1;
    var order = $(this).find(":selected").val();
    sendSearch(searchString, order, page);
    updatePrevAndNext("none");
  });

  $("body").on("click", "#goSearch", function(){
    var searchString = $("#movie_name").val();
    var page = 1;
    var order = $("#tri").find(":selected").val();
    sendSearch(searchString, order, page);
    updatePrevAndNext("none");
  });

});

function sendSearch(searchString, order, page){
  var url = "/films/search";
  $.post( url, {
    searchString : searchString,
    order : order,
    page : page
  }).done(function(data){
    if(data.success){
      var html = "";
      data.films.forEach(function(film){
        $("#create_movie_box .movie_img").attr("src", film.poster_path).attr("alt", film.title);
        $("#create_movie_box p").text(film.title);
        $("#create_movie_box .movie_desc_link").attr("href", film.link);
        html += $("#create_movie_box").html();
      });
      $("#movies_container").html(html);
      $("#nbre_results").text(data.nbre_results);
      result_number = data.pages;
    } else {
      popErrorMessage(data.error_message);
    }
  });
}

function checkPrevAndNext(){
  if($("#prev").attr("data-page") == 0 || $("#prev").attr("data-page") >= result_number){
    $("#prev").hide();
  } else {
    $("#prev").show();
  }
  if($("#next").attr("data-page") == 0 || $("#next").attr("data-page") >= result_number ){
    $("#next").hide();
  } else {
    $("#next").show();
  }
}

function updatePrevAndNext(from){
  if(from == "prev"){
    var new_value = parseInt($("#prev").attr("data-page"), 10) - 1;
    if(new_value > 0 && new_value <= result_number){
      $("#prev").attr("data-page", new_value);
    } else {
      $("#prev").attr("data-page", 0);
    }
    new_value = parseInt($("#next").attr("data-page"), 10) - 1;
    if(new_value > 0 && new_value <= result_number){
      $("#next").attr("data-page", new_value);
    }
  } else if(from == "next") {
    var new_value = parseInt($("#prev").attr("data-page"), 10) + 1;
    if(new_value > 0 && new_value <= result_number){
      $("#prev").attr("data-page", new_value);
    } else {
      $("#prev").attr("data-page", 0);
    }
    new_value = parseInt($("#next").attr("data-page"), 10) + 1;
    if(new_value > 0 && new_value <= result_number){
      $("#next").attr("data-page", new_value);
    }
  } else {
    $("#prev").attr("data-page", 0);
    $("#next").attr("data-page", 2);
  }
  checkPrevAndNext();
}
