const user_id = $('#user-pk').val()

let link = `${window.location.origin}/@${user_id}/`
$('#link').attr('href', link).text(link)
