const createModal = $('.create-overlay');
$('#create-button').click(() => {
    createModal.css('display', 'grid'); 
    $('.create-modal h1').html('Create New');
    $("#create-update-form").trigger('reset');
    $('[name="post_ids"]').val('');

    // remove all error messages from form
    const fieldErrors = $('.field-error');
    fieldErrors.each(() => {
        $('.field-error').html('&nbsp;')
    })
})

$('#cancel-create-button').click(() => {
    createModal.css('display', 'none');
})


const S = document.querySelector.bind(document);
const deletModal = S('.delete-overlay');
const deleteButton = S('#delete-button');
const confirmButton = S('.confirm-button');
const cancelButton = S('.cancel-button');
deleteButton.addEventListener('click', () => {
    deletModal.style.display = 'grid';
});

cancelButton.addEventListener('click', () => {
    deletModal.style.display = 'none';
});

confirmButton.addEventListener('click', () => {
    deletModal.style.display = 'none';
});

