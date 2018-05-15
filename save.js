$(function () {
    $('body').append('<input id="filename"><br>');
    $('body').append('<input name="save-data" id="save-data" type="checkbox"><label for="save-data">Save data</label><br>');

    window.playback.pause()

    window.setInterval(function () {
        if (!window.playback.isPaused()) {
            const filename = $('#filename').val();
            const saveData = $('#save-data').is(':checked');
            const svg = $('svg')[0].outerHTML;
            $.post('http://localhost:3000', {
                filename,
                saveData,
                svg
            })
        }
    }, 500);

    $('#filename').focus()
})
