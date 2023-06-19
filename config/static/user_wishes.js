const user_id = $('#user-pk').val()
let wishes = []
let wish_clicked = []


// отрисовка одного желания. end = True - вставка в конец, иначе - в начало
function draw_one_wish(element, end = true) {
    let wish_html = ''
    if (!element.is_busy) {
        wish_html = `<div class="wish" id="wish-m-${element.id}">
                    <div class="main-wish border rounded">
                        <div class="wish-clicked" id="wish-${element.id}">
                        <p class="busy-text" style="display: none">Уже занято!</p>
                        <p>${element.text}</p>`
        if (element.about)
        wish_html += `<div class="about"><small class="text-secondary">${element.about}</small></div>`
        wish_html += `</div>`
        if (element.link)
        wish_html += `<a href="${element.link}" class="text-secondary">${element.link}</a>`
        wish_html += `<div class="wish-settings" style="display: none" id="wish-s-${element.id}"><div class="pt-3 pb-2 d-flex justify-content-between w-100">
        <button class="btn btn-outline-secondary" id="wish-btn-${element.id}">Забронировать</button></div></div></div>`
    } else {
        wish_html = `<div class="wish" id="wish-m-${element.id}">
                        <div class="main-wish border rounded wish-busy">
                            <div class="wish-clicked" id="wish-${element.id}">
                            <p class="busy-text">Уже занято!</p>
                            <p>${element.text}</p>`
        if (element.about)
            wish_html += `<div class="about"><small class="text-secondary">${element.about}</small></div>`
        wish_html += `</div>`
        if (element.link)
            wish_html += `<a href="${element.link}" class="text-secondary">${element.link}</a>`
        wish_html += `<div class="wish-settings" style="display: none" id="wish-s-${element.id}"><div class="pt-3 pb-2 d-flex justify-content-between w-100">
        <button class="btn btn-outline-secondary wish-btn-busy" id="wish-btn-${element.id}">Отменить</button></div></div></div>`
    }

    if (end) {
        $('#wishes').append(wish_html)
    } else {
        $('#wishes').prepend(wish_html)
    }
}

// удаление желания
function delete_wish(wish_id) {
    $(`#wish-m-${wish_id}`).remove()
    // удаляем из списка нажатых
    wish_clicked.splice(wish_clicked.indexOf(wish_id), 1)
}

// отрисовка списка желаний
function draw_wishes() {
    if (wishes.length > 0) {
        $('#list-empty').fadeOut(200)
        //draw_wishes()
    } else {
        $('#empty-menu').fadeIn(200)
    }
    
    $('#wishes').html('')

    wishes.forEach(element => {
        draw_one_wish(element)
    })

    setTimeout(() => {
        $('#wishlist').fadeIn(200)
    }, 200)
}

// нажатие на желание для открытия меню управления
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
