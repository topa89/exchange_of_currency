var timer;
$(document).ready(function () {
    var form = $('#form_order');

    form.on('submit', function (e) {
        $('#exampleModal5').hide();
        e.preventDefault();

        var data = {};
        data.email = $('#user_email').val();
        data.card_number = $('#card_number').val();
        data.input = $('#input_value').attr('data-seo');
        data.sum_from = $('#input_from').val();
        data.output = $('#output_value').attr('data-seo');
        data.sum_to = $('#input_to').val();

        var csrf_token = $('#form_order [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,

        })

    });
    // считаем курс
    $('#input_from').keyup(function () {
        $('#input_to').val(parseInt($(this).val() * ($('#kurs_to').text() / $('#kurs_from').text())));
        push_exchange_on_modal();
        // TODO рассчитать минимальный платеж и сделать валидацию
    });

    $('#input_to').keyup(function () {
        $('#input_from').val($(this).val() / ($('#kurs_to').text() / $('#kurs_from').text()));
        push_exchange_on_modal();
    });



    $('#order').click(function () {
        if (validate()) {
            $('#user_email').css('border-color', '');
            $(this).attr('data-toggle', 'modal');
            $(this).attr('data-dismiss', 'modal')
        
        clearTimeout(timer);
        minutes = 14;
        seconds = 59;
        timer = setTimeout(function tick() {
            if (minutes >= 0) {
                if ((minutes == 0) && (seconds == 0)) {
                    timer.stop();
                }
                if (seconds > 0) {
                    seconds -= 1;
                }
                else {
                    minutes -= 1;
                    seconds = 59;
                }
                $('#minutes').text(minutes);
                $('#seconds').text(seconds);
            }
            if ((minutes == 0) && (seconds == 0)) {
                clearTimeout(timer);
                $('#exampleModal5').hide();
                $('.modal-backdrop.fade.show').hide();
            }
            timer = setTimeout(tick, 1000);
        }, 1000);
    }
    });

    $("#button_submit").click(function () {
        $('.modal-backdrop.fade.show').hide();
    })

    // проверка данных
    $('#check_inputs').click(function () {
        if (($('#input_from').val() == '') || ($('#input_to').val() == '')) {
            $('#input_from').css('border-color', 'red');
        }
        else {
            $('#input_from').css('border-color', '');
            $(this).attr('data-toggle', 'modal');
        }
    })

    $('#card_number').keyup(function () {
        len_val = $(this).val().length;
        if (len_val > 18) {
            $(this).val($(this).val().substr(0, 19));
        }
        if (len_val == 4 || len_val == 9 || len_val == 14) {
            $(this).val($(this).val() + " ");
        }
    });

    $('#stopTimer').click(function () {
        clearTimeout(timer);
        $('#minutes').text('14');
        $('#seconds').text('59');
    });

    $('#accept').click(function () {
        clearTimeout(timer);
        $('#minutes').text('14');
        $('#seconds').text('59');
    });

    $('#order').click(function () {
        $('#staticEmail').first().val($('#input_from').val() + ' ' + $('.input-group-text').first().text());
    })

    push_exchange_on_modal();


});

function push_exchange_on_modal() {
    $('.container').find('h5').first().text('Обмен ' + $('.form-control').first().val() + ' '
        + $('.input-group-text').first().text() + ' = ' + $('.form-control').eq(1).val() + ' ' + $('.input-group-text').eq(1).text());
}


function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validate() {
    if (!isEmail($('#user_email').val())) {
        alert('Введите правильный email');
        $('#user_email').css('border-color', 'red');
        return false;
    }
    if ($('#card_number').val().length < 19) {
        alert('Проверьте номер карты');
        $('#card_number').css('border-color', 'red');
        return false;
    }
    return true;
}