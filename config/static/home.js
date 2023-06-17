const user_id = $('#user-pk').val()
let wishes = []
let wish_clicked = []


$.ajax({
    url: '/api/wishlist/',
    method: 'get',
    data: {
        'user_id': user_id,
    },
    success: function (response) {
        if (response.status === 'ok') {
            response.wishlist.wishes.forEach(element => {
                wishes.push(element)
            })
        }
        if (wishes.length > 0) {
            $('#list-empty').fadeOut(200)
            draw_wishes()
        } else {
            $('#empty-menu').fadeIn(200)
        }
    }
})


function draw_wishes() {
    $('#wishes').html('')

    wishes.forEach(element => {
        let wish_html = ''
        if (element.is_busy) {
            wish_html = `<div class="wish" id="wish-m-${element.id}">
                    <div class="main-wish border rounded wish-busy">
                        <div class="wish-clicked" id="wish-${element.id}">
                        <p class="busy-text">Уже занято!</p>
                        <p>${element.text}</p>`
        } else {
            wish_html = `<div class="wish" id="wish-m-${element.id}">
                    <div class="main-wish border rounded">
                        <div class="wish-clicked" id="wish-${element.id}">
                        <p class="busy-text" style="display: none">Уже занято!</p>
                        <p>${element.text}</p>`
        }
        if (element.about)
        wish_html += `<div class="about"><small class="text-secondary">${element.about}</small></div>`
        wish_html += `</div>`
        if (element.link)
        wish_html += `<a href="${element.link}" class="text-secondary">${element.link}</a>`
        wish_html += `<div class="wish-settings" style="display: none" id="wish-s-${element.id}"><div class="pt-3 pb-2 d-flex justify-content-between w-100">
        <button class="btn btn-outline-secondary" id="wish-btn-${element.id}">Удалить</button></div></div></div>`

        $('#wishes').append(wish_html)
    })

    $('#wishlist').fadeIn(400)
}

$('#wishlist').on('click', '.wish-clicked', function () {
    let wish_id = $(this).attr('id').slice(5)
    if (wish_clicked.includes(wish_id)) {
        $(`#wish-s-${wish_id}`).fadeOut(200)
        wish_clicked.splice(wish_clicked.indexOf(wish_id), 1)
    } else {
        $(`#wish-s-${wish_id}`).fadeIn(200)
        wish_clicked.push(wish_id)
    }
})

$('#wishlist').on('click', '.btn', function () {
    let wish_id = $(this).attr('id').slice(9)
    $.ajax({
        url: '/api/wish/',
        method: 'delete',
        headers: {
            'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        data: {
            'wish_id': wish_id,
            'user_id': user_id,
        },
        success: function (response) {
            if (response.status === 'ok') {
                $(`#wish-m-${wish_id} .main-wish`).remove()
            }
            $(`#wish-s-${wish_id}`).fadeOut(0)
            wish_clicked.splice(wish_clicked.indexOf(wish_id), 1)
        }
    })
})
