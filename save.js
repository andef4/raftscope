$(function () {
    $('body').append('<input id="filename"><br>');
    $('body').append('<input name="save-data" id="save-data" type="checkbox"><label for="save-data">Save data</label><br>');
    $('body').append('<button id="start-button">Start</button><br>');
    $('#start-button').click(function () {
        const filename = $('#filename').val();
        const saveData = $('#save-data').is(':checked');
        const svg = $('svg')[0].outerHTML;
        $.post('http://localhost:3000', {
            filename,
            svg
        })
    })
});
