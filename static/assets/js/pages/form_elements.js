$(document).ready(function(){
    $('.datepicker').pickadate({
        selectMonths: true,
        selectYears: 15
    });

    $('input.autocomplete').autocomplete({
        data: {
            "Apple": null,
            "Microsoft": null,
            "Google": 'assets/images/google.png'
        }
    });
});
$('.datepicker').datepicker({
    format: 'dd-mm-yyyy'
});