$(document).ready(function() {
    $.getJson("", function(data) {
        $.each(data.results, function(index, movie) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        });
    });
});
