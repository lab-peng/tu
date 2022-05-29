$(function () {

    // model part 
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });

    // get all field names as an array
    let fields = $("[name]").map(function () {
        if ($(this).attr("name") !== 'csrfmiddlewaretoken' && $(this).attr("name") !== 'viewport') {
            return $(this).attr("name");
        }
    }).get();
    fields = $.unique(fields)


    // view part 
    // dynamically render action buttons (diable and enable)
    const renderButtons = () => {
        let checkeds = $('input[name=ids]:checked');
        console.log(checkeds)
            if (checkeds.length < 1) {
                $('#update-button').attr('disabled', true)
                $('#update-button').addClass('disabled')
                $('#delete-button').attr('disabled', true)
                $('#delete-button').addClass('disabled')
            } else if (checkeds.length === 1) {
                $('#update-button').attr('disabled', false)
                $('#update-button').removeClass('disabled')
                $('#delete-button').attr('disabled', false)
                $('#delete-button').removeClass('disabled')
            } else {
                $('#update-button').attr('disabled', true)
                $('#update-button').addClass('disabled')
                $('#delete-button').attr('disabled', false)
                $('#delete-button').removeClass('disabled')
            };
    
            // reverse toggle select-all checkboxes
            if (checkeds.length === $('input[name=ids]').length) {
                $('#toggle-checkboxes').val(['on'])
            } else {
                $('#toggle-checkboxes').val(['off'])
            }
    }


    // controller part 
    // toggle select-all checkboxes
    $('#toggle-checkboxes').click(function () {
        let checkedStatus = this.checked;
        $('input[name=ids]').each(function () {
            $(this).prop('checked', checkedStatus);
        });
        renderButtons();
    });


    $('table').on("click", "input[name=ids]", function () {
        renderButtons();
    })


    
    /* Populate the form with data of to-be-edited instance */
    $('#update-button').click(function (e) {
        $('.create-overlay').css('display', 'grid');
        $('.create-modal h1').html('Update')

        // remove all error messages from form
        const fieldErrors = $('.field-error');
        fieldErrors.each(() => {
            $('.field-error').html('&nbsp;')
        })

        // get checked ids
        const ids = $('input[name=ids]:checked').map(function () {
            return $(this).val();
        }).get();
        $('[name="post_ids"]').val(ids);
        $.ajax({
            type: 'POST',
            url: "/app_d/get_update_info/",
            data: {
                ids: JSON.stringify(ids),
            },
            success: function (response) {
                if (response.instances.length === 1) {
                    let instance = response.instances[0];
                    for (key in instance) {
                        // console.log(key, instance[key]);
                        if (key === 'bool') {
                            instance[key] === true ? $(`[name=${key}]`).val(["True"]) : $(`[name=${key}]`).val(["False"])
                        }
                        $(`#id_${key}`).val(instance[key]);
                    }
                }
            },
        })
    })

    // create and update
    $('#create-update-form').submit(function (e) {
        e.preventDefault();
        const serializedData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: '/app_d/create_update/',
            data: serializedData,
            success: function (response) {
                if (response.instance) {
                    let ids = $("tbody").find("tr").find('input[type=checkbox]:checked').map(function () {
                        return $(this).val();
                    }).get();
                    if (!ids.includes(response.instance.id.toString())) { 
                        // on successfull creating an object
                        location.href = '/app_d/'
                    } else {
                        // on successfull updating objects
                        $('.create-overlay').css('display', 'none');
                        const instance = response.instance;
                        $("#" + instance.id).replaceWith(
                            `<tr id="${instance.id}">
                                <td class="id-row"><input type="checkbox" value="${instance.id}" name="ids"></td>
                                <td class="title">${instance.char}</td>
                                <td>${instance.bool}</td>
                                <td>${instance.date}</td>
                                <td class="long">${instance.longer_char}</td>
                                <td>${instance.datetime.replace('Z', ' ').replace('T', ' ')}</td>
                                <td>${instance.integer}</td>
                                <td>${instance.float_info}</td>
                                <td>${instance.decimal}</td>
                                <td>${instance.text.substring(0,12)}...</td>
                            </tr>`
                        );
                        renderButtons();
                    }                    
                }
                else {
                    // on error display the error message
                    let errors = response.errors;
                    for (let i = 0; i < fields.length; i++) {
                        let field = fields[i];
                        let error = errors[field];
                        if (error) {
                            $("#" + field + "_error").html(error);
                        } else {
                            $("#" + field + "_error").html('&nbsp;');
                        }
                    }
                }
            }
        })
    })

    // delete
    $('#delete-button').click(() => {
        $('.delete-overlay').css('display', 'grid');
        const ids = $('input[name=ids]:checked').map(function () {
            return $(this).val();
        }).get();

        $('#js-delete-confirm').click(() => {
            $.ajax({
                type: 'POST',
                url: '/app_d/delete/',
                data: {
                    "ids": JSON.stringify(ids)
                },
                success: function (response) {
                    // console.log(response)
                    location.href = '/app_d/'
                    // if (response.status) {
                    //     // row.remove();
                    //     row.fadeOut();
                    // } else {
                    //     alert("Error deleting...");
                    // }
                }
            })
        })

    })





});