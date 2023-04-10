function cleanList() {
    $('ul.ajax-list li').remove();
}

(function loadScript() {
    $(document).ready(function () {
        $('.search-btn').click(function (e) {
            e.preventDefault(); // отмена события по умолчанию, при нажатии на кнопку теперь ничего не происходит
            cleanList(); // очистка списка, написали эту функцию выше

            $.ajax({
                url: '/search/tickets/',
                data: $('form').serialize(),
                success: function (data) {
                    $('ul.ajax-list').append(data);
                    $('.error-message').text('')
                },
                error: function () {
                    $('.error-message').text('Некорректно заполнена форма');
                }
            });
        });
    });
})();